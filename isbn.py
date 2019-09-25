#Albert
'''
The code shown below validates ISBN-10 numbers. If the user inputs an ISBN
number that doesn't have exactly 10 digits or if its made up of none-digits, it
will reprompt user.
'''

isbn_number = input("ISBN: ")

while len(isbn_number) != 10 or isbn_number.isdigit() == False:
    isbn_number = input("Retry: ")

sum_of_digits = 0
n = 1

'''
This loop adds the ISBN digits mulltiplied by its corresponding order number
together
'''

for i in isbn_number:
    sum_of_digits += int(i) * n
    n += 1

if sum_of_digits % 11 == 0:
    print("YES")
    
else:
    print("NO")
