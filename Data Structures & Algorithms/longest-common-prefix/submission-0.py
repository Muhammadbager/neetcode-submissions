class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(word) for word in strs)

        for i in range(min_len):
            for word in strs:
                if word[i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0][:min_len]