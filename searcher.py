import sys
class Gsearch_python:
   def __init__(self,name_search):
       self.name = '"' + name_search + '" ext:pdf'
   def Gsearch(self):
      count = 0
      try :
         from googlesearch import search
      except ImportError:
         print("No Module named 'google' Found")
      for i in search(query=self.name,tld='co.in',lang='fr',num=100,stop=100,pause=2):
         count += 1
         print (count)
         print(i + '\n')
if __name__=='__main__':
   gs = Gsearch_python(input(">"))
   gs.Gsearch()
