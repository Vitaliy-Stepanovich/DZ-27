class ProductExpert:
    """Товаровед"""
    def __init__(self):
      self.products = {}
      self.sales = Sale()
      
    def add_product(self, name, price, count):
        self.products[name] = Product(name, price, count)
      
    def update_products(self, order):
      for product, count in order.order.items():
        self.products[product].count -= count
        
    def reg_sale(self, order):
      if not order.order:
        return
      
      if self.check_order(order):
         self.sales.add_sale(order)
         self.update_products(order)
      else:
        print('Покупка отменена')
        
    def check_order(self, order):
      for product, count in order.order.items():
        if product not in self.products:
          print(f'Товара {product} нет у товароведа, покупку нельзя совершить!')
          return False
        elif count > self.products[product].count:
               print(f'У товароведа позиции {product} в наличие {self.products[product].count}, а запрошено {count}')
               return False
      return True         
       
    def show_products(self):
      print('Список продуктов: ')
      for product in self.products:
        print(product)
        
    def show_sales(self):
          print(self.sales)

class Product(ProductExpert):
    """Товар"""
    
    def __init__(self, name, price, count):
      self.name = name
      self.price = price
      self.count = count
      print(f'--{name}, цена {price} руб.')
      
    def __repr__(self):
      return self.name

class Client:
    """Клиент"""
    def __init__(self, product_expert: ProductExpert):
      self.product_expert = product_expert
      
    def make_order(self):
      order = Order()
      print()
      ans = input('Что покупаем и в каком колличестве через пробел (Пример: хлеб 1), "q" - завершить покупку: ')
      
      while ans != 'q':
        position, count = ans.split()
        order.add_position(position.lower(), int(count))
        ans = input('Что покупаем и в каком колличестве через пробел, "q" - завершить покупку: ')
        
      self.product_expert.reg_sale(order)
      

class Order:
    """Заказ"""
    def __init__(self):
      self.order = {}
      
    def add_position(self, name, count):
      self.order[name] = count
      
    def __repr__(self):
      return f'{self.order}'
      
    def __str__(self):
      return f'{self.order}'


class Sale:
    """Список продаж"""
    def __init__(self):
      self.sales = []
      
    def add_sale(self, order):
      self.sales.append(order)
      
    def __str__(self):
      return ' '.join(str(order) for order in self.sales)


def main():
    prod_exp = ProductExpert()
    client = Client(prod_exp)
    
    prod_exp.add_product('хлеб', 30, 20)
    prod_exp.add_product('шоколад', 67, 30)
    prod_exp.add_product('вода', 20, 100)
    prod_exp.add_product('пельмени', 90, 15)
    
    client.make_order()
    
    # prod_exp.show_products()
    prod_exp.show_sales()
    
    
if __name__ == '__main__':
    main()
