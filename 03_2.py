quote=input("What is the quote? ")

while not quote:
    print("Please enter a quote.")
    quote=input("What is the quote? ")

name = input("Who said it? ")

while not name:
    print("Please enter a name.")
    name=input("Who said it? ")

print("{} says, \"{}\"".format(name,quote))
