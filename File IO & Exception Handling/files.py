import os

#Deleting a file
# os.remove('data.txt')

# Writing to a file
file = open('data.txt', 'w')
file.write("\nThis is the first line of text.")
file.write("\nThis is the second line of text.")
file.write("\nThis is the third line of text.")
file.close()

#Append mode
file = open('data.txt', 'a')
file.write("\nThis is the fourth line of text.")

# Reading from a file 
file = open('data.txt', 'r')
content = file.read()
print(content)
file.close()


#Renaming a files
# os.rename('data.txt', 'updated_data.txt')

#Creating a directory
# os.mkdir('Files')

#Moving files
# os.renam('updated_data.txt', 'D:/College/Notes/Python-notes/File IO & Exception Handling/Files')
