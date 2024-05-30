# Task 1: Code Correction

# You are provided with a Python script that is supposed to help in event planning, but it has errors. 
# Identify and fix them.


attendees = float(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)


# Task 2: Catering Choices

# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, 
# otherwise recommend "Gourmet Meals Caterers".

food = input ("would you like vegetarian food?")

if food == "yes":
    print("We recommend Veggie Delight Caterers")
elif food == "no":
    print("We recommend Gourmet Meals Caterers")
else:
    print("please enter 'yes' or 'no'.")
