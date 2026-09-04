class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """

        if not nums:
            return None

        # Find the middle element
        mid = len(nums) // 2

        # Create root node
        root = TreeNode(nums[mid])

        # Recursively build left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root