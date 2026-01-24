class Solution:
    def substrCount(self, s, k):

        def atMostK(s, k):
            count = 0
            start = 0
            freq = {}

            for end in range(len(s)):

                if s[end] not in freq:
                    freq[s[end]] = 0
                freq[s[end]] += 1

                while len(freq) > k:
                    freq[s[start]] -= 1
                    if freq[s[start]] == 0:
                        del freq[s[start]]
                    start += 1

                count += end - start + 1

            return count

        return atMostK(s, k) - atMostK(s, k - 1)
