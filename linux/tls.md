# Using certbot to obtain a standalone certificate and enable TLS for web server


### Installing certbot
```console
apt install software-properties-common
add-apt-repository ppa:certbot/certbot
apt-get install certbot
```
### Requesting a new certificate
```console
certbot certonly --standalone --preferred-challenges http --agree-tos --email me@alinaderiparizi.com -d admin.alinaderiparizi.com
```

### Renewing the certificate
```console
certbot renew --force-renewal
```