fila = []
proxima_senha = 1
total_atendidos = 0
desistencias = 0
total_senhas = 0
soma_espera = 0
while True:
    print('============================================')
    print('----Bem-vindo ao sistema de atendimento!----')
    print('============================================')
    print('--------------MENU DE OPÇÕES--------------')
    print('G - Gerar senha comum')
    print('P - Gerar senha preferencial')
    print('C - Chamar próximo cliente')
    print('A - Avançar no tempo')  
    print('F - Exibir fila de atendimento')
    print('E - Exibir estatísticas')
    print('S - Sair do sistema')
    print('-----------------------------------------')
    opcao = input('Digite a opção desejada: ').upper()
    if opcao == 'G':
        novo_cliente = [proxima_senha,'C',0]
        fila.append(novo_cliente)
        print(f'Senha {proxima_senha} gerada para cliente comum')
        proxima_senha += 1
        total_senhas +=1
    elif opcao == 'P':
        novo_cliente = [proxima_senha,'P',0]
        fila.append(novo_cliente)
        print(f'Senha {proxima_senha} gerada para cliente preferencial')
        proxima_senha += 1
        total_senhas += 1
    elif opcao == 'C':
        if len(fila) > 0:
            indice_alvo = -1
            achou = False
            
            # 1. Procurar o Comum mais antigo e o Preferencial mais antigo da fila
            indice_comum = -1
            indice_preferencial = -1
            
            for i in range(len(fila)):
                if fila[i][1] == 'C' and indice_comum == -1:
                    indice_comum = i
                elif fila[i][1] == 'P' and indice_preferencial == -1:
                    indice_preferencial = i

            # 2. Decidir quem será chamado com base nas variáveis encontradas
            # Se existirem ambos os tipos na fila, fazemos o desempate correto
            if indice_comum != -1 and indice_preferencial != -1:
                tempo_comum = fila[indice_comum][2]
                tempo_pref = fila[indice_preferencial][2]
                
                # Regra 1: O comum só fura a fila se tiver espera >= 8 E for mais antigo que o preferencial
                if tempo_comum >= 8 and tempo_comum > tempo_pref:
                    indice_alvo = indice_comum
                    achou = True
                else:
                    # Regra 2: Se empatar no 8 ou se o pref for mais antigo, o Preferencial vai primeiro
                    indice_alvo = indice_preferencial
                    achou = True
            
            # Se só houver cliente preferencial na fila (Regra 2)
            elif indice_preferencial != -1:
                indice_alvo = indice_preferencial
                achou = True
                
            # Se só houver cliente comum na fila (Regra 3)
            elif indice_comum != -1:
                indice_alvo = indice_comum
                achou = True

            # 3. Executar o atendimento se alguém foi encontrado
            if achou == True:
                atendido = fila.pop(indice_alvo)
                print('>>> Cliente chamado: ')
                print(f'Senha:{atendido[0]} | Tipo:{atendido[1]} | Espera:{atendido[2]}')
                total_atendidos += 1
                soma_espera += atendido[2]
        else:
            print('A fila está vazia!')
    elif opcao == 'A':
        for i in range(len(fila)):
            fila[i][2] = fila[i][2] + 1
        fila_nova =[]
        for i in range(len(fila)):
            cliente = fila[i]
            if cliente[2] <10:
                fila_nova.append(cliente)
            else:
                desistencias += 1
                print(f'Senha {cliente[0]}({cliente[1]}) saiu após {cliente[2]} minutos de espera.')
        fila = fila_nova
        print('Tempo avançado em 1 unidade')
    elif opcao == 'F':
        if len(fila) == 0:
            print('Não há clientes na fila!')
        else:
            print('   ---- Fila atual ----   ')
            print('Senha | Tipo | Tempo de espera')
            for cliente in fila:
                print(f'{cliente[0]} | {cliente[1]} | {cliente[2]}')
    elif opcao == 'E':
        print('====== Estatísticas ======')
        print(f'Total de senhas geradas:{total_senhas}')
        print(f'Total de atendidos:{total_atendidos}')
        print(f'Total de desistências:{desistencias}')
        print(f'Clientes ainda na fila:{len(fila)}')
        if total_atendidos > 0:
            media = soma_espera / total_atendidos
            print(f'Tempo médio de espera dos atendidos:{media:.2f}')
        else:
            print('Não é possível calcular o tempo médio!')
    elif opcao == 'S':
        print('Encerrando o sistema. Até logo!')
        break
    else:
        print('Opção inválida!Tente Novamente.')
