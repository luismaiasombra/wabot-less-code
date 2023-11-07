from classes.consultant import Consultant
from database.history import in_history,add_to_history
def realizar_disparos():
    for row in Consultant.consultants:
        upgradable = row.upgradable()
        code, name, phone, level, status, debit_status, perks, points = row.code, row.name, row.phone, row.level, row.status, row.debit_status, row.perks,row.points
        if upgradable != False:
            if in_history(row.code, row.name,'DISPARO', row.level):
                print('already in')
            else:
                print('success')#faz o disparo agora
                add_to_history(row)