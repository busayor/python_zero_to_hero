def multiple_letter_count(phrase):
  return {letter: phrase.count(letter) for letter in phrase}


phrase = input("enter phrase here -->")
print(multiple_letter_count(phrase))


