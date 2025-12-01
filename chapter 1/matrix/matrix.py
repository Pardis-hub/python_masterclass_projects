#taking a matrix from the user
def take_matrix():
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            columns = int(input("Enter number of columns: "))
            if rows == 0 or columns == 0:
                print("Error: rows and columns cannot be 0!")
                continue
            else:
                break
        except ValueError:
            print("Error: Enter an integer.")
    matrix = [] 
    print("Please enter the entries row-wise:")
    for _ in range(rows):   
        row = []
        for _ in range(columns):
            while True:
                try:
                    row.append(int(input()))
                    break   
                except ValueError:
                    print("Error: Enter an integer.")
        matrix.append(row)  
    return matrix

#print the matrix
def print_matrix(matrix):
    print(f"\n{len(matrix)}*{len(matrix[0])} Matrix: ")
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(matrix[r][c], end = " ")
        print()

#calculating row and column summations
def summation(matrix):
    print("\nRow sums:")
    for r in range(len(matrix)):
        row_sum = 0
        for c in range(len(matrix[0])):
            row_sum += matrix[r][c]
        print(f"row {r+1}: {row_sum}")  
    print("\nColumn sums:")
    for c in range(len(matrix[0])):
        col_sum = 0
        for r in range(len(matrix)):
            col_sum += matrix[r][c]
        print(f"column {c+1}: {col_sum}")

#main function
def main():
    matrix = take_matrix()
    print_matrix(matrix)
    summation(matrix)

#run main
main()