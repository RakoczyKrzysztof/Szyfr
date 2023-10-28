from django.shortcuts import render
from django.http import HttpResponse

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
    if request.method == 'POST':
            wiadomosc = request.POST.get('wiadomosc')
            klucz = toList(request.POST.get('klucz'))  
            #cezarSzyfr(wiadomosc,1,[1])
            if (request.POST.get('szyfr') == 'cezar'):
                zakodowana_wiadomosc = cezarSzyfr(wiadomosc,klucz) 
            elif (request.POST.get('szyfr') == 'decezar'):
                inv_klucz = [-x for x in klucz]
                zakodowana_wiadomosc = cezarSzyfr(wiadomosc,inv_klucz) 
            elif (request.POST.get('inne szyfry') == 'szyfr2'):
                zakodowana_wiadomosc = cezarSzyfr(wiadomosc,klucz)
            else:
                zakodowana_wiadomosc = cezarSzyfr(wiadomosc,klucz)   
            return render(request, 'page.html', {'zakodowana_wiadomosc': zakodowana_wiadomosc})
    return render(request, 'page.html')