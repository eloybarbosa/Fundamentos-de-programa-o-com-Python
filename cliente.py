"""Projeto de Bloco - Arquitetura de Computadores, Sistemas Operacionais e Redes - TP9"""
"""Grupo - Eloy Barbosa , Victor Manuel, Henrique Francisco"""

import socket
import pickle
import time
import os
import datetime


def cliente_tcp():
    try: 
        host = socket.gethostname() 
        port = 35432 
        socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        socket_tcp.connect((host, port)) 
    except Exception: 
        raise Exception

    return socket_tcp

def menu_principal():
    while True:
        print()
        print('{:>60}'.format('SMRP - Sistema de Monitoramento Remoto em Python'))
        print()
        print('{:>45}'.format('MENU PRINCIPAL'))
        print()
        print('1. Uso de memória')
        print('2. Uso de disco')
        print('3. Informações de CPU')
        print('4. Informações sobre diretórios')
        print('5. Informações de processos')
        print('6. Informações de redes')
        print('0. Sair')
        print()
        print('Maquina de onde as informações estão sendo capturadas (servidor):', socket.gethostname(), '(',socket.gethostbyname(socket.gethostname()),')')
        print()

        sair = False
        
        while True:
            try:
                opcao = int(input('Insira a opção desejada: '))
                print()
            except:
                print('Insira um número válido.')
                continue

            if(opcao == 1):
                loop_info_memoria()
                input('\nPressione Enter para voltar ao menu... ')
                os.system("cls")
                break
            elif(opcao == 2):
                pdisco = get_data('disco')
                if pdisco == None:
                    break
                imprimir_uso_disco(pdisco)
                input('\nPressione Enter para voltar ao menu... ')
                os.system("cls")
                break
            elif(opcao == 3):
                os.system("cls")
                menu_cpu()
                break
            elif(opcao == 4):
                navegar_diretorio()
                break
            elif(opcao == 5):
                processos = get_data('processos')
                if processos == None:
                    break
                imprimir_processos(processos)
                input('\nPressione Enter para voltar ao menu... ')
                os.system("cls")
                break
            elif(opcao == 6):
                os.system("cls")
                menu_rede()
                break

            elif(opcao == 0):
                print('Fechando a aplicação...')
                sair = True
                break
            else:
                print('Opção inválida!')
            
        if sair: break
            
def menu_cpu():
    while True:
        print()
        print('{:>60}'.format('SMRP - Sistema de Monitoramento Remoto em Python'))
        print()
        print('{:>45}'.format('INFORMAÇÕES DE CPU'))
        print()
        print('1. Nome e modelo')
        print('2. Arquitetura')
        print('3. Palavra do processador')
        print('4. Frequência')
        print('5. Núcleos')
        print('6. Uso de CPU')
        print('7. Sumário das informações')
        print('0. Voltar')
        print()

        voltar = False
       
        while True:
            try:
                opcao = int(input('Insira a opção desejada: '))
                print()
            except:
                print('Insira uma opção válida.\n')
                continue

            if(opcao == 1):
                info_cpu = get_data('cpu')
                if info_cpu == None:
                    break
                imprimir_modelo_cpu(info_cpu['modelo'])
                input('\nPressione Enter para voltar ao menu... ')
                os.system("cls")
                break
            elif(opcao == 2):
                info_cpu = get_data('cpu')
                if info_cpu == None:
                    break
                imprimir_arq_cpu(info_cpu['arquitetura'])
                input('\nPressione Enter para voltar ao menu... ')
                os.system("cls")
                break
            elif(opcao == 3):
                info_cpu = get_data('cpu')
                if info_cpu == None:
                    break
                imprimir_palavra_cpu(info_cpu['palavra'])
                input('\nPressione Enter para voltar ao menu... ')
                os.system("cls")
                break
            elif(opcao == 4):
                info_cpu = get_data('cpu')
                if info_cpu == None:
                    break
                imprimir_freq_cpu(info_cpu['frequencia'])
                input('\nPressione Enter para voltar ao menu... ')
                os.system("cls")
                break
            elif(opcao == 5):
                info_cpu = get_data('cpu')
                if info_cpu == None:
                    break
                imprimir_nucleos_cpu(info_cpu['nucleos'], info_cpu['nucleos_fisicos'])
                input('\nPressione Enter para voltar ao menu... ')
                os.system("cls")
                break
            elif(opcao == 6):
                info_cpu = get_data('cpu')
                if info_cpu == None:
                    break
                imprimir_uso_cpu(info_cpu['pcpu'])
                input('\nPressione Enter para voltar ao menu... ')
                os.system("cls")
                break
            elif(opcao == 7):
                info_cpu = get_data('cpu')
                if info_cpu == None:
                    break
                imprimir_info_cpu(info_cpu)
                info_cpu = get_data('cpu')
                input('\nPressione Enter para voltar ao menu...')
                os.system("cls")
                break
            elif(opcao == 0):
                voltar = True
                os.system("cls")
                break
            else:
                print('Opção inválida!\n')
                
        if voltar: break
        
