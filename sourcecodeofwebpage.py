import urllib.request as ur
file = ur.urlopen("https://www.instagram.com/")
print(file.read())