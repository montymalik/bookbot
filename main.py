def main():
    f = open(
        "/home/monty/projects/boot.dev/github.com/montymalik/bookbot/books/frankenstein.txt",
        "r",
    )
    text = f.read()
    f.close()

    num_words = words(text)
    chars_dict = letter_count(text)
    chars_sorted_list = sorted(chars_dict)

    print(f"The book contains {words(text)} words")
    print()

    for item in chars_sorted_list:
        char, num = item
        if char.isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")


def words(text):
    word = text.split()
    return len(word)


def lowered(word):
    lower_text = []
    word = word.split()
    for w in word:
        lower_text.append(w.lower())
    return lower_text


def letter_count(lower_text):
    letter_freq = {}
    for i in lower_text:
        if i in letter_freq:
            letter_freq[i] += 1
        else:
            letter_freq[i] = 1
    return letter_freq


def sort_on(d):
    return d["num"]


def sorted(num_char_dict):
    sorted_list = []
    for char in num_char_dict:
        sorted_list.append({"char": char, "num": num_char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
