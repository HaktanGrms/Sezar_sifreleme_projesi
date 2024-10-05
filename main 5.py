alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#parametre=int(input("Lütfen sayı giriniz"))
#metin=input("lütfen metin giriniz")

metin = "Metin giriniz"
parametre=679
def sifrele(metin):
    sonuç=""
    
    
    for harfler in metin:
        if harfler in alphabet:
            index=alphabet.index(harfler)
            new_index=(index + parametre) % 26
            sonuç += alphabet[new_index]
        else:
            sonuç += harfler
            
    return(sonuç)
    
def coz(metin):
    sonuç=""
    
    
    for harfler in metin:
        if harfler in alphabet:
            index=alphabet.index(harfler)
            new_index=(index + (26 - parametre)) % 26
            sonuç += alphabet[new_index]
        else:
            sonuç += harfler
            
    return(sonuç)
    
sifreli = sifrele(metin)
print("Şifreli kelime =",sifreli)
print("ana metin ",coz(sifreli))