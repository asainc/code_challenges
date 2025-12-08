import sys
import re
from collections import Counter

text = sys.stdin.read()

tokens = re.findall(r"[A-Za-z']+|[^A-Za-z']+", text)
words = [t.lower() for t in tokens if re.match(r"[A-Za-z']+$", t)]


MAX_DICT = 3000

word_freq = Counter(words)

bigrams = Counter()
for i in range(len(words) - 1):
    bigrams[(words[i], words[i+1])] += 1

top_words = [w for w, _ in word_freq.most_common(MAX_DICT)]
top_bigrams = [(' '.join(b), freq) for b, freq in bigrams.most_common(MAX_DICT)]

combined = top_words + [b for b, _ in top_bigrams]
combined = combined[:MAX_DICT]

dictionary = combined

encoding_map = {entry: idx for idx, entry in enumerate(dictionary)}

compressed = []
i = 0
N = len(tokens)

while i < N:
    tok = tokens[i]
    if re.match(r"[A-Za-z']+$", tok):
        w = tok.lower()

        if i + 2 <= N and re.match(r"[A-Za-z']+$", tokens[i+1]):
            big = w + " " + tokens[i+1].lower()
            if big in encoding_map:
                compressed.append(str(encoding_map[big]))
                i += 2
                continue

        if w in encoding_map:
            compressed.append(str(encoding_map[w]))
        else:
            compressed.append(tok)
    else:
        compressed.append(tok)

    i += 1

compressed_text = "".join(compressed)

print(len(dictionary))
for idx, entry in enumerate(dictionary):
    print(f"{idx} {entry}")
print("#####")
print(compressed_text)