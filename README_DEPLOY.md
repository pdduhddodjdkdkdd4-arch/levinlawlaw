# Elementor 静态网站部署指南

## 📋 项目概述
这是一个从 WordPress + Elementor 网站导出的纯静态 HTML 网站，可以独立部署到任何静态文件服务器。

## ✅ 已修复内容
- ✅ 所有HTML文件路径已修复（绝对路径 → 相对路径）
- ✅ Elementor CSS 和 JS 资源已完整保存在 `wp-content/cache/` 目录
- ✅ `ultimate-team-carousel` 和 `elementor-section` 相关资源已就绪

---

## 🖥️ 本地预览方式

### 方法1：使用批处理脚本（Windows推荐）
1. 双击 `start_server.bat` 文件
2. 在浏览器中访问：`https://localhost:8000`
3. 查看首页或任意页面

### 方法2：使用Python HTTP服务器
```bash
# 进入项目目录
cd c:\Users\电脑\Desktop\us.com

# 启动服务器
python -m http.server 8000
```

### 方法3：使用Node.js
```bash
npm install -g http-server
http-server -p 8000
```

---

## 🚀 部署到服务器

### 方案A：使用静态文件服务器（Nginx/Apache）

#### Nginx 配置示例
```nginx
server {
    listen 80;
    server_name your-domain.com;
    root /var/www/us.com;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

#### Apache .htaccess 配置
```apache
DirectoryIndex index.html
RewriteEngine On
```

### 方案B：托管到静态网站服务
- **Vercel** / **Netlify** - 免费托管，支持自定义域名
- **GitHub Pages** - 免费托管
- **阿里云OSS/CDN** - 国内快速访问
- **腾讯云COS** - 国内快速访问

### 方案C：传统虚拟主机
直接上传所有文件到网站根目录即可。

---

## 📁 项目结构
```
us.com/
├── index.html                  # 首页
├── about-us.html              # 关于我们
├── teams.html                 # 团队页面（含团队轮播）
├── services.html              # 服务页面
├── ... (其他22个HTML页面)
├── wp-content/
│   ├── cache/                 # 缓存的CSS和JS（重要！）
│   │   └── wpo-minify/
│   │       └── 1776568923/
│   │           └── assets/    # Elementor、Bootstrap等资源
│   ├── plugins/               # 插件资源
│   ├── themes/                # 主题资源
│   └── uploads/               # 上传的图片
├── start_server.bat           # Windows启动脚本
└── README_DEPLOY.md           # 本文件
```

---

## ⚠️ 重要注意事项

### 1. 路径说明
- 所有资源链接已改为**相对路径**
- 支持本地预览和服务器部署
- 无需修改代码即可在任何环境运行

### 2. 必须上传的文件
确保以下内容完整上传到服务器：
- ✅ 所有 `.html` 文件
- ✅ 整个 `wp-content` 文件夹（包含缓存、图片、资源）
- ✅ `static` 文件夹（如果有）

### 3. Elementor 功能说明
这是静态导出版本，以下功能正常：
- ✅ Elementor 布局和样式
- ✅ 团队轮播组件 (ultimate-team-carousel)
- ✅ 响应式设计
- ✅ 动画效果
- ✅ 图片展示

以下功能不可用（静态网站特性）：
- ❌ 动态表单提交（需后端支持）
- ❌ 搜索功能（需后端支持）
- ❌ 用户登录/注册

---

## 🔧 故障排除

### 问题1：页面样式丢失
**解决**：检查 `wp-content/cache/` 文件夹是否完整上传

### 问题2：图片不显示
**解决**：检查 `wp-content/uploads/` 文件夹是否存在

### 问题3：本地打开HTML文件样式异常
**原因**：浏览器的CORS安全策略
**解决**：必须使用HTTP服务器（如上述方法1-3），不能直接双击HTML文件

---

## 📞 需要帮助？
如有问题，检查：
1. 文件权限是否正确
2. 路径是否大小写敏感（Linux服务器）
3. 浏览器控制台是否有错误 (F12)

---

**祝您部署顺利！** 🎉
