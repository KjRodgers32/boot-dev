class Wall:
    armor = 10
    height = 5

    def fortify(self):
        self.armor *= 2

    def get_cost(self):
        cost = self.armor * self.height
        return cost
