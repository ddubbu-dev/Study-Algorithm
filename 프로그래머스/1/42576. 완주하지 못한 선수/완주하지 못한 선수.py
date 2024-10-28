from collections import Counter

def solution(participant, completion):
    counts = Counter(participant)
    names = counts.keys()
    
    completion_counts = Counter(completion)
    
    for name in names:
        if counts[name] != completion_counts.get(name):
            return name