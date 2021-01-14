from io import open

# Normally we save the number and the name of the people
class contact:
    def __init__(self, number, name):
        self.number = number
        self.name = name

# Input the new contact
print("Input here the number: "); inputnumber = str(input())
print("Input here the name: "); inputname = str(input())

# Create contact class
newContact = contact(inputnumber, inputname)

# Save our contact on the book
book = open("contactbook.txt", "a")
contactstr = ("\n" + newContact.name + "   " + newContact.number)
book.write(contactstr)
book.close()
