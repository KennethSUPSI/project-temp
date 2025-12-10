# ghhg.py
# Create and print a matrix using two nested for loops

def create_matrix(rows: int, cols: int) -> list:
    matrix = [[0] * cols for _ in range(rows)]
    counter = 1
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = counter  # change to i*j or any formula you want
            counter += 1
    return matrix

def print_matrix(matrix: list) -> None:
    for row in matrix:
        print(" ".join(f"{v:4}" for v in row))

if __name__ == "__main__":
    try:
        r = int(input("Rows: ").strip() or 0)
        c = int(input("Cols: ").strip() or 0)
    except ValueError:
        print("Invalid input. Please enter integers.")
    else:
        if r <= 0 or c <= 0:
            print("Rows and cols must be positive integers.")
        else:
            m = create_matrix(r, c)
            print_matrix(m)

print("ghhg.py done.")
print("kobe")