# Fix for nginx
exec { 'change nginx ulimit':
command  => 'echo ULIMIT="-n 2000" > /etc/default/nginx',
path     => '/usr/bin',
provider => 'shell'
}

exec { 'restart nginx':
command  => 'service nginx restart',
path     => '/usr/bin',
provider => 'shell'
}

