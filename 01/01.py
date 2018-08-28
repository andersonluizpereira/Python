config = {"active": False,"admin": True}

def salario_descontado_imposto(salario, imposto=27.5):
     return salario - (salario * imposto * 0.01)

def new_user(active, admin):
    if active=='' or admin=='':
        active = config.get('active')
        admin = config.get('admin')
    
    if active and admin:
        return 'SIM'
    else:
        return 'NÃO'     

salario = int(input('Salario? '))
imposto = float(input('Imposto em % (ex: 27.5)? '))
active = bool(input('Ativar usuario ? '))
admin = bool(input('Admin usuario ? '))
edy_eh_trouxa = bool(input('edy é trouxa?'))

if imposto == '':
   imposto = 0
else:
    imposto = float(imposto)

print("Valor real: {0}, usuario  ativado: {1}".format(salario_descontado_imposto(salario),new_user(active,admin)))



