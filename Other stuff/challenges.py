import io
import pickle
import re
import string
import zipfile
from urllib.request import urlopen

import requests

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb " \
    "rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

alphabet = string.ascii_lowercase
print(s.translate(str.maketrans(alphabet, alphabet[2:] + alphabet[:2])))

f = open("rare.txt", "r")
s = f.read()

unique = set(s)

d = {}
for el in unique:
    d[el] = s.count(el)

m = min(d.items(), key=lambda x: x[1])[1]
print([k for k, v in d.items() if v == m])

f = open("small.txt", "r")
s = f.read()

p = re.compile("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]")
print(''.join(p.findall(s)))

code = None
url = ''
p = re.compile('nothing is ([0-9]+)')
while code is not None:
    url = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={code}'
    r = requests.get(url)
    s = p.search(r.text)
    code = s.group(1) if s is not None else None
print(url)

obj: list = pickle.load(urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))
for el in obj:
    print(''.join([x * y for x, y in el]))

r = requests.get('http://www.pythonchallenge.com/pc/def/channel.zip')
z = zipfile.ZipFile(io.BytesIO(r.content))

code = txt = '90052'
comments = []
while code is not None:
    txt = (z.read(f'{code}.txt').decode('utf8'))
    comments.append(z.getinfo(f'{code}.txt').comment.decode('utf8'))
    m = p.search(txt)
    code = m.group(1) if m is not None else None
print(txt)
comments = ''.join(comments)
print(comments)
