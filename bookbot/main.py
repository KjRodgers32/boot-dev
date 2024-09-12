from collections import defaultdict

def frankenstein_stats(map):
    with open("frankenstein.txt", "r") as f:
        frankenstein = f.read()
        words = frankenstein.split()
        for word in words:
            lowered_word = word.lower()
            for letter in lowered_word:
                map[letter] += 1

    return len(words), map


def main():
    words, word_map = frankenstein_stats(defaultdict(int))

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")

    for key, value in sorted(word_map.items(), key=lambda item: item[1], reverse=True):
        print(f"The '{key}' character was found {value} times")
 
    print("--- End Report ---")


if __name__ == "__main__":
    main()
 
