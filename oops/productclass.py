class Product:
    count=0
    def __init__(self,product_name,category,description,price):
        self.product_name=product_name
        self.category=category
        self.description=description
        self.price=price
        Product.count=Product.count+1
    def display_product(self):
        # details='''
        #       name: {self.product_name}
        #       category: {self.category}
        #       description: {self.description}
        #       price: {self.price}'''
       
        # print(details)
        print('name: ',self.product_name)
        print('category: ',self.category)
        print('description: ',self.description)
        print('price: ',self.price)
        
    def product_count(self):
        print('Total number of products: %d' %Product.count)

product1=Product("pen",'stationary','ball point' ,25)
product1.display_product()
product1.product_count()


product2=Product("apple",'grocery','green ooty',120)
product2.display_product()
product2.product_count()



