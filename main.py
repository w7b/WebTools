# from selenium import webdriver 
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import aiohttp
import json
import os
import asyncio

os.system('cls')
async def main_menu():
    while True:

        print("__________________\n")
        print("- MASS LOGIN TOOL")
        print("- [1] AUTO LOGIN")
        print("- [2] AUTO REGISTER")
        print("- [3] SCRAP ELEMENT")
        print("- [4] EXIT SCRIPT")
        print("__________________")

        select_a = input("\n- Select: ")

        if select_a == '1':
            await s_menu1()
        elif select_a == '2':
            await s_menu2()
        elif select_a == '3':
            await s_menu3()
        elif select_a == '4':
            print("Exit")
            break
        else:
            print("Error, option invalid!")

async def read_acc(path):
        with open(path, 'r') as file:
            accounts = [line.strip().split('|') for line in file.readlines()]
        return accounts 

async def global_login(url, user, password):
    data = {
        'username_field': user,
        'password_field': password
    }
#Retornando 200 mesmo não dando login, verificar isso

async def s_menu1():
    while True:
        print("__________________")
        print("- MASS LOGIN TOOL")
        print("- [1] START AUTO LOGIN")
        print("- [2] RETURN")
        print("__________________")

        select_b = input("\n- Select: ")

        if select_b == '1':
            print("__________________")
            # PREENCHA A INFORMAÇÕES ABAIXO
            url = input("\nPlace URL Here: ")
            print("__________________")
            read_acc_path = 'acc.txt'

            accounts = await read_acc(read_acc_path)

            logins = [global_login(url, user, password) for user, password in accounts]
            
            await asyncio.gather(*logins)

        elif select_b == '2':
            os.system('cls')
            return
        else:
            print("Error, option invalid!")


async def s_menu2():
    print("")


async def s_menu3():
    print("Oi")

asyncio.run(main_menu())
os.system('cls') ##APAGAR APOS SCRIPT FICAR PRONTO