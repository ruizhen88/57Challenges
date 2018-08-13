str_a=input("What is the first number? ")
str_b=input("What is the second number? ")

a=float(str_a)
b=float(str_b)

print(
"""
{is_a} + {is_b} = {plus}
{is_a} - {is_b} = {minus}
{is_a} * {is_b} = {mulitply}
{is_a} / {is_b} = {divide}
"""
.format(is_a=a, is_b=b, plus=a+b, minus=a-b, mulitply=a*b, divide=a/b)
      )

