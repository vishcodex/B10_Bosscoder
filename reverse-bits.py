


def reverseBits(n: int) -> int:

    # Solution 1
    res = 0
    for _ in range(0,32) :
        res <<= 1
        if n & 1 :
            res += 1
        n >>= 1
    return res

    # Solution 1


    return(int(str('{:032b}'.format(n))[::-1],2))


n = int('00000010100101000001111010011100')

r = reverseBits(n)
print(r)