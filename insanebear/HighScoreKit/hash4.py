def solution(genres, plays):
    answer = []
    
    # calculate how many times each genre was played (#1)
    genre_played = {}
    for g, cnt in zip(genres, plays): # O(n)
        if g not in genre_played:
            genre_played[g] = cnt
        else:
            genre_played[g] += cnt
    
    # sort in descending order by play counts
    # sorted: O(nlogn), reassigning for-loop: O(n) - max: O(nlogn)
    genre_played = {k: v for k, v in sorted(genre_played.items(), key = lambda x: x[1], reverse = True)}
    
    # play_dict = { genre : [play_count, id] }
    # play_dict[genre] list is sorted in index (ascending) order.
    play_dict = {}
    for i, (g, cnt) in enumerate(zip(genres, plays)): # O(n)
        if g not in play_dict:
            play_dict[g] = [(cnt, i)]
        else:
            play_dict[g].append((cnt, i))
    
    # sort the inside of play_dict[genre] in descending order by play count (#2)
    # maintain index order when comparing the same play counts (#3)
    # sorted: O(nlogn), reassigning for-loop: O(n) - max: O(nlogn)
    for genre in play_dict.keys():
        play_dict[genre] = sorted(play_dict[genre], key = lambda x: x[0], reverse = True)
    
    # select answers
    for key in genre_played.keys(): # O(n)
        values = play_dict[key]
        if len(values) > 1:
            answer.append(values[0][1])
            answer.append(values[1][1])
        else:
            answer.append(values[0][1])

    return answer