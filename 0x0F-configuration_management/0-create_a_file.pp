#writes 'I love Puppet' in /tmp/holberton
file { 'create_a_file':
ensure    => file,
path      => '/tmp/holberton',
mode      => '0744',
group     => www-data,
owner     => www-data,
content   => 'I love Puppet'
}
