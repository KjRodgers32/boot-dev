class Wall:
    armor = 10
    height = 5
    
    def fortify(self):
        self.armor *= 2

black_wall = Wall()

print(black_wall.armor)
black_wall.fortify()
print(black_wall.armor)

