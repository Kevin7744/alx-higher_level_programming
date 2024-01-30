#!/usr/bin/python3
"Module that fetches https://alx-intranet.hbtn.io/status"
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
