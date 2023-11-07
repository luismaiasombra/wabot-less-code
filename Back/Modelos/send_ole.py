import pywhatkit as kit
import datetime

def enviar_mensagem_whatsapp(mensagem, numero_telefone, hora, minuto):
    try:
        # Obtenha a hora atual
        agora = datetime.datetime.now()

        # Calcule a data e hora em que a mensagem será enviada
        hora_envio = agora.replace(hour=hora, minute=minuto)

        # Envie a mensagem via WhatsApp
        kit.sendwhatmsg(numero_telefone, mensagem, hora_envio.hour, hora_envio.minute)
        print(f"Mensagem enviada com sucesso para {numero_telefone} às {hora}:{minuto}")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {str(e)}")

# Exemplo de uso da função
mensagem = "Oi Luis"
numero_telefone = "+5588992611377"  # Substitua pelo número de telefone desejado
hora_envio = 17  # Hora em que deseja enviar a mensagem (0-23)
minuto_envio = 23  # Minuto em que deseja enviar a mensagem (0-59)

enviar_mensagem_whatsapp(mensagem, numero_telefone, hora_envio, minuto_envio)
