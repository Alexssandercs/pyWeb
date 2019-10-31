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
print(' ------------------------------------------')                                           
print('|               Administrador              |')
print(' ------------------------------------------')

#client = Client(wsdl='http://localhost:44383/WebService1.asmx?wsdl')
client = Client(wsdl='http://localhost:54202/WebService.asmx?wsdl')
while True:
    print('\n')
    print('1) Cadastrar Produto')
    print('2) Alterar Produto')  
    print('3) Buscar Produto')
    print('4) Listar Produtos')
    print('5) Histórico de Compras')
    print('6) Deletar Produto')
    print('0) Finalizar Seção')                                         
    print('\n')
    op = input('> ')
#----------------------------- Cadastrar Produtos -----------------------------    
    if op == '1':
        idP = input('ID > ')
        produto = input('Produto > ')
        descricao = input('Descrição > ')
        categoria = input('Categoria > ')
        modelo = input('Modelo > ')
        marca = input('Marca > ')
        valor = input('Valor > ')
        quantidade = input('Quantidade > ')
        cadastroDeProduto = ('{"id":'+str(idP)+
                               ', "nome":"'+str(produto)+
                               '", "descricao":"'+str(descricao)+
                               '", "categoria":"'+str(categoria)+
                               '", "modelo":"'+str(modelo)+
                               '", "marca":"'+str(marca)+
                               '", "valor":'+str(valor)+
                               ', "quantidade":'+str(quantidade)+'}')
        print(cadastroDeProduto) 
        op = input('Deseja Cadastrar esse Produto ? (1-Sim / 2-Não) > ')
        if op == '1':
            produtoCadastro = json.loads(cadastroDeProduto)
            x = client.service.addProdut(produtoCadastro)
            print(x)
            print('Produto Cadatrado com Sucesso!')
        else:
            print('Cadatrado Cancelado!')
    
#---------------------------- Alterar Produtos --------------------------------    
    elif op == '2':
        idP = input('ID > ')
        produto = input('Produto > ')
        descricao = input('Descrição > ')
        categoria = input('Categoria > ')
        modelo = input('Modelo > ')
        marca = input('Marca > ')
        valor = input('Valor > ')
        quantidade = input('Quantidade > ')
        cadastroDeProduto = ('{"id":'+str(idP)+
                               ', "nome":"'+str(produto)+
                               '", "descricao":"'+str(descricao)+
                               '", "categoria":"'+str(categoria)+
                               '", "modelo":"'+str(modelo)+
                               '", "marca":"'+str(marca)+
                               ', "valor":'+str(valor)+
                               ', "quantidade":'+str(quantidade)+'}')
        op = input('Deseja Alterar esse Produto ? (1-Sim / 2-Não) > ')
        if op == 1:
            produtoCadastro = json.loads(cadastroDeProduto)
            x = client.service.alterarProdut(cadastroDeProduto)
            print('Produto Alterado Com Sucesso!')
        else:
            print('Cadatrado Cancelado!')
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
            print ('Quantidade: ',produto[0]["quantidade"],' Produtos Disponível')
        except:
            print('< Não Encontrado >')
#---------------------------- Listar Produtos -----------------------------------             
    elif op == '4':
        listaDeProduto = json.loads(client.service.listProdut())
        i = 0
        for lista in listaDeProduto:
            print ('Codigo: ',listaDeProduto[i]["id"])
            print ('Produto: ',listaDeProduto[i]["nome"])
            print ('Descrição: ',listaDeProduto[i]["descricao"]) 
            print ('Categoria: ',listaDeProduto[i]["categoria"])
            print ('Modelo: ',listaDeProduto[i]["modelo"])
            print ('Marca: ',listaDeProduto[i]["marca"])
            print ('Valor: R$ ',listaDeProduto[i]["valor"])
            print ('Quantidade: ',listaDeProduto[i]["quantidade"],' Produtos Disponível')
            i = i + 1
            print('\n')
#-------------------------- Histórico de Compras ------------------------------             
    elif op == '5':
        print("operação 5")
#---------------------------- Deletar Produto ---------------------------------             
    elif op == '6':
        try:
            produto = json.loads(client.service.buscaProdut(input('Produto > ')))
            print ('Codigo: ',produto[0]["id"])
            print ('Produto: ',produto[0]["nome"])
            print ('Descrição: ',produto[0]["descricao"]) 
            print ('Categoria: ',produto[0]["categoria"])
            print ('Modelo: ',produto[0]["modelo"])
            print ('Marca: ',produto[0]["marca"])
            print ('Valor: R$ ',produto[0]["valor"])
            print ('Quantidade: ',produto[0]["quantidade"],' Produtos Disponível')
            print('\n')
            op = input('Deseja Deletar Esse Produto ? (1-Sim / 2-Não) > ')
            if op == '1':
                x = client.service.deletarProdut((produto[0]["id"]))
                print('Produto Deletado Com Sucesso!')
            else:
                print('Pedido Cancelado!')
        except:
            print('< Não Encontrado >')     
#-------------------------------- Sair ---------------------------------------- 
    elif op == '0':
        break
    else:
        print('Opcao invalida!')
