# Magic 8ball Program

# Importing Libaries required
import random as rand

# Magic 8ball responses
responses = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",

    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",

    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]
# Collecting users choice
def mainMenu():
    flag = True
    while flag:
        print("###############################################")
        print("Welcome to the famous Magic 8ball, would you:\n1) Ask a question\n2) Quit")
        print("###############################################")

        menuChoice = input("Enter a choice, 1 or 2\n> ")

        try:
            int(menuChoice)
            if int(menuChoice) < 1 or int(menuChoice) > 2:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(menuChoice)
        except:
            print("You did not have a valid choice")
            flag = True
  
            
# Collecting User's name as a function
def name():
    userName = input("What is your name?\n> ")
    for i in userName:
        if any(char.isnumeric() for char in userName):
            print("Your name cannot contain numbers")
            name()
        break
    return userName

# Collecting User's question
def question():
    userQuestion = input("What is your question?\n> ")
    return userQuestion

# Generating a random answer
def reply():
    magicReply = rand.choice(responses)
    return magicReply


def magicBall():
    Menu = mainMenu()
    # If statements for user input in menu function
    if Menu == 1:
        userName = name()
        userQuestion = question()
        magicReply = reply()
        while len(userQuestion) == 0:
            print("The magic 8 ball cannot provide your fortune if you do not provide it with a question")
            userQuestion = input("What is your question?\n> ")
        if len(userName) == 0:
            print(f"You asked {userQuestion}")
            print(f"The Magic 8ball replied with: {magicReply}")
        else:
            print(f"{userName} asked {userQuestion}")
            print(f"The Magic 8ball replied with: {magicReply}")
        
        askAgain = input("Would you like to ask again?\n>  ")
        if 'y' in askAgain.lower():
            magicBall()
        else:
            quit


    elif Menu == 2:
        quit

    else:
        print("Error")
magicBall()