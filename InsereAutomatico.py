# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:19:19 2019

@author: Alexssander
"""
from zeep import Client
import json

30.2 + 5.6

lista =  [["1", "Memória HyperX Fury", "8GB 2666MHz, DDR4 - Preto", "Memoria Ram", "HX426C16FB3 / 8", "HyperX", "232.82", "10"]]
lista = lista + [["2", "SSD Kingston A400", "SSD Kingston A400, 240GB, SATA, Leitura 500MB / s, Gravação 350MB / s - SA400S37 / 240G", "SSD", "SA400S37 / 240G", "Kingston", "205.76", "6"]]
lista = lista + [["3", "Galaxy A20", "Smartphone 32 GB - Preto", "Celular", "SM - A205G", "Samsumg", "739", "4"]]
lista = lista + [["4", "Asus Prime Gaming - BR", "As placas - mãe ASUS Prime Série B450", "Placa - Mãe", "Prime B450M Gaming / BR", "ASUS", "455.9", "2"]]
lista = lista + [["5", "Acer Aspire Nitro 5", "Intel Core i5 - 7300HQ 8GB 1TB NVIDIA GeForce GTX 1050 4GB GDDR5 15, 6", "Notbook", "AN515 - 51 - 55YB", "ACER", "3699.9", "1"]]
lista = lista + [["6", "Acer Aspire Nitro 3", "AMD Ryzen 3 2200U, 4GB, 1TB, Radeon Vega 3, Windows 10 Home, 15.6", "Notbook", "A315 - 41 - R790", "ACER", "2199.9", "2"]]
lista = lista + [["7", "Sharkoon", "HUB Sharkoon USB 3.0 4 Portas Tipo - C Alumínio BK", "Periferico", "HUB", "Sharkoon", "119.88", "4"]]
lista = lista + [["8", "DataTraveler", "Pen Drive Kingston DataTraveler USB 3.0 32GB", "Periferico", "DT100G3", "Kingston", "38.71", "20"]]
lista = lista + [["9", "Calculadora Vinik", "Calculadora Científica Vinik 10 + 2 Dígitos 240 Funções CC20 - 26096 Preta", "Eletronico", "26096", "Vinik", "18.71", "30"]]
lista = lista + [["10", "SSD WD", "SSD WD Green, 240GB, SATA, Leitura 545MB / s, Gravação 465MB / s", "SSD", "WDS240G2G0A", "Western Digital", "246.94", "7"]]


#
client = Client(wsdl='http://localhost:54202/WebService.asmx?wsdl')
for i in lista:
    cadastroDeProduto = ('{"id":'+str(i[0])+
                           ', "nome":"'+str(i[1])+
                           '", "descricao":"'+str(i[2])+
                           '", "categoria":"'+str(i[3])+
                           '", "modelo":"'+str(i[4])+
                           '", "marca":"'+str(i[5])+
                           '", "valor":'+str(i[6])+
                           ', "quantidade":'+str(i[7])+'}')
    #print(cadastroDeProduto)
    produtoCadastro = json.loads(cadastroDeProduto)
    x = client.service.addProdut(cadastroDeProduto)
    #print('\n',x,'\n')
    #print(produtoCadastro)



#print(lista)
#print(lista)
