
def open_file():
    lines = []
    with open('fortunes.txt') as f:
        lines = f.readlines()
    return lines


def get_phrases(lines):
    count = 0
    phrase = []
    fortune_list = []

    for line in lines:
        if line != '%\n':
            phrase.append(line)
        else:
            fortune_list.append(phrase)
            phrase = []
    return fortune_list


def get_random_quote(fortune_list):
    from random import choice
    
    phrase = choice(fortune_list)

    return phrase


def print_quote(phrase):
    print('FRASE DO DIA: ')
    print('------------------')
    for quote_line in phrase:
        print(quote_line)
    print('------------------')

    return 0

if __name__ == "__main__":

    lines = open_file()
    quote = get_random_quote(get_phrases(lines))
    print_quote(quote)
