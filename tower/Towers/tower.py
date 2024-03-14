class Tower:
    def __init__(self, x, y, width, height, price, imgs, range, damage, upgrade_cost, menu, selected: bool = False, sell_price: int = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.price = price
        self.imgs = imgs
        self.range = range
        self.damage = damage
        self.selected = False
        self.animation_count = 0
        self.img = imgs[0]

    def draw(self):
        pass

    def move(self):
        pass

    def click(self, x, y):
        pass

    def upgrade(self):
        pass

    def sell(self):
        pass
    