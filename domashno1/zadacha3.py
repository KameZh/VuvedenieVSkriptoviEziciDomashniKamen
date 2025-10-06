words = ["level", "python", "radar", "java", "civic", "kotlin", "refer"]
palindromes = []
for word in words:
	reversed_word = ""
	for ch in word:
		reversed_word = ch + reversed_word

	if word == reversed_word:
		palindromes.append(word)

print(palindromes)