def menu_rede():
    
    while True:
        print()
        print('{:>60}'.format('SMRP - Sistema de Monitoramento Remoto em Python'))
        print()
        print('{:>45}'.format('INFORMAÇÕES DE REDE'))
        print()
        print('1. Interfaces Disponíveis')
        print('2. Hosts disponíveis na sub-rede')
        print('3. Verificação de portas abertas no host')
        print('0. Voltar')
        print()

        voltar = False
       
        while True:
            try:
                opcao = int(input('Insira a opção desejada: '))
                print()
            except:
                print('Insira uma opção válida.\n')
                continue

            if(opcao == 1):
                info_redes = get_data('rede')
                if info_redes == None:
                    break
                imprimir_info_redes(info_redes)
                input('\nPressione Enter para voltar ao menu... ')
                os.system("cls")
                break
            elif(opcao == 2):
                print('Mapeando favor aguardar...')
                info_host = get_data('hosts')
                if info_host == None:
                    break
                imprimir_host_disponiveis(info_host)
                input('\nPressione Enter para voltar ao menu... ')
                os.system("cls")
                break
            elif(opcao == 3):
                info_port()
                input('\nPressione Enter para voltar ao menu... ')
                os.system("cls")
                break       
            elif(opcao == 0):
                voltar = True
                os.system("cls")
                break
            else:
                print('Opção inválida!\n')
                
        if voltar: break
        
def imprimir_info_port(info_port):
    print('\nHost mapeado: {}\nTipo de Protocolo: {} \nPortas abertas: {}\n'.format(info_port[0], info_port[1], info_port[2]))
    
        
def info_port():
    host = input('Informe o host para verificar a porta: ')
    print('\nMapeando portas do host informado, aguarde...\n')
    info_port = get_data('ports' + host)
     
    if info_port == None:
        print('Não foi possível mapear o host')
        return
    imprimir_info_port(info_port)
    
    
                        
def imprimir_host_disponiveis(info_host):
    qtd_host = len(info_host)
    subrede_split = (info_host[0]).split('.')
    subrede = ".".join(subrede_split[0:3]) + '.x'
    print('Foram encontrados {} Hosts na sub-rede: {}'.format(qtd_host, subrede), end='\n\n')
    for i in range (0, qtd_host):
        print (i+1, '-', info_host[i])   

def imprimir_uso_memoria(porcentagem):
    print("Porcentagem de uso de memória em tempo real: {}%".format(porcentagem), end='\r')
    print()

def loop_info_memoria():
    while True:
        porcentagem = get_data('memoria')
        if porcentagem == None:
            return
        for i in range (5):
            imprimir_uso_memoria(porcentagem)
            time.sleep(0.5)
        print()
        break
        
def imprimir_uso_disco(pdisco):
    print("Porcentagem de uso de disco: {}%".format(pdisco))

def imprimir_diretorio(data):
    print('{:<30}'.format('Nome'), end='')
    print('{:<9}'.format('Tipo'), end='')
    print('{:<13}'.format('Tamanho'), end='')
    print('{:<23}'.format('Criacao'), end='')
    print('{:<23}'.format('Modificação'), end='')
    print('{:<35}'.format('Caminho Absoluto'), end='')
    print()
    for arq in data:
        print('{:<30}'.format(arq['nome']), end='')
        print('{:<9}'.format('Pasta' if arq['tamanho'] == 0 else 'Arquivo'), end='')
        print('{:<13}'.format('' if arq['tamanho'] == 0 else formatar_tamanho(arq['tamanho'])), end='')
        print('{:<23}'.format(datetime.datetime.fromtimestamp(arq['Criação']).strftime('%Y-%m-%d %H:%M:%S')), end='')
        print('{:<23}'.format(datetime.datetime.fromtimestamp(arq['Modificação']).strftime('%Y-%m-%d %H:%M:%S')), end='')
        print('{:<35}'.format(arq['abspath']), end='')
        print()
                        
