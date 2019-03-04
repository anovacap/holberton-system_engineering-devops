# 0x1A-application_server
---
## Description
You web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.
## Files
---
File|Task
---|---
0-welcome_gunicorn-upstart_config | starts a Gunicorn instance to serve web_flask/0-hello_route.py
0-welcome_gunicorn-nginx_config | Nginx config file 
1-pass_parameter-upstart_config | starts a Gunicorn instance to serve web_flask/6-number_odd_or_even.py
1-pass_parameter-nginx_config | Setup Nginx so that the route/airbnb-dynamic/ points to your Gunicorn instance
2-api-upstart_config | Upstart script that starts a Gunicorn instance to serve api/v1/app.py
2-api-nginx_config | Setup Nginx so that the route /api/ points to your Gunicorn instance
3-complete_webapp-upstart_config | Setup Nginx so that the route / points to your Gunicorn instance
3-complete_webapp-nginx_config | Nginx must serve this page both locally and on its public IP on port 80
Directory Name | Description
---|---
holberton-system_engineering-devops | Gunicorn
## Author
Damon Nyhan