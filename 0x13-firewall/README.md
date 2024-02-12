# 0x13. Firewall

## What is a firewall

A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. A firewall typically establishes a barrier between a trusted network and an untrusted network, such as the Internet

[More info](https://en.wikipedia.org/wiki/Firewall_%28computing%29)

## Tasks

### 0-block_all_incoming_traffic_but

Configure `ufw` so that it blocks all incoming traffic, except the following TCP ports:

- `22` (SSH)
- `443` (HTTPS SSL)
- `80` (HTTP)

