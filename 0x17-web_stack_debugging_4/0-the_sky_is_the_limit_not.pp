# Fix for nginx
exec { 'fix nginx':
command  => 'echo ULIMIT="-n 2000" > /etc/default/nginx',
path     => '/usr/bin',
provider => 'shell'
}

