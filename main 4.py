alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

metin="metin giriniz"

def sifrele(metin):
    sonuç=""
    
    
    for harfler in metin:
        if harfler in alphabet:
            index=alphabet.index(harfler)
            new_index=(index + 13) % len(alphabet)
            sonuç += alphabet[new_index]
        else:
            sonuç += harfler
            
    return(sonuç)
    
print("İlk kelime =",metin)
print("Şifreli kelime =",sifrele(metin))