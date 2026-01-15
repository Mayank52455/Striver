from collection import Counter 
class Solution:
  def sort_character(self, s):
    freq = Counter(s)
    sorted_char = sorted(freq.items(), key = lambda x: x[1], reverse = True)
    result = ' '.join(i*j for i, j in sorted_chars)
    return result
  
  
