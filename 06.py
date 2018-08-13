import time
year=int(time.strftime("%Y"))

age = input("What is your current age? ")
while not age:
    print("Please enter an age.")
    age = input("What is your current age? ")

retire = input("At what age would you like to retire? ")
if not retire:
    print("Please enter an age.")
    retire = input("At what age would you like to retire? ")


left = int(retire)-int(age)
yr_retire = int(year)+int(left)


if left > 0:

    print("You have {} years left until you can retire.".format(left))
    print("It's {}, so you can retire in {}.".format(year,yr_retire))

if left <= 0:

    print("Congratulations! You've already retired.")