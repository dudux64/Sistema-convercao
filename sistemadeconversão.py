import dearpygui.dearpygui as dpg
dpg.create_context()

def sair():
    dpg.stop_dearpygui()

def sistemadeconversao():
    opcao = dpg.get_value ("opcao")
    moeda = dpg.get_value ("moeda")
    try:
        opcao = int(opcao)
        moeda = float(moeda)    # Converte os valores inseridos nos campos de entrada para int e float
        if opcao == 1:
            resultado = moeda / 5.17    # Calcula a conversão de Real para Dólar
            dpg.set_value("resultado",f"O valor da Conversão é:${resultado:,.2f} dólares")   # Atualiza o texto do widget de resultado com o valor calculado formatado
        elif opcao == 2:
            resultado = 5.17 * moeda   # Calcula a conversão de Dólar para Real
            dpg.set_value("resultado",f"O valor da Conversão é:${resultado:,.2f} reais")   # Atualiza o texto do widget de resultado com o valor calculado formatado
        
        elif opcao == 3:
            resultado = moeda / 5.33
            dpg.set_value("resultado",f"O valor da Conversão é:${resultado:,.2f} euros")
        elif opcao == 4:
            resultado = moeda * 5.33
            dpg.set_value("resultado",f"O valor da Conversão é:${resultado:,.2f} reais")

        elif opcao == 5:
            resultado =  0.92 * moeda
            dpg.set_value("resultado",f"O valor da Conversão é:${resultado:,.2f} euros")

        elif opcao == 6:
            resultado =  moeda / 0.92
            dpg.set_value("resultado",f"O valor da Conversão é:${resultado:,.2f} doláres")

        else:  
            dpg.set_value("resultado","Por favor, insira valores numéricos válidos")   # Caso a opção não seja 1 ou 2, exibe uma mensagem de erro

    except ValueError:
        dpg.set_value("resultado","Por favor, insira valores numéricos válidos")    # Se ocorrer um erro de conversão, exibe uma mensagem de erro

dpg.create_viewport(title='Sistema', width=700, height=300)

with dpg.window(label="Sistema de Conversão", width=700, height=300):
    dpg.add_text("Qual a opção vc quer \nReal/Dolar Digite = 1: \nDolar/Real Digite = 2: \nReal/Euro Digite = 3: \nReal/Euro Digite = 4: \nDolar/Euro = 5:\nDolar/Euro = 6: ")
    dpg.add_input_text(label="Opção", tag="opcao")
    dpg.add_input_text(label="Moeda", tag="moeda")
    dpg.add_button(label="Calcular", callback=sistemadeconversao)
    dpg.add_text("", tag="resultado")
    dpg.add_button(label="Exit", callback=sair)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

    
