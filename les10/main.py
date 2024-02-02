newFormulaLoop = True


def add(numb1, numb2):
    return numb1 + numb2


def devide(nr1, nr2):
    return nr1/nr2


def multiply(numb1, numb2):
    return numb1*numb2


def subtract(nr1, nr2):
    return nr1-nr2


while newFormulaLoop:
    firstNumber = float(input("what is your first number?: "))
    reuseFormulaLoop = True
    while reuseFormulaLoop:
        specialSign = input(" +\n -\n *\n /\nchoose one of the above: ")
        secondNumber = float(input("what is your second number?: "))
        if specialSign == "+":
            result = add(firstNumber, secondNumber)
        elif specialSign == "-":
            result = subtract(firstNumber, secondNumber)
        elif specialSign == "*":
            result = multiply(firstNumber, secondNumber)
        elif specialSign == "/":
            result = devide(firstNumber, secondNumber)
        print(f"{firstNumber} {specialSign} {secondNumber} = {result}")
        goingOn = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if goingOn == 'y':
            firstNumber = result
        else:
            reuseFormulaLoop = False
