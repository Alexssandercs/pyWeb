# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:02:41 2019

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
print('|                  Cliente                 |')
print('--------------------------------------------')

client = Client(wsdl='http://localhost:54202/WebService.asmx?wsdl')

minhasComprar = []
indexCompra = 0
while True:
    print('\n')
    print('1) Listar Produtos')
    print('2) Comprar Produtos')  
    print('3) Buscar Produtos')
    print('4) Meus Produtos')
    print('0) Sair')                                         
    print('\n')
    op = input('> ')
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
        x = [client.service.ObterProdutoPorMarca('todas')]
        x2 = [(x[0]['Produto'])]
        comprando = x2[0]
        i = 0
        listaNome = []
        print('\n< Lista de Produtos >')
        for prod in comprando:
            disponivel = (comprando[i]["quantidade"])
            if disponivel != '0':
                listaNome.append(comprando[i]["nome"])
                print(listaNome[i])
                i = i + 1
        
        try: 
            comprar = input('Produto > ')
            listaNome.index(comprar)
            quantidade = input('Quantidade > ')           
            if(int(quantidade) <= 0):
                print('Quantidade deve ser maior que 0(zero)')    
                while (int(quantidade) <= 0):
                    quantidade = input('Quantidade > ')
            compraJson = '{"nome": "'+comprar+'", "quantidade":"'+str(quantidade)+'"}'
            parsed_json = json.loads(compraJson)
            print(parsed_json['nome'])
            print(json.dumps(parsed_json))
                       
        except:
            print('< Produto Inexistente >')
            
#---------------------------- Buscar Produtos ---------------------------------         
    elif op == '3':
        try:
            produto = json.loads(client.service.buscaProdut(input('Produto > ')))
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
        print("operação 4")
#-------------------------------- Sair ---------------------------------------- 
    elif op == '0':
        break
    else:
        print('Opcao invalida!')

    
    
    