<?php

// Intentamos primero saber si se ha utilizado un proxy para acceder a la página,
// y si éste ha indicado en alguna cabecera la IP real del usuario.
if (getenv('HTTP_CLIENT_IP')) {
  $ip = getenv('HTTP_CLIENT_IP');
} elseif (getenv('HTTP_X_FORWARDED_FOR')) {
  $ip = getenv('HTTP_X_FORWARDED_FOR');
} elseif (getenv('HTTP_X_FORWARDED')) {
  $ip = getenv('HTTP_X_FORWARDED');
} elseif (getenv('HTTP_FORWARDED_FOR')) {
  $ip = getenv('HTTP_FORWARDED_FOR');
} elseif (getenv('HTTP_FORWARDED')) {
  $ip = getenv('HTTP_FORWARDED');
} else {
  // Método por defecto de obtener la IP del usuario
  // Si se utiliza un proxy, esto nos daría la IP del proxy
  // y no la IP real del usuario.
  $ip = $_SERVER['REMOTE_ADDR'];
}

echo "Su IP parece ser: ".$ip;
?>

