from PySimpleGUI import *

senha = "inforTop"
with open("source.txt", "w") as arq:
    arq.write("FD - Força Democrática: 0 votos \nPUMA - Para Um Melhor Aprendizado: 0 votos")

def semN(string):
    s = ''
    for i in string:
        if i in "\n":
            continue
        s += i
    return s

layout = [
[Text(("\n"*12) + (" "*144) + "Aguarde...")]
]
tela = Window("Aguarde...", layout, no_titlebar=True, finalize=True, disable_close=True)
tela.maximize()
telax = tela.size[0]
tela.close()
print(telax)

def tp(value, base=248): #transpose space position
    totalSpaces = int(telax/4.19)
    output = int((value/base) * totalSpaces)
    return output

def resultado():
    with open("source.txt", "r") as arq:
        lines = arq.readlines()
    layout = [
    [Text("\n")],
    [Text(" "*tp(70)), Text("Andamento da votação", font="Arial 30")],
    [Text("\n"*12)],
    [Text(" "*tp(60)), Text(semN(lines[0])), Text(" "*8),  Text(semN(lines[1]))],
    [Text("\n"*3)],
    [Text(" "*tp(105)), Button("Finalizar a votação")],
    [Text("")],
    [Text(" "*tp(107)), Button("Voltar ao menu")],
    [Text("\n"*9)],
    [Text(" "*tp(90)), Text("Desenvolvido pelo curso de informática")]
    ]
    
    tela = Window("Andamento da votação", layout, no_titlebar=True, finalize=True, disable_close=True)
    tela.maximize()
    
    run = 1
    while run:
        eventos = tela.read()
        for event in eventos:
            if event == WIN_CLOSED or event == "Exit":
                run = 0
            elif event == "Voltar ao menu":
                run = 0
            elif event == "Finalizar a votação":
                with open("source.txt", "r") as arq:
                    f = arq.readlines()
                popup("".join(f))
                tela.close()
                return 0
            
    tela.close()
    return 1

def voto():
    c = [0, 0]
    layout = [
    [Text("\n")],
    [Text(" "*tp(102)), Text("Votação", font="Arial 30")],
    [Text("\n"*11)],
    [Text(" "*tp(82)), Text("\n\nSelecione sua chapa e aperte em 'Confirmar' abaixo")],
    [Text(" "*tp(65)), Radio("FD - Força Democrática", "chapa", default=False,  key="a"), Text(" "*2), Radio("PUMA - Para Um Melhor Aprendizado", "chapa", default=False, key="b")],
    [Text("\n"*4)],
    [Text(" "*tp(110)), Button("Confirmar")],
    [Text("\n"*9)],
    [Text(" "*tp(90)), Text("Desenvolvido pelo curso de informática")]
    ]

        
    tela = Window("Tela de votação", layout, no_titlebar=True, finalize=True, disable_close=True)
    tela.maximize()

    run = 1
    while run:
        eventos = tela.read()
        for event in eventos:
            if event == "Confirmar":
                for i in eventos:
                    if isinstance(i, dict):
                        if i["a"]:
                            c[0] = 1
                            run = 0
                        elif i["b"]:
                            c[1] = 1
                            run = 0    
        

    tela.close()
    return c 

       
def main():
    cA = 0
    cB = 0
    layout = [
        [Text("\n")],
        [Text(" "*tp(50)), Text("SysGrêmio - TEC.INFORMÁTICA", font="Arial 30")],
        [Text("\n"*12)],
        [Text(" "*tp(72)), Text("Senha:"), Input(key="senha", password_char="")],
        [Text("\n"*5)],
        [Text(" "*tp(72)), Button("Verificar Senha"), Text(" "*49), Button("Votação")],
        [Text("\n"*11)],
        [Text(" "*tp(95)), Text("Desenvolvido pelo curso de informática")]
    ]
    
    tela = Window("Tela de controle", layout, no_titlebar=True, finalize=True, disable_close=True)
    tela.maximize()

    run = 1
    while run:
        eventos = tela.read()
        for event in eventos:
            if event == WIN_CLOSED or event == "Exit":
                run = 0
            elif event == "Verificar Senha":
                for i in eventos:
                    if isinstance(i, dict):
                        if i["senha"] == senha:
                            layout[3][2].update("") #input
                            run = resultado()
                            layout[3][2].update("") #input
                        elif i["senha"] == "":
                            popup("Digite algo")
                        else:
                            popup("Senha incorreta")
            elif event == "Votação":
                layout[3][2].update("") #input
                v = voto()
                layout[3][2].update("") #input
                cA += v[0]
                cB += v[1]
                with open("source.txt", "w") as arq:
                    arq.write("FD - Força Democrática: " + str(cA) + " voto" + ("" if cA == 1 else "s") + "\nPUMA - Para Um Melhor Aprendizado: " + str(cB) + " voto" + ("" if cB == 1 else "s") + "\nEm andamento")
                        
    tela.close()       

main()
#resultado()