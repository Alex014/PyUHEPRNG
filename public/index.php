<?php
$mode = '';

foreach ($_GET as $key => $value) {
    $mode = $key;
    break;
}

switch ($mode) {
    case 's':
        header('Content-Type: text/plain; charset=utf-8');
        echo file_get_contents('../out/seed.txt');
        break;
    case 'sb':
        header('Content-Type: text/plain; charset=utf-8');
        echo file_get_contents('../out/seed-big.txt');
        break;
    case 'n':
        header('Content-Type: application/json; charset=utf-8');
        echo file_get_contents('../out/numbers.json');
        break;
    case 'nb':
        header('Content-Type: application/json; charset=utf-8');
        echo file_get_contents('../out/numbers-big.json');
        break;
    default:
    echo "Usage: \n";
    echo "?s - seed   \n";
    echo "?sb - big seed   \n";
    echo "?n - numbers   \n";
    echo "?nb - big numbers   \n";
}
