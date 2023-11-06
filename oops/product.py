class Product:
    product_name='pen'
    category='stationary'
    description = 'ball point black'
    price = 50
    
    
    def display_product(self):
        print('display product details')
        print('product name: ',self.product_name)
        print('category: ',self.category)
        print('description: ',self.description)
        print('price: ',self.price)
        
product1=Product()
product1.display_product()