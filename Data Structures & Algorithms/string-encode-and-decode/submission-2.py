class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for i in strs:
            encode+=i+",@"
        return encode


    def decode(self, s: str) -> List[str]:
        decode = s.split(",@")
        return decode[:-1]
