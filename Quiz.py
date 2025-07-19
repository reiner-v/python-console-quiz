from modFiles import *

def validation(value):
    while True:
        if value == "":
            print("Please Enter a", value)
        else:
            break

class Quiz:
    def __init__(self):
        self.QandA = []
        self.QuizTitle = []

class MakeQuiz(Quiz):
    def createQuiz(self):
        while True:
            noOfQuestion = input("No. of Question:")  # input no. of question to be asked
            try:  # check if the inputted value is valid data type
                int(noOfQuestion)
                break
            except ValueError:
                print("Please enter a digit")

        title = input("Enter a Title: ").upper()
        self.QuizTitle.append(title)  # append the entered title

        for i in range(int(noOfQuestion)):  # loop until reach the noOfQuestion inputted value
            question = input("Enter the Question: ").upper()
            validation(question)  # call for validation
            answer = input("Enter the Answer: ").upper()
            validation(answer)  # call for validation
            self.QandA.append([str(i + 1), question, answer])  # append an array with number,question, answer

        createQ = Files(title, self.QandA, self.QuizTitle,title="",QTitles="",access="")  # call class from another module
        createQ.createQuizFile()  # call function in class to create a file


