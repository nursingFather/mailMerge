#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# list_names = open("Input/Names/invited_names.txt")
# guest = list_names.readlines()

with  open("Input/Names/invited_names.txt") as names:
    guest= names.readlines()


with open("Input/Letters/starting_letter.txt") as main_letter:
    letter = main_letter.read()
    for names in guest:
        names = names.strip("\n")
        final_letter = letter.replace("[name]", names)
        print(final_letter)
        with open(f"Output/ReadyToSend/letter_for_{names}.txt",mode="w") as invitation:
            invitation.write(final_letter)

