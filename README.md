# wireguard-watchdog
Simple Python to watch over wireguard and keep the connection stable.

## ROADMAP

### v0.1

[ ] Create "watch" command, which receives a conf name (i.e. wg0) and watch over the peers that have endpoints;
[ ] Check for wg command;
[ ] Create config file where the user can map alternative endpoints for a given peer. The watchdog should be able to use these as alternative ips:ports to switch over in case of lost connection;
[ ] Create example config file;
[ ] Create help.
