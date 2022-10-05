import re

WORD_TO_SEARCH_FOR = ['chromecast', "apple tv", "fire tv stick"]

def get_word_count(review):
  # give the number of words in the review
  output = re.split("\s|(?<!\d)[.?!](?!\d)", review)
  if '' in output: output.remove('')
  return len(output)

def get_mentions(review):
  for word in WORD_TO_SEARCH_FOR:
    if re.search(word, review): return 1
  return 0

