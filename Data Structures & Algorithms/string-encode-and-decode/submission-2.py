class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for element in strs:
            res = res + element + "\n"
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        word = ""
        for ch in s:
            if ch == "\n":
                res.append(word)
                word = ""
                continue
            word = word + ch
        return res