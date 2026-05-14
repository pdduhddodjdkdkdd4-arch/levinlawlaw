<?php
require_once __DIR__ . '/config.php';

function generateJWT($payload) {
    $header = base64_encode(json_encode(['typ' => 'JWT', 'alg' => 'HS256']));
    $payload['exp'] = time() + 86400;
    $payloadEncoded = base64_encode(json_encode($payload));
    $signature = base64_encode(hash_hmac('sha256', "$header.$payloadEncoded", JWT_SECRET, true));
    return "$header.$payloadEncoded.$signature";
}

function verifyJWT($token) {
    if (!$token) return false;
    $parts = explode('.', $token);
    if (count($parts) !== 3) return false;
    list($header, $payload, $signature) = $parts;
    $expectedSignature = base64_encode(hash_hmac('sha256', "$header.$payload", JWT_SECRET, true));
    if (!hash_equals($expectedSignature, $signature)) return false;
    $payloadData = json_decode(base64_decode($payload), true);
    if (!$payloadData || !isset($payloadData['exp'])) return false;
    if ($payloadData['exp'] < time()) return false;
    return $payloadData;
}

function getAuthToken() {
    $headers = getallheaders();
    $authHeader = $headers['Authorization'] ?? $headers['authorization'] ?? '';
    if (preg_match('/Bearer\s+(.*)$/i', $authHeader, $matches)) {
        return $matches[1];
    }
    return $_GET['token'] ?? null;
}

function requireAuth() {
    $token = getAuthToken();
    $payload = verifyJWT($token);
    if (!$payload) {
        jsonResponse(['error' => 'Unauthorized'], 401);
    }
    return $payload;
}