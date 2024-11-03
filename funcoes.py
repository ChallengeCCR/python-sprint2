import os
from datetime import datetime
import time

# Paths para os logs
path_action_log = 'log.txt'



# Função para escrever logs
def registrar_log(path_log, conteudo):
    file = open(path_log, 'a')
    file.write(f'{conteudo}\n')
    file.close()



# Função para limpar o terminal
def cls(): 
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para verificar e realizar login
def fazer_login(credencialAdministrador):
    print('\t### FAZER LOGIN AUTORAIL MONITOR\n')
    print('Informe os dados da credencial de administrador para acessar o menu\n')
    print('CREDENCIAL DE EXEMPLO: [usuario = admin || senha = 123]\n')
    
    nomeCredencial = input('Usuário: ')
    senhaCredencial = input('Senha: ')


    # Verifica se o nome de usuário existe e a senha está correta
    if credencialAdministrador.get(nomeCredencial) == senhaCredencial:
        cls()
        print('Credencial validada com sucesso!\n')
    else:
        cls()
        print('Nome de usuário ou senha incorretos. Tente novamente.\n')
        fazer_login(credencialAdministrador)
        return False
    
    
    
# Função para fazer logout
def fazer_logout(credencialAdministrador):
    cls()
    print('Logout realizado com sucesso!\n')
    for i in range(3, 0, -1):
        print(f'\rRetornando para a página de login em {i}... ', end='', flush=True)
        time.sleep(1)
    cls()   
    fazer_login(credencialAdministrador)



# Função para exibir as opções do menu
def exibir_menu():
    print('Escolha uma opção:')
    print('[A] Registrar alerta')
    print('[B] Remover alerta')
    print('[C] Exibir alertas\n\n')
    print('[Z] Fazer logout\n')
    print('[...] Encerrar programa\n')



# Função para REGISTRAR ALERTAS
def registrar_alerta(alertasAtivos):
    cls()
    print('\t### REGISTRAR ALERTA\n')
    print('# Informe os seguintes dados para registrar\n')
    
    alertaNomeInput = input('Nome: ') # Perguntando os dados que um alerta terá
    alertaDescricaoInput = input('Descrição: ')
    
    if alertaNomeInput.strip() and alertaDescricaoInput.strip():  # Verificando se as informações do menu NÃO são vazias
        
        alerta = { # Objeto de alerta que será guardado
            'nome': alertaNomeInput,
            'descricao': alertaDescricaoInput
        }
        
        alertasAtivos.append(alerta) # Adiciona o alerta na Array
        registrar_log(path_action_log, f' (++) CRIADO o alerta {alerta['nome'].upper()} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}')
    
        # Confirmação   
        cls()       
        print(f'Alerta \'{alertaNomeInput}\' registrado!\n')
        input('Pressione ENTER para voltar ao Menu Inicial')
        cls()

        # Escrevendo e registrando o log de ação
        registrar_log(path_action_log, f' (--) REMOVIDO o alerta {alerta['nome'].upper()} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}')
        
    # Mensagem caso uma das informações seja vazia
    elif not alertaNomeInput.strip() or not alertaDescricaoInput.strip():
        cls()
        print('!!! Nenhum dos dados podem ser vazios !!!')
        print('Retorne ao Menu Inicial e tente novamente\n')
        input('Pressione ENTER para voltar ao Menu Inicial')
        cls()



# Função para remover alertas
def remover_alerta(alertasAtivos):

    cls()         
    if not alertasAtivos: # Verificar se NÃO existem alertas registrados
        print('Nenhum alerta ativo.\n')
        
    else:
        
        print('\t### REMOVER ALERTAS ATIVOS\n')
        print('_' * 60 + '\n')
        
        for i, alerta in enumerate(alertasAtivos): # Lista todos os alertas presentes em [alertarAtivos]
            print(f'ID: {i}\nNome: {alerta['nome']}\nDescrição: {alerta['descricao']}')
            print('_' * 60 + '\n') 
    
        try: # Try and Except para remover o alerta
            print('Para voltar ao Menu Inicial digite \"Cancelar\"\n ')
            idParaRemover = input('ID do alerta a ser removido: ')
                       
            # Verificando se o usuário quer encerrar a operação
            if (idParaRemover.lower() == 'cancelar'):
                cls()
                return False
            
            intIdParaRemover = int(idParaRemover) # Convertendo a input para int 
            
            if 0 <= intIdParaRemover < len(alertasAtivos): 
                cls()

                # REGISTRA A AÇÃO NO LOG.TXT    
                registrar_log(path_action_log, f' (-) REMOVIDO o alerta {alerta['nome'].upper()} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}')

                # Confirmação
                print(f'Alerta \'{alertasAtivos[intIdParaRemover]['nome']}\' removido!')
                del alertasAtivos[intIdParaRemover] # deleta o alerta
                                  
        # Mensagem de erro caso a input não seja do tipo Int
        except ValueError:
                cls()
                print('O valor do ID deve ser um número INTEIRO!')
                print('Retorne ao Menu Inicial e tente novamente\n')
        
    # Volta ao início do programa
    input('Pressione ENTER para voltar ao Menu Inicial')
    cls()



# Função para exibir alertas ativos
def exibir_alerta(alertasAtivos):
        cls()
        if not alertasAtivos:  # Mensagem de erro caso não haja alertas registrados
            print('Nenhum alerta ativo.\n')
        else:
            print('\t### ALERTAS ATIVOS\n')
            print('_' * 60 + '\n')
            # Lista todos os alertas presentes em [alertarAtivos]
            for i, alerta in enumerate(alertasAtivos):
                print(f'ID: {i}\nNome: {alerta['nome']}\nDescrição: {alerta['descricao']}')
                print('_' * 60 + '\n')
            
        # Volta ao início do programa
        input('Pressione ENTER para voltar ao Menu Inicial')
        cls() 
