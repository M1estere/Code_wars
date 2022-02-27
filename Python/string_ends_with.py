def solution(word, ending):
    word_length = len(word)
    ending_length = len(ending)

    if (ending_length > word_length):
        return False

    free_chars = word_length - ending_length

    if (word[free_chars::] == ending):
        return True

    return False