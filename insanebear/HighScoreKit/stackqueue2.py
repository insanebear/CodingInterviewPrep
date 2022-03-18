def solution(priorities, location):
    printed = 0
    while len(priorities) > 0: # O(n)
        j = priorities.pop(0)
        
        # compare j with other priorities
        push_back = False
        for p in priorities: # O(n)
            if p > j:
                # if p is greater than j, push j to the end
                priorities.append(j)
                push_back = True
                break
        
        """
            repositioning the original location
            print if condition is satisfied 
        """
        # if location became 0 and do not have to push it back, print and stop
        if location == 0 and not push_back:
            printed += 1
            break

        # if location became 0 but have to push it back, reposition the location
        # else pull it forward
        if location == 0 and push_back:
            location += (len(priorities) - 1)
        else:
            location -= 1
        
        # something can be printed out. increase `printed`.
        if not push_back:
            printed += 1
        
        
        
    return location + printed