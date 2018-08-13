# 음수 넣을 수 없도록

a1 = True
while a1:
    try:
        a=float(input("What is the first number? "))
    except ValueError:
        print("Please enter a number.")
        continue
    else:
        break

b1 = True
while b1:
    try:
        b = float(input("What is the second number? "))
    except ValueError:
        print("Please enter a number.")
        continue
    else:
        break

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {}".format(a, b, a / b))


    if float(input("What is the first number? ")) < 0:
        a1 = False