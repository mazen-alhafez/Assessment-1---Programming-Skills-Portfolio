#in this code i made a dictionary where the user can type, store and print their info.
my_info = {
    "name": input("Enter your full name: "),
    "homeTown": input("Enter your hometown: "),
    "age": input("Enter your age: ") 
}
#when the user type thier info i used print to print all the info together in the console.
print(f"name: {my_info['name']}\nhome: {my_info['homeTown']}\nage: {my_info['age']}")
