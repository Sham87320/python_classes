def count_words_in_file(filename):
  """Counts the number of words in a given file.

  Args:
    filename: The name of the file to read.

  Returns:
    The number of words in the file.
  """

  with open(filename, 'r') as file:
    content = file.read()
    words = content.split()
    word_count = len(words)
    return word_count

# Example usage:
filename = "test_text.txt"
word_count = count_words_in_file(filename)
print("Number of words in the file:", word_count)