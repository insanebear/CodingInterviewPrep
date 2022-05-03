from itertools import combinations

class Solution:
    def maxArea(self, height: List[int]) -> int:
        fp = 0
        sp = 1
        max_n =0
        # for com in list(combinations(enumerate(height),2)):
        #     w = com[1][0]-com[0][0]
        #     h = com[1][1] if (com[0][1]>com[1][1]) else com[0][1]
        #     temp = w*h
        #     max = temp if temp>max else max
        
        # for i,h in enumerate(height):
        #     sp = i+1
        #     while sp < len(height):
        #         w = sp-i
        #         hh = h if h<height[sp] else height[sp]
        #         temp = w*hh
        #         max_n = temp if temp>max_n else max_n
        #         sp = sp+1
        
#         mw = 0
#         mh = 0
#         max_loc =0
#         for i,h in enumerate(height):
#             if h >= height[max_loc]:
#                 max_loc = i
        
#         for i,h in enumerate(height):
#             if max_loc == 0:
#                 sp = i+1
#             elif max_loc >=i:
#                 sp = max_loc
#             else:
#                 break
#             if h <= mh:
#                 continue
#             else:
#                 mh = h
#             c = max_n/h
#             while sp < len(height):
#                 if sp-i > c:
#                     w = sp-i
#                     hh = h if h<height[sp] else height[sp]
#                     temp = w*hh
#                     max_n = temp if temp>max_n else max_n
#                 sp = sp+1
            # print(i, max_n)
        mw = 0
        mh = 0
        max_loc =0
        ll = len(height)
        for i,h in enumerate(height):
            if h >= height[max_loc]:
                max_loc = i

        for i,h in enumerate(height):
            if max_loc == 0:
                sp = i+1
            elif max_loc >=i:
                sp = max_loc
            else:
                break
            if h <= mh:
                continue
            else:
                mh = h
            c = max_n/h
            k = ll
            while sp < ll:
                if sp-i > c:
                    w = sp-i
                    hh = h if h<height[sp] else height[sp]
                    temp = w*hh
                    if temp>max_n:
                        max_n = temp
                        k = sp+1
                sp = sp+1
            ll = k
        return max_n