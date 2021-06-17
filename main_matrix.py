from playLA.Matrix import Matrix

if __name__ == "__main__":

    matrix = Matrix([[1,2],[3,4]])
    otherMatrix = Matrix([[3,4], [5, 6]])

    zero2_3 = Matrix.zero(2,3)

    print(matrix)

    print(matrix.shape())
    print(matrix.row_num())
    print(matrix.col_num())
    print(matrix.size())

    print("{} [1][0] is {}".format(matrix, matrix[1,0]))
    print("{} row_vector(1) is {}".format(matrix, matrix.row_vector(1)))
    print("{} col_vector(1) is {}".format(matrix, matrix.col_vector(1)))

    print("{} + {} = {}".format(matrix, otherMatrix, matrix + otherMatrix))
    print("{} - {} = {}".format(otherMatrix, matrix, otherMatrix - matrix))

    print("3 * {} = {}".format(matrix, 3 * matrix))
    print("{} * 3 = {}".format(matrix, matrix * 3))
    print("{} * {} = {}".format(matrix, otherMatrix, matrix * otherMatrix))

    print("{} / {} = {}".format(otherMatrix, 3, otherMatrix / 3))

    print("{} - {} = {}".format(matrix, otherMatrix, matrix - otherMatrix))
    print("-({} - {}) = {}".format(matrix, otherMatrix, -(matrix - otherMatrix)))

    print("zero2_3 = {}".format(zero2_3))