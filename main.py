from controllers import *


def run(string):

    frase_correta, doc = parser(string)

    corrigir = important_replaces(' '.join(montar_frase(frase_correta)))

    print('Frase original: \n\n'
          '%s'
          '\n\n------------------------\n' % doc)

    print('Frase corrigida: \n\n'
          '%s'
          '\n\n\n\n\n' % corrigir)


if __name__ == '__main__':

    while True:
        doc = input('Digite uma frase para verificação [ :q para sair ]: \n')

        if doc == ':q':
            break

        else:
            run(doc)
