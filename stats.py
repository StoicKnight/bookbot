def count_words(text):
    return len(text.split())


def count_chars(text):
    count_dict = {}
    for c in text.lower():
        if c not in count_dict:
            count_dict[c] = 1
        else:
            count_dict[c] += 1
    return count_dict


def sort_on(items):
    return items["num"]


def sort_dict(dictionary):
    output_list = []
    for key in dictionary:
        if not key.isalpha():
            continue
        output_list.append({"char": key, "num": dictionary[key]})
    output_list.sort(reverse=True, key=sort_on)
    return output_list
