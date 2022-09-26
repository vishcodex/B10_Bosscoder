

def hammingWeight(n: int) -> int:
    # Solution 1
    # return bin(n).count('1')

    # Solution 2

    # count=0
    # while n>0:
    #     n=n&(n-1)
    #     count+=1
    # return count

    # Solution 3

    # count = 0
    # while n != 0:
    #     if n & 1:
    #         count += 1
    #         n = n >> 1
    # return count

    count = 0
    for i in range(0, 33):
        if n & 1<<i:
            count +=1
    return count




print(hammingWeight(int('00000000000000000000000000001011')))