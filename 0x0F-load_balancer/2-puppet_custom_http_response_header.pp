# Add a custom HTTP header with Puppet

exec {'Update APT manager':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['Install Nginx'],
}

exec {'Install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['Add header in nginx configuration'],
}

exec { 'Add header in nginx configuration':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  before      => Exec['Restart nginx'],
}

exec { 'Restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
