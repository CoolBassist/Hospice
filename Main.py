def start():
    token(input('> ')) #Starts to tokenise user input

def token(data):
    debug = False
    input = [data[0]] #Sets 'input' as an array and might as well set the first value as the first character of 'data' while we're here
    for i in range(1,len(data)): #A for loop to transfer each character as a data item in 'data'
        input.append(data[i]) #Creates a data item for every character, might be able to improve memory efficiency some other way...
    if debug:
        eatDebug(input) #Transfers 'data' to the eat function below
    else:
        eat(input)

def eat(data):
    count = 0
    i = 0
    found = False
    pointer = 0
    pointerValues = [0]
    while(i != len(data)): #Goes through each data item and processes it.
        if data[i] == '(':
            start = i + 1
            while not found:
                if data[len(data)-1-count] == ')':
                    end = len(data)-1-count
                    found = True


                    print("Found the end loop")


                elif count == len(data):
                    exit(0)


            #print("start = ", start)
            #print("end = ", end)


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
                    at(loop)
            else:
                for j in range(iterations):
                    eat(loop)
                i += len(loop)+1

        elif data[i] == 'I': #I for increase
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
        elif data[i] == 'D': #D for decrease
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
        i += 1

while True:
    start()
