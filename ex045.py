""" Crie um programa que faça o computador jogar jokenpô com você
"""
from random import randint
from time import sleep

nome = str(input('\33[0;49;33mOlá humano, para começar a jogar digite seu nome\33[0m: '))
print('Certo \33[0;49;33m{}\33[0m vamos começar!'.format(nome))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''\33[0;49;34mSUAS OPÇÕES\33[0m:
[ \33[0;49;90m0\33[0m ] - \33[0;49;90mPEDRA\33[0m
[ \33[0;49;97m1\33[0m ] - \33[0;49;97mPAPEL\33[0m
[ \33[0;49;93m2\33[0m ] - \33[0;49;93mTESOURA\33[0m''')
jogador = int(input('\33[0;49;33mQual sua jogada {}\33[0m? '.format(nome)))
print('\33[0;49;35mJO\33[0m')
sleep(1)
print('\33[0;49;96mKEN\33[0m')
sleep(1)
print('\33[0;49;31mPÔ\33[0m!!!')
sleep(1)
print('<><>' * 12)
print('O computador escolheu: \33[0;49;31m{}\33[0m '.format(itens[computador]))
print('{} jogou \33[0;49;32m{}\33[0m'.format(nome, jogador))
print('<><>' * 12)
if computador == 0:  # Computador jogou PEDRA
    if jogador == 0:
        print('\33[0;49;33mEMPATE\33[0m')
    elif jogador == 1:
        print('\33[0;49;32m \33[0;49;32m{}\33[0m  VENCE\33[0m'.format(nome))
    elif jogador == 2:
        print('\33[0;49;31mCOMPUTADOR VENCE\33[0m')
    else:
        print('\33[0;49;33mJOGADA INVÁLIDA\33[0m!')
elif computador == 1:  # Computador jogou PAPEL
    if jogador == 0:
        print('\33[0;49;31mCOMPUTADOR VENCE\33[0m')
    if jogador == 1:
        print('\33[0;49;33mEMPATE\33[0m')
    if jogador == 2:
        print('\33[0;49;32m \33[0;49;32m{}\33[0m VENCE\33[0m'.format(nome))
    else:
        print('\33[0;49;33MJOGADA INVÁLIDA\33[0m!')
elif computador == 2:  # computador jogou TESOURA
    if jogador == 0:
        print('\33[0;49;32m {} VENCE\33[0m'.format(nome))
    elif jogador == 1:
        print('\33[0;49;31mCOMPUTADOR VENCE\33[0m')
    elif jogador == 2:
        print('\33[0;49;33mEMPATE\33[0m')
    else:
        print('\33[0;49;33mJOGADA INVÁLIDA\33[0m!')
