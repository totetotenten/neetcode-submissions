class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        length = 0
        left = 0
        seen = dict()
        for i, char in enumerate(s):
            if char not in seen:
                length += 1
            else:
                left = seen[char] + 1
                length = i - seen[char]
                del_list = []
                for seen_char in seen:
                    if seen[seen_char] < left:
                        del_list.append(seen_char)
                for del_char in del_list:
                    del seen[del_char]

            result = max(result, length)
            seen[char] = i

        return result