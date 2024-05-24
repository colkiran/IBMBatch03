
class Player:           # pascal casing

    def get_runs(self):
        print("runs scored......")


sachin = Player()
sachin.get_runs()

print(type(sachin))
print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance(sachin, str))

