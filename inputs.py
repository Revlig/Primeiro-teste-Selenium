def name():
    nomes = ["carlos", "margot", "paulo", "caio", "vitor", "joao", "fabio",
             "priscila", "raquel", "marcia", "katia"]
    return nomes


def senha():
    senhas = ["123mudar", "teste123", "senha123", "github123", "admin",
              "passwd", "superuser", "oioto", "nove", "dez", "onze"]
    return senhas


def logins(tentativas):
    return name()[tentativas]


def passwords(tentativas):
    return senha()[tentativas]


def names_lenght():
    return (len(name()))
