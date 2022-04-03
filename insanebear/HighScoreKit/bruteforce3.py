def solution(brown, yellow):
    answer = []
    wl = [] # width list
    hl = [] # height list
    
    # make yello carpet first
    for d in range(1, yellow+1):
        if yellow % d == 0: # divider which makes no remainder
            q = yellow // d
            if d >= q:
                w = d # greater value becomes width
                h = q
                if w not in wl:
                    wl.append(w)
                    hl.append(h)
    
    # calculate brown using yellow
    for y in zip(wl, hl):
        if (y[0]+2) * (y[1]+2) - yellow == brown:
            answer.append(y[0]+2)
            answer.append(y[1]+2)
            break
    
    return answer