def word_frequencies(text: str, k: int) -> list:
    empty_dict = {}
    # Convert the text to lowercase and split it into words, remove punctuation that is not part of words
    words = text.lower().replace('.', '').replace('!', '').replace(',', '').split()
    for word in words:
        empty_dict[word] = empty_dict.get(word,0) + 1
    ans_list = list(empty_dict.items())
    ans_list.sort(key=lambda x: x[1], reverse = True)
    result = []
    for i in ans_list[:k]:
        result.append(i[0])

    return result


# Example
s = "Hello, hello! This is a test. This test is simple."
print("Input:", s)
out = word_frequencies(s, k=2)
print(out)
# print("Output (unsorted dict):", out)
# print("Output (sorted by freq desc):", sorted(out.items(), key=lambda x: -x[1]))
# Expected counts: this:2, is:2, hello:2, test:2, a:1, simple:1