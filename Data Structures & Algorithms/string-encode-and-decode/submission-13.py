class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)
        
        while i < n:
            j = s.find('#', i)
            length = int(s[i:j])
            i = j + 1
            res.append(s[i : i + length])
            i += length
            
        return res