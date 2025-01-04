class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        count_s1 = defaultdict(int)
        for char in s1:
            count_s1[char] += 1
        count_window = defaultdict(int)

        for r in range(len(s2)):
            # Skip characters not in s1
            if s2[r] not in count_s1:
                count_window.clear()
                l = r + 1
                continue

            # Add the current character to the window
            count_window[s2[r]] += 1

            # Shrink the window if it exceeds the size of s1 or becomes invalid
            if r - l + 1 > len(s1) or count_window[s2[r]] > count_s1[s2[r]]:
                count_window[s2[l]] -= 1
                if count_window[s2[l]] == 0:
                    del count_window[s2[l]]
                l += 1

            # Check if the current window matches count_s1
            if r - l + 1 == len(s1) and count_window == count_s1:
                return True

        return False