"""Projeto de Bloco - Arquitetura de Computadores, Sistemas Operacionais e Redes - TP9"""
"""Grupo - Eloy Barbosa , Victor Manuel, Henrique Francisco"""

import socket
import pickle
import os
import psutil
import cpuinfo
import subprocess
import platform
import nmap
import time

def servidor_tcp():
    print('SMRP - Sistema de Monitoramento Remoto em Python.(SERVIDOR)\n')
    host = socket.gethostname()
    port = 35432
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sckt.bind((host, port))
    sckt.listen()

    while True:
        aceitar_conexao(sckt)
        
    
    sckt.close()

def aceitar_conexao(s):
    (cliente, addrs) = s.accept()
    req = cliente.recv(128).decode('ascii')
    responder_cliente(cliente, req)

def responder_cliente(cliente, msg):
    data = None
    if msg == 'memoria':
        data = get_info_memoria()
    elif msg == 'disco':
        data = get_info_disco()
    elif msg == 'cpu':
        data = get_info_cpu()
    elif 'diretorio' in msg:
        dir = msg.replace('diretorio ', '')
        data = get_info_diretorio(dir)
    elif msg == 'processos':
        data = get_info_processos()
    elif msg == 'rede':
        data = get_info_rede()
    elif msg == 'hosts':
        data = get_info_hosts()
    elif 'ports' in msg:
        host = msg.replace('ports', '')
        data = get_info_port(host)

    b = pickle.dumps(data)
    cliente.send(b)
    
def get_info_port(host):
    print('\nEnviando dados sobre o host:', host)
    
    nm = nmap.PortScanner()
    nm.scan(host)
    list_port = []
    for i in nm[host].all_protocols():
        protocolo = i
    openport = nm[host][protocolo].keys()
    for port in openport:
        list_port.append(port)
    print('Dados sobre o host: {} enviados'.format(host))
    
    return host, protocolo, list_port
        

def get_info_memoria():
    pmemory = psutil.virtual_memory().percent
    print('Informações sobre memória enviadas...\n')
    return pmemory

def get_info_disco():
    pdisco = psutil.disk_usage('.').percent
    print('Informações sobre o disco enviadas...\n')
    return pdisco

def get_info_cpu():

    info = cpuinfo.get_cpu_info()
    pcpu = psutil.cpu_percent(interval=0.5, percpu=True)
    modelo = info['brand']
    palavra = info['bits']
    arquitetura = info['arch']
    frequencia = psutil.cpu_freq().max
    nucleos = psutil.cpu_count()
    nucleos_fisicos = psutil.cpu_count(logical=False)

    info_cpu = {'modelo':modelo, 'palavra':palavra, 'arquitetura':arquitetura, 'frequencia':frequencia, 'nucleos':nucleos, 'nucleos_fisicos':nucleos_fisicos, 'pcpu':pcpu}
    
    print('Informações sobre o CPU enviadas...\n')
    
    return info_cpu

def get_info_diretorio(caminho):
    info_dir = []
    try:
        abspath = os.path.abspath(caminho)
        for item in os.listdir(abspath):
            arq = os.path.join(abspath, item)
            info = os.stat(arq)
            tamanho = info.st_size
            criacao = info.st_ctime
            modificacao = info.st_mtime
            if os.path.isdir(arq):
                tamanho = 0
            info_dir.append({'nome':item, 'tamanho':tamanho, 'Criação':criacao, 'Modificação':modificacao, 'abspath':abspath})
    except:
        info_dir = None
        print('Informações sobre o diretório enviadas...\n')
        
    return info_dir

def get_info_processos():
    processos = []
    for p in psutil.process_iter():
        processos.append(p.as_dict(attrs = ['pid', 'name', 'username', 'memory_percent', 'cpu_percent']))
    
    print('Informações sobre PÌDs enviadas...\n')
    return processos

def get_info_rede():
    interfaces = psutil.net_if_addrs()
    data = {}
    for interface in interfaces:
        data[interface] = []
        for endereco in interfaces[interface]:
            data[interface].append({'familia':endereco.family.name, 'endereco':endereco.address, 'mascara':endereco.netmask})
    
    print('Informações sobre interfaces de rede enviadas...\n')
    return data

def retorna_codigo_ping(hostname):
    plataforma = platform.system()
    args = []
    if plataforma == "Windows":
        args = ["ping", "-n", "1", "-l", "1", "-w", "100", hostname]

    else:
        args = ['ping', '-c', '1', '-W', '1', hostname]

    ret_cod = subprocess.call(args, stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
    return ret_cod

def get_info_hosts():
    """Verifica todos os host com a base_ip entre 1 e 255 retorna uma lista com todos os host que tiveram resposta 0 (ativo)"""
    print("\nMapeando...")
    host_ip = socket.gethostbyname(socket.gethostname()).split('.')
    base_ip = ".".join(host_ip[0:3]) + '.'
    host_validos = []
    return_codes = dict()
    for i in range(1, 255):
        return_codes[base_ip + str(i)] = retorna_codigo_ping(base_ip + str(i))
        if i %20 == 0:
            print(".", end = "")
        if return_codes[base_ip + str(i)] == 0:
            host_validos.append(base_ip + str(i))
    print("\nMapeamento completo, informações sobre portas enviadas...")
    
    return host_validos       
    
if __name__ == '__main__':
    servidor_tcp()
    
    
