from playLA.Vector import Vector

if __name__ == "__main__":

    vec = Vector([5,2])
    otherVec = Vector([4, 3])
    zero2 = Vector.zero(2)

    print(vec)
    print("向量长度{} = {} ".format(vec, len(vec)))
    print("vec[0]={}, vec[1]={}".format(vec[0], vec[1]))

    print("向量运算->")
    print("{} + {} = {} ".format(vec, otherVec, vec+otherVec))
    print("{} - {} = {} ".format(vec, otherVec, vec - otherVec))
    print("{} * {} = {} ".format(vec, 3, vec *3))
    print("{} * {} = {} ".format(3, vec, 3*vec))

    print("+{} = {} ".format(vec, +vec))
    print("-{} = {} ".format(vec, -vec))

    print("零向量->")

    print("零向量 n维 = {} ".format(zero2))
    print("{} + {} = {} ".format(vec, zero2, vec + zero2))

    print("向量的模->")
    print("norm({}) = {} ".format(vec, vec.norm()))
    print("norm({}) = {} ".format(otherVec, otherVec.norm()))
    print("norm({}) = {} ".format(zero2, zero2.norm()))

    print("向量的单位向量->")
    print("normalize({}) = {} ".format(vec, vec.normalize()))
    print("单位向量的模为1，只表示方向 {} ".format(vec.normalize().norm()))

    try:
        print("normalize({}) = {} ".format(zero2, zero2.normalize()))
    except ZeroDivisionError:
        print("Can't normalize zero vector {}.".format(zero2))

    print("{} * {} = {} ".format(vec, otherVec, vec.dot(otherVec)))