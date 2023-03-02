# Fixes the typo extension in wp-setting file
exec { '/usr/bin/env sed -i "s/phpp/php/g" /var/www/html/wp-settings.php': }}
