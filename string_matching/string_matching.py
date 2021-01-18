def find(pattern, text):
	for i in range(0, len(text) - len(pattern) + 1):
		for j in range(0, len(pattern)):
			if pattern[j] != text[i]:
				break
			i += 1
		else:
			return i - len(pattern)

	return -1
