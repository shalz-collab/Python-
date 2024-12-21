
digits = input("Enter 3 digits: ")

if len(digits) == 3 and digits.isdigit():
    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i != j and j != k and k != i:  
                    print(digits[i] + digits[j] + digits[k])
else:
    print("Please enter exactly 3 digits.")
