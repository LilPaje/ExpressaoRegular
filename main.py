"""
Desenvolva, na linguagem de programação de sua preferência, um conjunto
de máscaras de validação, por meio de expressões regulares, que obedecem às especificações
prévias de cada campo abaixo. Considere os seguintes alfabetos Σ = {a, b, c, …, z}, Γ = {A, B, C,
…, Z} e N = {0, 1, 2, …, 9}.
"""

import re


def valida_nome(nome:str):
    """
    Comando:
        Nome: deve receber o nome e o sobrenome, ambos não vazios, separados por um espaço;
    não deve aceitar caracteres especiais ou numéricos; o primeiro símbolo do nome e do
    sobrenome deve ser do alfabeto Γ, e os outros símbolos devem ser do alfabeto Σ.
    ◦ Ex. de cadeias aceitas: Alan Turing, Noam Chomsky, Ada Lovelace
    ◦ Ex. de cadeias rejeitadas: 1Alan, Alan, A1an
    """

    mascara_nome = r'^[A-Z][a-z]+( [A-Z][a-z]+)+$'
    print("Validando nome: ",nome, end=" -> ")
    if re.match(mascara_nome ,nome):
        return True

    return False

def valida_email(email:str):
    """
    Comando:
        E-mail: as sentenças possuem símbolos de Sigma e deve conter exatamente um símbolo "@";
    não devem começar com o símbolo "@"; devem terminar com a sequência ".br"; devem ter, pelo
    menos, um símbolo de Sigma entre o símbolo "@" e o ".br"
    ◦ Ex. de cadeias aceitas: a@a.br, divulga@ufpa.br
    ◦ Ex. de cadeias rejeitadas: @, a@.br, T@tester.br
    """

    mascara_email = r'^[a-z]+@[a-z]+.br$'

    print("Validando e-mail: ",email, end=" -> ")


    if re.match(mascara_email, email):
        return True

    return False

def valida_senha(senha:str):
    """
    Comando:
        Senha: as cadeias podem conter símbolos dos alfabetos Σ, Γ e N; devem, obrigatoriamente,
    ter pelo menos um símbolo do alfabeto Γ e um símbolo do alfabeto N; devem ter
    comprimento igual a 8;
    ◦ Ex. de cadeias aceitas: 518R2r5e, F123456A, 1234567T, ropsSoq0
    ◦ Ex. de cadeias rejeitadas: F1234567A, abcdefgH, 1234567HI
    """

    mascara_senha = r'^(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8}$'

    print("Validando senha: ",senha, end=" -> ")


    if re.match(mascara_senha, senha):
        return True

    return False

def valida_cpf(cpf:str):
    """
    Comando:
        • CPF: as cadeias devem ter o formato xxx.xxx.xxx-xx, onde x N. ∈
    ◦ Ex. de cadeias aceitas: 123.456.789-09, 000.000.000-00
    ◦ Ex. de cadeias rejeitadas: 123.456.789-0, 111.111.11-11
    """

    mascara_cpf = r'^[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}$'

    print("Validando cpf: ",cpf, end=" -> ")

    if re.match(mascara_cpf, cpf):
        return True

    return False

def valida_telefone(telefone:str): # refazer
    """
    Comando:
        •Telefone: as cadeias devem ter o formato
    (xx) 9xxxx-xxxx ou
    (xx) 9xxxxxxxx ou
    xx 9xxxxxxxx
    onde x N. ∈
    ◦ Ex. de cadeias aceitas: (91) 99999-9999, (91) 999999999, 91 999999999
    ◦ Ex. de cadeias rejeitadas: (91) 59999-9999, 99 99999-9999, (94)95555-5555
    """

    mascara_telefone = r'^\([0-9]{2}\) 9[0-9]{4}-[0-9]{4}|\([0-9]{2}\) 9[0-9]{8}|[0-9]{2} 9[0-9]{8}$'

    print("Validando telefone: ",telefone, end=" -> ")


    if re.match(mascara_telefone, telefone):
        return True

    return False

#testes

print("---Nomes Válidos---")
print(valida_nome("Alan Turing"))
print(valida_nome("Noam Chomsky"))
print(valida_nome("Ada Lovelace"))

print("\n---Nomes Inválidos---")
print(valida_nome("1Alan"))
print(valida_nome("Alan"))
print(valida_nome("A1an"))

print("\n---E-mails Válidos---")
print(valida_email("a@a.br"))
print(valida_email("divulga@ufpa.br"))

print("\n---E-mails Inválidos---")
print(valida_email("@"))
print(valida_email("a@.br"))
print(valida_email("T@tester.br"))

print("\n---Senhas válidas---")
print(valida_senha("518R2r5e"))
print(valida_senha("F123456A"))
print(valida_senha("1234567T"))
print(valida_senha("ropsSoq0"))

print("\n---Senhas Inválidas---")
print(valida_senha("F1234567A"))
print(valida_senha("abcdefgH"))
print(valida_senha("1234567HI"))

print("\n---CPFs Válidos---")
print(valida_cpf("123.456.789-09"))
print(valida_cpf("000.000.000-00"))

print("\n---CPFs Inválidos")
print(valida_cpf("123.456.789-0"))
print(valida_cpf("111.111.11-11"))

print("\n---Telefones Válidos---")
print(valida_telefone("(91) 99999-9999"))
print(valida_telefone("(91) 999999999"))
print(valida_telefone("91 999999999"))

print("\n---Telefones Inválidos---")
print(valida_telefone("(91) 59999-9999"))
print(valida_telefone("99 99999-9999"))
print(valida_telefone("(94)95555-5555"))
