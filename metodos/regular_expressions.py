import re
import sys


def rule_1(string):
    if re.search(r"(?<=\w)cao\b", string):
        return re.sub(r"(?<=\w)cao\b", "ção", string)
    elif re.search(r"(?<=\w)coes\b", string):
        return re.sub(r"(?<=\w)(coes)\b", r"ções", string)
    else:
        if re.search(r"(qu?|ku)", string):
            return re.sub(r"(qu?|ku)", r"qu", string)
        else:
            match = re.search(r'(?<=\w)(k)[aáãâoôóõuú]', string)

            if match:
                start, end = match.span()
                value = match.group()
                replace_value = list(value.replace("k", "c"))
                palavra = list(string)
                palavra[start:end] = replace_value
                return "".join(palavra)
            else:
                return string


def rule_2(string):
    if re.search(r'(\b\w*)ç(\B)', string, re.IGNORECASE):
        return re.sub(r'(\b\w*)ç(\B)', r'\1#\2', string, re.IGNORECASE)
    elif re.search(r'(\b)s([aáâãeéêiíoóôõuú]\w*\b)', string, re.IGNORECASE):
        return re.sub(r'(\b)s([aáâãeéêiíoóôõuú]\w*\b)', r'\1#\2', string, re.IGNORECASE)
    elif re.search(r"(\B)[nlrs]s([aáâãeéêiíoóôõuú]\w*\b)", string, re.IGNORECASE):
        return re.sub(r"(\B)[nlrs]s([aáâãeéêiíoóôõuú]\w*\b)", r"\1#\2", string, re.IGNORECASE)
    elif re.search(r'(\B)[sx]c([eéêií]\w*\b)'):
        return re.sub(r'(\B)[sx]c([eéêií]\w*\b)', r'\1#\2', string, re.IGNORECASE)
    elif re.search(r"(\b(au))x([ií]\B)", string, re.IGNORECASE):
        return re.sub(r"(\b(au))x([ií]\B)", r"\1#\3", string, re.IGNORECASE)
    else:
        return string


def rule_3(string):
    if re.search(r'(\B)[xs]([bdfgklmnpqrtv]\w*\b)', string, re.IGNORECASE):
        return re.sub(r'(\B)[xs]([bdfgklmnpqrtv]\w*\b)', r'\1$\2', string, re.IGNORECASE)
    elif re.search(r'(\B)[sx]c([aáâãoóôõuú]\w*\b)', string, re.IGNORECASE):
        return re.sub(r'(\B)[sx]c([aáâãoóôõuú]\w*\b)', r'\1$c\2', string, re.IGNORECASE)
    elif re.search(r'(\B)[sz]([gmv]\B)', string, re.IGNORECASE):
        return re.sub(r'(\B)[sz]([gmv]\B)', r'\1$\2', string, re.IGNORECASE)
    else:
        return string


def rule_4(string):
    if re.search(r'(\b\w*)[sc]h(\B)', string, re.IGNORECASE):
        return re.sub(r'(\b\w*)[sc]h(\B)', r'\1%\2', string, re.IGNORECASE)
    elif re.search(r"(\b\w*[aáeéêoóôuú][i])x(\B)", string, re.IGNORECASE):
        return re.sub(r"(\b\w*[aáeéêoóôuú][i])x(\B)", r"\1%\2", string, re.IGNORECASE)
    elif re.search(r"(\b\w*[eéêiíoóô][u])x(\B)", string, re.IGNORECASE):
        return re.sub(r"(\b\w*[eéêiíoóô][u])x(\B)", r"\1%\2", string, re.IGNORECASE)
    elif re.search(r"(\b|\Bn)x(\B)", string, re.IGNORECASE):
        return re.sub(r"(\b|\Bn)x(\B)", r"\1%\2", string, re.IGNORECASE)
    elif re.search(r"(\B((a)|(e)|(i)|(o)|(u)))x(\1|\2|\3|\4|\5\w*\b)", string, re.IGNORECASE):
        return re.sub(r"(\B((a)|(e)|(i)|(o)|(u)))x(\1|\2|\3|\4|\5\w*\b)", r"\1%\2", string, re.IGNORECASE)
    return string


def rule_5(string):
    if re.search(r'(\B[aáâeéêiíoóôuú])s([aáâãeéêiíoóôõuú]\w*\b)', string, re.IGNORECASE):
        return re.sub(r'(\B[aáâeéêiíoóôuú])s([aáâãeéêiíoóôõuú]\w*\b)', r"\1&\2", string, re.IGNORECASE)
    elif re.search(r'(\b\w*)z([aáâãeéêiíoóôõuú]\w*\b)',  string, re.IGNORECASE):
        return re.sub(r'(\b\w*)z([aáâãeéêiíoóôõuú]\w*\b)',  r"\1&\2", string, re.IGNORECASE)
    elif re.search(r'(\b\w*[eê])x([aáâãeéêiíoóôõuú]\B)', string, re.IGNORECASE):
        return re.sub(r'(\b\w*[eê])x([aáâãeéêiíoóôõuú]\B)', r"\1&\2", string, re.IGNORECASE)
    else:
        return string


if __name__ == '__main__':

    corrected = getattr(sys.modules[__name__], "rule_%s" % sys.argv[1])(sys.argv[2])
    print(f"FRASE '{sys.argv[2]}' -> \033[32m {corrected} \033[m")
