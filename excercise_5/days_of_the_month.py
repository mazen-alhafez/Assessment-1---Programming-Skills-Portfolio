#first i made a dictionary that shows each moth of the year and its days
days = {
    "1": "31",
    "2": "28",
    "3": "31",
    "4": "30",
    "5": "31",
    "6": "30",
    "7": "31",
    "8": "31",
    "9": "30",
    "10": "31",
    "11": "30",
    "12": "31"
}
# used input to make the user to pick a number between 1-12 to choose the desired month
user_answer = input("Enter moth number between 1-12: ")
# used if statment to check if the entered month is valid to print the number of its days
if user_answer in days:
    print(f"There are {days[user_answer]} days in this month")
# and if its invalid it prints invalid 
else:
    print("invalid")
