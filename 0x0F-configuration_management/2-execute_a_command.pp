#kills the killmenow program
exec { 'kills killmenow':
command  => 'pkill -f killmenow',
path     => '/usr/bin',
provider => 'shell'
}
