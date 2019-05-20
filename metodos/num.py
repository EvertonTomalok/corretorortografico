_num_words = ['zero', 'um', 'dois', 'três', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
              'onze', 'doze', 'dúzia', 'dúzias', 'duzia', 'duzias', 'treze', 'catorze', 'quinze', 'dezesseis',
              'dezessete', 'dezoito', 'dezenove', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta',
              'setenta', 'oitenta', 'noventa', 'cem', 'cento', 'duzentos', 'trezentos', 'quatrocentos',
              'quinhentos', 'seicentos', 'setecentos', 'oitocentos', 'novecentos', 'mil', 'milhão', 'milhao',
              'milhões', 'milhoes', 'bilhão', 'bilhao', 'bilhões', 'bilhoes', 'trilhão', 'trilhao', 'trilhões',
              'trilhoes', 'quadrilhão', 'quadrilhao', 'quadrilhões', 'quadrilhoes']


_ordinal_words = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto',
                  'sétimo', 'oitavo', 'nono', 'décimo', 'vigésimo', 'trigésimo',
                  'quadragésimo', 'quinquagésimo', 'sexagésimo', 'septuagésimo',
                  'octogésimo', 'nonagésimo', 'centésimo', 'ducentésimo',
                  'trecentésimo', 'quadringentésimo', 'quingentésimo', 'sexcentésimo',
                  'septingentésimo', 'octingentésimo', 'nongentésimo', 'milésimo',
                  'milionésimo', 'bilionésimo']


def like_num(text):
    text = text.replace(',', '').replace('.', '').replace('º','').replace('ª','')
    if text.isdigit():
        return True
    if text.count('/') > 0:
        return all([num.isdigit() for num in text.split('/')])
    if text.lower() in _num_words:
        return True
    if text.lower() in _ordinal_words:
        return True
    return False
