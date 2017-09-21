# fixes typo in /var/www/html/wp-settings

exec { 'fix typo':
command  => 'sed \'s/class-wp-locale.phpp/class-wp-locale.php/\' /var/www/html/wp-settings.php',
path     => ['/usr/bin', '/bin', '/usr/sbin'],
provider => 'shell'
}
