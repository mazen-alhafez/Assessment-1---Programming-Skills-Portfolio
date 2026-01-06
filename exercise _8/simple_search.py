#created a list of names 
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
# stored the name i want to find
search_name = "Sam"
found = False
# loop goes through each name in the list i made ones
for name in names:
    #check if the current name is sam
    if name == search_name:
        found = True
        break
#if statement if the name is found it prints sam was found in the list
if found:
    print(f"{search_name} was found in the list.")
    #if its not then prints was not found in the list
else:
    print(f"{search_name} was not found in the list.")
