class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        content = ""
        for string in strs: 
            content += string
            res += str(len(string)) + ","
        res += "#" + content

        return res
    def decode(self, s: str) -> List[str]:
        res = []
        sizes = [int(x) for x in s.split("#")[0].split(",")[:-1]]
        content = s[s.find("#")+1:]
        print(content)
        print(sizes)
        curr = ""
        i = 0
        for size in sizes: 
            for q in range(size): 
                curr += content[i]
                i += 1
            res.append(curr)
            print(res)
            curr = ""
        return res