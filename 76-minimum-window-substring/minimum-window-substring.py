class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window = {}  # {c:count}
        dict_t = {c: t.count(c) for c in t}
        have, need = 0, len(t)  # at start, don't have what we need yet
        l = 0
        resLen, res = float("inf"), [-1, -1]

        for r in range(len(s)):
            if s[r] in dict_t:
                window[s[r]] = 1 + window.get(s[r], 0)

                if window[s[r]] <= dict_t[s[r]]:
                    have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                    # print(f"{res=} {resLen= }")

                if s[l] in dict_t:
                    window[s[l]] -= 1
                    if window[s[l]] < dict_t[s[l]]:
                        have -= 1
                l += 1

        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""