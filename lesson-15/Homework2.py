num = float(input("Enter a float number: "))
rounded_num = round(num, 2)
print("Rounded to 2 decimal places:", rounded_num)

num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))
if (num1>num2):
    print(num1)
else:
    print(num2)

distance = float(input("Enter a distance in km: "))
meters = distance*1000
cm = distance*100000
print( f" The distance {meters} in meters", f" The distance {cm} in centimeters")
