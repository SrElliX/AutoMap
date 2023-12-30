import os
import subprocess
import sys

os.system('clear')

# Códigos ANSI para cores
RED = '\033[91m'
RESET = '\033[0m'

texts = [
    '   _          _         __  __',
    r'  /_\   _  _ | |_  ___ |  \/  | __ _  _ __',
    r" / _ \ | || ||  _|/ _ \| |\/| |/ _` || '_ |",
    r'/_/ \_\ \_,_| \__|\___/|_|  |_|\__,_|| .__|',
    '                                     |_|'
]

for text in texts:
    print(f'{RED}{text}{RESET}')


def run_nmap(ip, scan_options):
    try:
        # Construa o comando nmap com base nas opções fornecidas
        command = ['nmap'] + scan_options + [ip]

        # Execute o comando nmap
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        # Imprime uma mensagem de carregamento antes do loop
        print("Aguarde enquanto o Nmap está sendo executado...")

        # Use um loop para ler e imprimir as linhas à medida que são geradas
        while True:
            line = process.stdout.readline()
            if not line:
                break

            # Imprime a linha sem pular uma linha para atualizar na mesma linha
            sys.stdout.write(line)
            sys.stdout.flush()

        process.stdout.close()
        process.wait()

        while True:
            # Solicita ao usuário opções para filtrar a saída
            print("\nOpções de filtragem:")
            print("[1] Filtrar por serviços e portas")
            print("[2] Filtrar por uma porta específica")
            print("[S] Sair")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                # Filtrar por serviços e portas
                services_ports = input("Digite os serviços/portas separados por espaço: ")
                for line in result.stdout.splitlines():
                    if any(service_port in line for service_port in services_ports.split()):
                        print(line)

            elif choice == '2':
                # Filtrar por uma porta específica
                specific_port = input("Digite a porta específica: ")
                for line in result.stdout.splitlines():
                    if f"{specific_port}/" in line:
                        print(line)

            elif choice.upper() == 'S':
                # Sair do programa
                print("Saindo do programa.")
                exit()

            else:
                print("Opção inválida.")

    except Exception as e:
        print(f"\nErro ao executar o nmap: {e}")

def main():
    # Solicita ao usuário o IP a ser varrido
    ip = input("\nDigite o IP ou a faixa de IP a ser varrida: ")

    while True:
        # Solicita ao usuário as opções de varredura
        print("\nEscolha as opções de varredura (separadas por espaço):")
        print("Exemplo: -sS -p 1-1000 -A")
        scan_options = input("Opções: ").split()

        # Executa o nmap com base nas escolhas do usuário
        run_nmap(ip, scan_options)

if __name__ == "__main__":
    main()
