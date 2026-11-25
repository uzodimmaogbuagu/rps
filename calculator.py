firstnumber = int(input("input first number"))

secondnumber = int(input("input second number"))

operator = input("Add operator (+, -, *, / ): ")

if operator == "+":
    result = firstnumber + secondnumber
    print(f"the result of{firstnumber} + {secondnumber} is equal to {result}")
elif operator == "-":
    result = firstnumber - secondnumber
    print(f"the result of{firstnumber} - {secondnumber} is equal to {result}")
elif operator == "*":
    result = firstnumber * secondnumber
    print(f"the result of{firstnumber} * {secondnumber} is equal to {result}")
elif operator == "/":
    result = firstnumber / secondnumber
    print(f"The result of {firstnumber} / {secondnumber} is equal to {result}")
    