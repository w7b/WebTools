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
    async with aiohttp.ClientSession() as session:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Type': 'application/json',
        }

        async with session.get(url, headers=headers) as initial_response:
            if initial_response == 200:
                soup = BeautifulSoup(await initial_response.text(), 'html.parser')

                csrf_token = soup.find('input', {'name': 'csrf_token'})
                if csrf_token:
                    csrf_token = csrf_token['value']
                else:
                    csrf_token = ''

                data = {
                    'username': user,
                    'password': password,
                    #'csrf_token': csrf_token
                }

                async with session.post(url, data=data, headers=headers) as login_response:
                    if login_response.status == 200:
                        page_content = await login_response.text()
                        print(page_content)
                        if "dashboard" in page_content.lower():
                            print(f"\nLogin bem-sucedido para o usuário {user}")
                        else:
                            print(f"\nFalha no login para o usuário {user}")
                    elif login_response.status == 401:
                        print(f"\nErro 401: Login não autorizado para o usuário {user}. Verifique as credenciais.")
                    else:
                        print(f"\nFalha ao tentar logar. Status HTTP: {login_response.status}")
            else:
                print(f"\nErro ao acessar o site. Status HTTP: {initial_response.status}") ##VERIFICAR ##VERIFICAR ##VERIFICAR ##VERIFICAR ##VERIFICAR ##VERIFICAR ##VERIFICAR ##VERIFICAR ##VERIFICAR ##VERIFICAR ##VERIFICAR ##VERIFICAR 

            

    

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