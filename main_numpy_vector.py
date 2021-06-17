import numpy as np

if __name__ == "__main__":
    print(np.__version__)

    lst = [1,2,3]
    lst[0] = "Linear Algebra"

    print(lst)

    # vec = np.array([3, 4, 6])
    # otherVec = np.array([5, 4, 3])

    vec = np.array([3, 4])
    otherVec = np.array([5, 4])

    print(vec)
    # vec[0] = 5
    print(vec)

# np 创建 vector
    print("zero vector {}".format(np.zeros(5)))
    print("ones vector {}".format(np.ones(5)))
    print("same elements vector {}".format(np.full(5, 888)))

# np vector 的基本属性
    print("{} vector size {}".format(vec, vec.size))
    print("{} index [0] = {}".format(vec, vec[0]))
    print("{} index [-1] = {}".format(vec, vec[-1]))
    print("{} index [0:2] = {}".format(vec, vec[0:2]))

# type is <class 'numpy.ndarray'>
    print("{} type is {}".format(vec, type(vec[0:2])))

# 基本运算
    print("{} + {} = {} ".format(vec, otherVec, vec + otherVec))
    print("{} - {} = {} ".format(vec, otherVec, vec - otherVec))
    print("{} * {} = {} ".format(vec, 3, vec *3))
    print("{} * {} = {} ".format(3, vec, 3 * vec))

    print("{} * {} = {} ".format(vec, otherVec, vec * otherVec)) # element-wise multiplicaation
    print("{}.dot({}) = {} ".format(vec, otherVec, vec.dot(otherVec))) # 两个向量点乘 -> 标量

    print("np.linalg.norm({}) = {} ".format(vec, np.linalg.norm(vec)))  # 向量的模
    # 向量的单位向量
    unitVec = vec/np.linalg.norm(vec)
    print("{} unit vector = {} ".format(vec, unitVec))
    print("{} unit vector 的模 =  {} ".format(unitVec, np.linalg.norm(vec/np.linalg.norm(vec))))