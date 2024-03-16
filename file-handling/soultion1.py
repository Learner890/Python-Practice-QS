output_dict={}
with open(r"C:\Users\nisha\Downloads\poem.txt",'r') as file:
    context=file.read()
    words=context.split(' ')
    for line in words:
        if line in output_dict:
            output_dict[line]+=1
        else:
            output_dict[line]=1

maximum=max(output_dict.values())

for key,value in output_dict.items():
    if value==maximum:
        print(f"word '{key}' has maximum word count i.e {value}")



