class Product:
    def __init__(self,id,name,brand,price,net,made):
        self.id = id
        self.name =name
        self.brand = brand
        self.price = price
        self.net = net
        self.made =made

    def getInfo(self):
        return "Id:{0}, Name: {1}, Brand: {2}, Price:{3}, Net: {4} ".format(self.id,self.name,self.brand,self.price,self.net,self.made)
