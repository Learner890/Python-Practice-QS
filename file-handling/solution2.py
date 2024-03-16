with open(r"stocks.csv",'r') as file,open(r"output.csv",'w') as out:
    next(file)
    out.write("Company Name,PE Ratio,PB Ratio\n")
    for line in file:
        tokens=line.split(',')
        stock=tokens[0]
        pe_ratio=float(tokens[1])/float(tokens[2])
        price_to_book_ratio=float(tokens[1])/float(tokens[3])
        out.write(f"{stock},{pe_ratio},{price_to_book_ratio}\n")

        

