'''
Lets say you are running a 5 km race. Write a program that,

Upon completing each 1 km asks you "are you tired?"
If you reply "yes" then it should break and print "you didn't finish the race"
If you reply "no" then it should continue and ask "are you tired" on every km
If you finish all 5 km then it should print congratulations message
'''
flag=True
for i in range(1,6):
    print(f"Congrats {i} KM race is completed")
    reply=input("Are you tired (type yes or no) : ")
    if reply.lower()=='yes':
        print("You didn't finish the race")
        flag=False
        break
    else:
        continue
if flag:
    print("Congrats you completed the race")
    
