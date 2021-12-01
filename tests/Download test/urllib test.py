import urllib.request

with urllib.request.urlopen('https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe') as response:
    html = response.read()
    print(html)
