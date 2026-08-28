class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        shortest = min(strs, key=len)

        for i in range(len(shortest)):
            current_char = shortest[i]
            for word in strs:
                if word[i] != current_char:
                    return shortest[:i]

        return shortest

if __name__ == "__main__":
    n = int(input("Enter number of words: "))
    words = []
    for i in range(n):
        word = input(f"Enter word {i + 1}: ")
        words.append(word)

    sol = Solution()
    result = sol.longestCommonPrefix(words)

    if result:
        print("Longest Common Prefix:", result)
    else:
        print("No common prefix found")