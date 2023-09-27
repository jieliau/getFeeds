import os, json, requests
from flask import Flask, jsonify

# Setup variable
# There are 5 instances of O365 around the World. Wordwide, USGovDoD, USGovGCCHigh, China and Germany. I put Wordwide, China and Germany at the moment.  
instances = ['Worldwide', 'China', 'Germany']
headers = {'content-type': 'application/json',
            'accept': 'application/json'}

# Disable warning
requests.packages.urllib3.disable_warnings()

ip4s = []
ip6s = []

def getO365_ips(url: str):
    res = requests.get(url, headers = headers, verify = False)
    for service in res.json():
        if service.get('ips') is not None:
            for ip in service['ips']:
                if ':' in ip:
                    ip6s.append(ip)
                else:
                    ip4s.append(ip)
    return ip4s, ip6s

def main():
    app = Flask(__name__)
    app.config['DEBUG'] = False

    @app.route('/', methods=['GET', 'POST'])
    def helloWorld():
        return 'Hello World !!!'
    
    @app.route('/o365', methods=['GET', 'POST'])
    def o365():
        try:
            for instance in instances:
                url = f"https://endpoints.office.com/endpoints/{instance}?clientrequestid=b10c5ed1-bad1-445f-b386-b919946339a7"
                res4s, res6s = getO365_ips(url)
                res = {'ipv4': res4s, 'ipv6': res6s}
                return jsonify(res)
        except:
            raise Exception("Something Error !!!")

    app.run(host='0.0.0.0', port=8888)

if __name__ == '__main__':
    main()
