#writes a 'Hello Holberton' in /var/www/html

file { 'create_index':
ensure  =>  file,
path    => '/var/www/html/index.html',
content => 'Hello Holberton'
}
