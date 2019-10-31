# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:02:41 2019

@author: Alexssander & Flavio
"""

from zeep import Client
import json
import os
os.system('cls' if os.name == 'nt' else 'clear')
print('\n')
print('     _   __     ______      ___  ____  ____    ')
print('    | | / /     | ___ \     |  \/  | | \ \ \   ')
print('    | |/ /  __ _| |_/ /_   _| .  . | |  \ \ \  ')
print('    |    \ / _` | ___ \ | | | |\/| | |   > > > ')
print('    | |\  \ (_| | |_/ / |_| | |  | |_|  / / /  ')
print('    \_| \_/\__,_\____/ \__,_\_|  |_(_) /_/_/   ')
print('    ------------------------------------------ ')                                           
print('   |                  Cliente                 |')
print('    ------------------------------------------ ')
client = Client(wsdl='http://localhost:54202/WebService.asmx?wsdl')
while True:
    print('\n')
    print('       ########################################')
    print('       ###        Menu de Navegação         ###')
    print('       ########################################')      
    print('       |          1) Listar Produtos          |')
    print('       |          2) Comprar Produtos         |')  
    print('       |          3) Buscar Produtos          |')
    print('       |          4) Meus Produtos            |')
    print('       |          5) Finalizar Compra         |')
    print('       |          0) Finalizar Seção          |')
    print('       |______________________________________|')                                         
    op = input('Por favor escolha uma opção [0-5] > ')
#------------------------------Listar Produtos -------------------------------------    
    if op == '1':
        listaDeProduto = json.loads(client.service.listProdut())
        i = 0
        for lista in listaDeProduto:
            print ('Produto: ',listaDeProduto[i]["nome"])
            print ('Descrição: ',listaDeProduto[i]["descricao"]) 
            print ('Categoria: ',listaDeProduto[i]["categoria"])
            print ('Modelo: ',listaDeProduto[i]["modelo"])
            print ('Marca: ',listaDeProduto[i]["marca"])
            print ('Valor: R$ ',listaDeProduto[i]["valor"])
            disponivel = (listaDeProduto[i]["quantidade"])
            if disponivel != '0':
                print("Status: Disponivel")
            else:
                print("Status: Indisponivel")
            i = i + 1
            print('\n')
#---------------------------- Comprar Produtos --------------------------------    
    elif op == '2':
        print('Este modulo não está pronto')  
#---------------------------- Buscar Produtos ---------------------------------         
    elif op == '3':
        try:
            produto = json.loads(client.service.buscaProdut(input('Buscar Produtos > Produto > ')))
            print ('Produto: ',produto[0]["nome"])
            print ('Descrição: ',produto[0]["descricao"]) 
            print ('Categoria: ',produto[0]["categoria"])
            print ('Modelo: ',produto[0]["modelo"])
            print ('Marca: ',produto[0]["marca"])
            print ('Valor: R$ ',produto[0]["valor"])
            disponivel = (produto[0]["quantidade"])
            if disponivel != '0':
                print("Status: Disponivel")
            else:
                print("Status: Indisponivel")
            print('\n')
        except:
            print('< Não Encontrado >')
#---------------------------- Meus Produtos -----------------------------------             
    elif op == '4':
        print('Este modulo não está pronto')  
#------------------------- Finalizar Compra -----------------------------------             
    elif op == '5':
        print('Este modulo não está pronto')          
#-------------------------------- Sair ---------------------------------------- 
    elif op == '0':
        break
    else:
        print('Opcao invalida!')    