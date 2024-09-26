def find_longest_word(document, longest_word=''):
    try:
        doc_list = document.split()

        if len(doc_list[0]) > len(longest_word):
            longest_word = doc_list[0]

        current_longest_word = find_longest_word(" ".join(doc_list[1:]), longest_word)
        if len(current_longest_word) > len(longest_word):
            longest_word = current_longest_word
    except IndexError:
        pass
    return longest_word