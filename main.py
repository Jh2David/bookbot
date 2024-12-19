def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    word_count = count_words(text)
    char_count = get_count_characters(text)
    char_dict = get_count_characters(text)
    char_sorted_list = char_dict_sorted_list(char_dict)

    # Report
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document.\n")
        
    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The {item['char']} character was found {item["num"]} times")
    
    print("--- End report ---")

def sort_on(d):
    return d["num"]

def char_dict_sorted_list(num_char_dict):
    sorted_list = []
    for ch in num_char_dict:
        sorted_list.append({"char": ch, "num": num_char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_words(text):
    words = text.split()
    return len(words)

def get_count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
        

if __name__ == "__main__":
    main()