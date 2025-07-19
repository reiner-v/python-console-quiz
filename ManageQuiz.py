from GenerateQuiz import *
import  os,time,sys
def findFile(title, path):
    for n in os.listdir(path):
        if title in n:
            return n
    else:
        print("Quiz Title Unavailable")
        return True

def enterQuiz(Username):
    ttl = ""
    while True:
        title = input("Enter Quiz: ").upper()
        if title == "":
            print("Enter a Quiz Title")
            continue
        ttl = findFile(title, r'C:\Users\user\PycharmProjects\MP\{0}'.format(Username + '-Quiz Title'))
        if ttl != True:
            return ttl

class Manage(Quiz):
    def yourQuizzes(self):
        print("=================================")
        print("\t\tYOUR QUIZZES")
        print("---------------------------------")
        path = r'C:\Users\user\PycharmProjects\MP\{0}'.format(self.Username + '-Quiz Title')
        for f in os.listdir(path): #list of files
            if f.endswith('-PUBLIC.txt'):
                f = f.rstrip('-PUBLIC.txt')
                print(f)
            else:
                f = f.rstrip('-PRIVATE.txt')
                print(f)

    def addQuestion(self):
        print("[Enter the Quiz Title where you will add the new Question...]")
        ttl = enterQuiz(self.Username)
        print("=================================")
        print("\t\tADD QUESTION")
        print("---------------------------------")
        path = r'C:\Users\user\PycharmProjects\MP\{0}'.format(self.Username + '-Quiz Title')
        file = os.path.join(path,ttl)


        noOfQuestion = ""

        quizFile = open(file, 'r+') #read and write mode
        count = len(quizFile.readlines())
        while True:
            try:
                noOfQuestion = int(input("Enter No. of Question: "))
                break
            except ValueError:
                print("Invalid Input")
                continue
            except TypeError:
                print("Invalid Input")
                continue
        for x in range(noOfQuestion):
            while True:
                newQuestion = input("Enter new question: ").upper()
                if newQuestion != "":
                    break
                print("Enter new Question")
            while True:
                newAnswer = input("Enter the answer: ").upper()
                if newQuestion != "":
                    break
                print("Enter the Answer")
            print("\n")
            count += 1
            add = str(count) + '|' + newQuestion + '|' + newAnswer + '\n'
            quizFile.write(add)
        quizFile.close()

    def delQuestion(self):
        print("=================================")
        print("\t\tDELETE QUESTION")
        print("---------------------------------")
        print("[Enter the Quiz Title where you will delete the Question...]")
        ttl = enterQuiz(self.Username)
        path = r'C:\Users\user\PycharmProjects\MP\{0}'.format(self.Username + '-Quiz Title')
        file = os.path.join(path,ttl)

        editFile = []
        quizFile = open(file , 'r+') #read and write
        while True:
            print("---------------------------------")
            print("[Type 'Question No.' to delete. Type 'view' if you want to see the question.]")
            delQuestion = input("Enter Question No. to Delete: ").upper()
            if delQuestion == 'VIEW':
                print("---------------------------------")
                for l in quizFile.readlines():
                    data = l.split('|')
                    print(data[0] + '-' + data[1])
                continue
            elif delQuestion.isdigit():
                break
            else:
                print("Invalid Input.")
                continue

        quizFile = open(file , 'r+')
        for q in quizFile.readlines():
            data = q.split('|')
            print(data)
            print(delQuestion,data[0])
            if delQuestion == data[0]:
                del data
            elif delQuestion != data[0]:
                print("hi")
                editFile.append([data[1],data[2]])
        quizFile.close()

        print(editFile)
        editedQuizFile = open(file,'w') #rewrite
        for x in range(len(editFile)):
            newQ = str(x+1) + '|' + editFile[x][0] + '|' + editFile[x][1]
            editedQuizFile.write(newQ)
        editedQuizFile.close()

    def deleteFile(self):
        print("=================================")
        print("\t\tDELETE QUIZ")
        print("---------------------------------")
        print("[Reminder: Your Quiz will be deleted Permanently]")
        ttl = enterQuiz(self.Username)
        path = r'C:\Users\user\PycharmProjects\MP\{0}'.format(self.Username + '-Quiz Title')
        file = os.path.join(path,ttl)
        choice = ""
        while choice != 'Y' or choice != 'N':
            choice = input("Are you sure you want to Delete? [Y-Yes/N-No]: ").upper()
            if choice == 'Y':
                os.remove(file)
                animation = "|/-\\"
                for i in range(50):
                    time.sleep(0.1)
                    sys.stdout.write("\r" + "Deleting File..." + animation[i % len(animation)])
                    sys.stdout.flush()
                print("\n")
                return
            elif choice == 'N':
                return

    def changeAccessFile(self):
        print("=================================")
        print("\tCHANGE ACCESS FILE")
        print("---------------------------------")
        path = r'C:\Users\user\PycharmProjects\MP\{0}'.format(self.Username + '-Quiz Title')
        for quiz in os.listdir(path):
            print(quiz)
        print("[Type \'Private\' if don't want to share your Quiz. "
              "Type 'Public' if you want other to see you Quiz...]")
        ttl = enterQuiz(self.Username)
        changeAccess = input("Type Private or Public: ").upper()

        for quizTitle in os.listdir(path):
            title = quizTitle.split('-')
            if ttl == quizTitle:
                if title[1] == "PUBLIC" or title[1] == "PRIVATE":
                    print("Access is already {0}".format(changeAccess))
                    break
                elif title[1] != "PUBLIC" or title[1] != "PRIVATE":
                    oldPath = r'C:\Users\user\PycharmProjects\MP\{0}\{1}'.format(self.Username + '-Quiz Title',quizTitle)
                    newPath = r'C:\Users\user\PycharmProjects\MP\{0}\{1}'.format(self.Username + '-Quiz Title',title[0] + '-' + changeAccess + '.txt')
                    os.rename(oldPath,newPath)
                    break

