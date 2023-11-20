from django.shortcuts import render, redirect
from django.http import HttpResponse

# This function generates the 
# key in a cyclic manner until 
# it's length isn't equal to 
# the length of original text
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

# This function returns the 
# encrypted text generated 
# with the help of the key
def cipherText(string, key):
    encrypted_text = ""
    key = key.lower()
    key_length = len(key)
    
    for i, char in enumerate(string):
        if char.isalpha():
            # Determine the shift value for the current character in the key
            key_shift = ord(key[i % key_length]) - ord('a')
            
            # Shift the character by the key_shift value, preserving case
            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + key_shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + key_shift) % 26) + ord('a'))
            
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

# This function decrypts the 
# encrypted text and returns 
# the original text
def originalText(cipher_text, key):
    decrypted_text = ""
    key = key.lower()
    key_length = len(key)

    for i, char in enumerate(cipher_text):
        if char.isalpha():
            # Determine the shift value for the current character in the key
            key_shift = ord(key[i % key_length]) - ord('a')
            
            # Shift the character back by the key_shift value, preserving case
            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - key_shift + 26) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - key_shift + 26) % 26) + ord('a'))
            
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

def cezarSzyfr(text,keys):
    wiad = ""
    piv = 0
    # traverse text
    for i in range(len(text)):
        char = text[i]
        shift = keys[piv]
        # Encrypt uppercase characters
        if (char.isupper()):
            wiad = wiad + chr((ord(char) + shift-65) % 26 + 65)
        # Encrypt lowercase characters
        else:
            wiad = wiad + chr((ord(char) + shift - 97) % 26 + 97)
        piv = piv + 1
        if(piv==len(keys)):
            piv=0
 
    return wiad

def toList(string):
    numbers = string.split(',')
    numbers = [int(num.strip()) for num in numbers]
    
    return numbers

def kod(request):
    try:
        if request.method == 'POST':
                wiadomosc = request.POST.get('wiadomosc') 
                if (request.POST.get('szyfr') == 'cezar'):
                    klucz = toList(request.POST.get('klucz'))
                    zakodowana_wiadomosc = cezarSzyfr(wiadomosc,klucz) 
                elif (request.POST.get('szyfr') == 'decezar'):
                    klucz = toList(request.POST.get('klucz'))
                    inv_klucz = [-x for x in klucz]
                    zakodowana_wiadomosc = cezarSzyfr(wiadomosc,inv_klucz) 
                elif (request.POST.get('szyfr') == 'vinegar' or request.POST.get('szyfr') == 'devinegar'):
                    klucz = request.POST.get('klucz')
                    key = generateKey(wiadomosc,klucz)
                    if (request.POST.get('szyfr') == 'vinegar'):
                        zakodowana_wiadomosc = cipherText(wiadomosc, key)
                    else:
                        zakodowana_wiadomosc = originalText(wiadomosc, key)  
                return render(request, 'page.html', {'zakodowana_wiadomosc': zakodowana_wiadomosc})
    except:
        zakodowana_wiadomosc = "Zły format klucza"
        return render(request, 'page.html', {'zakodowana_wiadomosc': zakodowana_wiadomosc})
    return render(request, 'page.html')
