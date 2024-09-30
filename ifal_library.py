def get_int(prompt, show_msg=False):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            if show_msg:
                print("Não é um número inteiro (integer)")
            else:
                pass


def get_float(prompt, show_msg=False):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            if show_msg:
                print("Não é um número decimal (float)")
            else:
                pass


def get_string(prompt, show_msg=False):
    while True:
        try:
            return input(prompt)
        except ValueError:
            if show_msg:
                print("Não é um texto (string)")
            else:
                pass


def help():
    print(
        "😌 Tenha calma, respire profundo 3x e analise o código atentamente.\n🛠️  Caso não encontre o erro, peça para um colega olhar seu código.\n❓ Se ainda precisar de ajuda: chame o professor 💙"
    )