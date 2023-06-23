#kills the killmenow file

exec {'pkill -f killmenow':
	path => '/usr/bin/:/usr/local/bin/:/bin/'
}
