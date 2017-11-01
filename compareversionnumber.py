class Solution:
    def compareVersion(self, version1, version2):
        """
        Compare two version numbers version1 and version2.
        If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

        You may assume that the version strings are non-empty and contain only digits and the . character.
        The . character does not represent a decimal point and is used to separate number sequences.
        For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

        Here is an example of version numbers ordering:

        0.1 < 1.1 < 1.2 < 13.37
        """
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