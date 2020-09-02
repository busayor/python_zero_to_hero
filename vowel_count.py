def check_vowel(phrase,vowels):
  phrase = phrase.casefold()
  count = {}.fromkeys(vowels,0)

  for char in phrase:
    if char in count:
      count[char] +=1
  return count

phrase = "mEn are the best"
vowels = "aeiou"
print(check_vowel(phrase,vowels))