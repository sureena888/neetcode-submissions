class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += f"{len(word)}#{word}"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        original_list = []
        count = ""
        i = 0
        while i < len(s):
            if s[i] != "#":
                count += s[i]
                i+=1
            else:
                original_list.append(s[i+1:i+int(count)+1])
                i+= int(count) + 1
                count = ""
        return original_list

