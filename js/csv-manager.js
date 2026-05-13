class CSVManager {
    constructor() {
        this.API_BASE = '/api';
    }

    async getData(page = 1, limit = 50) {
        try {
            const token = localStorage.getItem('levinlaw_admin_token');
            const headers = {};
            if (token) {
                headers['Authorization'] = 'Bearer ' + token;
            }
            const response = await fetch(this.API_BASE + '/records.php?page=' + page + '&limit=' + limit, {
                method: 'GET',
                headers: headers
            });
            if (!response.ok) {
                throw new Error('Failed to fetch data');
            }
            const result = await response.json();
            return result;
        } catch (error) {
            console.error('Error fetching data:', error);
            return { data: [], total: 0, page: 1, limit: 50, totalPages: 0 };
        }
    }

    async addRecord(record) {
        try {
            const response = await fetch(this.API_BASE + '/records.php', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(record)
            });
            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.error || 'Failed to add record');
            }
            const newRecord = await response.json();
            return newRecord;
        } catch (error) {
            console.error('Error adding record:', error);
            throw error;
        }
    }

    async updateRecord(id, updatedData) {
        try {
            const token = localStorage.getItem('levinlaw_admin_token');
            const response = await fetch(this.API_BASE + '/records.php?id=' + id, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token
                },
                body: JSON.stringify(updatedData)
            });
            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.error || 'Failed to update record');
            }
            const record = await response.json();
            return record;
        } catch (error) {
            console.error('Error updating record:', error);
            throw error;
        }
    }

    async deleteRecord(id) {
        try {
            const token = localStorage.getItem('levinlaw_admin_token');
            const response = await fetch(this.API_BASE + '/records.php?id=' + id, {
                method: 'DELETE',
                headers: {
                    'Authorization': 'Bearer ' + token
                }
            });
            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.error || 'Failed to delete record');
            }
            return true;
        } catch (error) {
            console.error('Error deleting record:', error);
            throw error;
        }
    }

    async exportCSV() {
        try {
            const token = localStorage.getItem('levinlaw_admin_token');
            const response = await fetch(this.API_BASE + '/export.php', {
                method: 'GET',
                headers: {
                    'Authorization': 'Bearer ' + token
                }
            });
            if (!response.ok) {
                throw new Error('Failed to export CSV');
            }
            const blob = await response.blob();
            const url = URL.createObjectURL(blob);
            const link = document.createElement('a');
            const now = new Date();
            const timeStr = now.getFullYear() +
                String(now.getMonth() + 1).padStart(2, '0') +
                String(now.getDate()).padStart(2, '0') +
                String(now.getHours()).padStart(2, '0') +
                String(now.getMinutes()).padStart(2, '0') +
                String(now.getSeconds()).padStart(2, '0');
            link.href = url;
            link.download = timeStr + '_levinlaw.csv';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            URL.revokeObjectURL(url);
        } catch (error) {
            console.error('Error exporting CSV:', error);
            alert('Export failed: ' + error.message);
        }
    }
}

window.csvManager = new CSVManager();

class AuthManager {
    constructor() {
        this.AUTH_KEY = 'levinlaw_admin_auth';
        this.TOKEN_KEY = 'levinlaw_admin_token';
        this.API_BASE = '/api';
    }

    async login(username, password) {
        try {
            const response = await fetch(this.API_BASE + '/auth.php', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username: username, password: password })
            });
            if (!response.ok) {
                return false;
            }
            const result = await response.json();
            if (result.success && result.token) {
                localStorage.setItem(this.AUTH_KEY, 'true');
                localStorage.setItem(this.TOKEN_KEY, result.token);
                return true;
            }
            return false;
        } catch (error) {
            console.error('Login error:', error);
            return false;
        }
    }

    isLoggedIn() {
        return localStorage.getItem(this.AUTH_KEY) === 'true';
    }

    logout() {
        localStorage.removeItem(this.AUTH_KEY);
        localStorage.removeItem(this.TOKEN_KEY);
    }

    getToken() {
        return localStorage.getItem(this.TOKEN_KEY);
    }
}

window.authManager = new AuthManager();

class FormValidator {
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

    static showErrors(formElement, errors) {
        this.clearErrors(formElement);

        for (const [field, message] of Object.entries(errors)) {
            const input = formElement.querySelector('[name="' + field + '"], #edit-' + field);
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

    static clearErrors(formElement) {
        formElement.querySelectorAll('.input-error').forEach(function(input) {
            input.classList.remove('input-error');
        });
        formElement.querySelectorAll('.error-message').forEach(function(el) {
            el.remove();
        });
    }

    static addRealtimeValidation(formElement) {
        const inputs = formElement.querySelectorAll('input');
        const self = this;
        inputs.forEach(function(input) {
            input.addEventListener('blur', function() {
                const fieldName = input.name || input.id.replace('edit-', '');
                const value = input.value;

                let result;
                switch (fieldName) {
                    case 'name':
                        result = self.validateName(value);
                        break;
                    case 'email':
                        result = self.validateEmail(value);
                        break;
                    case 'phone':
                        result = self.validatePhone(value);
                        break;
                    case 'platform':
                        result = self.validatePlatform(value);
                        break;
                    case 'amount':
                        result = self.validateAmount(value);
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

            input.addEventListener('input', function() {
                input.classList.remove('input-error');
                const formGroup = input.closest('.form-group');
                const existingError = formGroup ? formGroup.querySelector('.error-message') : null;
                if (existingError) existingError.remove();
            });
        });
    }
}

window.FormValidator = FormValidator;

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

    const validation = FormValidator.validateForm(data);
    if (!validation.valid) {
        FormValidator.showErrors(form, validation.errors);

        const firstError = form.querySelector('.input-error');
        if (firstError) {
            firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
            firstError.focus();
        }
        return;
    }

    FormValidator.clearErrors(form);

    csvManager.addRecord(data).then(function() {
        window.location.href = 'thank-you.html';
    }).catch(function(error) {
        alert('Submission failed, please try again: ' + error.message);
    });
};

window.initContactForm = function() {
    const form = document.getElementById('contact-form');
    if (form) {
        FormValidator.addRealtimeValidation(form);
    }
};

window.escapeHtml = function(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
};

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
