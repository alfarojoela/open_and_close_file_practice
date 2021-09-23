#BELOW SOLUTION FOR COMPARE AND CONTRAST OF ORIGINAL SOLUTION

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        #print(f"BEFORE STRIP: {name}")
        stripped_name = name.strip()
        #print(f"AFTER STRIP: {name}")

        #made error.  used name below.  ended up having , on separate line
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        #print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)







