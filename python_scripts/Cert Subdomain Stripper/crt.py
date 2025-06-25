#!/usr/bin/python3

import sys
import requests
from bs4 import BeautifulSoup

domain = input("Enter a domain name to search certificate transparency logs: ").strip()
url = "https://crt.sh?q=" + domain

print("Getting domain details from crt.sh")
resp = requests.get(url)

print("Extracting subdomains from " + domain)
soup = BeautifulSoup(resp.content, "html.parser")
urls = []

for i in soup.select("table tr td:nth-of-type(5)"):
    if not "*" in i.text:
        urls.append(i.text)

print("Unique subdomains from " + domain)
for i in sorted(set(urls)):
    print(i)
