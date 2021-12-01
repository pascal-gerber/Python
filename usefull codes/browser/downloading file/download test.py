import urllib.request

link = "https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe"

f2 = open("download.exe", "wb")

f = urllib.request.urlopen(link)

try:
    while True:
        data = f.read(4096)
        if not data:
            break
        f2.write(data)
finally:
    f.close()
    f2.close()
