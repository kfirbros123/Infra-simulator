#/bin/bash
set -e
HTML_SOURCE="configs/index.html"
HTML_TARGET="/var/www/html/index.html"

echo "=== NGINX INSTALLER (Ubuntu) ==="

echo "Checking if nginx is installed..."

if ! dpkg -l nginx| grep -q "^ii  nginx"; then
    echo "Nginx not installed. Installing..."
    apt update
    apt install -y nginx
    echo "Nginx successfully installed."
else
    echo "Nginx is already installed."
fi

echo "Replacing index.html..."


if [ ! -f "$HTML_SOURCE" ]; then
    echo "Error: Source file '$HTML_SOURCE' does not exist. EXITING INSTSLLATION SCRIPT"
    exit 1
fi

#Copy custom html
cp "$HTML_SOURCE" "$HTML_TARGET"

echo "Restarting nginx..."
systemctl restart nginx

echo "Installation complete! Custom html has been applied."