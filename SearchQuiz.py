import filecmp
from GenerateQuiz import *
import os
import shutil #for copy


class Search(Quiz):
    def publicAvailable(self):
        publicFile = []
        file = open('User\'s File.txt', 'r')
        for user in file.readlines():
            un = user.split('-')
            self.User.append(un[0])
            path = r'C:\Users\user\PycharmProjects\MP\{0}'.format(un[0] + '-Quiz Title')
            for txt in os.listdir(path):
                if '-PUBLIC.txt' in txt and txt not in publicFile:
                        publicFile.append(txt)

        for t in publicFile:
            ttl = t.rstrip("-PUBLIC.txt")
            print(ttl)
        print("---------------------------------")
        return

    def addFileInFolder(self):
        print("[Type title to add in YOUR QUIZZES. Type 'X' if you want to exit...]")
        add = input("Enter you want to add: ").upper() + '-PUBLIC.txt'
        if add == 'x':
            return
        else:
            destPath = r'C:\Users\user\PycharmProjects\MP\{0}\{1}'.format(self.Username + '-Quiz Title',add)
            for u in self.User:
                if add in os.listdir(r'C:\Users\user\PycharmProjects\MP\{0}'.format(u + '-Quiz Title')):
                    try:
                        if filecmp.cmp(r'C:\Users\user\PycharmProjects\MP\{0}\{1}'.format(u + '-Quiz Title', add),
                                       r'C:\Users\user\PycharmProjects\MP\{0}\{1}'.format(self.Username + '-Quiz Title', add)):
                            print("This Quiz already exist")
                            return
                    except FileNotFoundError:
                        shutil.copy(r'C:\Users\user\PycharmProjects\MP\{0}\{1}'.format(u + '-Quiz Title',add),destPath)
                        animation = "|/-\\"
                        for i in range(50):
                            time.sleep(0.1)
                            sys.stdout.write("\r" + "Adding File..." + animation[i % len(animation)])
                            sys.stdout.flush()
                        print('\n')
                    print("Successfully Added!")
                    break
            else:
                print("Quiz Title Unavailable")




def displayPublicFile(username):
    print("=================================")
    print("\t\t SEARCH QUIZ")
    print("---------------------------------")
    users = Search(username=username)
    users.publicAvailable()
    users.addFileInFolder()
    return
