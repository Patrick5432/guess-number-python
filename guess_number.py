import random

#Генерируется рандомное число

def randomNumber():
    a = int(input("Укажите диапазон загаданного числа: "))
    hiddenNumber = random.randint(1, a)
    return hiddenNumber

# hideNumber = randomNumber()

#Изменяет имя

def changeName():
    namePerson = input("Введите ваше имя: ")
    return namePerson

#Начинает игру(действует один раз)

def startGame():
    print("Игра начинается")
    hNumber = randomNumber()
    namePerson = changeName()
    namePerson = namePerson.replace(" ", "")
    if len(namePerson) != 0:
        guessNumber(hNumber, namePerson)
    else :
        print("Вы не ввели имя")
        print("Игра завершается")

#Продолжает игру(можно использовать бесконечно)

def contGame():
    check = input("Продолжите игру? ")
    
    if check.lower() == "yes" or check.lower() == "да":
        checkName = input("Желаете изменить имя? ")
        if checkName.lower() == "yes" or checkName.lower() == "да":
            name = changeName()
            hNumber = randomNumber()
            guessNumber(hNumber, name)
        else:
            return False
    elif check.lower() == "no" or check.lower() == "нет":
        print("Игра завершена")
        return True
        

#Сама игра

def guessNumber(hideNumber, namePerson):
    finishRound = False
    attemptCounter = 1

    while finishRound == False:
        print(hideNumber)
        number = int(input("Введите число: "))

        if hideNumber < number:
            if number - hideNumber <= 2:
                print("Близко")
            else:
                print("Меньше")

        elif hideNumber > number:
            if hideNumber - number <= 2:
                print("Близко")
            else:
                print("Больше")

        if hideNumber == number:
            print("Вы угадали число")
            print(namePerson, "ваше число", hideNumber, "количество попыток: ", attemptCounter)
            with open("person.txt", "w") as file:
                file.write(f"Name: {namePerson}\n")
                file.write(f"Attempts: {attemptCounter}\n")
            finishRound = contGame()
            if finishRound == False:
                guessNumber(randomNumber(), namePerson) 
        else:
            attemptCounter += 1
            # if attemptCounter == 3:
            #     endGame = input("Желаете закончить игру? ")
            #     if endGame.lower() == "yes" or endGame.lower() == "да":
            #         print("Игра завершена")
            #         finishRound = True
            #     attemptCounter = 0

startGame()