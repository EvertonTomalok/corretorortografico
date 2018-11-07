from controllers import *


def run(string):

    frase_correta, doc = parser(string)

    corrigir = important_replaces(' '.join(montar_frase(frase_correta)))

    print(' => Frase original: \n\n'
          '%s' % doc)

    print('\n\n => Frase corrigida: \n\n'
          '%s'
          '\n\n' % corrigir)

    correcao_com_pesos = important_replaces(' '.join(montar_frase(frase_correta, only_words=False)))

    print(' => Frase corrigida com seu determinado peso: \n\n'
          '%s'
          '\n\n' % correcao_com_pesos)

    print('\n\n------------------------------------')


if __name__ == '__main__':

    while True:
        doc = input('Digite uma frase para verificação [ :q para sair ]: \n')

        if doc == ':q':
            break

        else:
            run(doc)
