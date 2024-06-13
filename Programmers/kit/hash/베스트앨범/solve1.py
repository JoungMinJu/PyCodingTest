from collections import defaultdict

def solution(genres, plays) :
    genre_play_count = defaultdict(int)
    genre_songs = defaultdict(list)

    for i in range(len(genres)) :
        genre = genres[i]
        play_count = plays[i]
        genre_play_count[genre] += play_count
        genre_songs[genre].append((i, play_count))
    sorted_genres = sorted(genre_play_count.keys(), key=lambda x: genre_play_count[x], reverse=True)

    answer = []
    for genre in sorted_genres:
        songs = genre_songs[genre]
        sorted_songs = sorted(songs, key=lambda x: (-x[1], x[0]))
        answer.extend([song[0] for song in sorted_songs[:2]])

    return answer