#/bin/bash
yum install nginx -y
cp /home/kfir/Git/kfirbros123-project/kfirbros123-project/Project/First/configs/index.html /usr/share/nginx/html -f
systemctl start nginx
