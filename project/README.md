# The Little Professor Game in Python
#### Video Demo: https://www.youtube.com/watch?v=qY-VGkYNd1A
#### Description:

This is a python program which simulates the Little Professor game. The Little Professor Game is a game designed to enhance the mental math skills of children aged 5 to 9. It presents
math expressions challenging the players to solve them, thereby providing an enjoyable gaming experience while fostering learning and development

## Project Structure:

### project.py

This is the python executable that is used to run the whole project. It consists of 7 functions, starting with the `main()`. The `main()` method, starts off with printing a few statetements for the user to understand the game as well as keep a few things in mind, such as how to answer decimal questions, and how to handle problems with division by zero. A while loop, which runs the main game, begins. at first, the `run_professor()` function is called to return a score. Once that function is run, the score is printed along with a message based on how much the player scored. Then, an inner while loop runs, where we ask the user whether they want to play the game again. The while loop is looking for "yes" or "no" inputs. If the user presses any buttons causing an EOFError, instead of an ugly python generated error message, it simply prints "Process Terminated"

The `run_professor()` function is the flesh of this code. The code starts with the `get_level()` function, which will return a number between 1 and 3, which the user will provide. The score starts at 0 and the counter starts at 10, signifying the 10 problems it will generate. It runs `generate_integer()` and `generate_operation()` to get the two numbers and the operation for the expression that will be printed for the user to answer. If the user answers the correct answer, we add 1 to the score and proceed to generate the next question. If the answer is wrong, we give the user 2 more chances to enter the correct answer, otherwise it prints out the right answer and proceeds to the next question. The program calculates the right answer by the `operation()` function.

The inputs from the user are handled in a robust manner. The program does a good job on collecting inputs and checking them to be of the expected format in every scenario. This is ensured so that any unwelcome input does not break the program. The input is handled in the `main()`, `get_level()` and `input_check()` functions


### test_project.py

Unit testing is an integral process of developing any software. Since this is an interactive game, the input needed to be tested. Upon research, the `unittest.mock` library did provide the `patch` method to help with testing the core project with inputs by simulating input scenarios in two functions. the `test_input_check()` function makes use of the `patch` method by simulating input scenarios which the user can give when prompted with questions. The `test_get_level()` tests whether 1, 2 and 3 are the only acceptable inputs by the `get_level()` function.

The remaining three test functions, check the authenticity of operations, as well as whether the acceptable numbers and operations are being generated. `test_operation()` tests all possible operations based on the parameters given to the `operation()` function. the `test_generate_integer()` and `test_generate_operation()` checks if my code is getting the numbers and operations that we intend it to generate.

To run the tests, please run `pytest test_project.py` in your terminal

#### `requirements.txt`

This file mentions all the libraries used in this project

Enjoy playing and learning with the Little Professor Game in Python!