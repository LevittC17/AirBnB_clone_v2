#!/usr/bin/env bash
# Set up a web server for the development of web_static
# Update and install nginx if not installed
if ! command -v nginx &> /dev/null; then
    apt-get update
    apt-get -y install nginx
fi

# Create directories and sub directories if they don't exist yet
directories=(
    "/data/"
    "/data/web_static/"
    "/data/web_static/releases/"
    "/data/web_static/shared/"
    "/data/web_static/releases/test/"
)

for dir in "${directories[@]}"; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
    fi
done

# Create a fake HTML file for testing Nginx configuration
echo "Testing Nginx configuration" > /data/web_static/releases/test/index.html

# Create / recreate(if exists) a symbolic link
if [ -L "/data/web_static/current" ]; then
    rm /data/web_static/current
fi
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership of /data/ recursively
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content to hbnb_static
config_file="/etc/nginx/sites-available/default"
alias_line="location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
if grep -q "location /hnbn_static/" "$config_file"; then
    sed -i /'location \/hbnb_static\//d' "$config_file"
fi
sed -i "s|server_name _;|server_name_;\n\n\t$alias_line|g" "$config_file"

# Restart nginx service
service nginx restart
