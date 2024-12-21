year = int(input("Enter year: "))

if year % 400 == 0:
    print("Given year is Leap Year")
elif year % 100 == 0:
    print("Given year is Non Leap Year")
elif year % 4 == 0:
    print("Given year is Leap Year")
else:
    print("Given year is Non Leap Year")
