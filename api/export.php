<?php
require_once __DIR__ . '/config.php';
require_once __DIR__ . '/middleware.php';

$authPayload = requireAuth();

$pdo = getDBConnection();

$stmt = $pdo->query("SELECT * FROM form_submissions ORDER BY created_at DESC");
$records = $stmt->fetchAll();

$filename = date('Ymd_His') . '_levinlaw.csv';

header('Content-Type: text/csv; charset=utf-8');
header('Content-Disposition: attachment; filename="' . $filename . '"');

$output = fopen('php://output', 'w');

fprintf($output, chr(0xEF) . chr(0xBB) . chr(0xBF));

fputcsv($output, ['ID', 'Name', 'Email', 'Phone', 'Platform', 'Amount', 'Submitted At', 'IP']);

foreach ($records as $record) {
    fputcsv($output, [
        $record['id'],
        $record['name'],
        $record['email'],
        $record['phone'],
        $record['platform'],
        $record['amount'],
        $record['created_at'],
        $record['ip']
    ]);
}

fclose($output);
exit();
