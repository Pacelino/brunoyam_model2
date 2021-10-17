class StringVar:
    def __init__(self):
         self.s = ''
    def set (self, val):
        self.s = val


    def get (self):
        return self.s


s = StringVar()
s.set('я люблю python')
print(s.get())