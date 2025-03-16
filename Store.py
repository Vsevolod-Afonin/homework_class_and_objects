class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}
    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f' товар {item_name} был добавлен в {self.name}')

    def remove_item(self, item_name):
        if item_name in self.name:
            del self.items[item_name]
            print(f' товар {item_name} удалён из {self.name}')

    def get_price(self, item_name):
        if item_name in self.name:
            return self.items.get(item_name)
        else:
            print(f'Товара {item_name} нет в наличии!')

    def update_price(self, item_name, price):
        if item_name in self.name:
            self.items.update({item_name:price})
            print(f'Цена на товар {item_name} была обновлена')
        else:
            print(f'Товара {item_name} нет в наличии!')

    def  show_items(self):
        print('Товары в наличии')
        print(self.items)

s1 = Store('Sportmaster', 'ТРЦ Волна')

s1.add_item('Boots', 14000)
s1.add_item('Jacket', 18000)
s1.add_item('Ball', 3000)

s1.show_items()

s1.remove_item('Jacket')


s1.show_items()