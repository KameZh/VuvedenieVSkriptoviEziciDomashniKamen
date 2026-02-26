def remove_even_index(words):
    for i, n in enumerate(words):
        if i % 2 == 1:
            words.remove(n)

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
remove_even_index(words)
print(words)