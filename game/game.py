from draw.draw import *
import time
import random

rpcValue = {0:"주먹", 1:"보", 2:"가위"}


def rpcComp(user, com):
    if (user + 1) % 3 == com:
        return -1
    elif user == com:
        return 0
    else:
        return 1

def gameStart(name, coin):
    finalCoin = None
    userCoin = int(coin)
    while True:
        title()
        print("-----")
        print()
        print(" {} {}".format(name, coin))
        print()
        while True:
            try:
                vet = int(input("배팅: "))
                if (vet >= 0 and vet <= userCoin):
                    break
                else:
                    print("똑바로 입력해")
                    time.sleep(1)
            except:
                print("똑바로 입력해")
                time.sleep(1)
        time.sleep(1)
        comValue = random.randrange(0, 3)
        title()
        print(" {} {}".format(name, coin))
        print()
        print("-----")
        print("[0] 주먹")
        print("[1] 보")
        print("[2] 가위")
        print()
        while True:
            try:
                select = int(input("> "))
                if (select == 0 or select == 1 or select == 2):
                    break
                else:
                    print("[0] 주먹 / [1] 보 / [2] 가위")
            except:
                print("[0] 주먹 / [1] 보 / [2] 가위")
        print()
        print()
        time.sleep(1)
        print("가위..", end=" ")
        time.sleep(1)
        print("바위..", end=" ")
        time.sleep(1)
        print("보!")
        time.sleep(1)
        print()

        result = rpcComp(select, comValue)

        if result == -1:
            print("컴퓨터: {} ".format(rpcValue[comValue]))
            print()
            print("패배")
            finalCoin = userCoin - vet
        elif result == 0:
            print("컴퓨터: {} ".format(rpcValue[comValue]))
            print()
            print("무승부")
            finalCoin = userCoin
        else:
            print("컴퓨터: {} ".format(rpcValue[comValue]))
            print()
            print("승리")
            finalCoin = userCoin + vet

        time.sleep(3)
        return finalCoin
        