age = int(input("Are you a cigarette addict older than 75 years old?:"))
chronic = input("Do you have a severe chronic disease?:(Yes/No)")
immune = input("Is your immune system too weak:(Yes/No)")


ageCheck = age >= 75



chronicCheck = chronic == "Yes"
checkImmune = immune == "Yes"

if(ageCheck and chronicCheck and checkImmune):
    print("You have corona virus risk!")
else:
    print("You dont have a corona virus risk!")

