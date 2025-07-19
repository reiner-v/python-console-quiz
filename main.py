import Signing
import GenerateQuiz
import ManageQuiz
import StartQuiz
import SearchQuiz
import MiniGame

def manageQ(username):
    mq = ManageQuiz.Manage(username)
    while True:
        print("=================================")
        print("\t\tMANAGE QUIZ")
        print("1.Your Quizzes\n2.ADD Question\n3.DEL Question\n4.DEL File\n5.CHANGE ACCESS\n0.Back")
        print("---------------------------------")
        choice = input("Enter your Choice: ")
        print("---------------------------------")
        print("Choice: ", choice)

        if choice =='1':
            mq.yourQuizzes()
        elif choice =='2':
            mq.addQuestion()
        elif choice == '3':
            mq.delQuestion()
        elif choice == '4':
            mq.deleteFile()
        elif choice == '5':
            mq.changeAccessFile()
        elif choice == '0':
            return displayMenu(username)
        else:
            print("Invalid Input")

def displayMenu(username): # username for access
    GenerateQuiz.Quiz(username)  # call
    while True:
        print("=================================")
        print("\t\tKNOW WHAT?")
        print("1.Take Quiz\n2.Create Quiz\n3.Search Quiz\n4.Manage Quiz\n5.Mini Game\n0.Exit")
        print("---------------------------------")
        choice = input("Enter your Choice: ")
        print("---------------------------------")
        print("Choice: ", choice)
        if choice == '1':
            StartQuiz.takeQuiz(username)
        elif choice == '2':
            mq = GenerateQuiz.MakeQuiz(username)
            mq.createQuiz() # call a method from make quiz class
        elif choice == '3':
            SearchQuiz.displayPublicFile(username)
        elif choice == '4':
            manageQ(username)
        elif choice == '5':
            MiniGame.miniGameMenu(username)
        elif choice == '0':
            startMenu()
        else:
            print("Invalid Input")


def startMenu():
    print(
        " ___  __    ________   ________  ___       __           ___       __   ___  ___  ________  _________  ________  "
        "    ")
    print(
        "|\\  \\|\\  \\ |\\   ___  \\|\\   __  \\|\\  \\     |\\  \\        |\\  \\     |\\  \\|\\  \\|\\  \\|\\   __  \\"
        "|\\___   ___\\\\_____  \\     ")
    print(
        "\\ \\  \\/  /|\\ \\  \\\\ \\  \\ \\  \\|\\  \\ \\  \\    \\ \\  \\       \\ \\  \\    \\ \\  \\ \\  \\\\\\  \\ "
        "\\  \\|\\  \\|___ \\  \\_\\|____|\\  \\    ")
    print(
        " \\ \\   ___  \\ \\  \\\\ \\  \\ \\  \\\\\\  \\ \\  \\  __\\ \\  \\       \\ \\  \\  __\\ \\  \\ \\   __  \\ \\ "
        "  __  \\   \\ \\  \\      \\ \\__\\   ")
    print(
        "  \\ \\  \\\\ \\  \\ \\  \\\\ \\  \\ \\  \\\\\\  \\ \\  \\|\\__\\_\\  \\       \\ \\  \\|\\__\\_\\  \\ \\  \\ \\"
        "  \\ \\  \\ \\  \\   \\ \\  \\      \\|__|   ")
    print(
        "   \\ \\__\\\\ \\__\\ \\__\\\\ \\__\\ \\_______\\ \\____________\\       \\ \\____________\\ \\__\\ \\__\\ \\__"
        "\\ \\__\\   \\ \\__\\         ___ ")
    print(
        "    \\|__| \\|__|\\|__| \\|__|\\|_______|\\|____________|        \\|____________|\\|__|\\|__|\\|__|\\|__|    \\|"
        "__|        |\\__\\ ")
    print(
        "                                                                                                              "
        " \\|__|")

    while True:
        print("===============================")
        print("1. Sign In\n2. Sign Up\n0. Exit")
        print("-------------------------------")
        choice = input("Enter Choice: ")
        print("-------------------------------")
        if choice == '1':
            un = Signing.signIn()
            displayMenu(un)
        elif choice == '2':
            Signing.signUp()
        elif choice == '0':
            print(" ________  ________  ________  ________  ________      ___    ___ _______   ___       ")
            print(
                "|\\   ____\\|\\   __  \\|\\   __  \\|\\   ___ \\|\\   __  \\    |\\  \\  /  /|\\  ___ \\ |\\  \\      ")
            print(
                "\\ \\  \\___|\\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\_|\\ \\ \\  \\|\\ /_   \\ \\  \\/  / | \\   __/|\\ \\  \\    ")
            print(
                " \\ \\  \\  __\\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\  \\ \\\\ \\ \\   __  \\   \\ \\    / / \\ \\  \\_|/_\\ \\  \\")
            print(
                "  \\ \\  \\|\\  \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\  \\_\\\\ \\ \\  \\|\\  \\   \\/  /  /   \\ \\  \\_|\\ \\ \\_"
                "_\\   ")
            print(
                "   \\ \\_______\\ \\_______\\ \\_______\\ \\_______\\ \\_______\\__/  / /      \\ \\_______\\|__|   ")
            print("    \\|_______|\\|_______|\\|_______|\\|_______|\\|_______|\\___/ /        \\|_______|   ___ ")
            print("                                                     \\|___|/                     |\\__\\ ")
            print("                                                                                 \\|__|")

            quit()
        else:
            print("Invalid Input")


startMenu()