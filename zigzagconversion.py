class Solution:
    def convert(self, s, numRows):
        """
        Description:
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
        (you may want to display this pattern in a fixed font for better legibility)
        P   A   H   N
        A P L S I I G
        Y   I   R
        And then read line by line: "PAHNAPLSIIGYIR"
        Write the code that will take a string and make this conversion given a number of rows:

        string convert(string text, int nRows);
        convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
        """

        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l = []
        res = ''
        for i in range(numRows):
            l.append(i)
            l[i] = []

        row = 0
        direction = 1
        for i in s:
            l[row].append(i)
            if (row + direction == numRows or row + direction < 0):
                direction = 0 - direction
            row += direction

        for i in range(numRows):
            for j in (l[i]):
                res = res + j

        return res


s = Solution()
print(s.convert("PAYPALISHIRING", 3))