#positional Arguement
def positional(ram,shyam,harish):
	print(ram,shyam,harish)
a='Ram'
b='Shyam'
c='Harish'
positional(a,b,c)
#Keyword Arguement
def Keyword(ram,shyam,harish):
	print(ram,shyam,harish)
a='Ram'
b='Shyam'
c='Harish'
positional(ram=a,harish=c,shyam=b)
#Default Arguement
def Keyword(ram,shyam,harish='harish'):
	print(ram,shyam,harish)
a='Ram'
b='Shyam'
Keyword(ram=a,shyam=b)
