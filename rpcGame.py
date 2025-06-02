from draw.draw import *
from game.game import *
import time
import json
import sys

usersData = None

def login():

    loginTitle()

    name = input(" 이름 :")
    
    password = input("비밀번호 : ")

    f = open("gameData.json", "r", encoding = "utf-8")
    global usersData
    usersData = json.load(f)

    for user in usersData:
        if name in user.values():
            if password == user["password"]:
                coin = user["Coin"]
                return 1, name, coin
            
    return 0



def signup():

    signupTitle()

    name = input(" 종료[3] 이름 : ")
    if name == '3':
        print("종료..")
        time.sleep(2)
        return
    
    password = input("비밀번호 : ")
    ispassword = input("비밀번호 확인 : ")

    
    if password == ispassword:
        checkUser(name, password)
        print()
    else:
        print("비밀번호가 다릅니다.")


def checkUser(name, password):
    try:
        f = open("gameData.json", "r", encoding = "utf-8")
        global usersData
        usersData = json.load(f)
        f.close()
    except:
        usersData = []
    if(usersData):
        for user in usersData:
            if name in user.values():
                print("이미 존재하는 이름입니다.")
                print("..이동중")
                time.sleep(2)
                break
                
        if name not in user.values():
            user = { "userName" : name, "password" : password, "Coin" : 1000 }

            f = open("gameData.json", "w", encoding = "utf-8")
            usersData.append(user)
            json.dump(usersData, f)
            f.close()
            print("가입 되었습니다.")
            print("..이동중")
            time.sleep(2)
        
        
        

    elif(not usersData):
        user = { "userName" : name, "password" : password, "Coin" : 1000 }

        f = open("gameData.json", "w", encoding = "utf-8")
        usersData.append(user)
        json.dump(usersData, f)
        f.close()
        print("가입 되었습니다.")
        print("..이동중")
        time.sleep(2)
        
sys_exit = None
while True:
    
    title()
    menu()

    select = input("선택> ")

    if select == '1':
        try:
            [isauth, name, coin] = login()
            if isauth == 1:
                print()
                print("로그인 성공")
                time.sleep(2)

                while True:
                    
                    title()
                    print(" {}  {}".format(name, coin))
                    print()
                    print("[1] 시작")
                    print("[2] 로그아웃")
                    print("[3] 종료")

                    print()
                    select = input("> ")

                    if select == '1':
                        coin = gameStart(name, coin)
                        if coin <= 0:
                            clear()
                            pepe()
                            time.sleep(2)
                            sys_exit = 1
                            break
                        
                    elif select == '2':
                        print()
                        print("로그아웃.")
                        time.sleep(2)
                        break
                    else:
                        print()
                        print("종료..")
                        time.sleep(2)
                        sys_exit = 1
                        break

                    
        except:
            print()
            print("로그인 실패")
            time.sleep(2)
        

        if sys_exit == 1:
            clear()
            break    
            

    elif select == '2':
        signup()
    
    else:
        print("종료.")
        time.sleep(3)
        clear()
        break


