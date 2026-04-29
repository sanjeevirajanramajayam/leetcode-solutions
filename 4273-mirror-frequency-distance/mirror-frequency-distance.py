class Solution:
    def mirrorFrequency(self, s: str) -> int:
        alpha_map = {}
        number_map = {}
        for i in range(len(string.ascii_lowercase)):
            alpha_map[string.ascii_lowercase[i]] = string.ascii_lowercase[len(ascii_lowercase) - i - 1]
        for i in range(0, 10):
            number_map[str(i)] = str(9 - i)
        # print(alpha_map, number_map)
        total = 0
        seen = set()
        freqMap = {}
        for i in range(len(s)):
            freqMap[s[i]] = freqMap.get(s[i], 0) + 1
        # print(freqMap)
        for i in range(len(s)):
            if s[i] not in seen:
                freq_c = freqMap.get(s[i], 0) 
                seen.add(s[i])
                if s[i] in number_map:
                    freq_m = freqMap.get(number_map[s[i]], 0)
                    seen.add(number_map[s[i]])
                else:
                    freq_m = freqMap.get(alpha_map[s[i]], 0)
                    seen.add(alpha_map[s[i]])
                # print(s[i], freq_c, freq_m)
                total += abs(freq_c - freq_m)
        return total
            