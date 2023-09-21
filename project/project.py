# Necessary Libraries
import random
import sys
from rich import print, pretty
pretty.install()

def main():

    # Game guidelines
    print("\nWelcome to the Little Professor Game in Python!\n")

    print(" Designed by Rakshan Nagesh \n\t Alpharetta, Georgia, United States \n")

    print("The Little Professor is a math game designed for children aged 5 to 9.")
    print("Instead of providing answers, it generates unsolved math expressions and prompts you to solve them.")
    print("Your goal is to answer as many correctly as possible.\n")
    print("You'll be asked, 'How many digits do you want for your numbers?' Choose 1, 2, or 3.")
    print(" - 1 for problems with one-digit numbers.")
    print(" - 2 for problems with two-digit numbers.")
    print(" - 3 for problems with three-digit numbers.\n")
    print("If you make a mistake, you'll see: 'Incorrect answer. Try again.'")
    print("You'll have 2 more chances to get it right after that.")
    print("Failing to answer correctly will result in losing a point.\n")
    print("\nBefore we begin, please keep these guidelines in mind:")
    print("   1. In case of division by zero problems, such as '3/0', please enter '0'.")
    print("   2. If an answer has more than three decimal places, round it to the nearest thousandth.")
    print("      (e.g., 0.6666 should be rounded to 0.667)")
    print("   3. The game uses standard arithmetic operations: addition, subtraction, multiplication, and division.")
    print("   4. You'll receive 10 math problems and be scored out of 10.")
    print("   5. If you wish to exit the game at any time, press 'Ctrl+D' to receive a 'Process Terminated' message. (only on cs50 python codespace)\n")

    # Main loop
    while True:
        print("\nGet Ready to test your mental math skills!\n\n")

        # Run the function and get the score
        score = run_professor()

        print(f"\nYou Scored: {score}")

        # Provide message based on score
        if score > 8:
            print("\nYou are a Genius!")
        elif 6 <= score <= 8:
            print("\nGetting there!")
        elif 4 <= score <= 6:
            print("\nI don't want to be mean!")
        else:
            print("\nThat is strange")

        # Ask if the player wants to retry the game
        while True:
            try:
                response = input("\nWanna go again? \n")
                if response.lower() == "yes":
                    break
                elif response.lower() == "no":
                    sys.exit("Thank you for playing, hope you had fun\n")
                else:
                    print("I am sorry I didn't quite catch that")
                    continue
            except EOFError:
                sys.exit("\nProcess Terminated\n")


def run_professor():
    level = get_level() # Level of difficulty
    score = 0
    count = 10

    # Main while loop
    while count > 0:
        # (Num1) (Operation) (num2)
        X = generate_integer(level)
        Y = generate_integer(level)
        Opr = generate_operation()

        # Inner While loop
        while True:
            try:
                user_answer = float(input_check(X,Y,Opr))
                correct_answer = operation(X,Y,Opr)

                # Check if the user typed the correct answer
                if correct_answer == user_answer:
                    # Generate a new problem and exit the inner loop
                    score += 1
                    break
                else:
                    # Ask the user to answer again (2 more attempts)
                    errorcount = 2
                    while errorcount > 0:
                        print("EEE.")
                        second_answer = float(input_check(X,Y,Opr))

                        # Update the score if the user answers correctly and break this error loop
                        if second_answer == correct_answer:
                            score += 1
                            break
                        # If after last attempt, print the answer and exit this loop
                        elif errorcount == 1:
                            print("EEE.\n")
                            print(f"{X} {Opr} {Y} = " + str(correct_answer))
                            break
                        # error loop counter
                        else:
                            errorcount -= 1
                    break
            # Handle invalid input
            except ValueError:
                continue

        # Main while loop iterator decreases by 1
        count -= 1

    return score

def get_level():
    # Prompt the user to choose a level ( 1, 2, 3)
    while True:
        try:
            level = int(input("How many digits do you want your numbers to be? \n"))
        except ValueError:
            continue
        except EOFError:
            sys.exit("\nProcess Terminated\n")
        if level not in [1, 2, 3]:
            continue
        else:
            break

    return level

def input_check(x,y,opr):
    looper = True


    while looper:
        try:
            result = input("\n" + f"{x} {opr} {y} = ")
            float(result)
            break
        except EOFError:
            sys.exit("\nProcess Terminated\n")
        except ValueError:
            print("Invalid Input! please try again")
            continue

    return result


def generate_integer(level):
    result = 0

    # Generate a random number
    match level:
        case 1:  # Single-digit
            result = random.randint(0, 9)
        case 2:  # Double-digit
            result = random.randint(10, 99)
        case 3:  # Triple-digit
            result = random.randint(100, 999)

    return result

def generate_operation():

    # generate a random operation
    return random.choice("+-*/")


def operation(x,y,op):
    result = 0

    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        if y == 0:
            result = 0
        else:
            result = round(x / y,3)

    return result

if __name__ == "__main__":
    main()