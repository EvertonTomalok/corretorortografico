import jellyfish as jf
from fuzzywuzzy import fuzz
from string import punctuation
import re
import time


# You can load your dictionary here
with open('files/dic_senhora.txt', 'r') as fp:
    dicionario = set(fp.read().split('\n'))


def meu_tokenizer(string):
    """
    Just a tokenizer created using module 're'
    """
    pattern = r"\w+\S+\w+|\w+|[,.;:!?#$%&*]+"

    return re.findall(pattern, string)


def corretor(string):
    """"
    :return: A STRING if a typo wasn't found, or a LIST of TUPLES of possibilties if a typo was found
    """

    lista = set()

    if string.lower() in dicionario or string.title() in dicionario:
        return string

    else:
        for frase in dicionario:
            distance = jf.levenshtein_distance(string, frase)
            lista.add((distance, frase))

        distancia_inicial = 0
        lista_new = list()

        for distance, frase in sorted(lista):

            if distancia_inicial == 0:
                distancia_inicial = distance

            elif distance > distancia_inicial:
                break

            ratio = fuzz.ratio(string, frase)

            lista_new.append((ratio, frase))

        return sorted(lista_new, reverse=True)


def parser(doc):
    """
    Parse the initial string

    Tokenize -> correct where is necessary -> return a LIST and a STRING

    :param doc: STRING
    :return: A LIST with no typo, and a new initial_string colored where occurred a typo
    """

    ini = time.perf_counter()

    frase_correta = []

    tokens = meu_tokenizer(doc)

    for token in tokens:
        if token not in punctuation:

            worker = corretor(token)

            if isinstance(worker, list):
                # Coloring a token of red, on the initial string, where a typo was found
                doc = doc.replace(token, f'\033[1;41m{token}\033[m')

            frase_correta.append(worker)
        else:
            # It's a punctuation. It doesn't need to be parsed
            frase_correta.append(token)

    print('\n\n------------------------------------')
    print('Tempo de processamento: {:.4f} segundos'.format(time.perf_counter() - ini))
    print('\n\n')

    return frase_correta, doc


def montar_frase(lista, only_words=True):
    """
    Join the list of tuples, showing the correct words and ratio of fuzzy logic.

    A list is received, like this: ['Eu', [(95, 'amo'), (90, 'amar')], 'tudo', 'isso', '!'] # 4 string and 1 list of 2 tuples

    If the current element of the list is a String, just append on new_frase. If it's a list, we will remove the words
    from tuple and join all correct words, and transform it in a string.

    The list after processing, will be -> ['Eu', '(amo|amar)', 'tudo', 'isso', '!'] if only_words is True
    or ['Eu', '(95|amo, 90|amar)', 'tudo', 'isso', '!'] if only_words is False

    :param lista: LIST
    :param only_words: Boolean
    :return: A list with tokens with the correct word and the ratio of fuzzy logic (if only_words is True)
    """

    new_frase = list()

    for elemento in lista:

        # It's a list, let's process!
        if isinstance(elemento, list):

            join_tupla = list()

            if only_words:

                for tupla in elemento:

                    join_tupla.append(f'{tupla[1]}')

                    # Get until 5 correct words
                    if len(join_tupla) > 4:
                        break

                new_frase.append('({})'.format('|'.join(join_tupla)))

            else:

                # Use only_words=False to see the ratio of each possibility on the final print

                for tupla in elemento:

                    join_tupla.append(f'{tupla[0]}|{tupla[1]}')

                    # Get until 5 correct words
                    if len(join_tupla) > 4:
                        break

                new_frase.append('({})'.format(', '.join(join_tupla)))

            # Refreshing memory
            del join_tupla

        # It's a string, just append
        else:
            new_frase.append(elemento)

    return new_frase


def important_replaces(string):

    string = re.sub(r'\s?\.\s?', '. ', string)
    string = re.sub(r'\s?,\s?', ', ', string)
    string = re.sub(r'\s?;\s?', '; ', string)
    string = re.sub(r'\s?:\s?', ': ', string)
    string = re.sub(r'\s?!\s?', '! ', string)
    string = re.sub(r'\s?\?\s?', '? ', string)
    string = re.sub(r'\s?-\s?', '-', string)

    return string
