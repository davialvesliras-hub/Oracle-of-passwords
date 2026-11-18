import random
from time import sleep
# items for my prog
characteres = [1,2,3,4]

characteres_copies = []
trys = 0

print('====================WELCOME TO ORACLE OF PASSWORDS!===========================')
sleep(5)
#loop for trys different combinations

while characteres_copies != characteres:
    characteres_copies = [random.choice(characteres) for _ in characteres]
    if characteres_copies != characteres:
        trys += 1
        print(f'wrong trys : {characteres_copies}, how many trys: {trys}')
    if characteres_copies == characteres:
        print(f'result : {characteres_copies}, how many trys: {trys+1}')


