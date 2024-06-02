#----------Import -------------------#
import os
import test
import random
import requests
from concurrent.futures import ThreadPoolExecutor as tred

os.system('clear')
logo = ("""
\33[1;92m
▬ \33[1;92m███████ ██    ██ ██   ██  █████       \033[33;1m▬▬▬▬▬▬▬\33[1;92m
▬ \33[1;92m██      ██    ██ ██   ██ ██   ██      \033[33;1m█ V : 0.1 █\33[1;92m
▬ \33[1;92m███████ ██    ██ ███████ ███████ 
▬ \33[1;92m     ██ ██    ██ ██   ██ ██   ██ 
▬ \33[1;92m███████  ██████  ██   ██ ██   ██ 
▬\033[1;92m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;37m
\033[1;97m Owner   :            MD JAKARIA FIAD      █    
\033[1;32m Facebook:            MD JAKARIA FIAD      █
\033[1;97m Github  :            phinerx              █
\033[1;32m Whatsapp:            (Personal)           █
\033[1;97m Tool    :            FB DUMP              █
\033[1;32m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;37m""")
def main():
    pass
    print(logo)
    print("[A]Method 1{need login}")
    print("[B]Method 2 {No need Login}(Slow)")
    print("[C]Method 3 {No need Login}(Fast)")
    print("[D]Admin info")
    print("[X]Exit")
    cho = input("Choice : ")
    #------All File------#
    def mainx():
        file_path = input("Enter the file path where the results will be saved: ")
        axo = int(input("How much: "))
        with tred(max_workers=30) as xxxx:
            xxxx.submit(au, file_path, axo)
    def runxo():
        os.system("git clone https://github.com/phinerx/FB_DUMP")
        os.system("cd FB_DUMP")
        os.system("python fire-dump.py")
    def m1():
        pass
    def m2():
        os.system('clear')
        mainx()
    def m3():
        runxo()
    if cho in ("A","a"):
        m1()
    elif cho in ("B","b"):
        m2()
    elif cho in ("C","c"):
        m3()
    elif cho in ("X","x","0"," ",""):
        os.system("exit")
    else:
        print("Choice a Right option")
        main()
if __name__== "__main__":
    main()
