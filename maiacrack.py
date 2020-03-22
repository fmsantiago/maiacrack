import sys
import os
import crypt

if len(sys.argv) <= 1:
	print "Utilizando lista de senhas padrao..."
	f = open('senhas.txt', 'r')
else:
	nomelista = sys.argv[1]
	print "Utilizando a lista",sys.argv[1]
	f = open(sys.argv[1], 'r')
	
qhash = raw_input("Digite o hash completo: ")
salt = raw_input("Digite o salt: ")

for line in f:
	senha = line.replace('\n', '')
	ghash = crypt.crypt(senha,salt)
	if (qhash==ghash):
		print "Senha Encontrada: ", senha
		break	
	else:
		print "Tentando senha", senha







