class Solution(object):
    MOD = 10**9 + 7

    def countGoodNumbers(self, n):
        def power(base, exp, mod):
            res = 1
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % mod
                base = (base * base) % mod
                exp //= 2
            return res

        even_count = (n + 1) // 2
        odd_count = n // 2

        total_good = (power(5, even_count, self.MOD) *
                      power(4, odd_count, self.MOD)) % self.MOD

        return total_good
