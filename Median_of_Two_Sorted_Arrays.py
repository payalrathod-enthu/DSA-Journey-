class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # Make sure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        # Binary search boundaries
        lo, hi = 0, m

        while lo <= hi:

            # Partition nums1
            i = (lo + hi) // 2

            # Partition nums2
            j = (m + n + 1) // 2 - i

            # Elements around the partitions
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')

            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            # Correct partition found
            if left1 <= right2 and left2 <= right1:

                # Odd total number of elements
                if (m + n) % 2 == 1:
                    return max(left1, left2)

                # Even total number of elements
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0

            # We have taken too many elements from nums1
            elif left1 > right2:
                hi = i - 1

            # We need to take more elements from nums1
            else:
                lo = i + 1