sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello
sudo ln -s /home/box/web/etc/qa.py /etc/gunicorn.d/qa
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
mysql -uroot -e "create database qa"
mysql -uroot -e "create user qa identified by '123456'";
mysql -uroot -e "grant all on qa.* to qa identified by '123456'";
