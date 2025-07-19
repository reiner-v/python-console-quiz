import os

class Files:
    def __init__(self,username,password,q_a,title,QTitles,access):
        self.Username = username
        self.Password = password
        self.QandA = q_a
        self.Title = title
        self.QTitles = QTitles
        self.Access = access


    def createQuizFile(self):
        path = r'C:\Users\user\PycharmProjects\MP\{0}'.format(self.Username + '-Quiz Title') # for folder
        if not os.path.exists(path): # if the folder doesn't exist create else continue
            os.mkdir(path)
        quiz = os.path.join(path,self.Title + '-' + self.Access + '.txt') #place the txt into the designated folder

        quizFile = open(quiz,'w')
        for i in range(len(self.QandA)):
            data = self.QandA[i][0] + '|' + self.QandA[i][1] + '|' + self.QandA[i][2] + '\n'
            quizFile.write(data)
        quizFile.close()

    def createUsersFile(self):
        usersFile = open('User\'s File.txt','a') #user's information
        newUser = self.Username + '-' + self.Password + '\n'
        usersFile.write(newUser)
        usersFile.close()

    def signValidation(self,user):
        f = open('User\'s File.txt','r')
        for u in f.readlines():
            if user == u:
                print("=================================")
                print("Welcome Back!{0}".format(self.Username))
                break
        else:
            print("Invalid Username or Password")
            return False
        return self.Username

    def leaderBoard(self,score):
        info = []
        f = open('LeaderBoard.txt', 'r')
        for i in f.readlines():
            x = i.split('-')
            info.append(x)
        f.close()

        fw = open('LeaderBoard.txt', 'w+')
        for c in range(len(info)):
            if self.Username == info[c][0]:
                info[c][1] = str(score) + '\n'
            fw.write(info[c][0] + '-' + info[c][1])
            if c == len(info)-1:
                return
        else:
            fw.write(self.Username + '-' + str(score) + '\n')


