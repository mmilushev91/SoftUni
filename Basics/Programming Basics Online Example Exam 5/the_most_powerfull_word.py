vowels = ['a', 'e', 'i', 'o', 'u', 'y']

command = input()

max_word_score = float("-inf")
max_score_word = None


while command != "End of words":
  word = command
  
  word_score = 0
  start_letter = word[0]
  word_len = len(word)
  
  for char in word:
    word_score += ord(char)
  
  if start_letter.lower() in vowels:
    word_score *= word_len
  else:
    word_score = int(word_score / word_len)
  
  if word_score > max_word_score:
    max_word_score = word_score
    max_score_word = word
  
  command = input()

print(f"The most powerful word is {max_score_word} - {max_word_score}" )
