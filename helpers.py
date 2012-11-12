from pattern.en.wordnet import sentiment

sentiment.load()

def sentiment_score(s):
    """Caculate total sentiment score of a sentence"""
    #docs here: http://www.clips.ua.ac.be/pages/pattern-en#sentiment
    v = 0
    for w in s.split(" "):
        w = w.strip(",.!?)(#:;\"\'").lower()
        if w in sentiment:
            v = v + sentiment[w][0] - sentiment[w][1]
    return v

