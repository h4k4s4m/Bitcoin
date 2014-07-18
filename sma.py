class SimpleMovingAverage():

    def set(self, navg, items):
        self.navg = navg
        self.items = items

    def calculate(self):
        av = []
        for i in range(len(self.items)):
            if i+1 < self.navg:
                av.append(0)
            else:
                av.append(round(sum(self.items[i+1-self.navg:i+1])/self.navg , 2))
        return av

