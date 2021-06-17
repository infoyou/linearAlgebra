class Vector:

    def __init__(self, lst):
        self._values = list(lst)

# 返回向量长度(有多少个元素)
    def __len__(self):
        return len(self._values)

#取向量第index个元素
    def __getitem__(self, index):
        return self._values[index]

# 系统调用
    def __repr__(self):
        return "Vector({})".format(self._values)

# 用户调用
    def __str__(self):
        return "({})".format(",".join(str(e) for e in self._values))

# 返回向量的迭代器
    def __iter__(self):
        return self._values.__iter__()

# 向量相加
    def __add__(self, other):
        assert len(self) == len(other),\
        "Error in adding. Length of vectors must be same."
        return Vector([a+b for a,b in zip(self, other)])

# 向量相减
    def __sub__(self, other):
        assert len(self) == len(other), \
                "Error in adding. Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, other)])

# 向量 * 标量
    def __mul__(self, k):
        return Vector([k*e for e in self])
    def __rmul__(self, k):
        return self*k

# 向量取正
    def __pos__(self):
        return 1*self

# 向量取负
    def __neg__(self):
        return -1*self