import random

from numpy import char

def password_generate():
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    characters = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    character_data = uppercase + lowercase + numbers + characters

    password = []

    for i in range(15):
        random_character = random.choice(character_data)
        password.append(random_character)

    password = "".join(password)

    return password

def run():
    password = password_generate()
    print("Tu nueva contraseña es: "+password)
    input("Pulse un tecla para finalizar...")

if __name__ == '__main__':
    run()