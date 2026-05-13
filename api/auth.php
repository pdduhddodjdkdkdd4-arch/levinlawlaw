<?php
require_once __DIR__ . '/config.php';
require_once __DIR__ . '/middleware.php';

$method = $_SERVER['REQUEST_METHOD'];

if ($method === 'OPTIONS') {
    http_response_code(200);
    exit();
}

if ($method !== 'POST') {
    jsonResponse(['error' => 'Method not allowed'], 405);
}

$input = getInput();

if (!$input || !isset($input['username']) || !isset($input['password'])) {
    jsonResponse(['error' => 'Username and password are required'], 400);
}

$pdo = getDBConnection();

$stmt = $pdo->prepare("SELECT id, username, password_hash FROM admin_users WHERE username = ?");
$stmt->execute([$input['username']]);
$user = $stmt->fetch();

if (!$user || !password_verify($input['password'], $user['password_hash'])) {
    jsonResponse(['error' => 'Invalid credentials'], 401);
}

$token = generateJWT([
    'user_id' => $user['id'],
    'username' => $user['username']
]);

jsonResponse([
    'success' => true,
    'token' => $token,
    'username' => $user['username']
]);
