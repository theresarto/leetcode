class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = defaultdict(int)  # character: count
        l = 0
        longest = 0
        max_freq = 0
        # r keeps expanding to the right
        for r in range(len(s)):
            # for each character s[r], the count gets updated
            hash_map[s[r]] += 1

            # get the max frequency
            max_freq = max(max_freq, hash_map[s[r]])

            while (r-l+1) - max_freq > k:
                hash_map[s[l]] -= 1
                l += 1
            # check the window size. For example if r = 0, l = 0, window is 1
            longest = max(longest, r - l + 1)

        return longest