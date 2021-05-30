#final work
#success

# Give a brief explanation on the game instructions
print("------------------------------------------------------------------------")
print("|                             Mastermind Game                          |")
print("------------------------------------------------------------------------")
print("\n                     Welcome to Mastermind Game!")
print("\n      To be a mastermind, dare to guess the code I have in mind ")
print("\n      4 out of the 6 colours below are chosen (with sequence):")
print("\n      (r)ed   (o)range   (y)ellow   (g)reen   (b)lue   (p)ink")
print("\n    Can you guess the 4 chosen colours in their corresponding order?")
print("\n                        * * * Take note! * * *                        ")
print("\n      * Colours may duplicate.")
print("\n      * You have a total of 10 guesses to crack the code.")
print("\n      * Enter 'exit' to quit the game halfway.")
print("\n      * Input answer from previous attempts will be displayed.")
print("\n      * Feedback will be given in this format:                        ")
print("           C: Number of correct colours in the correct position")
print("           W: Number of correct colours in the wrong position")
print("\n      * Here's an example of how you should input your guessed answer:")
print("                      If your colour of choice is")
print("                  (r)ed, (o)range, (y)ellow, (g)reen")
print("                  Your Guess [r, o, y, g, b, p]: royg ")
print("\n")
print("Now it's your turn! Good luck. ".center(80,"-"))

def validate_usercolour():
    """A function that prompts the user to input guessed colours, 
        returns validated user input and 
        quits the program if 'exit' is inputted """
    while True:
        usercolour = input("\n                  Your Guess [r, o, y, g, b, p] = ").lower()
        # If user input 'exit', quit game
        if 'exit' in usercolour:
            print("\n          Thank you for playing! Goodbye...")
            quit()
        # Check if the input only consist of characters from colourlist
        colourslist = ['r', 'o', 'y', 'g', 'b', 'p']
        if any(character not in colourslist for character in usercolour):
            print("       Error! Only characters", colourslist, "are allowed!")
            continue
        # Check if the number of colors nunbers are 4
        if len(usercolour) != 4: 
            print("                  Error! Only 4 characters allowed!")
            continue
        break
    return usercolour

def split(v_usercolour):
    """Fuunction that splits string into a list of characters and 
       returns the list"""
    return list(v_usercolour)

def random():
    """Funtion that randomly chooses 4 out of 6 colours and returns the 
       chosen colours as a list"""
    import random
    colourslist = ['r','o','y','g','b','p']
    compcolour = random.choices(colourslist, k=4)
    return compcolour

again = 'y'
while again == 'y':  
   
    attempt = 1 # number of attempts
    compcolour = random() # randomly chooses 4 out of 6 colours 
    history_lst = [] # List that stores all the user's attempted answers
    c_w_lst = [] # List that stores all the 'C' and 'W' feedback 

    while attempt <= 10:
        v_usercolour = validate_usercolour() # Validate user input
        s_v_usercolour_lst = split(v_usercolour)  # split string into a list of characters 

        if s_v_usercolour_lst != compcolour:
            print("\n - - - - - - - - - - - - - Oh no! Try again - - - - - - - - - - - - - - -")
            history_lst.append(s_v_usercolour_lst) 
            attempt += 1

            correct = 0  # Number of correct colour in correct position (C)
            wrong = 0   # Number of correct colour in wrong position (W)
            
            # a copy of compcolour for code checking
            tempcompcolour = compcolour.copy()  
            # a copy of s_v_usercolour_lst for code checking
            tempusercolour = s_v_usercolour_lst.copy()

            # To count 'C' and remove the 'C' from the duplicated list 
            # so that it won't be counted as 'W'
            for i in range(len(tempusercolour)):
                if tempusercolour[i] in compcolour:
                    if tempusercolour[i] == tempcompcolour[i]:
                        tempcompcolour[i] = "x"
                        tempusercolour[i] = "z"
                        correct += 1

            # To count 'W"
            for i in range(len(tempusercolour)):
                if tempusercolour[i] in tempcompcolour:
                    if tempusercolour[i] != tempcompcolour[i]:
                        wrong += 1

            c_w = '    C: ' + str(correct) + '   W: ' + str(wrong)
            c_w_lst.append(c_w) # Store 'C' & 'W' feedback into C_W_lst

            #print('\ncompcolour:', compcolour) #test

            # To print the number of attempts and all elements in history_lst and c_w_lst 
            for i in range(len(history_lst)):
                print("\n           Attempt", str(i + 1) , ":", history_lst[i], c_w_lst[i])
                
            continue

        if s_v_usercolour_lst == compcolour:
            print("\n               Congratulation! You guessed it right.  ")
            print("\n                     Number of attempts: ", attempt )
            print("\n             Y O U   A R E   A   M A S T E R M I N D  !")
            break
        
    if attempt >= 10:
        print("\n           Too bad! You have exhausted your guesses T ^ T ")
    
    while True:
        again = input("\nDo you want to play again? [y/n]: ").lower()
        if again == 'y':
            print("\n------------------------------New Game---------------------------------")
            break
        elif again == 'n':
            break
        else:
            print("Invalid input")
            continue

print("\n            Thank You for playing. Hope seeing you soon = ) ")
print("\n---------------------------Program Ended------------------------------")
print()

