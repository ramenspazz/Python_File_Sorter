import os 



Audio_EXT = ['.aif', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg',
             '.wav', '.mwa', '.wpl'],

Documents_EXT = ['.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.txt',
                 '.wks', '.wps', '.wpd', '.ods', '.xlr', '.xls', '.xlsx', '.key', '.odp',
                 '.pps', '.ppt', '.pptx', '.csv', '.dat', '.db', '.dbf', '.log', '.mdb',
                 '.sav', '.sql', '.tar', '.xml', '.html'],

Picture_EXT = ['.ai', '.bmp', '.gif', '.ico', '.jpeg', '.jpg', '.png',
               '.ps', '.psd', '.svg', '.tif', '.tiff'],

Video_EXT = ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv',
             '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv'],

Program_EXT = ['.apk', '.bat', '.bin', '.cgi', '.pl', '.com', '.exe',
               '.gadget', '.jar', '.py', '.wsf', '.iso']

    

class sorting_hat:
    def __init__(self, foo = None, slist = None):
        self.flist = None 
        self.sort_mtd = foo
        self.sort_list = slist
        self.f_arr = None
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
            for i in range(j,len(self.sort_list)):
                if len(self.sort_list) == i + j + 1:
                    break         
                if i == j:
                    continue
                if self.sort_mtd(self.sort_list[i+j], self.sort_list[i+j+1]):
                    print("{:d}, {:d}".format(i,j))
                    self.n = self.n + 1
                    temp = self.sort_list[i+j]
                    self.sort_list[i+j] = self.sort_list[i+j+1]
                    self.sort_list[i+j+1] = temp
                    return()
                        #swap 2 elements
        raise StopIteration

    def browse_dir(self):
        usr_in = None
        while usr_in != 'q':
            if usr_in == 'l':
                self.sort_list = os.listdir()
            elif not (usr_in == None) and not (usr_in == 'q'):
                os.chdir(usr_in) 
            print(os.getcwd())
            usr_in = input("Enter a direrctory \n ") 

    def sort_file_type(self):
        self.sort_mtd = lambda a,b: (a.split("."))[-1][0] > (b.split("."))[-1][0]


Harry = sorting_hat(foo = lambda a, b : a[0] > b[0], slist = ['zharry','jon','linda', 'barak obama', 'jesus' ,'matthew piazza'])

for val in Harry:
    pass
    
Harry.p_list()

Harry.browse_dir()

Harry.sort_file_type()

for val in Harry:
    pass

Harry.p_list()
