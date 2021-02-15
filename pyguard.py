from sys import argv
from os import getcwd,path
from subprocess import Popen as run
from subprocess import PIPE
from keyboard import is_pressed
from colorama import Fore,init
from time import sleep

init()

def pyguard(file):
    if not path.exists(getcwd()+"/"+file):
       print(Fore.RED+"[-] cant find file"+Fore.WHITE)
       return 
    a=run(f"python {getcwd()}/{file}")
    while 1:
        sleep(0.1)
        if is_pressed("ctrl+c"):
            run.kill(a)
        if is_pressed("ctrl+s"):
            run.kill(a)
            print(Fore.GREEN+"[+] restarting script"+Fore.WHITE)
            a=run(f"python {getcwd()}/{file}")
            sleep(0.1)


        
if __name__=="__main__":
   if len(argv) == 1:
      print(Fore.GREEN+"pyguard is a auto starter for python scripts")
      print(Fore.GREEN+"usage : pyguard [python-file-name]")
      print(Fore.RED+"\n[tip] press twice ctrl+s for restart" +Fore.WHITE+" \U0001F60E")
      print(Fore.GREEN+"\nif you like that you can follow my github account for more useful codes"+Fore.WHITE+" \U0001F60D	")
      print(Fore.GREEN+"https://www.github.com/kaankarakoc42"+Fore.WHITE)
      exit()
   try:
    print(Fore.GREEN+"[+] pyguard has been started"+Fore.WHITE)
    print(Fore.GREEN+"[+] running script"+Fore.WHITE)
    if argv[1].endswith(".py"): 
       pyguard(argv[1])
    else:
       pyguard(argv[1]+".py")
   except:
    sleep(0.2)
    print("\n"+Fore.RED+"[-] app has been shutdown"+Fore.WHITE+"\n")