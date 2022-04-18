def solution(genres, plays):
    answer = []
    play_dict = {}
    genre_dict = {}
    for i in range(len(genres)):
        # Make genre-count(genre) dictionary
        play = play_dict.get(genres[i], 0)
        play += plays[i]
        play_dict[genres[i]] = play

        # Make genre-idx-count(song) dictionary
        genre = genre_dict.get(genres[i], dict())
        genre[i] = plays[i]
        # print(f'genre:{genre[i]}, number:{i}, play:{plays[i]}')
        genre_dict[genres[i]] = genre
        # hash_dict[genres[i]] = [play, temp[1]]

        # sorting
        # sorted_dict = sorted(my_dict.items(), key = lambda item: item[1], reverse = True)
        # print(sorted_dict)

    # print(play_dict)
    # print(genre_dict)

    # genre sorting
    play_dict = sorted(play_dict.items(), key=lambda item: item[1], reverse=True)
    for item in play_dict:
        # print(item)
        # song sorting
        temp_dict = genre_dict[item[0]]
        temp_dict = sorted(temp_dict.items(), key=lambda item2: item2[1], reverse=True)

        # pick 2 item from each genre
        cnt = 0
        for item2 in temp_dict:
            # print(item2)
            if cnt == 2:
                break
            answer.append(item2[0])
            cnt += 1

    return answer