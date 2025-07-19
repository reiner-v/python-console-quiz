import modFiles
import time,sys
#from threading import Timer

def miniGameMenu(username):
    print("=================================")
    print("\t\tMINI GAME")
    print("---------------------------------")
    while True:
        print("1.Play\n2.Leaderboard\n0.Back")
        choice = input("Enter Choice: ")
        if choice == '1':
            Play(username)
        elif choice == '2':
            leaderBoard1()
        elif choice == '0':
            return

def Play(username):
    score = 0  # to count the correct score
    print("=================================")
    print("\t\tLET's PLAY")
    print("---------------------------------")
    print("\nDescription:\n"
          "Simple Minigame, It is made of various Subject and question. Your goal is to finish the question and get a high score\n"
          "                  Don't worry there will be no time limit so answer comfortably.There will be 20 Question\n"
          "                                                 GOOD LUCK! ENJOY!")

    animation = "|/-\\"
    for i in range(40):
        time.sleep(0.1)
        sys.stdout.write("\r" + "Starting..." + animation[i % len(animation)])
        sys.stdout.flush()

    quizFile = open('MiniQuiz_Game.txt', 'r')
    for info in quizFile.readlines():
        data = info.split('|')
        print('\n'*50)
        print("Question:", data[1] + '\n')
        for n in range(2,6):
            print(data[n])
        while True:
            ans = input("Answer:").upper() + '\n'
            if ans in ["A\n","B\n","C\n","D\n"]:
                if ans == data[6]:
                    score += 1
                break
            else:
                print("Invalid Input")

    print("You Got!",score)
    lb = modFiles.Files(username=username, password="", q_a="", title="", QTitles="",access="")
    lb.leaderBoard(score)

def leaderBoard1():
    print("=================================")
    print("\t\tLEADERBOARD")
    print("---------------------------------")
    userScores = []
    f = open('LeaderBoard.txt','r')
    for s in f.readlines():
        score = s.split('-')
        u = [score[0], score[1].rstrip('\n')]
        userScores.append(u)

    userScores.sort(key=lambda x:x[1],reverse=True)

    print("---------------------------------")
    print("\t\t RANKING")
    print("---------------------------------")
    for p in range(len(userScores)):
        print("{0}. {1}\tSCORE: {2}".format(p+1,userScores[p][0],userScores[p][1].rstrip('\n')))
    print("---------------------------------")


