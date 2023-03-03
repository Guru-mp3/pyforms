from copy import deepcopy


def addition_of_matrices(
    x,
    y
) -> list:
    if len(x) != len(y):
        raise ValueError("Not a square matrix")
    result = [[x[b][a] + y[b][a] for a in range(len(x[0]))] for b in range(len(x))]
    return result


def subtraction_of_matrices(
    x,
    y
) -> list:
    if len(x) != len(y):
        raise ValueError("Not a square matrix")
    result = [[x[a][b] - y[a][b] for a in range(len(x[0]))] for b in range(len(x))]
    return result


def scalar_multiplication(
    x,
    mul,
) -> list:
    b = [[x[r][c] * mul for c in range(len(x[0]))] for r in range(len(x))]
    return b


def multiply_matrix(
        x1: list,
        x2: list,
) -> list:
    rows_1 = len(x1)
    column_1 = len(x1[0])
    rows_2 = len(x2)
    column_2 = len(x2[0])
    if column_1 != rows_2:
        raise ValueError('Matrix Multiplication not Possible')
    b = [[0 for c in range(column_2)] for r in range(rows_1)]
    print(b)
    for k in range(column_2):
        for ind in range(rows_1):
            s = 0
            for j in range(column_1):
                s = s + x1[ind][j]*x2[j][k]
            b[ind][k] = s
    return b


def transpose(
    x
) -> list:
    b = [[x[r][c] for r in range(len(x))] for c in range(len(x[0]))]
    return b


def smallermatrix(
    original_matrix,
    row,
    column
) -> list:
    new = deepcopy(original_matrix)
    new.remove(original_matrix[row])
    for temp in range(len(new)):
        new[temp].remove(new[temp][column])
    return new


def determinant(
    matrix
) -> int | None:
    num_rows = len(matrix)
    for row in matrix:
        if len(row) != num_rows:
            raise ValueError("Not a square matrix")
    if len(matrix) == 2:
        simple_det = matrix[0][0]*matrix[1][1]-matrix[1][0]*matrix[0][1]
        return simple_det
    else:
        answer = 0
        num_columns = num_rows
        for j in range(num_columns):
            cofactor1 = (-1) ** (0+j) * matrix[0][j] * determinant(smallermatrix(matrix, 0, j))
            answer += cofactor1
        return answer


def cofactor(
    arr
) -> list:
    row = len(arr[0])
    column = len(arr)
    zeros = [[0 for rows in range(len(arr))] for columns in range(len(arr[0]))]
    for it in range(1, row+1):
        for j in range(1, column+1):
            zeros[it-1][j-1] = (-1)**(it+j)*determinant(smallermatrix(arr, it-1, j-1))
    return zeros


def inverse(
    arr
) -> list:
    a = transpose(cofactor(arr))
    det = determinant(arr)
    lst = [[a[iti][j]/det for j in range(len(a[0]))]for iti in range(len(a))]
    return lst


if __name__ == "__main__":
    m = int(input("number of rows"))
    n = int(input("number of columns"))
    li = list()
    for i in range(m):
        d = list(map(int, input("Enter numbers").split()))
        li.append(d)
    li2 = list()
    for i in range(m):
        d = list(map(int, input("Enter numbers").split()))
        li2.append(d)
    print(addition_of_matrices(li, li2))
# print(inverse(l))

# print(transpose(cofactor(l)))

# print(determinant(l))
