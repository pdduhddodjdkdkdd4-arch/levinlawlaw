# CSV 迁移 MySQL 数据库 Spec

## Why
当前表单数据存储在浏览器 localStorage 中（通过 CSVManager 类），存在以下问题：
1. 数据仅存在客户端浏览器中，换设备/清缓存即丢失
2. 无法多用户共享数据，管理员无法远程查看
3. localStorage 容量有限（约5MB），数据量大时性能下降
4. 无法实现真正的服务端数据持久化和安全管控

## 部署环境约束
- **服务器**: GoDaddy cPanel 共享主机
- **后端语言**: PHP（cPanel 原生支持，无需额外配置）
- **数据库**: MySQL（cPanel 自带，通过 MySQL Database Wizard 创建）
- **数据库管理**: phpMyAdmin（cPanel 内置）
- **注意**: cPanel 共享主机通常不支持 Node.js，因此采用 PHP 方案

## What Changes
- 新增后端 API 服务（PHP），提供表单数据的 CRUD 接口
- 新增 MySQL 数据库表结构，替代 localStorage 存储
- 修改前端 `csv-manager.js` 中的 `CSVManager` 类，将数据操作从 localStorage 改为调用后端 PHP API
- 修改前端 `AuthManager` 类，将登录验证从硬编码改为后端 PHP 验证
- 保留 CSV 导出功能（从数据库查询后导出）

## Impact
- Affected code: `js/csv-manager.js`（核心修改）、`admin_26_5_9.html`（管理后台）、15个引用 csv-manager.js 的 HTML 页面
- 新增文件：后端服务（`api/` 目录）、数据库配置
- **BREAKING**: 前端不再能独立运行，必须部署到支持 PHP 的服务器

## 需要用户提供的信息

### 必需信息（从 GoDaddy cPanel 获取）
1. **MySQL 数据库信息**（在 cPanel → MySQL Databases 中创建）
   - 数据库名：例如 `levinlaw_db`
   - 数据库用户名
   - 数据库密码
   - 主机地址（GoDaddy 通常为 `localhost`）

2. **cPanel 文件管理**
   - 网站根目录路径（通常为 `public_html/`）
   - FTP/cPanel 登录信息（用于上传文件）

3. **管理员账户**
   - 管理员用户名和密码（替代当前硬编码的 `admin_5_9` / `admin@2659Levinlaw`）

### 可选信息
- 是否需要多个管理员账户？
- 是否需要数据备份策略？
- 是否需要 IP 获取功能（当前是模拟的 `127.0.0.1`）？

## ADDED Requirements

### Requirement: PHP 后端 API 服务
系统 SHALL 提供基于 PHP 的 RESTful API 服务，兼容 GoDaddy cPanel 共享主机环境，包含以下端点：

- `POST /api/records.php` - 新增表单记录
- `GET /api/records.php` - 获取所有记录（需认证）
- `GET /api/records.php?id=N` - 获取单条记录（需认证）
- `PUT /api/records.php?id=N` - 更新记录（需认证）
- `DELETE /api/records.php?id=N` - 删除记录（需认证）
- `POST /api/auth.php` - 管理员登录
- `GET /api/export.php` - 导出 CSV（需认证）

#### Scenario: 用户提交表单
- **WHEN** 用户在前端页面提交联系表单
- **THEN** 前端调用 `POST /api/records.php`，PHP 后端将数据写入 MySQL 并返回新记录

#### Scenario: 管理员登录
- **WHEN** 管理员输入用户名和密码
- **THEN** PHP 后端验证凭据，返回 JWT token，前端存储 token 用于后续请求

### Requirement: MySQL 数据库表
系统 SHALL 创建以下数据库表（可通过 phpMyAdmin 执行）：

```sql
CREATE TABLE form_submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    platform VARCHAR(255) NOT NULL,
    amount VARCHAR(100) NOT NULL,
    ip VARCHAR(45) DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE admin_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Requirement: PHP 项目结构
系统 SHALL 创建以下目录结构（部署到网站根目录下）：

```
api/
├── config.php          # 数据库连接配置
├── auth.php            # 登录认证端点
├── records.php         # 表单记录 CRUD 端点
├── export.php          # CSV 导出端点
├── middleware.php       # JWT 验证中间件
└── .htaccess           # Apache URL 重写和安全规则
```

### Requirement: 安全措施
系统 SHALL 实现以下安全措施：
- 数据库配置文件放在 web 根目录外或通过 .htaccess 保护
- 所有 API 输入使用 prepared statements 防止 SQL 注入
- 管理员密码使用 `password_hash()` 加密存储
- CORS 配置限制为当前域名
- .htaccess 阻止直接访问配置文件

### Requirement: 前端数据层迁移
系统 SHALL 将 `CSVManager` 类的数据操作从 localStorage 迁移到后端 PHP API 调用，保持相同的公共接口（addRecord, getData, updateRecord, deleteRecord, exportCSV）。

#### Scenario: 兼容性
- **WHEN** 前端调用 `csvManager.addRecord(data)`
- **THEN** 数据通过 fetch API 发送到 PHP 后端存储到 MySQL，而非 localStorage

## MODIFIED Requirements

### Requirement: 认证系统
原 `AuthManager` 类的硬编码凭据验证 SHALL 改为调用后端 `POST /api/auth.php`，使用 JWT token 进行会话管理。

## REMOVED Requirements

### Requirement: localStorage 数据存储
**Reason**: 迁移到 MySQL 后不再需要 localStorage 作为主存储
**Migration**: 保留 localStorage 仅作为 JWT token 存储，不再存储表单数据

### Requirement: CSV 导入功能
**Reason**: 数据已持久化在数据库中，不再需要从 CSV 导入恢复数据
**Migration**: 管理后台可通过数据库直接查看历史数据
