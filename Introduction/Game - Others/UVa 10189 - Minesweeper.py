def count_mines(matrix, i, j, n, m):
    count = 0
    if i-1 >= 0:
        if j-1 >= 0 and matrix[i-1][j-1] == '*':
            count += 1
        if matrix[i-1][j] == '*':
            count += 1
        if j+1 < m and matrix[i-1][j+1] == '*':
            count += 1
    if i+1 < n:
        if j-1 >= 0 and matrix[i+1][j-1] == '*':
            count += 1
        if matrix[i+1][j] == '*':
            count += 1
        if j+1 < m and matrix[i+1][j+1] == '*':
            count += 1
    if j-1 >= 0 and matrix[i][j-1] == '*':
            count += 1
    if j+1 < m and matrix[i][j+1] == '*':
            count += 1
    matrix[i][j] = str(count)
        
def print_matrix(matrix):
    for ele in matrix:
        print("".join(ele))

def main():
    case = 1
    while True:
        temp = input().split(" ")
        if len(temp) == 1:
            continue
        n = int(temp[0])
        m = int(temp[1])
        matrix = []
        if case > 1 and (n != 0 and m != 0):
            print()
        if n == 0 and m == 0:
            break
        for _ in range(n):
            matrix.append(list(input()))
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '.':
                    count_mines(matrix, i, j, n, m)
        
        print("Field #%d:" % case)
        print_matrix(matrix)
        case += 1


if __name__ == "__main__":
    main()