def solution(phone_book):
    pb_dict = {}

    # make each number in the phone book as a key
    for number in phone_book: # O(n)
        pb_dict[number] = 1
    
    # iterate the phone book and find whether a partial number is in the dictionary key
    for number in phone_book: # O(n)
        for i in range(len(number)): # O(20) <- max length: 20
            if number[:i] in pb_dict:
                return False
        
    return True