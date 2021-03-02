class Product(object):
    def __init__(self,name,price,size,discount):
        self.name=name
        self.price=price
        self.size=size
        self.discount=discount

    def __repr__(self):
        return repr((self.name,self.price,self.size,self.discount))

    def discountPrice(self):
        return self.price-self.price*self.discount


prodList=[
    Product("Widget",50,10,0.05),
    Product("TestProduct1",30,1,0.55),
    Product("TestProduct2",20,80,0.6),
    Product("TestProduct3",25,10,0.5),

]

print(sorted(prodList,key=lambda a:a.discountPrice(),reverse=True))