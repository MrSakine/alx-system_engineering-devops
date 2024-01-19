# Create a manifest that kills a process named killmenow
exec {'Execute a command':
    command => 'pkill killmenow'
}
