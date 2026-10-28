import random
numero_secreto = random.randint(1,100)
while True:
    palpite = int(input("Seu palpite:"))
    if palpite < numero_secreto:
        print("Maior!")
    elif palpite > numero_secreto:
        print("Menor!")
    else:
        print("Acertou!")    
        break