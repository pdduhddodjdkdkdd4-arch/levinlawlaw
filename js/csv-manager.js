/**
 * CSV 数据管理工具类
 */
class CSVManager {
    constructor() {
        this.STORAGE_KEY = 'levinlaw_form_data';
        this.CSV_HEADERS = ['id', 'name', 'email', 'phone', 'platform', 'amount', 'timestamp', 'ip'];
    }

    /**
     * 从 localStorage 获取数据
     */
    getData() {
        const data = localStorage.getItem(this.STORAGE_KEY);
        return data ? JSON.parse(data) : [];
    }

    /**
     * 保存数据到 localStorage
     */
    saveData(data) {
        localStorage.setItem(this.STORAGE_KEY, JSON.stringify(data));
    }

    /**
     * 添加新记录
     */
    addRecord(record) {
        const data = this.getData();
        const newRecord = {
            id: Date.now().toString(),
            ...record,
            timestamp: new Date().toISOString(),
            ip: this.getClientIP()
        };
        data.unshift(newRecord);
        this.saveData(data);
        return newRecord;
    }

    /**
     * 更新记录
     */
    updateRecord(id, updatedData) {
        const data = this.getData();
        const index = data.findIndex(r => r.id === id);
        if (index !== -1) {
            data[index] = { ...data[index], ...updatedData };
            this.saveData(data);
            return true;
        }
        return false;
    }

    /**
     * 删除记录
     */
    deleteRecord(id) {
        const data = this.getData();
        const filtered = data.filter(r => r.id !== id);
        this.saveData(filtered);
    }

    /**
     * 清空所有记录
     */
    clearAll() {
        this.saveData([]);
    }

    /**
     * 获取客户端 IP（模拟）
     */
    getClientIP() {
        return '127.0.0.1'; // 实际项目中可以通过第三方API获取
    }

    /**
     * 导出 CSV
     */
    exportCSV(records = null, filename = null) {
        const data = records || this.getData();
        
        if (data.length === 0) {
            alert('没有数据可导出');
            return;
        }

        // 构建 CSV 内容
        const headers = ['ID', '姓名', '邮箱', '电话', '平台', '金额', '提交时间', 'IP'];
        const csvContent = [
            headers.join(','),
            ...data.map(record => [
                record.id,
                `"${record.name}"`,
                record.email,
                record.phone,
                `"${record.platform}"`,
                record.amount,
                record.timestamp,
                record.ip
            ].join(','))
        ].join('\n');

        // 创建下载
        const blob = new Blob(['\ufeff' + csvContent], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        
        if (!filename) {
            const now = new Date();
            const timeStr = now.getFullYear() + 
                String(now.getMonth() + 1).padStart(2, '0') + 
                String(now.getDate()).padStart(2, '0') + 
                String(now.getHours()).padStart(2, '0') + 
                String(now.getMinutes()).padStart(2, '0') + 
                String(now.getSeconds()).padStart(2, '0');
            filename = `${timeStr}_levinlaw.csv`;
        }
        
        link.setAttribute('href', url);
        link.setAttribute('download', filename);
        link.style.visibility = 'hidden';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);
    }

    /**
     * 导入 CSV
     */
    importCSV(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = (e) => {
                try {
                    const content = e.target.result;
                    const lines = content.split('\n').filter(line => line.trim());
                    
                    if (lines.length < 2) {
                        reject('CSV 文件格式不正确');
                        return;
                    }

                    const data = [];
                    for (let i = 1; i < lines.length; i++) {
                        const values = this.parseCSVLine(lines[i]);
                        if (values.length >= 8) {
                            data.push({
                                id: values[0],
                                name: values[1].replace(/"/g, ''),
                                email: values[2],
                                phone: values[3],
                                platform: values[4].replace(/"/g, ''),
                                amount: values[5],
                                timestamp: values[6],
                                ip: values[7]
                            });
                        }
                    }
                    
                    this.saveData(data);
                    resolve(data);
                } catch (error) {
                    reject('解析 CSV 文件失败: ' + error.message);
                }
            };
            reader.onerror = () => reject('读取文件失败');
            reader.readAsText(file);
        });
    }

