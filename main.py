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

#not sure if this step was necessary
#iterates through the list of names like names_list_with_newline_char[0] = "Aang\n"
#then replaces the \n char with an empty string
#appends this edited to names_edited list
for index in names_list_with_newline_char:
    name_without_char = index.replace('\n', '')
    names_edited.append(name_without_char)

names.close()

#reads letter contents to a list named letter_body
letter_contents= open("./Input/Letters/starting_letter.txt", "r")
letter_body = letter_contents.readlines()
letter_contents.close()

#empty string called finished_letter.
finished_letter = []
#loops trhough the edited names list
for index in range(len(names_edited)):
    #takes first generic line of letter.  replaces [name] with an edited name
    first_line_to_append = letter_body[0].replace('[name]', names_edited[index])
    #adds back newline char.  all the replace stuff above may have been unnecessary
    first_line_to_append = first_line_to_append + '\n'
    #print(first_line_to_append)
    #appends customized opening line to the empty list
    finished_letter.append(first_line_to_append)
    #iterates through the rest of the letter body.  starts at 2 and goes through the letter body
    #unintentionally correct.  starts at index 2 of letter.  this eliminates line 0 which is the opening line
    #then passes empty line.
    for jindex in range(2, len(letter_body)):
        finished_letter.append(letter_body[jindex])
    #print(finished_letter)
    #now need to write to a file
    #creates string for title of file.  adds name from list
    name_of_file = f"send_letter_to_{names_edited[index]}"
    #opens a newfile.  w flag included to create file or overwrite
    f = open(f"./Output/ReadyToSend/_{name_of_file}", "w" )
    #writes all lines to new file.
    f.writelines(finished_letter)
    #closes file
    f.close()

    #blanks out string name for file
    name_of_file = ""
    #clears list.
    finished_letter.clear()










