myfile=open("sonic.txt","w")
for i in range(5) :
    name=input("Enter charator name :- ")
    myfile.write(name)
    myfile.write('\n')
myfile.close()
      