    /**
     * 解析 CSV 行（处理引号）
     */
    parseCSVLine(line) {
        const result = [];
        let current = '';
        let inQuotes = false;
        
        for (let i = 0; i < line.length; i++) {
            const char = line[i];
            
            if (char === '"') {
                inQuotes = !inQuotes;
            } else if (char === ',' && !inQuotes) {
                result.push(current.trim());
                current = '';
            } else {
                current += char;
            }
        }
        result.push(current.trim());
        
        return result;
    }
}

// 全局实例
window.csvManager = new CSVManager();

/**
 * 登录管理
 */
class AuthManager {
    constructor() {
        this.CREDENTIALS = {
            username: 'admin_5_9',
            password: 'admin@2659Levinlaw'
        };
        this.AUTH_KEY = 'levinlaw_admin_auth';
    }

    login(username, password) {
        if (username === this.CREDENTIALS.username && password === this.CREDENTIALS.password) {
            localStorage.setItem(this.AUTH_KEY, 'true');
            return true;
        }
        return false;
    }

    isLoggedIn() {
        return localStorage.getItem(this.AUTH_KEY) === 'true';
    }

    logout() {
        localStorage.removeItem(this.AUTH_KEY);
    }
}

window.authManager = new AuthManager();

/**
 * 表单验证工具类
 */
class FormValidator {
    /**
     * 验证姓名
     * @param {string} name - 姓名字符串
     * @returns {object} 验证结果 { valid: boolean, message: string }
     */
    static validateName(name) {
        if (!name || !name.trim()) {
            return { valid: false, message: 'Name is required' };
        }
        if (name.trim().length < 2) {
            return { valid: false, message: 'Name must be at least 2 characters' };
        }
        if (name.trim().length > 50) {
            return { valid: false, message: 'Name must not exceed 50 characters' };
        }
        return { valid: true, message: '' };
    }

