"""
<https://programmers.co.kr/learn/courses/30/lessons/42579>
"""


def solution(genres, plays):
    genre_plays = {}
    genre_dict = {}
    for index, (gen, play) in enumerate(zip(genres, plays)):
        if gen in genre_plays:
            genre_plays[gen] += play
        else:
            genre_plays[gen] = play
            genre_dict[gen] = []

        genre_dict[gen].append([-play, index])

    best_genres = sorted(genre_plays.items(), key=lambda x: x[1], reverse=True)

    for items in genre_dict.values():
        items.sort()

    answer = []
    for genre in best_genres:
        items = genre_dict[genre[0]]
        for i in range(min(2, len(items))):
            answer.append(items[i][1])

    return answer
