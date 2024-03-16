'''
You are given following list of stocks and their prices in last 3 days,

Stock	Prices
info	[600,630,620]
ril	[1430,1490,1567]
mtl	[234,180,160]

Write a program that asks user for operation. Value of operations could be,
print: When user enters print it should print following,
info ==> [600, 630, 620] ==> avg:  616.67
ril ==> [1430, 1490, 1567] ==> avg:  1495.67
mtl ==> [234, 180, 160] ==> avg:  191.33
add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.
'''
info = [600,630,620]
ril= [1430,1490,1567]
mtl= [234,180,160]

stock_dict={'info':info,'ril':ril,'mtl':mtl}

def user_operation(user_ops):
    for key,value in stock_dict.items():
        print(f"{key} ==> {value} ==> avg : {round(sum(value)/len(value),2)}")
 

def add(stock_ticker,price):
    if stock_ticker.lower() in stock_dict.keys():
        stock_dict[stock_ticker].append(price)
        return stock_dict
    else:
        stock_dict[stock_ticker]=[price]
        return stock_dict


def main():
    user_input=input('Enter an option between print and add : ')
    if user_input.lower()=='print':
        user_operation(user_input)
    elif user_input.lower()=='add':
        output=add(stock_ticker=input('Enter the stock_ticker : '),price=int(input('Enter stock price : ')))
        print(output)
        
if __name__=='__main__':
    main()

#user_operation(input('Enter the operation you want to perform : '))
