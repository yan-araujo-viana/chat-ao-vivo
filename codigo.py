#Título: hashzap
# botao de iniciar chat
  # clicou no botão:
     # popup / modal
        # titulo : bem vindo ao Hashzap
        #campo: escreva seu nome no chat
        # botao : entrar no site
# chat
# embaixo do chat
    # campo de Digite sua mensagem
    # botão de enviar

# sempre que vc editar a pagina depois de carregada vc tem que rodar um pagina.update

# flet -> framework do python

import flet as ft # importar

def main(pagina): # criar a função principal/main
    texto = ft.Text("helo world")

    chat = ft.Column()

    def enviar_mensagem_tuenl(mensagem):
        print(mensagem)

        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tuenl)




    def enviar_mensagem(evento):
        print("enviar mensagem")
        pagina.pubsub.send_all(f"{nome_usuario.value}:  {campo_mensagem.value}")
       
        campo_mensagem.value = ''


        pagina.update()




    

    campo_mensagem = ft.TextField(label="Digite sua mensagem")
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])
    def entrar_chat(evento):
         print("entrar no chat")
         popup.open=False
         pagina.remove(botao_iniciar)
         pagina.remove(texto)
         pagina.add(chat)
         pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
 
         pagina.add(linha_enviar)
         pagina.update()

    titulo_popup = ft.Text("Bem vindo ao Testezap")
    nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)




    popup = ft.AlertDialog(open=False, modal=True, title=titulo_popup, content=nome_usuario, actions=[botao_entrar])

    def abrir_popup(evento): # toda função de butao tem que receber um evento
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER)    # criar o app chamando a função principal