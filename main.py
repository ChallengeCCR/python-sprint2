from funcoes import *

def cls(): #* Função para limpar o console
    os.system('cls' if os.name == 'nt' else 'clear')

# Declarações 
alertasAtivos = [] #* Os alertas serão armazenados aqui
credencialAdministrador = { "admin": "123" } 

def main():
    cls() # Limpa todo o terminal na primeira inicialização
    
    fazer_login(credencialAdministrador) # Verificando ologin
        
    menuAtivo = True
    
    while menuAtivo:
        exibir_menu() #* Exibe as opções iniciais do Menu

        opcoesMenu = ['a', 'b', 'c', 'z', '...']
        opcaoUsuario = input().lower() # Input do usuário, sempre em minúsculo
        
        if opcaoUsuario in opcoesMenu: #* Verificando se uma opção é válida
            
            if opcaoUsuario == 'a': #* OPÇÃO 'A' - REGISTRAR ALERTAS
                registrar_alerta(alertasAtivos)
            
            elif opcaoUsuario == 'b': #* OPÇÃO 'B' -- REMOVER ALERTAS
                remover_alerta(alertasAtivos)

            elif opcaoUsuario == 'c': #* OPÇÃO 'C' -- VISUALIZAR ALERTAS
                exibir_alerta(alertasAtivos)

            elif opcaoUsuario == 'z': #* OPÇÃO 'Z' -- FAZER LOGOUT
                cls()
                fazer_logout(credencialAdministrador)

            elif opcaoUsuario == '...': #* OPÇÃO '..' - ENCERRAR O MENU  
                cls()
                print('Encerrando...')
                menuAtivo = False   
        else:
            cls()
            print('\t!!! OPÇÃO INVÁLIDA !!!\n')

# Executa a função main
if __name__ == '__main__':
    main()