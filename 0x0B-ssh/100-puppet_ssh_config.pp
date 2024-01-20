# Client configuration file

exec { 'Turn off passwd auth':
  path    =>  ['/usr/bin', '/bin'],
  command =>  'echo "PasswordAuthentication no" >> /etc/ssh/sshd_config'
}

exec { 'Declare identity file':
  path    =>  ['/usr/bin', '/bin'],
  command =>  'echo -e "\tIdentityFile ~/.ssh/school" >> /etc/ssh/sshd_config'
}
