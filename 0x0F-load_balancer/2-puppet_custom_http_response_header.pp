# Add a custom HTTP header with Puppet

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

file { '/var/www/html/404.html':
    ensure  => file,
    content => 'Ceci n'est pas une page'
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => @("EOF"
    server {
        listen 80;
        listen [::]:80;
        server_name _;
        error_page 404 /404.html;
        add_header X-Served-By $::hostname;
        location / {
            root /var/www/html;
            index index.html;
        }
        location /redirect_me {
            return 301 https://www.google.com/;
        }
        location /404 {
            root /var/www/html;
            internal;
        }
    }
  EOF
  ),
  require => Package['nginx'],
  notify  => Service['nginx']
}
