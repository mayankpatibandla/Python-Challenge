x = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
y = "map"

key = 2


def decrypt(text, key):
    decrypted = ""
    for char in text:
        if char.isalpha():
            decrypted += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            decrypted += char
    return decrypted


print(decrypt(x, key))
print(decrypt(y, key))
