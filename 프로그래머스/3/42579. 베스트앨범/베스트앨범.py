from collections import defaultdict
import heapq
def solution(genres, plays):
    answer = []
    genre_play = defaultdict(int)
    genre_order = defaultdict(list)
    for genre,play in zip(genres,plays):
        genre_play[genre] += play       
    sorted_genre = list(genre_play.items())
    sorted_genre.sort(key = lambda x: -x[1])
    print(sorted_genre)
    
    for i,(genre,play) in enumerate(zip(genres,plays)):
        heapq.heappush(genre_order[genre],(-play,i))
    
    for genre, play in sorted_genre:
        for _ in range(2):
            if genre_order[genre]:
                play,i = heapq.heappop(genre_order[genre])
                answer.append(i)
                
    
    
    return answer