# Create a manifest that kills a process named killmenow
exec {'Execute a command':
    path     => ['/usr/bin', '/bin'],
    provider => shell,
    command  => 'pkill -f killmenow'
}
