'''
We have following information on countries and their population (population is in crores),

Country	Population
China	143
India	136
USA	    32
Pakistan	21
Using above create a dictionary of countries and its population
Write a program that asks user for three type of inputs,
print: if user enter print then it should print all countries with their population in this format,
china==>143
india==>136
usa==>32
pakistan==>21
add: if user input add then it should further ask for a country name to add. If country already exist 
in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for 
population and add that new country/population in our dictionary and print it
remove: when user inputs remove it should ask for a country to remove. If country exist in our 
dictionary then remove it and print new dictionary using format shown above in (a). 
Else print that country doesn't exist!
query: on this again ask user for which country he or she wants to query. When user inputs that 
country it will print population of that country.
'''

Country=['China','India','USA','Pakistan']
Population=[143,136,32,21]
result_dict=dict(zip(Country,Population))
#print(result_dict.keys())
user_inp=input('Enter an input between options print,add,remove,query : ')
for key,value in result_dict.items():
    if user_inp.lower()=='print':
        print(f"{key}==>{value}\n")
    elif user_inp.lower()=='add':
        country_to_add=input('Enter country name to add : ')
        if country_to_add in result_dict.keys():
            print('Country already exists')
            break
        else:
            populatio_to_add=input('Enter population to add : ')
            result_dict[country_to_add]=populatio_to_add
            print(f"Entry successfully added new record is {result_dict}")
            break
    elif user_inp.lower()=='remove':
        country_to_remove=input('Enter country name to remove : ')
        if country_to_remove in result_dict.keys():
            result_dict.pop(country_to_remove)
            print(f"{country_to_remove} removed from dictionary update dictionary is {result_dict}")
            break
        else:
            print(f"{country_to_remove} doesn't exist in dictionary")
            break
    elif user_inp.lower()=='query':
        country_to_query=input('Enter the country name you want to query : ')
        print(f"Population of {country_to_query} is {result_dict[country_to_query]}")
        break
