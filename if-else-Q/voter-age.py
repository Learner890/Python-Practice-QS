def voter_age(age):
    if age<18:
        print('Not able to vote')
    else:
        print('Able to Vote')
voter_age(int(input('Enter you age : ')))