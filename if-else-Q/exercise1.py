'''
Q1. Write a program that asks user to enter a city name and it should tell which 
country the city belongs to
'''
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# user=input('Enter a city name : ')

# if user in india:
#     print(f"This city belongs to country India")
# elif user in pakistan:
#     print(f"This city belongs to country pakistan")
# elif user in bangladesh:
#     print(f"This city belongs to country bangladesh")
# else:
#     print(f"Invalid Input")

'''
Q2. Write a program that asks user to enter two cities and it tells you if they both are in 
same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" 
but if I enter mumbai and dhaka 
it should print "They don't belong to same country
'''
user_2=input('Enter two cities separated by comma : ').split(',')
if user_2[0] in india and user_2[1] in india:
    print('They belong to same country India')
elif user_2[0] in pakistan and user_2[1] in pakistan:
    print('They belong to same country pakistan')
elif user_2[0] in bangladesh and user_2[1] in bangladesh:
    print('They belong to same country bangladesh')
else:
    print("They don't belong to same country")