    /**
     * 验证邮箱
     * @param {string} email - 邮箱字符串
     * @returns {object} 验证结果
     */
    static validateEmail(email) {
        if (!email || !email.trim()) {
            return { valid: false, message: 'Email is required' };
        }
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email.trim())) {
            return { valid: false, message: 'Please enter a valid email address' };
        }
        return { valid: true, message: '' };
    }

    /**
     * 验证电话
     * @param {string} phone - 电话字符串
     * @returns {object} 验证结果
     */
    static validatePhone(phone) {
        if (!phone || !phone.trim()) {
            return { valid: false, message: 'Phone number is required' };
        }
        const phoneRegex = /^[\+]?[1-9][\d\s-]{7,15}$/;
        if (!phoneRegex.test(phone.trim())) {
            return { valid: false, message: 'Please enter a valid phone number (7-15 digits)' };
        }
        return { valid: true, message: '' };
    }

    /**
     * 验证平台名称
     * @param {string} platform - 平台名称
     * @returns {object} 验证结果
     */
    static validatePlatform(platform) {
        if (!platform || !platform.trim()) {
            return { valid: false, message: 'Platform name is required' };
        }
        if (platform.trim().length < 2) {
            return { valid: false, message: 'Platform name must be at least 2 characters' };
        }
        if (platform.trim().length > 100) {
            return { valid: false, message: 'Platform name must not exceed 100 characters' };
        }
        return { valid: true, message: '' };
    }

    /**
     * 验证金额
     * @param {string} amount - 金额字符串
     * @returns {object} 验证结果
     */
    static validateAmount(amount) {
        if (!amount || !amount.trim()) {
            return { valid: false, message: 'Amount is required' };
        }
        const amountRegex = /^[\$\€\£\¥]?\s?[\d,]+\.?\d*$/;
        if (!amountRegex.test(amount.trim())) {
            return { valid: false, message: 'Please enter a valid amount format (e.g., $1000 or 1000.00)' };
        }
        return { valid: true, message: '' };
    }

    /**
     * 验证完整表单
     * @param {object} formData - 表单数据对象
     * @returns {object} 验证结果 { valid: boolean, errors: object }
     */
    static validateForm(formData) {
        const errors = {};
        
        const nameResult = this.validateName(formData.name);
        if (!nameResult.valid) errors.name = nameResult.message;
        
        const emailResult = this.validateEmail(formData.email);
        if (!emailResult.valid) errors.email = emailResult.message;
        
        const phoneResult = this.validatePhone(formData.phone);
        if (!phoneResult.valid) errors.phone = phoneResult.message;
        
        const platformResult = this.validatePlatform(formData.platform);
        if (!platformResult.valid) errors.platform = platformResult.message;
        
        const amountResult = this.validateAmount(formData.amount);
        if (!amountResult.valid) errors.amount = amountResult.message;
        
        return {
            valid: Object.keys(errors).length === 0,
            errors: errors
        };
    }

    /**
     * 显示表单错误
     * @param {HTMLElement} formElement - 表单元素
     * @param {object} errors - 错误信息对象
     */
    static showErrors(formElement, errors) {
        // 清除之前的错误
        this.clearErrors(formElement);
        
        // 添加新错误
        for (const [field, message] of Object.entries(errors)) {
            const input = formElement.querySelector(`[name="${field}"], #edit-${field}`);
            if (input) {
                input.classList.add('input-error');
                
                const errorDiv = document.createElement('div');
                errorDiv.className = 'error-message';
                errorDiv.textContent = message;
                errorDiv.style.color = '#dc2626';
                errorDiv.style.fontSize = '12px';
                errorDiv.style.marginTop = '4px';
                
                const formGroup = input.closest('.form-group');
                if (formGroup) {
                    formGroup.appendChild(errorDiv);
                }
            }
        }
    }

    /**
     * 清除表单错误
     * @param {HTMLElement} formElement - 表单元素
     */
    static clearErrors(formElement) {
        formElement.querySelectorAll('.input-error').forEach(input => {
            input.classList.remove('input-error');
        });
        formElement.querySelectorAll('.error-message').forEach(el => {
            el.remove();
        });
    }

    /**
     * 为输入添加实时验证
     * @param {HTMLElement} formElement - 表单元素
     */
    static addRealtimeValidation(formElement) {
        const inputs = formElement.querySelectorAll('input');
        inputs.forEach(input => {
            input.addEventListener('blur', () => {
                const fieldName = input.name || input.id.replace('edit-', '');
                const value = input.value;
                
                let result;
                switch (fieldName) {
                    case 'name':
                        result = this.validateName(value);
                        break;
                    case 'email':
                        result = this.validateEmail(value);
                        break;
                    case 'phone':
                        result = this.validatePhone(value);
                        break;
                    case 'platform':
                        result = this.validatePlatform(value);
                        break;
                    case 'amount':
                        result = this.validateAmount(value);
                        break;
                    default:
                        return;
                }
                
                const formGroup = input.closest('.form-group');
                if (!formGroup) return;
                
                const existingError = formGroup.querySelector('.error-message');
                
                if (!result.valid) {
                    input.classList.add('input-error');
                    if (!existingError) {
                        const errorDiv = document.createElement('div');
                        errorDiv.className = 'error-message';
                        errorDiv.textContent = result.message;
                        errorDiv.style.color = '#dc2626';
                        errorDiv.style.fontSize = '12px';
                        errorDiv.style.marginTop = '4px';
                        formGroup.appendChild(errorDiv);
                    } else {
                        existingError.textContent = result.message;
                    }
                } else {
                    input.classList.remove('input-error');
                    if (existingError) existingError.remove();
                }
            });
            
            input.addEventListener('input', () => {
                input.classList.remove('input-error');
                const formGroup = input.closest('.form-group');
                const existingError = formGroup?.querySelector('.error-message');
                if (existingError) existingError.remove();
            });
        });
    }
}

window.FormValidator = FormValidator;

/**
 * 通用表单处理函数
 */
window.handleFormSubmit = function(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const data = {
        name: formData.get('name'),
        email: formData.get('email'),
        phone: formData.get('phone'),
        platform: formData.get('platform'),
        amount: formData.get('amount')
    };

    // 验证表单
    const validation = FormValidator.validateForm(data);
    if (!validation.valid) {
        FormValidator.showErrors(form, validation.errors);

        // 滚动到第一个错误
        const firstError = form.querySelector('.input-error');
        if (firstError) {
            firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
            firstError.focus();
        }
        return;
    }

    // 清除错误状态
    FormValidator.clearErrors(form);

    // 保存到本地存储
    const record = csvManager.addRecord(data);

    // 跳转到感谢页面
    window.location.href = 'thank-you.html';
};

/**
 * 初始化表单
 */
window.initContactForm = function() {
    const form = document.getElementById('contact-form');
    if (form) {
        FormValidator.addRealtimeValidation(form);
    }
};

// HTML escape
window.escapeHtml = function(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
};

// Date format
window.formatDate = function(isoString) {
    const date = new Date(isoString);
    return date.toLocaleString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
};
