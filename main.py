def main():
    path_to_book = "books/frankenstein.txt"
    # text = get_book_text(path_to_book)
    # words = get_num_words(text)
    # char_dict = get_char_count(text)
    # create_report(char_dict)
    report = create_report(path_to_book)
    print(report)

def get_book_text(path):
    with open(path) as file:
        return file.read()

def get_num_words(text):
    words = text.split()
    return len(words)
            
def get_char_count(text):
    text = text.lower()
    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    char_dict = {key: 0 for key in keys}
    for chars in text:
        if(chars in keys):
            char_dict[chars] = char_dict[chars] + 1
    return char_dict

def get_char_info(char_dict):
    list_of_dicts = [{"char" : key, "num" : value} for key, value in char_dict.items()]
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def create_report(path):
    text = get_book_text(path)
    words = get_num_words(text)
    char_dict = get_char_count(text)
    list_of_dicts = get_char_info(char_dict)
    ret_string = f"--- Begin report of {path} ---\n{words} words found in the document\n\n"
    for summary in list_of_dicts:
        ret_string += f"The '{summary['char']}' character was found {summary['num']} times\n"
    return ret_string + "--- End report ---"

def sort_on(dict):
    return dict["num"]

main()
