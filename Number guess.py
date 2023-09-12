import random
i=0
y=100
javab='k'
answer=int(input("What is your number: "))
if answer >=0 and answer <=100:
    num=random.randint(i,y)
    while javab=='k' or javab=='b' or javab=='d':
        print("The number guess by computer is: ",num)
        javab=input("Your answer is k or b or d :")
        if javab=='k':
            y=num
        if javab=='b':
            i=num
        if javab=='d':
            print("Your number is right: ",num)
            break
        num=random.randint(i,y)
else:
    print("The number is wrong")