def formatar_tamanho(tamanho):
    tamanho_formatado = ''
    tamanho = int(round(tamanho/1024))
    tamanho_formatado = str(tamanho) + 'KB'
    return tamanho_formatado
    
    

def navegar_diretorio():
    input('Abaixo será mostrada informações sobre diretorio em que o "servidor" está sendo executado.\nPressione Enter para continuar...\n')
    info_diretorio = get_data('diretorio ')
    if info_diretorio == None:
        print('Não foi possível listar o diretório, tente novamente.')
        return
    imprimir_diretorio(info_diretorio)
    input('\nPressione Enter para voltar ao menu... ')
    os.system("cls")

def imprimir_processos(processos):
    print('{:<6}'.format('PID'), end='')
    print('{:<30}'.format('Nome'), end='')
    print('{:<30}'.format('Usuário'), end='')
    print('{:<25}'.format('Uso de memória'), end='')
    print('{:<25}'.format('Uso de Processamento'), end='')
    print()
    for p in processos:
        pid = p['pid']
        nome = p['name']
        usuario = '--' if p['username'] == None else p['username']
        memory_percent = p['memory_percent']
        cpu_percent = p['cpu_percent']
        print('{:<6}'.format(pid), end='')
        print('{:<30}'.format(nome), end='')
        print('{:<30}'.format(usuario), end='')
        print('{:<25}'.format(round(memory_percent, 2)), end='')
        print('{:<25}'.format(cpu_percent), end='')
        print()

def imprimir_info_redes(data):
    for interface in data:
        print('Lista de endereços da interface', interface)        
        print('{:<10}'.format('Família'), end='')
        print('{:<15}'.format('Máscara'), end='')
        print('{:<25}'.format('Endereço'), end='')
        print()
        for endereco in data[interface]:
            print('{:<10}'.format(endereco['familia']), end='')
            print('{:<15}'.format('--' if endereco['mascara'] == None else endereco['mascara']), end='')
            print('{:<25}'.format(endereco['endereco']), end='')
            print()
        print()

def imprimir_info_cpu(data):
    print()
    print('Resumo das informações:\n')
    print('{:<19}'.format('Modelo:'), data['modelo'])
    print('{:<19}'.format('Palavra:'), str(data['palavra']) + ' bits')
    print('{:<19}'.format('Arquitetura:'), data['arquitetura'])
    print('{:<19}'.format('Frequência:'), str(data['frequencia']) + 'Hz')
    print('{:<19}'.format('Nucleos (físicos):'), (str(data['nucleos']) + '(' + str(data['nucleos_fisicos']) +')'))
    print()

def imprimir_modelo_cpu(modelo):
    print('Modelo:', modelo)

def imprimir_arq_cpu(arquitetura):
    print('Arquitetura:', arquitetura)

def imprimir_palavra_cpu(palavra):
    print('Palavra:', str(palavra) + ' bits')

def imprimir_freq_cpu(frequencia):
    print('Frequência:', str(frequencia) + 'Hz')

def imprimir_nucleos_cpu(nucleos, nucleos_fisicos):
    print('Nucleos (físicos):', str(nucleos) + '(' + str(nucleos_fisicos) +')')

def imprimir_uso_cpu(pcpu):
    for n in range(1, len(pcpu)+1):
        print('Porcentagem de uso do núcleo {}:'.format(n), pcpu[n-1],'%')

def get_data(mensagem):
    data = None
    try:
        s = cliente_tcp()
        s.send(mensagem.encode('ascii'))
        b = s.recv(16000)

        data = pickle.loads(b)
    except:
        print('Não foi possível abrir uma conexão com o servidor remoto.')
    return data
    
if __name__ == '__main__':
    menu_principal()

