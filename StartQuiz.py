import os
import time
import sys

quiz = [] # store the question and answer
currentAnswers = [] #store the inputted answers

currentPage = 0 # store the current visiting page or question
page = 1
forward_stack = [] # Stores page when pressed forward
backward_stack = []# Stores page when pressed backward
ctr = 0

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

def takeQuiz(username):
    path = r'C:\Users\user\PycharmProjects\MP\{0}'.format(username + '-Quiz Title')
    while True:
        print("=================================")
        print("\t\tTAKE QUIZ")
        print("---------------------------------")
        ttl = enterQuiz(username)
        print("---------------------------------")
        file = os.path.join(path,ttl)

        quizFile = open(file ,'r')
        for info in quizFile.readlines():
            data = info.split('|')
            quiz.append(data)

        backForward()
        return

#def index_in_list(currentAnswers, index):
#    return index < len(currentAnswers)

def visitPage(page): # function when visit the page
    global currentPage
    global score
    print("\n" * 50)
    try:
        if currentPage != 0: # if current page is 0 append in backward_stack
            backward_stack.append(currentPage)

        print("Question",quiz[page-1][0]) #-1 since index starts to 0
        print(quiz[page-1][1]) # print the question

        if page-1 < len(currentAnswers): # if the page is lesser than the length the current answer print the cA
            print("Enter Answer:",currentAnswers[page-1])
        else:
            ans = input("Enter Answer: ").upper() # else input then append to current answer
            currentAnswers.append(ans)
        currentPage = page # set the current page to page
        return  True
    except IndexError:
        print("You have Finish the Quiz")
        submitQuiz()
        return False


def forward():
    global currentPage
    if len(forward_stack) == 0:
        return
    else:
        backward_stack.append(currentPage) # append current page in backward
        currentPage = forward_stack[-1] # set the current page to top stack
        forward_stack.pop() # pop from the forward stack

def backward():
    global currentPage
    if len(backward_stack) != 0:
        return
    else:
        forward_stack.append(currentPage) # append the current page in the forward stack
        currentPage = backward_stack[-1] # set the current page to the top o backward stack
        backward_stack.pop(-1) #pop from the backwards

def newAnswer():
    newAns = input("Enter new Answer: ").upper()
    currentAnswers[currentPage-1] = newAns # replace the answer in the current answer with new

def backForward():
    global page
    animation = "|/-\\"
    for i in range(30):
        time.sleep(0.1)
        sys.stdout.write("\r" + "Generating..." + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n" * 50)
    while True:
        fn = visitPage(page)
        if not fn:
            return
        keypress = input("Backward(<)/Forward(>)/New Answer(N):").upper()
        if keypress == '>':
            forward()
            page += 1
        elif keypress == '<':
            backward()
            page-=1
        elif keypress == 'N':
            newAnswer()


def scoring():
    score = 0
    total = len(quiz)
    for cAns in range(len(currentAnswers)):
        if currentAnswers[cAns] +'\n' == quiz[cAns][2]:
            score +=1

    if total > score >= score//2 :
        print("Very Good!You got {0}/{1}".format(score,total))
    elif total == score:
        print("Perfect!You got {0}/{1}".format(score,total))
    elif total > score <= score >= score//2:
        print("Almost There!You got {0}/{1}".format(score,total))
    elif score == 0:
        print("Try again, :< You got {0}/{1}".format(score,total))

def submitQuiz():
    print("[Type 'Submit' to submit. Type 'No', if you won't submit yet]")
    submit = input("Do you want to submit: ").upper()
    if submit == "SUBMIT":
        scoring()
        return
    elif submit == "NO": #return
        backward()

