## Cap 5 - Loops
#EX1 - Subtraction Quiz Loop
import random
import time

correct_count = 0 #count the number of correct answers
count = 0 #count the number of questions
number_of_questions = 5 #constant

start_time = time.time()

while   count < number_of_questions:
    #generate two random single digit integers
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)

    #if number1 < number 2 swap numbers
    if number1 < number2:
        number1, number2 = number2, number1

    #Prompt the user to answer "What is number1 - number2?"
    answer = eval(input("What is" + str(number1) + "-" + str(number2) + "? "))

    #grade the answer and display the result
    if number1 - number2 == answer:
        print("You are correct!")
        correct_count += 1
    else:
        print("Your answer is wrong. \n", number1, "-",
              number2, "is", number1 - number2)
    #increase the count
    count += 1

end_time = time.time()
test_time = int(end_time - start_time)
print("Correct count is", correct_count, "out of",
      number_of_questions, "\n Test time is", test_time, "seconds.")