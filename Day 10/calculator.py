
def addition(first_num, second_num):
    """Returns the sum of two numbers"""
    return first_num + second_num

def subtraction(first_num, second_num):
    """Returns the difference between two numbers"""
    return first_num - second_num
    
def multiplication(first_num, second_num):
    """Returns the product of two numbers"""
    return first_num * second_num

def division(first_num, second_num):
    """Returns the quotient of two numbers"""
    return first_num / second_num


def display_answer(first_num, second_num, operation, answer):
    print(f"{first_num} {operation} {second_num} = {answer}")

def main():
    isTrue = True
    user_continue = ""
    while isTrue:
        if user_continue == "y":
            print("+\n-\n*\n/")
            operation = input("Pick an operation: ")
            second_num = float(input("What's the second number?: "))
        else:
            first_num = float(input("What is the first number?: "))
            print("+\n-\n*\n/")
            operation = input("Pick an operation: ")
            second_num = float(input("What's the second number?: "))

        #stores functions into variables
        add = addition
        subtract = subtraction
        multiply = multiplication
        divide = division

        if operation == "+":
            if user_continue == "y":
                new_answer = add(answer, second_num)
                display_answer(answer, second_num, operation, new_answer)
            else:
                answer = add(first_num, second_num)
                display_answer(first_num, second_num, operation, answer)

        elif operation == "-":
            if user_continue == "y":
                new_answer = subtract(first_num, second_num)
                display_answer(answer, second_num, operation, new_answer)
            else:
                answer = subtract(first_num, second_num)
                display_answer(first_num, second_num, operation, answer)

        elif operation == "*":
            if user_continue == "y":
                new_answer = multiply(answer, second_num)
                display_answer(answer, second_num, operation, new_answer)
            else:
                answer = multiply(first_num, second_num)
                display_answer(first_num, second_num, operation, answer)
        elif operation == "/":
            if second_num == float(0):
                print("You can't divide by 0. Please pick another number!")
            else:
                if user_continue == "y":
                    new_answer = divide(answer, second_num)
                    display_answer(answer, second_num, operation, new_answer)
                else:
                    answer = divide(first_num, second_num)
                    display_answer(first_num, second_num, operation, answer)
        user_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or 'q' to quit: ").lower()

        if user_continue == "q":
            isTrue = False
            break
main()