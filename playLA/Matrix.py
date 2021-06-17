from .Vector import Vector

class Matrix:

    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    def __repr__(self):
        return "Matrix({})".format(self._values)

    __str__ = __repr__

# 零矩阵
    @classmethod
    def zero(cls, r, c):
        return cls([[0] * c for _ in range(r)])

# 行
    def row_num(self):
        return self.shape()[0]
# 列
    def col_num(self):
        return self.shape()[1]

# size
    def size(self):
        return self.row_num() * self.col_num()

# 返回矩阵的形状：(行数，列数)
    def shape(self):
        return len(self._values), len(self._values[0])

# 返回矩阵pos位置的元素
    def __getitem__(self, pos):
        r, c = pos
        return self._values[r][c]

# 行向量
    def row_vector(self, index):
        return Vector(self._values[index])

# 列向量
    def col_vector(self, index):
        return Vector(row[index] for row in self._values)

# 向量相加
    def __add__(self, other):
        assert self.shape() == other.shape(), \
            "Error in adding. Shape of matrix must be same."
        return Matrix([a + b for a, b in zip(self.row_vector(i), other.row_vector(i))] for i in range(self.row_num()))

# 向量相减
    def __sub__(self, other):
        assert self.shape() == other.shape(), \
            "Error in adding. Shape of matrix must be same."
        return Vector([a - b for a, b in zip(self.row_vector(i), other.row_vector(i))] for i in range(self.row_num()))

# 矩阵 * 矩阵
    def dot(self, other):
        assert self.shape() == other.shape(),\
        "Error in adding. Shape of matrix must be same."
        return sum([a * b for a, b in zip(self.row_vector(i), other.row_vector(i))] for i in range(self.row_num()))

# 矩阵 * 标量
    def __mul__(self, k):
        return Matrix([[k*e for e in self.row_vector(i)] for i in range(self.row_num())])

    def __rmul__(self, k):
        return self*k

# 矩阵除法
    def __truediv__(self, k):
        return (1 / k) * self

# 矩阵取正
    def __pos__(self):
        return 1 * self

# 矩阵取负
    def __neg__(self):
        return -1 * self