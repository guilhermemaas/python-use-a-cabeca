phrase = "Dont't panic!"
plist = list(phrase)
print(phrase)
print(plist)
#on tap
for i in range(4):
    plist.pop()
plist.remove("'")
plist.remove("D")
plist.pop(2)
plist.insert(2, " ")
plist.insert(4, plist.pop(6))
plist.insert(5, plist.pop(6))
new_phrase = "".join(plist)
print(plist)
print(new_phrase)
