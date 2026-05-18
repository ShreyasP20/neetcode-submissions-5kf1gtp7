class Solution:
    def decodeString(self, s: str) -> str:
        decodestck = []
        chars = ""

        for i in s:

            # only push letters, digits, and '['
            if i.isalpha() or i.isdigit() or i == '[':
                decodestck.append(i)

            if i == ']':

                chars = ""

                while decodestck and decodestck[-1] != '[':
                    chars = decodestck.pop() + chars

                decodestck.pop()

                num = ""
                while decodestck and decodestck[-1].isdigit():
                    num = decodestck.pop() + num

                chars = int(num) * chars

                decodestck.append(chars)

        return "".join(decodestck)