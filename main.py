#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#letters = open("./Input/Letters/starting_letter.txt", "r")
#print(letters.readlines())

names = open("./Input/Names/invited_names.txt", "r")
#appears that return values of readlines() need to be stored into a variable after assignment.
#cannot access names.readlines() repeatedly.
#not sure why this is?
list_of_names = names.readlines()  #returns a list of text from file?  does this only work 1 time after opening?
#print(list_of_names)

new_list = []
new_line = chr(10)
for name in list_of_names:
    new_list.append(name.replace(new_line, " "))

#print(list_of_names)
#print(new_list)

list_edited = []
for name in new_list:
    list_edited.append(name.strip())

print(list_edited)

file = open("./Input/Letters/starting_letter.txt")

#needs a loop here.  salutation stays the same.  overwrite salutation_and_name through each iteration
#then take body_of_letter and overwrite subscript 0.  then write and export to separate file.
#appears body of letter needs to be saved as a list before the loop iterates.
#also needs list_edited name appended to name of file name to save.
salutation = file.readline()
salutation_and_name = salutation.replace("[name]", list_edited[0])
print(salutation_and_name)
salutation_and_name = salutation.replace("[name]", list_edited[2])
print(salutation_and_name)
#print(names.readlines())  #returns a list of text from file?


file = open("./Input/Letters/starting_letter.txt")
body_of_letter = file.readlines()
print(body_of_letter)

body_of_letter[0] = salutation_and_name

print(body_of_letter)

#list_of_names = names.readlines()
#print(list_of_names)
#print(len(list_of_names))




#examples = open("./Output/ReadyToSend/example.txt", "r")
#print(examples.readlines())


#HOW replace() works:
# to replace text in a string like txt = "one one was a race horse"
#x = txt.replace("one", "fuck") # first argument finds text to replace, second argument is the replacement.
# print(x)

#HOW strip() works:
#txt = "      banana      "
#x = txt.strip()  #this gets rid of all blank space in the string






