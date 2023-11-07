from classes.consultant import Consultant
from tools.send_message import  send as send_message

def broadcast(levels_to_broadcast,message):
    for consultant in Consultant.consultants:
        if consultant.level in levels_to_broadcast:
            number = consultant.phone
            send_message(message,number)

