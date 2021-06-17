from playLA.Vector import Vector

if __name__ == "__main__":

    vec = Vector([5,2])
    print(vec)
    print(len(vec))
    print("vec[0]={}, vec[1]={}".format(vec[0], vec[1]))

    otherVec = Vector([4,3])
    print("{} + {} = {} ".format(vec, otherVec, vec+otherVec))
    print("{} - {} = {} ".format(vec, otherVec, vec - otherVec))
    print("{} * {} = {} ".format(vec, 3, vec *3))
    print("{} * {} = {} ".format(3, vec, 3*vec))

    print("+{} = {} ".format(vec, +vec))
    print("-{} = {} ".format(vec, -vec))