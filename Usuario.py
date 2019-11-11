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
flagCompra = 0
idPedido = 0
while True:
    print('\n')
    print('       ########################################')
    print('       ###        Menu de Navegação         ###')
    print('       ########################################')      
    print('       |          1) Listar Produtos          |')
    print('       |          2) Comprar Produtos         |')  
    print('       |          3) Buscar Produtos          |')
    print('       |          4) Carrinho                 |')
    print('       |          5) Cancelar Compra          |')    
    print('       |          6) Finalizar Compra         |')
    print('       |          0) Finalizar Seção          |')
    print('       |______________________________________|')                                         
    op = input('Por favor escolha uma opção [0-8] > ')
#------------------------------Listar Produtos -------------------------------------    
    if op == '1':
        listaDeProduto = json.loads(client.service.listProdut())
        i = 0
        for lista in listaDeProduto:
            print ('ID: ',listaDeProduto[i]["id"])
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
        if flagCompra == 0:
            idPedido = json.loads(client.service.addPedido('{"Id":"0","valor": "0", "status": "0"}'))
            flagCompra = 1
        else:
            listaDeProduto = json.loads(client.service.listProdut())
            i = 0
            for lista in listaDeProduto:
                print ('Codigo: ',listaDeProduto[i]["id"])
                print ('Produto: ',listaDeProduto[i]["nome"])
                print ('Valor: R$ ',listaDeProduto[i]["valor"])
                print ('Quantidade: ',listaDeProduto[i]["quantidade"],' Produtos Disponível')
                i = i + 1
            print('\n')
            produto = json.loads(client.service.buscaProdut(input('Comprar Produtos > Produto > ')))
            print ('Produto: ',produto[0]["nome"])
            print ('Valor: R$ ',produto[0]["valor"])
            idProduto = int(produto[0]["id"])             
            disponivel = int(produto[0]["quantidade"])                
            if disponivel > 0:
                qt = int(input('Quantidade Desejada > '))
                if qt > disponivel:
                    print('Desculpe!, Quantidade Indisponivel')
                else:
                    valor = float(produto[0]["valor"])   
                    valor = qt*valor
                    compraDeProduto = ('{"id":0'+
                                           ', "IdPedido":'+str(idPedido)+
                                           ', "IdProduto":'+str(idProduto)+
                                           ', "valor":'+str(valor)+
                                           ', "qtd":'+str(qt)+'}')
                    print(compraDeProduto)
                    op = input('Deseja pedir esse Produto ? (1-Sim / 2-Não) > ')
                    if op == '1':
                        x = client.service.addItem(compraDeProduto)
                        print('Produto Adicionado ao Carrinho com Sucesso!')
                    else:
                        print('Pedido Cancelado!')
            else:
                print("Status: Indisponivel")
                
            #{"Id":"1","IdPedido": "1", "IdProduto": "4", "valor":"2", "qtd":"2"}    
        
         
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
        meusPedidos = json.loads(client.service.listItem(idPedido))
        i = 0
        valorTotal = 0
        print('################# Carrinho ################\n')
        for lista in meusPedidos:            
            carrinho = meusPedidos[i]["produto"]
            print('------------------ Item( '+str(i+1) +' ) --------------------')           
            print ('Codigo: ',carrinho["id"])
            print ('Produto: ',carrinho["nome"])
            print ('Descrição: ',carrinho["descricao"]) 
            print ('Categoria: ',carrinho["categoria"])
            print ('Modelo: ',carrinho["modelo"])
            print ('Marca: ',carrinho["marca"])
            print ('Valor do Produto: R$ ',carrinho["valor"])
            print ('  > Quantidade de Itens: ',meusPedidos[i]["qtd"])
            print ('  > Valor do(s) Iten(s): R$ ',meusPedidos[i]["valor"])
            valorTotal = valorTotal + float(meusPedidos[i]["valor"])
            #-----------------------------------------------------------
            i = i + 1
        print('')
        print('    > Quantidade Total de Itens:',str(i))
        print('    > Valor Total : R$ ',str(valorTotal))
#------------------------- Cancelar a Compra ----------------------------------             
    elif op == '5':
        if idPedido == 0:
            print('Você ainda não realizou pedido!')
        else:
            client.service.deletarPedido(idPedido)
            print('Pedido Cancelado com sucesso!')
            flagCompra = 0
            idPedido = 0        
#------------------------- Finalizar Compra -----------------------------------             
    elif op == '6':
        meusPedidos = json.loads(client.service.listItem(idPedido))
        i = 0
        valorTotal = 0
        print('')
        for lista in meusPedidos:            
            carrinho = meusPedidos[i]["produto"]           
            print ('Produto: ',carrinho["nome"])
            print ('Quantidade de Itens: ',meusPedidos[i]["qtd"])
            print ('Valor do(s) Iten(s): R$ ',meusPedidos[i]["valor"])
            print('')
            valorTotal = valorTotal + float(meusPedidos[i]["valor"])
            #-----------------------------------------------------------
            i = i + 1
        print('    > Quantidade Total de Itens:',str(i))
        print('    > Valor Total : R$ ',str(valorTotal))
        print('')
        op = input('Confirmar a Compra ? (1-Sim / 2-Não) > ')
        if op == '1':
            client.service.alterarPedido('{"Id":'+str(idPedido)+',"valor":'+str(valorTotal)+', "status": "1"}')
            print('Compra realizado com sucesso ! \nObrigado por comprar com a KaBuM!')
        break
#-------------------------------- Sair ---------------------------------------- 
    elif op == '0':
        if idPedido == 1:
            op = input('Existe pedido em aberto, deseja cancelar ? (1-Sim, 2-Não)')
            if op == 1:
                client.service.deletarPedido(idPedido)
                print('Pedido Cancelado com sucesso!')
                break
            else:
                print('Pedido de Finalização Negado!')
        else:
            print('Saindo...')
            break
       
    else:
        print('Opcao invalida!')    