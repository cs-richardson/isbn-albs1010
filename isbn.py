isbn_number = input("ISBN: ")
new_number = 0
n = 1

while len(isbn_number) != 10:
    isbn_number = input("Retry: ")
    
for i in isbn_number:
    new_number += int(i) * n
    n += 1
    
if new_number % 11 == 0:
    print("YES")
    
else:
    print("NO")
