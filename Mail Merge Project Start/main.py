# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names_file = open("./Input/Names/invited_names.txt")
names1 = names_file.readlines()
names2 = []

for n in names1:
    names2.append(n.strip("\n"))
letter_file = open("./Input/Letters/starting_letter.txt")
letter1 = letter_file.read()
for n in names2:
    with open(f"./Output/ReadyToSend/{n}'s_Invitation", mode="w") as inv:
        inv.write(letter1.replace("[name]", n))
letter_file.close()        
names_file.close()
