import pickle
import os
from itertools import islice
import re
import requests
from bs4 import BeautifulSoup
import string
from string import punctuation
import sys


def store_data(dict):
    dbfile = open('pickleStore', 'wb')
    pickle.dump(dict, dbfile)
    dbfile.close()

def load_data():
    try:
        infile = open('pickleStore', 'rb')
        new_dict = pickle.load(infile)
        infile.close()
        return new_dict
    except:
        return {}

def update_word_counter(word_list, input_dict):
    word_list = normalize_all_types(word_list)
    for line in word_list:
        for word in line:
            if word in input_dict:
                input_dict[word] += 1
            else:
                input_dict[word] = 1
    return input_dict

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta']:
        return False
    return True


def normalize_all_types(input):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  
        r'localhost|'  
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' 
        r'(?::\d+)?' 
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if re.match(regex, input):
        r = requests.get(input, allow_redirects=False)
        soup = BeautifulSoup(r.content, 'html.parser')
        words = soup.findAll(text=True)
        visible_texts = filter(tag_visible, words)
        stripped = [x.rstrip(punctuation).lower() for y in visible_texts for x in y.split()]
        yield stripped
    if os.path.isfile(input):
        for f in open(input):
            table = str.maketrans('', '', string.punctuation)
            yield str(f).translate(table).lower().split()
    if not os.path.isfile(input) and not re.match(regex, input):
        words = input.split()
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in words]
        yield  stripped

def run_program(text):
    dic = load_data()
    new_dic = update_word_counter(text, dic)
    store_data(new_dic)
    return new_dic


def start_over():
    os.remove('pickleStore')

def slice_huge_file(input_file, num_lines):
    cnt = 0
    with open(input_file) as f:
        while True:
            next_n_lines = list(islice(f, num_lines))
            cnt += 1
            if not next_n_lines:
                break
            with open('sub_huge_{}.txt'.format(cnt), 'w') as out:
                out.writelines(next_n_lines)

def main(input, word):
    if os.path.isfile(input):
        slice_huge_file(input, 50000)
        sub_files = [os.path.join('.', f) for f in os.listdir('.') if f.startswith('sub_huge')]
        for file in sub_files:
            run_program(file)
    else:
        run_program(input)
    data = load_data()
    try:
        if word is not '':
            print(data[word])
    except:
        print("That word doesn't exist in our database! Try another word.")


if __name__ == '__main__':
    args = sys.argv[1:]
    word_list = args[0]
    search_word = args[1]
    main(word_list, search_word)








