# Tasks

- [ ] Task 1: 创建 PHP 后端项目结构
  - [ ] SubTask 1.1: 创建 api/ 目录及文件（config.php, auth.php, records.php, export.php, middleware.php, .htaccess）
  - [ ] SubTask 1.2: 编写 config.php（数据库连接配置，使用环境变量或配置常量）
  - [ ] SubTask 1.3: 编写 .htaccess（CORS 头、安全规则、阻止直接访问配置文件）

- [ ] Task 2: 创建数据库初始化脚本
  - [ ] SubTask 2.1: 编写 SQL 建表脚本（form_submissions、admin_users）
  - [ ] SubTask 2.2: 编写 PHP 初始化脚本（创建表、插入默认管理员账户，密码使用 password_hash 加密）

- [ ] Task 3: 实现后端 PHP API
  - [ ] SubTask 3.1: 编写 middleware.php（JWT 生成与验证，使用 Firebase JWT 或简单 token 方案）
  - [ ] SubTask 3.2: 编写 auth.php（登录认证端点，验证用户名密码，返回 token）
  - [ ] SubTask 3.3: 编写 records.php（CRUD 端点：增删改查，使用 prepared statements 防注入）
  - [ ] SubTask 3.4: 编写 export.php（CSV 导出端点，从数据库查询后生成 CSV 下载）
  - [ ] SubTask 3.5: 在 records.php 中实现 IP 获取（从 $_SERVER 获取客户端 IP）

- [ ] Task 4: 修改前端数据层
  - [ ] SubTask 4.1: 重写 CSVManager 类，将 localStorage 操作改为 fetch 调用 PHP API
  - [ ] SubTask 4.2: 重写 AuthManager 类，将硬编码验证改为调用 auth.php API + JWT
  - [ ] SubTask 4.3: 保留 CSV 导出功能（改为从 API 获取数据后导出，或直接跳转到 export.php 下载）

- [ ] Task 5: 修改管理后台页面
  - [ ] SubTask 5.1: 更新 admin_26_5_9.html 中的数据加载逻辑（从 API 获取）
  - [ ] SubTask 5.2: 更新登录流程（调用 auth.php API）

- [ ] Task 6: 部署指南与测试
  - [ ] SubTask 6.1: 编写 cPanel 部署步骤说明（创建数据库、上传文件、运行初始化脚本）
  - [ ] SubTask 6.2: 本地测试表单提交流程
  - [ ] SubTask 6.3: 本地测试管理员登录和数据管理
  - [ ] SubTask 6.4: 本地测试 CSV 导出功能

# Task Dependencies
- [Task 2] depends on [Task 1]
- [Task 3] depends on [Task 2]
- [Task 4] depends on [Task 3]
- [Task 5] depends on [Task 4]
- [Task 6] depends on [Task 5]
