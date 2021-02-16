from sys import argv
from os import getcwd,path,remove
from subprocess import Popen,PIPE,run
from keyboard import is_pressed
from colorama import Fore,init
from time import sleep

init()

class pyguard:
   def __init__(self):
       self.selections={"python":"py","javascript":"js","c++":"cpp"}
       self.runtimes={"py":"python","js":"node","cpp":"g++"}
       self.selected=self.selections["python"]
       self.run=None
       self.proccess=None
       self.parse()

   def parse(self):
       if len(argv) > 1:
          if len(argv[1].split("."))>1:
             if argv[1].split(".")[1]!=self.selected:
                if argv[1].split(".")[1] in self.selections.values():
                   self.selected=argv[1].split(".")[1]
                   self.listen(argv[1].split(".")[0]+"."+self.selected)
                else:
                   return print(Fore.RED+"[-] you cant use that extension"+Fore.WHITE)
             else:
                self.listen(argv[1])
          else:
             self.listen(argv[1]+"."+self.selected)
       else:
          return print(details)
   

   def runFile(self,file):
       if self.proccess:
          Popen.kill(self.proccess)
       if not path.exists(getcwd()+"/"+file):
          print(Fore.RED+"[-] cant find file"+Fore.WHITE)
          exit()
       self.run(file)
       sleep(0.1)

   def runScript(self,file):
       self.proccess=Popen(f'{self.runtimes[self.selected]} "{getcwd()}/{file}"')
   
   def runCpp(self,file):
       if self.proccess:
          Popen.kill(self.proccess)
       if path.exists(f"{getcwd()}/"+file.split(".")[0]+".exe"):
          remove(f"{getcwd()}/"+file.split(".")[0]+".exe")
       self.proccess=Popen(f'{self.runtimes[self.selected]} "{getcwd()}/{file}" -o "{getcwd()}/{file.split(".")[0]}.exe"')
       while not path.exists(f"{getcwd()}/"+file.split(".")[0]+".exe"):
             pass
       sleep(0.1)
       Popen.kill(self.proccess)
       self.proccess=Popen(f'"{getcwd()}/{file.split(".")[0]}.exe"')
   
   def runTimeExists(self,file):
       if not self.runtimes[file.split(".")[1]] in run(["path"], capture_output=True, text=True,shell=True).stdout:
          if self.runtimes[file.split(".")[1]]=="g++" and "mingw" in run(["path"], capture_output=True, text=True,shell=True).stdout:
             pass
          else:
             print(Fore.RED+"[-] you dont have "+{self.runtimes[file.split(".")[1]]}+" runTime please install"+Fore.WHITE)
             exit()

       

   def listen(self,file):
       print(Fore.GREEN+f"[+] starting {file}"+Fore.WHITE)
       self.runTimeExists(file)
       if self.selected != "cpp":
          self.run=self.runScript
       else:
          self.run=self.runCpp
       self.runFile(file)
       while 1:
         sleep(0.1)
         if is_pressed("ctrl+c"):
             Popen.kill(self.proccess)
         if is_pressed("ctrl+s"):
             print(Fore.GREEN+"[+] restarting script"+Fore.WHITE)
             self.runFile(file)



def main():
    try:
      pyguard()
    except KeyboardInterrupt:
      print(Fore.RED+"[-] session closed"+Fore.WHITE)


details="""
pyguard42

version: 0.0.5
author: Mevlüt Kaan Karakoç
github: https://www.github.com/kaankarakoc42/pyguard42
pypi: https://pypi.org/user/kaankarakoc42/pyguard42

usage: pyguard [file-name]
suported-langs: [python,javascript,c++]
suported-extensions: [.py,.js,.cpp]


tips: press ctrl+s twice for auto-restart program
"""

if __name__=="__main__":  
   main()
