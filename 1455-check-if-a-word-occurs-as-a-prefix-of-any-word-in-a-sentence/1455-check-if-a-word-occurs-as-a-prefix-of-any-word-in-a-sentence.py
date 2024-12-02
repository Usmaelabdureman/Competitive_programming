class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # List to store the words from the sentence
        words_list = []
        # String to build the current word
        current_word = ""

        # Iterate through each character in the sentence
        for character in sentence:
            if character != " ":
                # Append the character to the current word
                current_word += character
            else:
                # If we encounter a space, add the current word to the list
                if current_word:
                    words_list.append(current_word)
                    current_word = ""  # Reset the string

        # Add the last word if the sentence doesn't end with a space
        if current_word:
            words_list.append(current_word)

        # Iterate through the list of words to find the prefix match
        for word_index, word in enumerate(words_list):
            if len(word) >= len(searchWord):
                is_match = True
                for char_index in range(len(searchWord)):
                    if word[char_index] != searchWord[char_index]:
                        is_match = False
                        break
                if is_match:
                    return word_index + 1  # Return 1-based index

        return -1  # Return -1 if no match is found