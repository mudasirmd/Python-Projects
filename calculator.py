logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print("logo")
def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divisible(n1,n2):
    return n1/n2



operation={
    "+": add,
    "-" :subtract,
    "*" :multiply,
    "/" :divisible

}
def calculator():

    should_accumulate=True

    num1=float(input("enter the number:"))
    while should_accumulate:
        for symbol in operation:
            print(symbol)
        operation_symbol=input("enter the operator:")
        num2=float(input("what is the next number:"))
        answer=operation[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol}{num2}={answer}")
        choice=input(f"type 'y' for calculating with {answer}and 'n' for ending the calculating \n")
        if choice == "y":
            num1=answer
        else:
            should_accumulate=False
            print("\n"*20)
            calculator()

calculator()
