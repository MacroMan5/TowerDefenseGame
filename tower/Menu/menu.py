class Menu:
    def __init__(self, pos_x: int, pos_y: int, width: int, height: int, bg_img, buttons, title):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.bg_img = bg_img
        self.buttons = buttons
        self.title = title
       

    def draw(self):
        pass

    def get_choice(self):
        pass