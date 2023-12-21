# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:


def encrypteer(tekst):
    versleutelde_tekst = ""
    for karakter in tekst:
        if karakter.isalpha():
            code = ord(karakter) + 5
            if karakter.islower():
                if code > ord('z'):
                    code -= 26
            else:
                if code > ord('Z'):
                    code -= 26
            versleutelde_tekst += chr(code)
        else:
            versleutelde_tekst += karakter
    return versleutelde_tekst

def decrypteer(versleutelde_tekst):
    ontsleutelde_tekst = ""
    for karakter in versleutelde_tekst:
        if karakter.isalpha():
            code = ord(karakter) - 5
            if karakter.islower():
                if code < ord('a'):
                    code += 26
            else:
                if code < ord('A'):
                    code += 26
            ontsleutelde_tekst += chr(code)
        else:
            ontsleutelde_tekst += karakter
    return ontsleutelde_tekst


invoer_tekst = "Hello, World!"
versleutelde_tekst = encrypteer(invoer_tekst)
print(f"Versleutelde tekst: {versleutelde_tekst}")

ontsleutelde_tekst = decrypteer(versleutelde_tekst)
print(f"Ontsleutelde tekst: {ontsleutelde_tekst}")

