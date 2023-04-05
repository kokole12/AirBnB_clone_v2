#!/usr/bin/env bash
# script that sets up deployment of webstatic
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow "Nginx HTTP"

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo
"<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s -f /data/we_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i 'listen 80 default_server/a \tlocation /hbnb_static {\n\t\t alias /data/web_static/current/; }' /etc/nginx/sites-enabled/default
sudo service nginx restart
