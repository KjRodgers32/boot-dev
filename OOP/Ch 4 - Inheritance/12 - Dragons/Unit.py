class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    def in_area(self, x_1, x_2, y_1, y_2):
        return (x_1 <= self.pos_x and x_2 >= self.pos_x) and (y_1 <= self.pos_y and y_2 >= self.pos_y)

class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range
    
    def breathe_fire(self, x, y, units):
        in_area = []
        for unit in units:
            if unit.in_area(x - self.__fire_range, x + self.__fire_range, y - self.__fire_range, y + self.__fire_range):
                in_area.append(unit)
        return in_area