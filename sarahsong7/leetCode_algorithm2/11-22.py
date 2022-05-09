class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        recur("", answer, 0, 0, n)
        return answer
    
def recur (old_list, answer, left, right,  n):
    # print(old_list)
    if right > left or right > n or left > n:
        return
    if right is left and left is n:
        answer.append(old_list)
        
    new_list = old_list[:]
    new_list=new_list+"("
    recur(new_list, answer, left+1, right, n)
    
    new_list2 = old_list[:]
    new_list2= new_list2+")"
    recur(new_list2, answer, left, right+1, n)