import requests
import sqlite3
def send(message,number):
    
    def numbers_only(phone_number):
        # Remove non-numeric characters from the input string
        numeric_string = ''.join(filter(str.isdigit, phone_number))
        return numeric_string

    # Example usage:
    
    url = "https://v5.chatpro.com.br/chatpro-0e358013c5/api/v1/send_message"

    payload = {
        "number": numbers_only(number),
        "message": message
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "f7841b1677153acd798304d815db5ef2"
    }

    response = requests.post(url, json=payload, headers=headers) #aqui a mensagem é enviada
    #vamos mandar ela pro histórico:
    return response
send('hello','5588992611377')