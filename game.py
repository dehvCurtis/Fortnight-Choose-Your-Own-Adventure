print ("Welcome to Fortnite - Battle Royal")

#When the gamer first starts the game
print ("Your above Tilted Towers do you jump?.")
print('Do you want to jump')

## raw_input gets input from the user
## Here, we take the input, and *assign* it to a variable called 'ans'
answer = input("please type yes or no ")

## conditionals
## see if the user's answer is interesting or not
if answer=="yes":
    print ("That was foolish!  You are now dead.")
## elif means "else-if"
elif answer == "no":
    print ("That was wise!  You are alive, but thoroughly bored.")
## else is a 'catch-all' for "any condition not all ready covered"
else:
    print ("I don't know what to do, based on what you said, which was, |", ans, "|")

print ("Thank you for playing!")
