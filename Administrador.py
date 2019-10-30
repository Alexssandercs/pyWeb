# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:02:30 2019

@author: Alexssander & Flavio
"""

from zeep import Client
import json
import os
os.system('cls' if os.name == 'nt' else 'clear')
#client = Client(wsdl='http://localhost:44383/WebService1.asmx?wsdl')
#client = Client(wsdl='http://localhost:44383/WebService1.asmx')
print('\n')
print('  _   __     ______      ___  ____  ____    ')
print(' | | / /     | ___ \     |  \/  | | \ \ \   ')
print(' | |/ /  __ _| |_/ /_   _| .  . | |  \ \ \  ')
print(' |    \ / _` | ___ \ | | | |\/| | |   > > > ')
print(' | |\  \ (_| | |_/ / |_| | |  | |_|  / / /  ')
print(' \_| \_/\__,_\____/ \__,_\_|  |_(_) /_/_/   ')
print('--------------------------------------------')                                           
print('|               Administrador              |')
print('--------------------------------------------')

#client = Client(wsdl='http://localhost:44383/WebService1.asmx?wsdl')

while True:
    print('\n')
    print('1) Cadastrar Produto')
    print('2) Alterar Produto')  
    print('3) Buscar Produto')
    print('4) Listar Produtos')
    print('5) Histórico de Compras')
    print('6) Deletar Produto')
    print('0) Sair')                                         
    print('\n')
    op = input('> ')
#------------------------------Listar Produtos --------------------------------    
    if op == '1':
        produto = input('Produto > ')
        descricao = input('Descrição > ')
        categoria = input('Categoria > ')
        modelo = input('Modelo > ')
        valor = input('Valor > ')
        quantidade = input('Quantidade > ')
        cadastroDeProduto = ('{"nome": "'+str(produto)+'", "descricao":"'+str(descricao)+
                        '", "categoria":"'+str(categoria)+
                        '", "modelo":"'+str(modelo)+
                        '", "valor":"'+str(valor)+
                        '", "quantidade":"'+str(quantidade)+'"}')
        parsed_json = json.loads(cadastroDeProduto)
        print(json.dumps(parsed_json))
        break
#---------------------------- Comprar Produtos --------------------------------    
    elif op == '2':
        print("operação 2")
#---------------------------- Buscar Produtos ---------------------------------         
    elif op == '3':
        print('opecação 3')
#---------------------------- Meus Produtos -----------------------------------             
    elif op == '4':
        print("operação 4")
#-------------------------- Histórico de Compras ------------------------------             
    elif op == '5':
        print("operação 5")
#---------------------------- Deletar Produto ---------------------------------             
    elif op == '6':
        print("operação 6")        
#-------------------------------- Sair ---------------------------------------- 
    elif op == '0':
        break
    else:
        print('Opcao invalida!')
