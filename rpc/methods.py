from simple_print.functions import sprint_f


async def upper_word__internal_messager(*, word):
    sprint_f(word)
    return word.upper()
