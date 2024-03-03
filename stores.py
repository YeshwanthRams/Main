class v:
    def __init__(self,data):
        self.data = data 

    def __add__(self,ndata):
        return v([n+m for n,m in zip(self.data,ndata.data)])
    
    def __sub__(self,ndata):
        return v([n-m for n,m in zip(self.data,ndata.data)])

    def __mul__(self,ndata):
        return v([n*m for n,m in zip(self.data, ndata.data)])
    
    def __iter__(self):
        return iter(self.data)
    
    def intersection(self,ndata):
        return v([n for n in self.data if n in ndata.data] + [n for n in ndata.data if n in self.data])

    def union(self,ndata):
        one = [n for n in self.data]
        two  = [n for n in ndata.data if n not in one]

        return v(one + two)
