#!/usr/bin/python
# -*- coding: UTF-8

from pymongo import MongoClient
import datetime

#Para realizar a conexão você tem duas opções, na primeira você indica o host e a porta, dessa forma:

cliente = MongoClient('localhost', 27017)

cliente = MongoClient('mongodb://localhost:27017/')

banco = cliente['teste-database']

musica = {
              "_id": 1,
              "nome": "Nothing lef to say",
              "banda": "Imagine Dragons",
              "categorias": ["indie", "rock"],
              "lancamento": datetime.datetime.now()
             }

#--------------------------------------------------------------------------------------------------

# Para inserir um documento em uma collection usamos o método insert_one().

album = banco.album
#musica_id = album.insert_one(musica).inserted_id

#--------------------------------------------------------------------------------------------------
# Realizando a busca


#Buscando

#print(album.find_one())

#--------------------------------------------------------------------------------------------------
# Buscando por ObjectID
#print(album.find_one({"_id": 1}))

#--------------------------------------------------------------------------------------------------
#Buscando por Nome
#print(album.find_one({"nome": "Nothing lef to say"}))

#--------------------------------------------------------------------------------------------------
# para pesquisas com mais de um item por vez

"""for musica_id in range(album.count()):
    print(album.find_one({"_id": musica_id}))"""
#--------------------------------------------------------------------------------------------------

#UPDATE
#album.update_one({'_id': 1}, {'$set': {'nome':'50Cent'}})

#--------------------------------------------------------------------------------------------------

# DELETE

#album.delete_one({"_id": 1})


#  apagar mais de um objeto

#album.delete_many({"banda": "Imagine Dragons"})
#--------------------------------------------------------------------------------------------------