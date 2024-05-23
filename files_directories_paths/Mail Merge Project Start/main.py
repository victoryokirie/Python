PLACEHOLDER = "[name]"

## open the invited names and convert it to a list of names
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

## read the sample letter and assign it to a string
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    ## loop through the names and replace the placeholder with each name
    for name in names:
        stripped_name = name.strip()
        new_letter =letter_contents.replace(PLACEHOLDER, stripped_name)
        ## output the new letters to separate files
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)