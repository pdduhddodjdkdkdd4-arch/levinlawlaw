<?php
require_once __DIR__ . '/config.php';

$pdo = getDBConnection();

$pdo->exec("CREATE TABLE IF NOT EXISTS form_submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    platform VARCHAR(255) NOT NULL,
    amount VARCHAR(100) NOT NULL,
    ip VARCHAR(45) DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci");

echo "Table 'form_submissions' created successfully.\n";

$pdo->exec("CREATE TABLE IF NOT EXISTS admin_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci");

echo "Table 'admin_users' created successfully.\n";

$stmt = $pdo->prepare("SELECT COUNT(*) FROM admin_users WHERE username = ?");
$stmt->execute(['admin_5_9']);
$exists = $stmt->fetchColumn();

if (!$exists) {
    $passwordHash = password_hash('admin@2659Levinlaw', PASSWORD_DEFAULT);
    $stmt = $pdo->prepare("INSERT INTO admin_users (username, password_hash) VALUES (?, ?)");
    $stmt->execute(['admin_5_9', $passwordHash]);
    echo "Default admin user 'admin_5_9' created successfully.\n";
} else {
    echo "Admin user 'admin_5_9' already exists, skipping.\n";
}

echo "\nDatabase initialization complete!\n";