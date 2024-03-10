'''Print square of all numbers between 1 to 10 except even numbers'''
square=[i*i for i in range(1,11) if i%2!=0]
print(square)