class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        main1 = 0
        main2 = 0
        branch1 = 0
        branch2 = 0
        list1 = version1.split('.')
        list2 = version2.split('.')
        for i in range(max(len(list1),len(list2))):
            item1 = 0 if (i > len(list1)-1) else int(list1[i])
            item2 = 0 if (i > len(list2)-1) else int(list2[i])
            if item1 > item2:
                return 1
            if item2 > item1:
                return -1
        return 0


s = Solution()
print(s.compareVersion('10.1.1.1.2.6','10.1.1.1.2.5.111'))