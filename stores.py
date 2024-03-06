class v: #Vector
    def __init__(self,data):
        self.data = data

    def __add__(self,ndata):
        if isinstance(ndata,list): return v([n+m for n,m in zip(self,ndata)])
        return v([n+m for n,m in zip(self,ndata)])

    def __sub__(self,ndata):
        if isinstance(ndata,list): return v([n-m for n,m in zip(self,ndata)])
        return v([n-m for n,m in zip(self,ndata)])

    def __mul__(self,ndata):
        if isinstance(ndata,list): return v([n*m for n,m in zip(self,ndata)])
        return v([n*m for n,m in zip(self, ndata)])

    def __truediv__(self,ndata):
        if isinstance(ndata,list): return v([n/m for n,m in zip(self,ndata)])
        return v([n/m for n,m in zip(self, ndata)])

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def intersection(self,ndata):
        if isinstance(ndata,list): return v([n for n in ndata if n in self])
        return v([n for n in ndata if n in self])

    def union(self,ndata):
        final = self.data[:]

        for n in ndata:
            if n not in final: final.append(n)

        return v(sorted(final))

    def dot(self,ndata):
        if len(self.data) != len(ndata.data) or len(ndata) == 0:
            print('Undefined')
            return

        return sum([n*m for n,m in zip(self.data, ndata)])


class M: #Matrix
    def __init__(self,mat):
        self.mat = mat if self.ismat(mat) else None

    def __iter__(self):
        return iter(self.mat)

    def __add__(self,nmat):
        if not isinstance(nmat,M):

            if isinstance(nmat,int):
                final = self.mat
                for n in range(len(self.mat)):
                    for m in range(len(self.mat[n])):
                        final[n][m] += nmat

                return M(final)
            elif isinstance(nmat,list):
                if not len(nmat) > 0:
                    print("Nmat is empty")
                    return
                if len(self.mat[0]) > len(nmat):
                    nmat = nmat + [0]*(len(self.mat[0]) - len(nmat))
                final = []
                for n in range(len(self.mat)):
                    final.append([])
                    for m in range(len(self.mat[n])):
                        final[n].append(self.mat[n][m] + nmat[m])
                return M(final)

        final = []
        for n in range(len(self.mat)):
            final.append([])
            for m in range(len(self.mat[n])):
                final[n].append(self.mat[n][m] + nmat.mat[n][m])

        return M(final)


    def __repr__(self):
        return  "\n".join([" ".join(map(str,n)) for n in self.mat])

    def ismat(self,mat):
        if len(mat) > 1:
            mt = [True if isinstance(n,list) else False for n in mat]
            if not all(mt):
                print("Not a matrix")
                return False
        return True