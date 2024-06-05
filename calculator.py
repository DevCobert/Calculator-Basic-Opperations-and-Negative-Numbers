pointers = []
numbers = []
opperators = []
number = 0
integer = 0
answer = 0
opp = False #Makes sure 2 opperations are not next to each other, (input sanitation)
x1 = 0 
x2 = 1
x3 = 0
calculate = input ("Calculator")
def numreset():
    global opp
    global number
    global integer
    numbers.append(number)
    opp = False
    number = 0
    integer = 0
def UserInput():
    i = 0
    global opp
    global number
    global integer
    global answer
    lastOppWasDash = False #Handles Negative Numbers --------
    lastCharWasDash = False
    NumberIsNegative = False #Handels Negative Number ---------
    for c in calculate:
        if c == " ":
            lastCharWasDash = False
            NumberIsNegative = False
            if number != 0:
                numreset()
        if c == "1" or c == "2" or c == "3" or c == "4" or c == "5" or c == "6" or c == "7" or c == "8" or c == "9" or c == "0":
            if lastOppWasDash == 1 and lastCharWasDash == 1: #Positive Number
                NumberIsNegative = True
            if NumberIsNegative == False:
                opp = True
                integer = int(c)
                if number == 0:
                    number = integer
                else:
                    number = number * 10
                    number = number + integer
            if NumberIsNegative == True: #Negative Number
                opp = True
                integer = int(c)
                if number == 0:
                    number = integer * -1
                else:
                    number = number * -10
                    number = number + integer
        if c == "*":
            lastOppWasDash = False
            NumberIsNegative = False
            if opp == True:
                numreset()
            opperators.append(3)
        if c == "/":
            lastOppWasDash = False
            NumberIsNegative = False
            if opp == True:
                numreset()
            opperators.append(0)
        if c == "+":
            lastOppWasDash = False
            NumberIsNegative = False
            if opp == True:
                numreset()
            opperators.append(2)
        if c == "-":
            if opp == False and lastOppWasDash == True and NumberIsNegative == False: #Handles Negative Opperators
                numreset()
            lastOppWasDash = True
            lastCharWasDash = True
            NumberIsNegative = False
            if opp == True:
                numreset()
                opperators.append(1)
    numbers.append(number)
def Calculate():
    i = 0
    global opp
    global number
    global integer
    global answer
    global x1
    global x2 
    global x3 
    while i == 0:
        num1 = numbers[x1]
        num2 = numbers[x2]
        opp1 = opperators[x3]
        if opp1 == 3:
            answer = num1 * num2 
            i = 1
        if opp1 == 0:
            if num1 == 0 or num2 == 0:
                print("undefined divide by zero error")
                answer = 0
                i = 1
                return
            answer = num1 / num2
            i = 1
        if opp1 == 2:
            answer = num1 + num2
            i = 1
        if opp1 == 1:
            answer = num1 - num2
            i = 1
def Controller():
    global number
    global integer
    global answer
    global x1
    global x2 
    global x3
    UserInput()
    i = 0
    while i == 0:
        z = -1
        y = 0
        g = -1
        lenop = len(opperators)
        if lenop == 1:
            x1 = 0
            x2 = 1
            x3 = 0
            Calculate()
            i = 1
        if lenop < 1:
            i = 1
        if lenop > 1:
            for x in opperators:
                g += 1 
                if x == 3 or x == 0:
                    z = -1
                    if y == 0:
                        x1 = g
                        x2 = g + 1
                        x3 = g
                        Calculate()
                        numbers.pop(x2)
                        numbers.pop(x1)
                        opperators.pop(x3)
                        numbers.insert(x1 , answer)
                    y = 1
                if x == 2 or x == 1:
                    if y == 0:
                        z = g
            if z != -1:
                x1 = 0
                x2 = 1
                x3 = 0
                Calculate()
                numbers.pop(x2)
                numbers.pop(x1)
                opperators.pop(x3)
                numbers.insert(x1 , answer)
if calculate == "":
    print("you did not provide an input")
else:
      Controller()
      print(answer)

     