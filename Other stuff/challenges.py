import string

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb " \
    "rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

alphabet = string.ascii_lowercase

print(s.translate(str.maketrans(alphabet, alphabet[2:] + "ab")))

f = open("rare.txt", "r")
s = f.read()

unique = set(s)

d = {}
for el in unique:
    d[el] = s.count(el)

m = min(d.items(), key=lambda x: x[1])[1]
print([k for k, v in d.items() if v == m])
