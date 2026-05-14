<?php
require_once __DIR__ . '/config.php';
require_once __DIR__ . '/middleware.php';

$method = $_SERVER['REQUEST_METHOD'];

if ($method === 'OPTIONS') {
    http_response_code(200);
    exit();
}

$pdo = getDBConnection();

switch ($method) {
    case 'GET':
        handleGet($pdo);
        break;
    case 'POST':
        handlePost($pdo);
        break;
    case 'PUT':
        handlePut($pdo);
        break;
    case 'DELETE':
        handleDelete($pdo);
        break;
    default:
        jsonResponse(['error' => 'Method not allowed'], 405);
}

function handleGet($pdo) {
    $id = $_GET['id'] ?? null;

    if ($id) {
        requireAuth();
        $stmt = $pdo->prepare("SELECT * FROM form_submissions WHERE id = ?");
        $stmt->execute([$id]);
        $record = $stmt->fetch();
        if (!$record) {
            jsonResponse(['error' => 'Record not found'], 404);
        }
        jsonResponse($record);
    }

    $authPayload = verifyJWT(getAuthToken());
    if (!$authPayload) {
        jsonResponse(['error' => 'Authentication required'], 401);
    }

    $page = max(1, intval($_GET['page'] ?? 1));
    $limit = min(100, max(1, intval($_GET['limit'] ?? 50)));
    $offset = ($page - 1) * $limit;

    $countStmt = $pdo->query("SELECT COUNT(*) as total FROM form_submissions");
    $total = $countStmt->fetch()['total'];

    $stmt = $pdo->prepare("SELECT * FROM form_submissions ORDER BY created_at DESC LIMIT ? OFFSET ?");
    $stmt->execute([$limit, $offset]);
    $records = $stmt->fetchAll();

    jsonResponse([
        'data' => $records,
        'total' => intval($total),
        'page' => $page,
        'limit' => $limit,
        'totalPages' => ceil($total / $limit)
    ]);
}

function handlePost($pdo) {
    $input = getInput();

    if (!$input) {
        jsonResponse(['error' => 'No data provided'], 400);
    }

    $required = ['name', 'email', 'phone', 'platform', 'amount'];
    foreach ($required as $field) {
        if (!isset($input[$field]) || empty(trim($input[$field]))) {
            jsonResponse(['error' => "Field '$field' is required"], 400);
        }
    }

    $ip = getClientIP();

    $stmt = $pdo->prepare("INSERT INTO form_submissions (name, email, phone, platform, amount, ip) VALUES (?, ?, ?, ?, ?, ?)");
    $stmt->execute([
        trim($input['name']),
        trim($input['email']),
        trim($input['phone']),
        trim($input['platform']),
        trim($input['amount']),
        $ip
    ]);

    $id = $pdo->lastInsertId();

    $stmt = $pdo->prepare("SELECT * FROM form_submissions WHERE id = ?");
    $stmt->execute([$id]);
    $record = $stmt->fetch();

    jsonResponse($record, 201);
}

function handlePut($pdo) {
    $authPayload = requireAuth();

    $id = $_GET['id'] ?? null;
    if (!$id) {
        jsonResponse(['error' => 'Record ID is required'], 400);
    }

    $input = getInput();
    if (!$input) {
        jsonResponse(['error' => 'No data provided'], 400);
    }

    $fields = [];
    $values = [];
    $allowed = ['name', 'email', 'phone', 'platform', 'amount'];

    foreach ($allowed as $field) {
        if (isset($input[$field])) {
            $fields[] = "$field = ?";
            $values[] = trim($input[$field]);
        }
    }

    if (empty($fields)) {
        jsonResponse(['error' => 'No valid fields to update'], 400);
    }

    $values[] = $id;
    $sql = "UPDATE form_submissions SET " . implode(', ', $fields) . " WHERE id = ?";
    $stmt = $pdo->prepare($sql);
    $stmt->execute($values);

    if ($stmt->rowCount() === 0) {
        jsonResponse(['error' => 'Record not found or no changes made'], 404);
    }

    $stmt = $pdo->prepare("SELECT * FROM form_submissions WHERE id = ?");
    $stmt->execute([$id]);
    $record = $stmt->fetch();

    jsonResponse($record);
}

function handleDelete($pdo) {
    $authPayload = requireAuth();

    $id = $_GET['id'] ?? null;
    if (!$id) {
        jsonResponse(['error' => 'Record ID is required'], 400);
    }

    $stmt = $pdo->prepare("DELETE FROM form_submissions WHERE id = ?");
    $stmt->execute([$id]);

    if ($stmt->rowCount() === 0) {
        jsonResponse(['error' => 'Record not found'], 404);
    }

    jsonResponse(['success' => true, 'message' => 'Record deleted']);
}