# 0x0A. Configuration management

## Puppet

Puppet provides tools to automate managing your infrastructure. Puppet is an open source product with a vibrant community of users and contributors. You can get involved by fixing bugs, influencing new feature direction, publishing your modules, and engaging with the community to share knowledge and expertise

## Note on Versioning

Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.
Install puppet

```bash
apt-get install -y ruby=1:2.7+1 --allow-downgrades
apt-get install -y ruby-augeas
apt-get install -y ruby-shadow
apt-get install -y puppet
```

You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

Puppet 5 Docs
Install puppet-lint

```bash
gem install puppet-lint
```

