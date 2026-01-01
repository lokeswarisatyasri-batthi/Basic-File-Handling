try:
    # Open the file and read its content
    file = open("input.txt", "r")
    content = file.read()
    file.close()

    if content.strip() == "":
        print("The file is empty.")
    else:
        print("File content before replacement:\n")
        print(content)

        find_word = input("\nEnter the word to find: ")
        replace_word = input("Enter the word to replace with: ")

        if find_word not in content:
            print("\nThe word was not found in the file.")
        else:
            updated_content = content.replace(find_word, replace_word)

            file = open("input.txt", "w")
            file.write(updated_content)
            file.close()

            print("\nFile updated successfully.")
            print("\nFile content after replacement:\n")
            print(updated_content)

except FileNotFoundError:
    print("File not found. Please check the file name.")

except Exception as e:
    print("An unexpected error occurred:", e)

