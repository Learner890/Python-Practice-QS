sugar_level=int(input('Enter your sugar level : '))

if sugar_level>=80 and sugar_level<=100:
    print(f"your sugar level is {sugar_level} which is normal")
elif sugar_level>100:
    print(f"your sugar level is {sugar_level} which is not high")
else:
    print(f"your sugar level is {sugar_level} which is low")