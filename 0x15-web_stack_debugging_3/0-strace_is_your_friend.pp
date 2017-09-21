# fixes typo in /var/www/html/wp-settings

exec { 'fix typo':
command  => 'sed -i \'s/class-wp-locale.phpp/class-wp-locale.php/\' /var/www/html/wp-settings.php; service apache2 restart',
path     => ['/usr/bin', '/bin', '/usr/sbin'],
provider => 'shell'
}
