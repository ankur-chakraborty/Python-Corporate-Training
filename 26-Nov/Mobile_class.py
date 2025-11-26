class Mobile:
    def __init__(self,brand, model, storage):
        self.brand=brand
        self.model=model
        self.storage=storage

    def upgrade_storage(self, new_storage):
        self.storage=new_storage+self.storage

    def display(self):
        print(self.brand)
        print(self.model)
        print(self.storage)

m=Mobile("Apple","iPhone",128)
m.upgrade_storage(256)
m.display()