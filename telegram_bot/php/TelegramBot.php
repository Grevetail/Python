$TOKEN = file_get_contents('telegram_temp_todo.txt', FILE_USE_INCLUDE_PATH);
//const BASE_URL = 'https://api.telegram.org/bot'.$TOKEN.'/';
$BASE_URL = 'https://api.telegram.org/bot'.$TOKEN.'/setWebhook?url=https://work-example-site.netlify.app/php/';

$update = json_decode(file_get_contents('php://input'));

file_put_contents(__DIR__.'/logs.txt', print_r($update, 1), FILE_APPEND);