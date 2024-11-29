import random
def oddeven():
    while True:

        user=input("enter the choice even or odd\n").lower()
        
        if user.lower() not in ["odd","even"]:
            print("Invalid input. Please enter 'odd' or 'even'.")
            continue
        if user.lower()=='even':
            computer1='odd'
        else:
            computer1="even"
        print(f"computer chooses :{computer1}")
        com=random.randint(0,6)
        print("computer value",com)
        userchoice=int(input("enter the value :"))
        result=userchoice+com
        if result%2==0:
            if user.lower()=="even":
                print("user to choose bowl or bat")
                user_bat_choice = input("Enter 'bat' or 'bowl': ")
                if user_bat_choice.lower() == 'bat':
                    batting = 'user'
                else:
                    batting = 'computer'
                break
            else:
                print("computer won,computer to choose the bowlling or batting ")
                # values=["bowling","batting"]
                computer_choice = random.choice(["bowl","bat"])
                print(f"computer choice is{computer_choice}")
                if computer_choice=='bat':
                    batting='computer'
                else:
                    batting='user'
                break
        elif user.lower()=="odd":
            print("user to choose bowl or bat")
            user_bat_choice = input("Enter 'bat' or 'bowl': ")
            if user_bat_choice.lower() == 'bat':
                batting = 'user'
            else:
                batting = 'computer'
            break
        else:
            print("computer won,computer to choose the bowlling or batting ")
            # values=["bowling","batting"]
            computer_choice = random.choice(["bowl","bat"])
            print(f"computer choice is{computer_choice}")
            if computer_choice=='bat':
                batting='computer'
            else:
                batting='user'
        break
    print('_FIRST SESSION_')
    user_score=0
    computer_score=0

    while True:
        if batting == 'user':
            user_run=int(input('Enter your run : '))
            computer_run = random.randint(1, 6)
            if user_run<1 or user_run>6:
                print('Please enter run between 1 and 6')
                continue
            print(f"Computer rolled: {computer_run}")
            if user_run == computer_run:
                print("You are out!")
                batting = 'computer'
                break
            else:
                user_score += user_run
        else:
            user_run = int(input('Enter your bowl : '))
            computer_run = random.randint(1, 6)
            if user_run<1 or user_run>6:
                print('Please enter run between 1 and 6')
                continue
            print(f"Computer rolled: {computer_run}")
            if user_run == computer_run:
                print("Computer's out!")
                batting = 'user'
                break
            else:
                computer_score += computer_run


    print(f'user score is {user_score}')
    print(f'computer score is {computer_score}')

    print('_SECOND SESSION_')



    while True:
        if batting == 'user':

            user_run=int(input('Enter your run : '))
            computer_run = random.randint(1, 6)
            if user_run<1 or user_run>6:
                print('Please enter run between 1 and 6')
                continue
            print(f"Computer rolled: {computer_run}")
            if   user_score>computer_score:
                break
            if user_run == computer_run:
                print("You are out!")
                batting = 'computer'
                break
            else:
                user_score += user_run
        else:
            user_run = int(input('Enter your bowl : '))
            computer_run = random.randint(1, 6)
            print(f"Computer rolled: {computer_run}")
            if user_run == computer_run:
                print("Computer's out!")
                batting = 'user'
                break
            else:
                computer_score += computer_run
                if computer_score > user_score:
                    break


    print(f'user score is {user_score}')
    print(f'computer score is {computer_score}')


    if computer_score>user_score:
        print('Computer Won!')
    elif user_score>computer_score:
        print('You Won')
    else:
        print('Tie Match!')

oddeven()
