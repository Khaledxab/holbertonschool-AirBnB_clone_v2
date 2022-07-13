#!/usr/bin/env bash
# set up web servers 
sudo su
apt-get update -y
apt-get updgrade -y
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
echo "Hello KH" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current 
chown ubuntu:ubuntu -hR /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart