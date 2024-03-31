import random    #score getirilebilir streak gibisinden, kelimeler dil eklenebilir genişletilebilir. Belki 
from word_list import word_list_all
import hangman_art
import time
import os
clear = lambda: os.system('cls')  #Terminali temizlemek için fonksiyonumuz.

desicion = 1
while desicion ==  1:

    print("\n\nWelcome to Hangman")
    print(hangman_art.logo) 
    stages = hangman_art.stages_of_hangman

    life = 6
    all_letters = []

    word = random.choice(word_list_all)
    length = len(word)


    #Kelime Sayısı Kadar '_' oluşturma
    answer= [] 
    for i in word:
        answer.append("_")

    #Kelimeyi listeye çevirme
    word_list = [] 
    for i in word:
        word_list.append(i)

    all_letters_string = " "

    game = True #devam
    while game == True:

        print(f"\n\n\n\n{all_letters_string}") #önceden yazılan harfler

        guess = ""  #boşluk girilirse tekrar soracak
        while guess == "":
            guess = input("Guess a letter: ").lower()  
        clear()

        if guess not in all_letters:
            all_letters.append(guess)
            all_letters_string+=guess + " "   
        else:
            print(f"You has already enter {guess}")
            if guess not in word_list:
                life += 1 #İkinci kez puan silmesin diye. 
            

        if guess not in word_list:
            life -= 1
            if life == 0: #Canı kalmadı
                game == False  #Döngüyü Bitir
                win = False  #İyi mi bitti Kötü mü
                print(f"\n{answer_string}") #Son durum
                print(stages[life]) #Adam
                break

        #Harf var mı, varsa cevaba ekliyor
        for i in range(0,length):
            if word_list[i] == guess:
                answer[i] = guess

        #Liste halindeki cevabı stringe çeviriyor
        answer_string = ""
        for e in range (0,len(answer)):
            answer_string +=answer[e]

        print(f"\n{answer_string}") #Son durum
        print(stages[life]) #Adam

        if '_' not in answer: #Hepsini Bildi
            game = False
            win = True
            break
        
    if win == True: 
        print("You win!")
    if win == False: 
        print(f"\n{answer_string}")
        print(f"\nYou lost!")
        print(f"the word was {word}")
    print(hangman_art.logo)
    print("")
    

    desicion = int(input("Press 1 for try again, 2 for exit."))
    clear()