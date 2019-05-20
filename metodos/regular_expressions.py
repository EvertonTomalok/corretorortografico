import re
import sys


def rule_1(string):
    if re.search(r'(\b)(ku?|qu?)(\w*)', string, re.IGNORECASE):
        string = re.sub(r'(\b)(ku?|qu?)(\w*)', r'\1qu\3', string, re.IGNORECASE)
    if re.search(r"(?<=\w)cao\b", string, re.IGNORECASE):
        string = re.sub(r"(?<=\w)cao\b", "ção", string, re.IGNORECASE)
    if re.search(r"(?<=\w)coes\b", string, re.IGNORECASE):
        string = re.sub(r"(?<=\w)(coes)\b", r"ções", string, re.IGNORECASE)

    match = re.search(r'(?<=\w)(k)[aáãâoôóõuú]', string, re.IGNORECASE)

    if match:
        start, end = match.span()
        value = match.group()
        replace_value = list(value.replace("k", "c"))
        palavra = list(string)
        palavra[start:end] = replace_value
        string = "".join(palavra)

    return string


def rule_2(string):
    if re.search(r'(\b\w*)ç(\B)', string, re.IGNORECASE):
        string = re.sub(r'(\b\w*)ç(\B)', r'\1#\2', string, re.IGNORECASE)
    if re.search(r'(\b)s([aáâãeéêiíoóôõuú]\w*\b)', string, re.IGNORECASE):
        string = re.sub(r'(\b)s([aáâãeéêiíoóôõuú]\w*\b)', r'\1#\2', string, re.IGNORECASE)
    if re.search(r'(\B)ss([aáâãeéêiíoóôõuú]\w*\b)', string, re.IGNORECASE):
        string = string.replace("ss", "#").replace("SS", "#")
    if re.search(r"(\B)[nlrs]s([aáâãeéêiíoóôõuú]\w*\b)", string, re.IGNORECASE):
        string = re.sub(r"(\B)[nlrs]s([aáâãeéêiíoóôõuú]\w*\b)", r"\1#\2", string, re.IGNORECASE)
    if re.search(r'(\B)[sx]c([eéêií]\w*\b)', string, re.IGNORECASE):
        string = re.sub(r'(\B)[sx]c([eéêií]\w*\b)', r'\1#\2', string, re.IGNORECASE)
    if re.search(r"(\b(au))x([ií]\B)", string, re.IGNORECASE):
        string = re.sub(r"(\b(au))x([ií]\B)", r"\1#\3", string, re.IGNORECASE)

    return string


def rule_3(string):
    if re.search(r'(\B)[xs]([bdfgklmnpqrtv]\w*\b)', string, re.IGNORECASE):
        string = re.sub(r'(\B)[xs]([bdfgklmnpqrtv]\w*\b)', r'\1$\2', string, re.IGNORECASE)
    if re.search(r'(\B)[sx]c([aáâãoóôõuú]\w*\b)', string, re.IGNORECASE):
        string = re.sub(r'(\B)[sx]c([aáâãoóôõuú]\w*\b)', r'\1$c\2', string, re.IGNORECASE)
    if re.search(r'(\B)[sz]([gmv]\B)', string, re.IGNORECASE):
        string = re.sub(r'(\B)[sz]([gmv]\B)', r'\1$\2', string, re.IGNORECASE)

    return string


def rule_4(string):
    if re.search(r'(\b\w*)[sc]h(\B)', string, re.IGNORECASE):
        string = re.sub(r'(\b\w*)[sc]h(\B)', r'\1%\2', string, re.IGNORECASE)
    if re.search(r"(\b\w*[aáeéêoóôuú][i])x(\B)", string, re.IGNORECASE):
        string = re.sub(r"(\b\w*[aáeéêoóôuú][i])x(\B)", r"\1%\2", string, re.IGNORECASE)
    if re.search(r"(\b\w*[eéêiíoóô][u])x(\B)", string, re.IGNORECASE):
        string = re.sub(r"(\b\w*[eéêiíoóô][u])x(\B)", r"\1%\2", string, re.IGNORECASE)
    if re.search(r"(\b|\Bn)x(\B)", string, re.IGNORECASE):
        string = re.sub(r"(\b|\Bn)x(\B)", r"\1%\2", string, re.IGNORECASE)
    if re.search(r"(\B((a)|(e)|(i)|(o)|(u)))x(\1|\2|\3|\4|\5\w*\b)", string, re.IGNORECASE):
        string = re.sub(r"(\B((a)|(e)|(i)|(o)|(u)))x(\1|\2|\3|\4|\5\w*\b)", r"\1%\2", string, re.IGNORECASE)

    return string


def rule_5(string):
    if re.search(r'(\B[aáâeéêiíoóôuú])s([aáâãeéêiíoóôõuú]\w*\b)', string, re.IGNORECASE):
        string = re.sub(r'(\B[aáâeéêiíoóôuú])s([aáâãeéêiíoóôõuú]\w*\b)', r"\1&\2", string, re.IGNORECASE)
    if re.search(r'(\b\w*)z([aáâãeéêiíoóôõuú]\w*\b)', string, re.IGNORECASE):
        string = re.sub(r'(\b\w*)z([aáâãeéêiíoóôõuú]\w*\b)', r"\1&\2", string, re.IGNORECASE)
    if re.search(r'(\b\w*[eê])x([aáâãeéêiíoóôõuú]\B)', string, re.IGNORECASE):
        string = re.sub(r'(\b\w*[eê])x([aáâãeéêiíoóôõuú]\B)', r"\1&\2", string, re.IGNORECASE)

    return string


def rule_6(string):
    if re.search(r"(\b\w*)[gj]([eéêií]\w*\b)", string, re.IGNORECASE):
        string = re.sub(r"(\b\w*)[gj]([eéêií]\w*\b)", r"\1*\2", string, re.IGNORECASE)

    return string


def rule_7(string):
    if re.search(r"(\B)[aáeéêiíoóô][lu]([bcdfgjklmnpqrstvxz]\B|\b)", string, re.IGNORECASE):
        string = re.sub(r"(\B)[aáeéêiíoóô][lu]([bcdfgjklmnpqrstvxz]\B|\b)", r"\1@\2", string, re.IGNORECASE)

    return string


def rule_8(string):
    if re.search(r'(\B)[mn]([pb]\B)', string, re.IGNORECASE):
        string = re.sub(r'(\B)[mn]([pb]\B)', r"\1!\2", string, re.IGNORECASE)

    return string


def rule_9(string):
    if re.search(r'([bcdfgkptv])[rl]([aáâãeéêiíoóôõuú]\w*\b)', string, re.IGNORECASE):
        string = re.sub(r'([bcdfgkptv])[rl]([aáâãeéêiíoóôõuú]\w*\b)', r"\1!\2", string, re.IGNORECASE)

    return string


if __name__ == '__main__':

    corrected = getattr(sys.modules[__name__], "rule_%s" % sys.argv[1])(sys.argv[2])
    print(f"FRASE '{sys.argv[2]}' -> \033[3 {'2m ' + corrected if corrected else '1m NÃO ALTERADO'} \033[m")
