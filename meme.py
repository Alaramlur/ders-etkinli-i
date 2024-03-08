#dictionary = {  "key": "value",
#                "anahtar" : "değer" }
print("merhaba, online ortamda görüp anlamamış olabileceğin bazı kelimelerin anlamlarını sana veriyoruz.")
meme_dict = {
            "Cringe": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL" : "bir şakaya karşılık cevap",
            "Creepy" : "korkunç",
            "Slay": "olağanüstü başarı ve mükemmelik karşısında söylenen bir kelime",
            "Sheesh": "onaylamamak",
            "AGGRO": "agresifleşmek/sinirlenmek"
            }

for i in range(5):
    
    word = input("Anlamadığınız bir kelime yazın: ")
    
    
    if word in meme_dict.keys():
        # Kelime eşleşiyorsa ne yapmalıyız?
        print(meme_dict[word])
        
    else:
        # Kelime eşleşmiyorsa ne yapmalıyız?
        print("Lütfen geçerli bir kelime gir.")
