# Install Nginx web server

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!'
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => 'server {
    listen 80;
    listen [::]:80;
    server_name _;
    location / {
        root /var/www/html;
        index index.html;
    }
    location /redirect_me {
        return 301 https://www.google.com/;
    }
}',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
