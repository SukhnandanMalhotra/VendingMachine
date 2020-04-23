class Product:
    def __init__(self,name,price,qty):
        self.name = name
        self.price = price
        self.qty = qty
    

class VendingMachine:
    money =(1,5,10,25)

    def __init__(self):
        self.total =0
        self.products=[]
        
    def reset(self,val):
        for i in self.products:
              i.qty = val
              
    def add_product(self,item):
        self.products.append(item)

    def display(self):
        print('Following are the items available : \n')

        for item in self.products:
            if item.qty ==0:
                self.products.remove(item)
        print('Item', 'Price', 'Quantity')
        for item in self.products:
            print(item.name,item.price,item.qty)
            
    def  has_products(self,required):
        flag = False
        for item in self.products:
            if item.name == required:
                flag = True
                break
        return flag

    def get_item(self, wanted):
        a = None
        for item in self.products:
            if item.name == wanted:
                a = item
                break
        return a

    def insert_money(self,item):
        price = item.price
        while self.total < price:
            print('insert :'+ str(price - self.total) )
            coin = int(input())
            if coin not in self.money:
                print('The machine accepts only: {}.'.format(self.money), end=' ')
            else:
                self.total += coin

    def buy_product(self, item):
        if self.total < item.price:
            print('You can\'t but this item. Insert more coins.')
        else:
            self.total -= item.price
            item.qty-=1
            print('You got ' +item.name)
            print('Cash remaining: ' + str(self.total))

    def change(self):
        if self.total > 0:
            print('Your Change :' +str(self.total))
            self.total = 0

        print('Thank you, have a nice day!\n')


def vending():
    vm = VendingMachine()
    item1 = Product('Coke',25,10)
    item2 = Product('Pepsi',35,10)
    item3 = Product('Soda',45,10)
    vm.add_product(item1)
    vm.add_product(item2)
    vm.add_product(item3)

    while True:
        print('Welcome to the vending machine!')
        print('Choose an Action: ')
        print('1 : Purchase')
        print('2 : Reset')
        action = int(input())
        if action ==1:
            purchase = True
            while purchase == True:
                vm.display()
                sel = input('Enter product name: ')
                if vm.has_products(sel):
                    item = vm.get_item(sel)
                    vm.insert_money(item)
                    vm.buy_product(item)

                    a = input('Do you wish to buy something else? (y/n): ')
                    if a == 'n':
                        purchase = False
                        vm.change()
                    else:
                        continue

                else:
                    print('Item not available. Select another item.')
                    continue
        elif action == 2:
            print('Enter Stock quantity to refil: ')
            stock = int(input())
            vm.reset(stock)
            

vending()


        
            
                
    
    
        
    
    
