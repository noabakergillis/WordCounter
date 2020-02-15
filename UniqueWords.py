import WordCounter
import sys

def main():
    args = sys.argv[1:]
    WordCounter.main(args[0], '')
    print(len(WordCounter.load_data()))

if __name__ == '__main__':
    main()
