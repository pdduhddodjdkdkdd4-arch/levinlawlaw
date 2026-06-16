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
     * 获取最新提交的记录
     */
    getLatestRecord() {
        const data = this.getData();
        return data.length > 0 ? data[0] : null;
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

/**
 * Messenger跳转管理器
 */
class MessengerManager {
    constructor() {
        // Facebook Page ID (291205327989296)
        this.DEFAULT_PAGE_ID = '291205327989296';
        this.DEFAULT_MESSENGER_LINK = 'https://m.me/291205327989296';
        
        // 应用商店链接
        this.IOS_APP_STORE_URL = 'https://apps.apple.com/us/app/messenger/id454638411';
        this.ANDROID_PLAY_STORE_URL = 'https://play.google.com/store/apps/details?id=com.facebook.orca';
        this.MESSENGER_WEB_URL = 'https://www.messenger.com/t/';
        
        // URL Scheme
        this.MESSENGER_SCHEME = 'fb-messenger://';
    }

    /**
     * 检测当前平台
     * @returns {string} 'ios', 'android', 'web'
     */
    detectPlatform() {
        const userAgent = navigator.userAgent.toLowerCase();
        
        if (userAgent.includes('iphone') || userAgent.includes('ipad') || userAgent.includes('ipod')) {
            return 'ios';
        } else if (userAgent.includes('android')) {
            return 'android';
        }
        return 'web';
    }

    /**
     * Build Messenger message content
     * @param {object} formData - Form data object
     * @returns {string} Formatted message text
     */
    buildMessage(formData) {
        const message = `
Case Report Details:

Name: ${formData.name || 'Not provided'}
Email: ${formData.email || 'Not provided'}
Phone: ${formData.phone || 'Not provided'}
Scam Platform: ${formData.platform || 'Not provided'}
Amount Lost: ${formData.amount || 'Not provided'}

Please assist with my case. Thank you!
        `.trim();
        
        return encodeURIComponent(message);
    }

    /**
     * 构建Messenger跳转URL
     * @param {object} formData - 表单数据对象
     * @returns {object} { schemeUrl, fallbackUrl }
     */
    buildURL(formData) {
        const message = this.buildMessage(formData);
        const pageId = this.DEFAULT_PAGE_ID;
        
        return {
            // Messenger URL Scheme（用于App跳转）
            schemeUrl: `${this.MESSENGER_SCHEME}user-thread/${pageId}`,
            // 网页版链接（包含预填充消息）
            webUrl: `${this.MESSENGER_WEB_URL}${pageId}?text=${message}`,
            // m.me链接（自动检测App或网页，包含预填充消息）
            mMeUrl: `https://m.me/${pageId}?text=${message}`
        };
    }

    /**
     * 获取应用商店链接
     * @param {string} platform - 平台类型
     * @returns {string} 应用商店URL
     */
    getAppStoreUrl(platform) {
        return platform === 'ios' ? this.IOS_APP_STORE_URL : this.ANDROID_PLAY_STORE_URL;
    }

    /**
     * 尝试打开Messenger应用
     * @param {object} formData - 表单数据对象
     */
    openMessenger(formData) {
        const platform = this.detectPlatform();
        const urls = this.buildURL(formData);
        
        if (platform === 'ios') {
            // iOS: 使用多级深度链接策略
            this.tryOpenIOSMessenger(urls);
        } else if (platform === 'android') {
            // Android: 使用Intent打开应用
            this.tryOpenAndroidMessenger(urls);
        } else {
            // Web: 在新标签页打开Messenger网页版
            window.open(urls.webUrl, '_blank');
        }
    }

    /**
     * iOS专用：多级深度链接策略
     * 1. 首先尝试URL Scheme (最可靠)
     * 2. 失败则回退到Universal Links
     * 3. 最后回退到网页版
     */
    tryOpenIOSMessenger(urls) {
        // Step 1: 尝试URL Scheme直接打开Messenger应用
        const schemeUrl = `fb-messenger://user-thread/${this.DEFAULT_PAGE_ID}`;
        
        // 创建隐藏的iframe来触发URL Scheme（iOS上更可靠）
        const iframe = document.createElement('iframe');
        iframe.style.display = 'none';
        iframe.style.border = 'none';
        iframe.src = schemeUrl;
        document.body.appendChild(iframe);
        
        // 设置超时检测应用是否成功打开
        const timeout = setTimeout(() => {
            // URL Scheme失败，回退到Universal Links
            if (document.body.contains(iframe)) {
                document.body.removeChild(iframe);
            }
            
            // Step 2: 尝试Universal Links (m.me链接)
            window.location.href = urls.mMeUrl;
            
            // 设置二级回退：Universal Links也失败则打开网页版
            setTimeout(() => {
                // Step 3: 最后回退到网页版
                window.open(urls.webUrl, '_blank');
            }, 3000);
        }, 1500);
        
        // 监听页面可见性变化（表示应用成功打开）
        const handleVisibilityChange = () => {
            if (document.hidden) {
                // 页面被隐藏，说明应用已成功打开
                clearTimeout(timeout);
                if (document.body.contains(iframe)) {
                    document.body.removeChild(iframe);
                }
            }
        };
        
        document.addEventListener('visibilitychange', handleVisibilityChange, { once: true });
        
        // 清理：3秒后移除事件监听和iframe（防止内存泄漏）
        setTimeout(() => {
            document.removeEventListener('visibilitychange', handleVisibilityChange);
            if (document.body.contains(iframe)) {
                document.body.removeChild(iframe);
            }
        }, 5000);
    }

    /**
     * Android专用：使用Intent打开Messenger应用
     */
    tryOpenAndroidMessenger(urls) {
        const mMeUrl = urls.mMeUrl;
        
        // 使用Intent Scheme直接打开Messenger应用
        const intentUrl = `intent://user-thread/${this.DEFAULT_PAGE_ID}#Intent;scheme=fb-messenger;package=com.facebook.orca;end`;
        window.location.href = intentUrl;
        
        // 设置回退：如果Intent失败，使用m.me链接
        setTimeout(() => {
            window.location.href = mMeUrl;
        }, 1500);
    }

    /**
     * 获取可复制的Messenger链接（带预填充消息）
     * @param {object} formData - 表单数据对象
     * @returns {string} 可分享的链接
     */
    getShareableLink(formData) {
        const message = this.buildMessage(formData);
        return `https://m.me/${this.DEFAULT_PAGE_ID}?text=${message}`;
    }
}

// 全局实例
window.messengerManager = new MessengerManager();

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

/**
 * Auto-redirect to Messenger after 1 second delay
 * Called on thank-you.html page load
 */
window.autoRedirectToMessenger = function() {
    const record = csvManager.getLatestRecord();
    
    if (record) {
        // Auto-redirect after 1 second
        setTimeout(function() {
            messengerManager.openMessenger(record);
        }, 1000);
    } else {
        // No form data available, redirect anyway
        setTimeout(function() {
            messengerManager.openMessenger({});
        }, 1000);
    }
};

/**
 * Start Messenger chat manually via button click
 * Detects platform and redirects accordingly
 */
window.startMessengerChat = function() {
    const record = csvManager.getLatestRecord();
    const formData = record || {};
    
    // Detect platform
    const platform = messengerManager.detectPlatform();
    
    if (platform === 'ios' || platform === 'android') {
        // Mobile: Try to open Messenger app
        messengerManager.openMessenger(formData);
        
        // Show notification about app
        // const loadingIndicator = document.getElementById('loading-indicator');
        // if (loadingIndicator) {
        //     loadingIndicator.innerHTML = `
        //         <div style="padding: 15px; background: #d4edda; border: 1px solid #c3e6cb; border-radius: 6px; color: #155724; margin-top: 20px;">
        //             <p style="margin: 0;">Opening Messenger app...</p>
        //         </div>
        //     `;
        // }
    } else {
        // Desktop/Web: Open Messenger webpage
        const urls = messengerManager.buildURL(formData);
        window.open(urls.webUrl, '_blank');
        
        // Show notification
        // const loadingIndicator = document.getElementById('loading-indicator');
        // if (loadingIndicator) {
        //     loadingIndicator.innerHTML = `
        //         <div style="padding: 15px; background: #d4edda; border: 1px solid #c3e6cb; border-radius: 6px; color: #155724; margin-top: 20px;">
        //             <p style="margin: 0;">Messenger opened in new tab. If it didn't open, <a href="${urls.webUrl}" target="_blank" style="color: #007bff;">click here</a>.</p>
        //         </div>
        //     `;
        // }
    }
};
