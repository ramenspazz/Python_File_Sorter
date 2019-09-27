import androidhelper
droid = androidhelper.Android()
droid.makeToast('Hello, Android!')
print('\n\nHello, waiting for more...\n')


class sorting_hat:
    def __init__(self, foo = None, slist = None):
        self.sort_mtd = foo
        self.sort_list = slist
    def __iter__(self):
        self.n = 0
        return(self)
    def p_list(self):
        print(self.sort_list)
    def __next__(self):
        if self.sort_mtd == None:
            print("please give function first!\n")
            raise StopIteration
        for j in range(0,len(self.sort_list)):
            for i in range(0,len(self.sort_list)-j):
                if len(self.sort_list) == i + j + 1:
                    break         
                if self.sort_list[i+j] > self.sort_list[i+j+1]:
                    self.n = self.n + 1
                    temp = self.sort_list[i+j]
                    self.sort_list[i+j] = self.sort_list[i+j+1]
                    self.sort_list[i+j+1] = temp
                    return(i)
                        #swap 2 elements
        raise StopIteration
        
                        
Harry = sorting_hat(foo = None, slist = [2,5,7,3,9,3,7,1,5,4,7])

for dick in Harry:
    print(dick)
    
Harry. p_list()
