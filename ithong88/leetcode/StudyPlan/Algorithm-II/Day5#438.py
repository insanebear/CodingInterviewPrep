# # Ver.1
# import itertools
#
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         answer = []
#         if len(p) > len(s):
#             return answer
#         alphabet = 'abcdefghijklmnopqrstuvwxyz'
#         count_p = {t: p.count(t) for t in alphabet}
#
#         for i in range(len(s) - len(p) + 1):
#             exist = True
#             sub_s = s[i:(i + len(p))]
#             for k in count_p:
#                 if sub_s.count(k) != count_p[k]:
#                     exist = False
#                     break
#             if exist:
#                 answer.append(i)
#
#         return answer


# Ver.2
import itertools

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        if len(p) > len(s):
            return answer
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        count_p = {t: p.count(t) for t in alphabet}

        sub_s = s[0:len(p)]
        count_s = {t: sub_s.count(t) for t in alphabet}

        for i in range(len(s) - len(p) + 1):
            exist = True
            if i > 0:
                prev = s[i - 1]
                cur = s[i + len(p) - 1]
                count_s[prev] = count_s[prev] - 1
                count_s[cur] = count_s[cur] + 1

            for k in count_p:
                if count_s[k] != count_p[k]:
                    exist = False
                    break

            if exist:
                answer.append(i)

        return answer