"""
Problem Description:
Given a decimal number m. Convert it in binary string and apply n iterations, in each iteration 0 becomes 01
and 1 becomes 10. Find kth character in the string after nth iteration.

Input:
The first line consists of an integer T i.e number of test cases. The first and only line of each test case consists
of three integers m,k,n.

Output:
Print the required output.

Constraints:
1<=T<=100
1<=m<=50
1<=n<=10
0<=k<=|Length of final string|

Example:
Input:
2
5 5 3
11 6 4

Output:
1
1
"""

import math
T = int(input().strip())
while (T>0):
    T -= 1
    m, k, n = map(int, input().strip().split())
    str = bin(m).split('b')[1]
    digit = int(k/math.pow(2,n))
    remain = int(k - math.pow(2,n)*digit)
    str = str[digit]
    for j in range(n):
        str1 = ''
        for i in range(len(str)):
            if str[i] == '0':
                str1 = str1 + '01'
            else:
                str1 = str1 + '10'
        str = str1
    print(str[remain])