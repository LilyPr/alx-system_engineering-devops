# Fix 500 error when a GET HTTP method is requested to Apache web server

exec {'replace':
  provider => ubuntu,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
