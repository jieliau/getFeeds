# This is one little toy

getFeeds is the little toy to get the IPv4/IPv6 range of the well-know SaaS services. At the moment, it only gets Office 365 IPv4/IPv6

# Description

Running this toy will be listening on 0.0.0.0 port 8888. Feel free to change the port if you want
> - Example: http://192.168.0.204:8888/
> - Example: http://192.168.0.204:8888/o365

# Execution

```sh
$ python3 getFeeds.py
 * Serving Flask app 'getFeeds' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:8888
 * Running on http://192.168.0.204:8888 (Press CTRL+C to quit)
192.168.0.43 - - [27/Sep/2023 15:18:53] "GET / HTTP/1.1" 200 -
192.168.0.43 - - [27/Sep/2023 15:18:58] "GET /o365 HTTP/1.1" 200 -

```
