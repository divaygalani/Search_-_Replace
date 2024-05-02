# Function to search and optionally replace a word in a passage
def linear_search_replace(passage, search_word, replace_word=None):
    # Split the passage into a list of words
    words = passage.split()
    
    # Loop through the list of words
    for i in range(len(words)):
        # If the current word matches the search word
        if words[i] == search_word:
            # If a replace word is provided, replace the search word with it
            if replace_word:
                words[i] = replace_word
            # If no replace word is provided, underline the search word
            else:
                words[i] = '\033[4m' + words[i] + '\033[0m'
    
    # Join the modified list of words back into a passage
    result_passage = ' '.join(words)
    return result_passage

# Function to display a menu to the user and perform actions based on their choice
def menu():
    # Display menu options to the user
    print("1. Search for a word")
    print("2. Search and replace a word")
    
    # Get the user's choice
    choice = int(input("Enter your choice: "))
    
    # Get the passage from the user
    user_passage = input("Enter a passage: ")
    
    # Get the search term from the user
    search_term = input("Enter the word to search: ")
    
    # Perform actions based on the user's choice
    if choice == 1:
        # If the user chose option 1, search for the word in the passage and underline it
        result_passage = linear_search_replace(user_passage, search_term)
    elif choice == 2:
        # If the user chose option 2, get the replace term from them
        replace_term = input("Enter the word to replace it with: ")
        # Search for the word in the passage and replace it with the replace term
        result_passage = linear_search_replace(user_passage, search_term, replace_term)
    
    # Print out the resulting passage
    print("Resulting passage:", result_passage)

# Call the menu function to start the program
menu()