import random

message = 'litwo! ojczyzno moja! ty jesteś jak zdrowie. ile cię trzeba cenić ten tylko się dowie, kto cię stracił.'
sentence = message.upper()
alfabet = 'AĄBCĆDEĘFGHIJKLŁMNOÓPRSŚTUWYZŻŹ'
keys = [ord(a) for a in alfabet]
values = list(keys)
random.shuffle(values)
code = dict(zip(keys, values))
encrypted_sentence = sentence.translate(code)

guessed_sentence = encrypted_sentence

list_enc = []
list_guess = []

for i in encrypted_sentence:
    list_enc += i

for i in guessed_sentence:
    list_guess += i

hits = []

print(encrypted_sentence)
while True:
    guess = input('please type eg. A = S : ')
    guess = guess.strip()
    guess = guess.replace(' ', '')
    letter1 = guess[0].upper()
    letter2 = guess[2].upper()

    for i in range(len(list_enc)):
        if letter1 == list_enc[i]:
            hit = i
            hits.append(hit)

    for i in range(len(hits)):
        list_guess[hits[i]] = letter2

    guessed_sentence1 = ''.join(list_guess)

    hits = []

    print(guessed_sentence1)
    if guessed_sentence == sentence.upper():
        print(f"{guessed_sentence}\nCONGRATULATIONS!")
