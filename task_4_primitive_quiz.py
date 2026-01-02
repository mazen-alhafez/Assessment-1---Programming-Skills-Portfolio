#first i made a dictionary, each key is a country, each value is the capital city, and all capitals stored in lower case so the can use different cases.

quiz = {
    "France": "paris",
    "Germany": "berlin",
    "Italy": "rome",
    "Spain": "madrid",
    "UK": "london",
    "Netherlands": "amsterdam",
    "Belgium": "brussels",
    "Austria": "vienna",
    "Portugal": "lisbon",
    "Greece": "athens"
}

#here i made a for loop so the code runs once for each country
for country, capital in quiz.items():
    answer = input(f"What is the capital of {country}?: ").strip().lower()
    # here is the if statement that says if the answer mathces the capital the answer will be correct if not it will be wrong
    if answer == capital:
        print("Correct")
    else:
        print(f"Wrong! The capital is {capital.capitalize()}.")