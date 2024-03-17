def print_star(number=5):
    for i in range(number):
        s=''
        for j in range(i+1):
            s+='*'
        print(s)


print_star()