#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# f = open("demofile.txt", "r")
# print(f.readline())
# f.close()

#names is saved as a class object.
names = open("./Input/Names/invited_names.txt", "r")

#reads every line of names object.  each line becomes an element in the names_list.  however each name will be followed
#by a newline char.  example: name_list[0] = 'Aang\n'
names_list_with_newline_char = names.readlines()

names_edited = []

for index in names_list_with_newline_char:
    name_without_char = index.replace('\n', '')
    names_edited.append(name_without_char)

names.close()

letter_contents= open("./Input/Letters/starting_letter.txt", "r")
letter_body = letter_contents.readlines()
letter_contents.close()

finished_letter = []
for index in range(len(names_edited)):
    first_line_to_append = letter_body[0].replace('[name]', names_edited[index])
    #print(first_line_to_append)
    finished_letter.append(first_line_to_append)
    for jindex in range(2, len(letter_body)):
        finished_letter.append(letter_body[jindex])










