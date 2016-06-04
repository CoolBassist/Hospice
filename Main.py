def start():
    token(input()) #Starts to tokenise user input

def token(data):
    debug = False
    input = [data[0]] #Sets 'input' as an array and might as well set the first value as the first character of 'data' while we're here
    for i in range(1,len(data)): #A for loop to transfer each character as a data item in 'data'
        input.append(data[i]) #Creates a data item for every character, might be able to improve memory efficiency some other way...
    if debug:
        eatDebug(input) #Transfers 'data' to the eat function below
    else:
        eat(input)

def eatDebug(data):
    pointer = 0;
    pointerValues = [0]
    for i in range(len(data)): #Goes through each data item and processes it.
        if data[i] == ')': #Hold onto your butts
            end = i
            print("Start = ", start)
            print("End = ", end)
            print("data[start] = " + data[start])
            print("int(data[start])", int(data[start]))
            try:
                if int(data[start],10) % 1 == 0: #Tests if it's an integer
                    iterations = int(data[start])
                    print("Is integer? Yes")
            except:
                if data[start] == ' ': #If theres a space set iterations to the hex value BADA55, which translates to repeating forever
                    iterations = 0xBADA55
                    print("Is integer? No its is a space")
                else:
                    print("Not anything so exiting")
                    exit(0) #Exit if no number or space
            loop = [data[start+1]]
            print("loop = ", loop)
            for j in range(2,end-start):
                loop.append(data[start+j])
            print("loop = ", loop)
            if iterations == 0xBADA55:
                while True:
                    eatDebug(loop)
            else:
                for j in range(iterations):
                    eatDebug(loop)
        elif data[i] == 'U': #U for up
            try:
                pointerValues[pointer] += int(data[i-1])
            except:
                pointerValues[pointer] += 1
        elif data[i] == 'R': #R for right
            try:
                pointerValues.append(0)
                pointer += int(data[i-1])
            except:
                pointer += 1
        elif data[i] == 'D': #D for down
            if pointerValues[pointer] != 0:
                try:
                    pointerValues[pointer] -= int(data[i-1])
                except:
                    pointerValues[pointer] -= 1
            else:
                exit(0)
        elif data[i] == 'L': #L for left
            if pointer != 0:
                try:
                    pointer -= int(data[i-1])
                except:
                    pointer -= 1
            else:
                exit(0)
        elif data[i] == 'P':
            print(pointerValues[pointer])
        elif data[i] == '(':
            start = i + 1


def eat(data):
    pointer = 0;
    pointerValues = [0]
    for i in range(len(data)): #Goes through each data item and processes it.
        if data[i] == ')': #Hold onto your butts
            end = i
            try:
                if int(data[start],10) % 1 == 0: #Tests if it's an integer
                    iterations = int(data[start])
            except:
                if data[start] == ' ': #If theres a space set iterations to the hex value BADA55, which translates to repeating forever
                    iterations = 0xBADA55
                else:
                    exit(0) #Exit if no number or space
            loop = [data[start+1]]
            for j in range(2,end-start):
                loop.append(data[start+j])
            if iterations == 0xBADA55:
                while True:
                    eat(loop)
            else:
                for j in range(iterations):
                    eat(loop)
        elif data[i] == 'U': #U for up
            try:
                pointerValues[pointer] += int(data[i-1])
            except:
                pointerValues[pointer] += 1
        elif data[i] == 'R': #R for right
            try:
                pointerValues.append(0)
                pointer += int(data[i-1])
            except:
                pointer += 1
        elif data[i] == 'D': #D for down
            if pointerValues[pointer] != 0:
                try:
                    pointerValues[pointer] -= int(data[i-1])
                except:
                    pointerValues[pointer] -= 1
            else:
                exit(0)
        elif data[i] == 'L': #L for left
            if pointer != 0:
                try:
                    pointer -= int(data[i-1])
                except:
                    pointer -= 1
            else:
                exit(0)
        elif data[i] == 'P':
            print(pointerValues[pointer])
        elif data[i] == '(':
            start = i + 1

while True:
    start()
