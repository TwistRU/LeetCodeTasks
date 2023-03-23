class Solution:
    def romanToInt(self, s: str) -> int:
        inputRoman = s
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        ans = inputRoman.count("IV") * 4 + inputRoman.count("IX") * 9 + inputRoman.count("XL") * 40 + inputRoman.count("XC") * 90 + inputRoman.count("CD") * 400 + inputRoman.count("CM") * 900
        for number in ("IV", "IX", "XL", "XC", "CD", "CM"):
            inputRoman = inputRoman.replace(number, "")
        return ans + sum(map(lambda x: d[x], inputRoman))


s = Solution()
assert s.romanToInt("MCMXCIV") == 1994
