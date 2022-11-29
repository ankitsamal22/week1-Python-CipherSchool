# a="     ankit     "
# b="............."
# print(a+b)
# print(a.lstrip() +b )
# print(a.rstrip() +b)
# print(a.strip()+b)
# c="anki    t"
# print(c.replace(" ","")+b)
d,e=input().split()
print(d.strip().lower().count(e.strip().lower()))
print(len(d))
