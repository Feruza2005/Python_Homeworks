#Number data type questions
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

num_1 = int(input("Enter a number1: "))
num_2 = int(input("Enter a number2: "))
result = num_1//num_2
remainder = num_1%num_2
print(f"Result is {result}" f" Remainder is {remainder}")

temperature = int(input("Enter a temperature in celcius: "))
fahrenheit = (temperature * 9/5) + 32 
print(f"Temperature is {fahrenheit}")

numb = int(input("Enter a number: "))
last_digit = numb%10
print(f"Last digit is {last_digit}")

number = int(input("Enter a number: "))
if (number%2==0):
    print("This number is even")
else:
     print("This number is odd")

#String questions

name = str(input("Enter your name: "))
BOY = int(input("Enter yout birth of year: "))
age= 2025 - BOY
print("Your age is ", age)

txt = 'LMaasleitbtui'
print(txt[1::2])
print(txt[::2])

text = str(input("Enter a text: "))
len = len(text)
upper = text.upper()
lower = text.lower()
print(f"The length of the text is {len}, in uppercase text will be {upper}, in lowercase text will be {lower} ")

text1 = str(input("Enter a text: "))
reverse = text1[::-1]
if (reverse == text1):
    print ("The text is a palindrome")
else:
    print ("The text is not a palindrome")

text2 = input("Enter a text: ")
text2 = text2.lower() 
count_vowels = 0 
count_consonants = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for char in text2:
    if char.isalpha(): 
        if char in vowels:
            count_vowels = count_vowels + 1 
        else:
            count_consonants = count_consonants + 1  

print(f"The number of vowels: {count_vowels} The number of consonants: {count_consonants}")

text_a = input("Enter a text: ")
text_b = input("Enter a text: ")
count_s = 0 
count_d = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for char in text_a:
    if char.isalpha(): 
        if char in text_b:
            count_s = count_s + 1 
        else:
            count_d = count_d + 1  
if (count_s>0):
    print("First text contains the second text")
else:
     print("First text doesn't contain the second text")

sentence = input("Enter a text: ")
old_word = input("Enter a text: ")
new_word = input("Enter a text: ")
final = sentence.replace(old_word, new_word)
print(final)

txt1 = input("Enter a text: ")
first_char=(txt1[0])
last_char=(txt1[-1])
print(f"The first char is {first_char}, the last char is {last_char}")

txt1 = input("Enter a text: ")
reversed_version=(txt1[::-1])
print(f"The text is {txt1}, the reversed text is {reversed_version}")

txt1 = input("Enter a text: ")
count = 1
i = 0
length = len(txt1)
while  (i < length):
    if (txt1[i] == " "):
        count = count+1
    i = i +1
print ("The number of words in the text is", count)        

txt2 = input("Enter a text: ")
count = 0
i = 0
length = len(txt2)
while  (i < length):
    if (txt2[i].isdigit() == True):
        count = count+1
    i = i +1
if (count > 0):
    print("Yes, the text contains digit")
else:
     print("No, the text doesn't contain digit")       

words = input("Enter a text: ").split()
print(words)
string = "-".join(words)
print(string)       

string1 = input("Enter a text: ")
fin = string1.replace(" ", "") 
print("String without spaces:", fin)

string1 = input("Enter a text: ")
string2 = input("Enter a text: ")
len1 = len(string1)
len2 = len(string2)
if (len1==len2):
    print("They are equal")
else:
    print("They are not equal")

string1 = input("Enter a text: ")
i=0
fin = string1[0]
len1 = len(string1)
while (i<len1):
    if (string1[i]==" "):
        fin = fin + string1[i+1]
        i = i + 1
    else:
        i=i+1
print(fin)

string1 = input("Enter a text: ")
str2= input("Enter a single character:")
i=0
fin = " "
len1 = len(string1)
while (i<len1):
    if (string1[i]!=str2):
        fin = fin + string1[i]
        i = i + 1
    else:
        i=i+1
print(fin)

string1 = input("Enter a text: ")
vowels= ['a','e','u', 'i','o']
result = string1
for vowel in vowels :
    result = result.replace(vowel, "*")
print(result)

text = input("Enter a sentence: ")
start_word = input("Enter the starting word: ")
end_word = input("Enter the ending word: ")

if text.startswith(start_word) and text.endswith(end_word):
    print("The sentence starts and ends with the given words.")
else:
    print("The sentence does not match the given words.")


username = input("Enter a username: ").strip()
password = input("Enter a password: ").strip()

if (username == ""):
    if ( password == ""):
        print("They are empty.")
    else:
        print("Only username is empty.")
else:
    if( password == ""):
        print("Only password is empty.")
    else:
        print("They are not empty.")

num1 = input("Enter a number: ")
num2 = input("Enter a number: ")

if (num1==num2):
    print("They are equal.")
    
else:
    print("They are not equal.")

num1 = int(input("Enter a number: "))
if (num1%2==0 and num1>0):
    print("The number is even and positive.")
elif (num1%2==0 or num1>0) :
    print("The number is either not even or negative.")
else:
    print("The number is neither even nor positive.")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
if (num1==num2 and num1==num3 and num2==num3):
    print("They are all equal")
elif (num1==num2 or num1==num3 or num2==num3) :
    print("Some of them are equal.")
else:
    print("They are all different.")

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if len(string1) == len(string2):
    print("Both strings have the same length.")
else:
    print("The strings have different lengths.")

num = int(input("Enter a number: "))
if (num % 3 == 0 and num % 5 == 0):
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
total = num1 + num2
if (total > 50):
    print("The sum is greater than 50.")
else:
    print("The sum is not greater than 50.")

num1= int(input("Enter a number: "))
if num1>10 and num1<20:
    print("The number is between desired range")
else:
    print("The number is not between desired range")


