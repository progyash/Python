stack=[]
choice='y'
while choice=='y':
    print("1.PUSH")
    print("2.POP")
    print("3.Display elements of stack")
    c=int(input("Enter your choice: "))
    if c==1:
        a=int(input("Enter the elements which you want to push: "))
        stack.append(a)
    elif c==2:
        if stack==[]:
            print("Stack empty")
    else:
        print("Delete elements is: ",stack.pop())
    if c==3:
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])
    else:
        choice=input("Do you want to continue ? (y/n)")
        
