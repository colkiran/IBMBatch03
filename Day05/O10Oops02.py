
class Player:

    def __init__(self):          # constructor
        print("Player initialized......")

    def get_runs(self):
        print("runs scored......")

sachin = Player()
sehwag = Player()
sachin.__init__()
print("-" * 60)
sachin.get_runs()
sehwag.get_runs()
