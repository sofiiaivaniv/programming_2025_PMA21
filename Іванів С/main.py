def read_matrix(file):
    m = []
    with open(file) as f:
        for line in f:
            line = line.strip().split()
            m.append([int(x) for x in line])
    return m
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

def write_matrix(filename, name, matrix):
    with open(filename, "a") as f:
        f.write(f"{name}:\n")
        for row in matrix:
            f.write(" ".join(map(str, row)) + "\n")
        f.write("\n")

def add_matrix(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Matrices have different sizes for addition")
        return None
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def sub_matrix(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Matrices have different sizes for subtraction")
        return None
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def mult_matrix(a, b):
    if len(a[0]) != len(b):
        print("Matrices cannot be multiplied (wrong dimensions)")
        return None
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

def determinant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]
    det = 0
    for c in range(len(m)):
        minor = [row[:c] + row[c+1:] for row in m[1:]]
        det += ((-1)**c) * m[0][c] * determinant(minor)
    return det
def transpose(m):
    return [list(row) for row in zip(*m)]
def inverse_matrix(m):
    det = determinant(m)
    if det == 0:
        print("Matrix is singular, cannot divide")
        return None
    if len(m) == 2:
        return [[m[1][1]/det, -m[0][1]/det],
                [-m[1][0]/det, m[0][0]/det]]
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = [row[:c] + row[c+1:] for row in (m[:r]+m[r+1:])]
            cofactorRow.append(((-1)**(r+c)) * determinant(minor))
        cofactors.append(cofactorRow)
    cofactors = transpose(cofactors)
    for i in range(len(cofactors)):
        for j in range(len(cofactors)):
            cofactors[i][j] = cofactors[i][j] / det
    return cofactors

def div_matrix(a, b):
    inv = inverse_matrix(b)
    if inv is None:
        return None
    return mult_matrix(a, inv)
m1 = read_matrix("matrix1.txt")
m2 = read_matrix("matrix2.txt")

print("Matrix 1:")
print_matrix(m1)
print("Matrix 2:")
print_matrix(m2)

open("out.txt", "w").close()
res = add_matrix(m1, m2)
if res:
    print("Matrix1 + Matrix2:")
    print_matrix(res)
    write_matrix("out.txt", "Matrix1 + Matrix2", res)
res = sub_matrix(m1, m2)
if res:
    print("Matrix1 - Matrix2:")
    print_matrix(res)
    write_matrix("out.txt", "Matrix1 - Matrix2", res)
res = mult_matrix(m1, m2)
if res:
    print("Matrix1 * Matrix2:")
    print_matrix(res)
    write_matrix("out.txt", "Matrix1 * Matrix2", res)

res = div_matrix(m1, m2)
if res:
    print("Matrix1 / Matrix2:")
    print_matrix(res)
    write_matrix("out.txt", "Matrix1 / Matrix2", res)