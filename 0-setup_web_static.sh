#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update -y
sudo apt-get install nginx -y
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo -e '<html>\n\t<head>\n\t</head>\n\t<body>\n\tHolberton School\n\t</body>\n\t</html>' > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/
sed -i "/server;/a \\t location /static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-enabled/default
sudo service nginx restart
