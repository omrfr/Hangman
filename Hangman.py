import random
from Words import words
import string


def get_valid_word(_words):
    word = random.choice(_words)

    while '-' in word or ' ' in word:
        word = random.choice(_words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives >0:
        print('Bu harfleri kullandınız.', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Şu anki kelime', ' '.join(word_list))

        user_letter = input("Harf girin: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Can sayınız: ",lives)
            else:
                lives = lives - 1
                print("Can sayınız: ",lives)
                print("Bu harf kelimede yok.")



        elif user_letter in used_letters:
            print('Bu harfi zaten denediniz.Başka bir harf deneyin.')

        else:
            print('Geçersiz karakter.Tekrar deneyin.')
    if lives == 0:
        print("Maalesef öldünüz.Kelime: ",word)
    else:
        print("Bravo,doğru bildiniz!!!Kelime: ",word)


hangman()
