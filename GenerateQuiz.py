from modFiles import *
import time
import sys

def validation(value):
    while True:
        if value == "":
            print("Please Enter a", value)
        else:
            break

class Quiz:
    def __init__(self,username):
        self.QandA = []
        self.QuizTitles = []
        self.PublicFile = []
        self.User = []
        self.Username = username


class MakeQuiz(Quiz):
    def createQuiz(self):
        print("=================================")
        print("\t\t CREATE QUIZ")
        print("---------------------------------")
        title = input("Enter a Title: ").upper()
        self.QuizTitles.append(title)  # append the entered title
        print("---------------------------------")
        while True:
            noOfQuestion = input("No. of Question:")  # input no. of question to be asked
            try:  # check if the inputted value is valid data type
                int(noOfQuestion)
                break
            except ValueError:
                print("Please enter a digit")
        print("---------------------------------")

        for i in range(int(noOfQuestion)):  # loop until reach the noOfQuestion inputted value
            question = input("Enter the Question {0}: ".format(i+1)).upper()
            validation(question)  # call for validation
            answer = input("Enter the Answer: ").upper()
            validation(answer)  # call for validation
            self.QandA.append([str(i + 1), question, answer])  # append an array with number,question, answer
            print("\n")

        print("---------------------------------")
        while True:
            print("[Type \'Private\' if don't want to share your Quiz. "
                  "Type 'Public' if you want other to see you Quiz...]")
            access = input("Do you want it Private or Public?: ").upper()
            if access != "PRIVATE" and access != "PUBLIC":
                continue
            else:
                break
        print("---------------------------------")

        animation = "|/-\\"
        for i in range(80):
            time.sleep(0.1)
            sys.stdout.write("\r" + "Creating..." + animation[i % len(animation)])
            sys.stdout.flush()

        createQ = Files(username=self.Username, password="", q_a=self.QandA, title=title, QTitles=self.QuizTitles,access=access)  # call class from another module
        createQ.createQuizFile()  # call function in class to create a file
        print("\nSuccessfully Created!")

