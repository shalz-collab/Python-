
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

Mat1 = []
Mat2 = []

print("Enter elements for Mat1:")
for i in range(rows):
    row = list(map(int, input().split()))
    Mat1.append(row)

print("Enter elements for Mat2:")
for i in range(rows):
    row = list(map(int, input().split()))
    Mat2.append(row)

Mat_sum = [[Mat1[i][j] + Mat2[i][j] for j in range(cols)] for i in range(rows)]

print("Mat Sum =")
for row in Mat_sum:
    print(" ".join(map(str, row)))
