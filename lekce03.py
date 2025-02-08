# Vytvoří nový prázdný slovník user_1,doplní do slovníku user_1 klíč name (hodnota "Marek") a surname (hodnota "Parek"),
# pomocí vhodné metody rozšíří stávající slovník user_1 o zadanou proměnnou user_email,
# vypiš hodnoty nového slovníku user_1 s úvodním textem "User #01:".
# Ukázka průběhu: User #01 {'name': 'Marek', 'surname': 'Parek', 'email': 'marek.parek@gmail.com'}

import string  # puntaction cleaning

print(60 * "*")  # welcome
print(60 * "*")
print(
    """               Welcome to the text analyzer.
              ===============================
        Please enter your name and password to continue"""
)
print(60 * "*")
print(60 * "*")
print()
users = {  # users, name + password
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}
# input name + password
name = input("Name:")
if name in users:
    print(10 * "=")
    print("")
else:
    print("Unregistered user, terminating the program..")
    exit()

print(10 * "=")
password = input("Password:")
if users.get(name) == password:
    print(10 * "=")
    print(
        f"""  ***  Welcome to the app, {name}  *** 
>>>  We have 3 texts to be analyzed.  <<<"""
    )
    print()
else:
    print("Wrong password, terminating the program..")
    exit()
# texts for analyse
texts = (
    """Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.""",
    """At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.""",
)
# while true , text choice
while True:
    choice_input = input("Enter a number from 1 to 3: ")
    if not choice_input.isdigit():
        print(f"Oops - please enter a number.")
        continue

    choice = int(choice_input)
    if choice < 1 or choice > 3:
        print(f"Oops - please enter a number between 1 and 3.")
        continue
    # Text select
    text = texts[choice - 1]
    # list of values ​​from the assignment
    word_count = len(text.split())
    titlecase_words = sum(1 for word in text.split() if word.istitle())
    uppercase_words = sum(1 for word in text.split() 
                            if word.isupper() and word.strip(string.punctuation).isalpha())
    lowercase_words = sum(1 for word in text.split() if word.islower())
    numeric_strings = sum(1 for word in text.split() if word.isdigit())
    sum_numbers = sum(int(word) for word in text.split() if word.isdigit())

    # Outputs prints
    print(50*'-')
    print(f"There are {word_count} words in the selected text.")
    print(50*'-')
    print(f"There are {titlecase_words} titlecase words.")
    print(50*'-')
    print(f"There are {uppercase_words} uppercase words.")
    print(50*'-')
    print(f"There are {lowercase_words} lowercase words.")
    print(50*'-')
    print(f"There are {numeric_strings} numeric strings.")
    print(50*'-')
    print(f"The sum of all the numbers {sum_numbers}")
    print(50*'*')

    # Counting word length frequency >>>> Graph
    length_frequencies = {}
    for word in text.split():
        punctuation = word.strip(string.punctuation)  # Remove punctuation
        if punctuation:
            length = len(punctuation)
            length_frequencies[length] = length_frequencies.get(length, 0) + 1

    if length_frequencies:
        max_length = max(length_frequencies.keys())
    else:
        max_length = 0

    print("+", "-" * 26, "+")
    print(f"| {'LEN':<3}|{'OCCURRENCES':^17}|{'NR.':>4} |")
    print("+", "-" * 26, "+")
    for i in range(1, max_length + 1):
        graph = "*" * length_frequencies.get(i, 0)
        print(f"| {i:<3}|{graph:<17}|{length_frequencies.get(i, 0):>4} |")
    print("+", "-" * 26, "+")

    # option for further analysis
    repeat = (
        input(
            """Do you want to perform another analysis? (y/n),
otherwise the program will be terminated >>>>>> :"""
        )
        .strip()
        .lower()
    )
    if repeat != "y":

        print()
        print(f"Thank you for using our app, {name}!")
        print()
        print(
            """        ******          ******
        ***********     ***********
        *************    **********
        **************************
         ************************
          ********************
            ****************
              ********
                **"""
        )
        break