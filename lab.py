# В рядку написан текст.
# Для кожного слова підрахуйте
# кілька разів воно зустрічалось в цьому тексті.
text = """ Little girl, little girl Why are you crying
Inside your restless soul your heart is dying Little one, little one Your soul is 
purging Of love and razor blades Your blood is surging 
Runaway From the river to the street And find yourself with your face in the gutter 
Your a stray for the salvation army 
There is no place like home When you got no place to go Little girl, little girl Your life is calling 
The charlatans and saints of your abandon Little one little one The sky is falling The lifeboat of deception is 
now sailing In the wake all the way No rhyme or reason Your bloodshot eyes Will show your heart of treason 
Little girl little girl You dirty liar Youre just a junkie Preaching to the choir Runaway To your 
lost tranquility And find yourself with your face in the gutter Your a stray for the dregs of humanity 
There is no place like home When you got no place to go The traces of blood Always follow you home 
Like the Mascara tears From your getaway Your walking with blisters And running with shears So unholy. 
Sister of grace. Runaway From the river to the street And find yourself with your face in the gutter 
Youre a stray for the salvation army There is no place like home When you got no place to go"""

words = dict()
clear_text = text.lower().replace(",", " ").replace(".", " ").replace("!"," ")
for word in clear_text.split():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(words)
