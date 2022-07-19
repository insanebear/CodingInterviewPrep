class Solution:
    def decodeString(self, s: str) -> str:
        decoded = ''
        num = ''
        lowercases = 'abcdefghijklmnopqrstuvwxyz'
        numbers = '0123456789'
        i = 0
        
        while i < len(s):
            if s[i] in lowercases:
                decoded += s[i]
                i += 1
            elif s[i] in numbers:
                num += s[i]
                i += 1
            else:
                repeat = ''
                depth = 1
                i += 1
                
                while depth != 0:
                    if s[i] == '[':
                        depth += 1
                    elif s[i] == ']':
                        depth -= 1
                    repeat += s[i]
                    i += 1
                decoded += self.decodeString(repeat[:-1]) * int(num)
                num = ''
        return decoded