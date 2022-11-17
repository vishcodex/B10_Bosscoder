class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        print("a : b :", a, b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
                print("carry 1:", carry)
            if b:
                carry += int(b.pop())
                print("carry 2:", carry)

            result += str(carry %2)
            print("result :", result)
            carry //= 2
            print("carry 3 :", carry)
        return result[::-1]


c = Solution()

print(c.addBinary(a = "11", b = "1"))