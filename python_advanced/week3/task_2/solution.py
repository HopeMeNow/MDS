words = input().split()
scores = map(float, input().split())

words_scores_map = zip(scores, words)
words_scores_map = filter(
    lambda pair: pair[0] > 0.5, words_scores_map
)
sorted_map = sorted(words_scores_map, reverse=True)
result = list(zip(*sorted_map))[1]
print(*result, sep='\n')
