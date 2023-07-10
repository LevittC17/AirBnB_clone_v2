#!/usr/bin/env bash
# Set up a web server for the development of web_static
# Update and install nginx if not installed
sudo apt -y update
sudo apt install -y nginx

# Create directories and sub directories if they don't exist yet
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html

# Create a fake HTML file for testing Nginx configuration
cat <<EOF | sudo tee /data/web_static/current/index.html > /dev/null
<html>
  <head>
  </head>
  <body>
    Testing Nginx Configuration
  </body>
</html>
EOF

# Createa symbolic link to remove and recreate if not exists
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Write permmissions to user and group
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "44i \\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default

# Restart nginx service
service nginx restart
