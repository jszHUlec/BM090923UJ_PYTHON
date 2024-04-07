# from requests_html import HTMLSession
# from termcolor import colored
from bs4 import BeautifulSoup as bs
import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

mainurl = "https://host-v1e6bqkw-prod.prod.cywar.xyz:50708"
par_name = "/?FIREFLIES="
param = "12431"
url = mainurl + par_name + param
req_type = "GET"

while True:
    print(req_type, param)
    if req_type == "POST":
        params1 = {'FIREFLIES': param}
        print(params1)
        resp = requests.request(req_type, url=mainurl, data=params1, verify=False)
        print(resp.text)
    else:
        resp = requests.request(req_type, url=url, verify=False)

    soup_new = bs(resp.text, 'html.parser')

    canva = soup_new.find_all('canvas')[0].get('title')
    if canva:
        elems = canva.split(" ")
        param = elems[1]
        req_type = elems[0]
        if req_type == "Flag:":
            print("flaga:")
            print("-----------------------------------------------")
            print(canva)
            print("-----------------------------------------------")
            exit(0)
        url = mainurl + par_name + param

# POST 34062