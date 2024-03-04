def voter_age(age):
    if age<=0:
        print('Enter a valid age')
    elif age>0 and age <18:
        print('Not eligible to vote')
    else:
        print('Eligible to Vote')
voter_age(int(input('Enter you age : ')))