from pyvi import ViTokenizer, ViPosTagger
import string
import os
import requests

def create_tokens(doc) -> list:
    """
    Tạo danh sách các token từ một văn bản cho trước.
    
    :param doc: Văn bản đầu vào
    """

    doc = ViTokenizer.tokenize(doc) 
    doc = doc.lower() 
    tokens = doc.split()
    table = str.maketrans('', '', string.punctuation.replace("_", "")) 
    tokens = [w.translate(table) for w in tokens]
    tokens = [word for word in tokens if word]
    with open('datasets_func/stopwords.txt', 'r', encoding='utf-8') as file:
        stopwords = [line.strip() for line in file.readlines()]
    tokens = [word for word in tokens if word not in stopwords and not word.isdigit()]
    tokens = [word for word in tokens if len(word) > 2]
    return tokens

def remove_tokens_from_file(file_path, tokens) -> list:

    """
    Xóa bỏ các tokens đã tồn tại trong file cho trước.

    :param file_path: Đường dẫn đến file chứa các tokens
    :param tokens: Danh sách các tokens

    """
    if not os.path.exists(file_path):
        return tokens
    with open(file_path, 'r', encoding='utf-8') as file:
        existing_tokens = set(line.strip() for line in file.readlines())
    return [token for token in tokens if token not in existing_tokens]

def write_tokens_by_category(tokens) -> None:
    """
    Ghi các tokens vào các file tương ứng với loại từ. Thêm các từ vào trong file nếu chưa tồn tại.
    - Thêm các từ vào file 'base_data/noun.txt' nếu chúng là danh từ.
    - Thêm các từ vào file 'base_data/adjective.txt' nếu chúng là tính từ.
    - Thêm các từ vào file 'base_data/verb.txt' nếu chúng là động từ.
    
    :param tokens: Danh sách các tokens.
    """
    tokens = remove_tokens_from_file('base_data/region.txt', tokens)
    pos_tags = ViPosTagger.postagging(" ".join(tokens))
    categories = {'N': 'base_data/noun.txt', 'A': 'base_data/adjective.txt', 'V': 'base_data/verb.txt'}
    categorized_tokens = {key: [] for key in categories.keys()}

    # Remove adjectives from noun tokens
    noun_tokens = categorized_tokens['N']
    adjective_tokens = categorized_tokens['A']
    noun_tokens = [token for token in noun_tokens if token not in adjective_tokens]
    categorized_tokens['N'] = noun_tokens

    for token, tag in zip(pos_tags[0], pos_tags[1]):
        if tag in categorized_tokens:
            categorized_tokens[tag].append(token)

    for category, tokens in categorized_tokens.items():
        file_path = categories[category]
        existing_tokens = read_existing_tokens(file_path)
        new_tokens = existing_tokens.union(set(tokens))
        write_tokens_to_file(file_path, new_tokens)

def read_existing_tokens(file_path) -> set:

    """
    Đọc các tokens đã tồn tại từ file.

    :param file_path: Đường dẫn đến file chứa các tokens.
    
    """

    if not os.path.exists(file_path):
        return set()
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(line.strip() for line in file.readlines())

def write_tokens_to_file(file_path, tokens) -> None:

    """
    Ghi các tokens vào file.

    :param file_path: Đường dẫn đến file cần ghi.
    """
    
    with open(file_path, 'w', encoding='utf-8') as file:
        existing_tokens = read_existing_tokens(file_path)
        new_tokens = existing_tokens.union(set(tokens))
        for token in new_tokens:
            file.write(token + '\n')

def count_tokens_in_file(file_path, tokens) -> int:

    """
    Đếm số lần xuất hiện của các tokens trong file.

    :param file_path: Đường dẫn đến file chứa các tokens.
    
    """

    if not os.path.exists(file_path):
        return 0
    with open(file_path, 'r', encoding='utf-8') as file:
        file_tokens = set(line.strip() for line in file.readlines())
    return sum(1 for token in tokens if token in file_tokens)


def get_tokens_from_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None

    return set(response.text.splitlines())

def count_tokens_in_url(url, tokens):
    keywords = get_tokens_from_url(url)

    count = 0
    for token in tokens:
        if token in keywords:
            count += 1

    return count