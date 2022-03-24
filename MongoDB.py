from pymongo import MongoClient
import json

class MongoDB():
    def set_database(self):
        conection="mongodb+srv://AngelVargas2003:Angel2003@basesdedatosenlanube.fsnez.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        client=MongoClient(conection)
        self.db=client['Sensores']
        self.collection=self.db['SensoresRegister']
    def insertar(self,listadicc):
        try:
            self.set_database()
            self.collection.insert_one(listadicc)
        except:
            print("No hay internet")

    def getSensores(self):
        self.set_database()
        result=self.collection.find()
        return result
    