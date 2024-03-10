expense=int(input("Enter your monthly expense : "))

expense_list = [2340, 2500, 2100, 3100, 2980]
c=True
for exp in expense_list:

    if exp==expense:
        c=False

        index=expense_list.index(exp)

        if  index==0:

            print("Given expense is of month January")

        elif index==1:

            print("Given expense is of month Febuary")

        elif index==2:

            print("Given expense is of month March")

        elif index==3:

            print("Given expense is of month April")

        elif index==4:

            print("Given expense is of month May")

if c:
    print("Expense is not between January and May")

