class Solution:
    def nextClosestTime(self, time):
        """
        Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

        You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

        Example 1:

        Input: "19:34"
        Output: "19:39"
        Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
        Example 2:

        Input: "23:59"
        Output: "22:22"
        Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
        
        :type time: str
        :rtype: str
        """

        nexttime = time
        timeInMin = 0
        list = []
        j = 0
        for i in time:
            if i != ':':
                list.append(i)

        mintime = (int(list[0])*10+int(list[1]))*60 + int(list[2])*10 + int(list[3])
        resulttime = 23*60+59+24*60
        for i in range(4):
            for a1 in list:
                for a2 in list:
                    for a3 in list:
                        for a4 in list:
                            newtime = (int(a1)*10+int(a2))*60 + int(a3)*10 + int(a4)
                            str = a1+a2+':'+a3+a4
                            if str != time:
                                if 0 <= int(a1)*10+int(a2) < 24 and 0 <= int(a3)*10 + int(a4) < 60:
                                    if newtime < mintime:
                                        newtime = newtime + 24*60
                                    if resulttime > newtime > mintime:
                                        resulttime = newtime
                                        nexttime = a1+a2+':'+a3+a4

        return nexttime

sol = Solution()
print(sol.nextClosestTime("10:00"))
