def rijec_unatrag(s):
    if s == "":
        return""
    return rijec_unatrag(s[1:])+s[0]
print(rijec_unatrag("zdravo"))
