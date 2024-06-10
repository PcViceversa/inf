import requests
url_root = "http://localhost:6969/api"

def setup():
    print("**** *** ** BIENBENIDO A CommuniKen ** *** ****")
    print("**** **** *** ** INICIO SESION ** *** **** ****")
    print()
    mail_usr = input("INGRESE MAIL: ")
    pass_usr = input("INGRESE PASS: ")
    tup = (mail_usr , pass_usr)
    return tup

def loop():
    print()
    print("**** **** *** ** ************* ** *** **** ****")
    print("**** **** *** ** ************* ** *** **** ****")
    print()
    print("MENU")
    print("1 - Enviar un correo")
    print("2 - Ver información de un correo electrónico")
    print("3 - Ver correos marcados como favoritos")
    print("4 - Marcar un correo como favorito")
    print("5 - Terminar la ejecución del cliente")
    print()
    print("**** **** *** ** ************* ** *** **** ****")
    print("**** **** *** ** ************* ** *** **** ****")

## SERVICOS 1 : VALIDAR REGITRO
def api_aws_1(tup):
    tup = (0,0)
    return True

## SERVICOS 2 : ...
def api_aws_2(tup):
    url = url_root + "/aws2"
    inf = {}
    response = requests.post(url,inf)
    response = requests.get(url)
    return True

## SERVICOS 3 : ...
def api_aws_2(tup):
    url = url_root + "/aws3"
    inf = {}
    response = requests.post(url,inf)
    response = requests.get(url)
    return True

def main():
    tup = setup()
    if api_aws_1(tup) == True:
        loop()
        op = input("\nSELECCIONE UNA OPCION DE 1-5 ")

        while op != "5":
            if   op == "1":
                print("OPCION 1 ...")
                ## LOGIC OP 1
            elif op == "2":
                print("OPCION 2 ...")
                ## LOGIC OP 2
            elif op == "3":
                print("OPCION 3 ...")
                ## LOGIC OP 3
            elif op == "4":
                print("OPCION 4 ...")
                ## LOGIC OP 4
            else:
                print("OPCION NO VALIDA, SELECCIONAR 1-5")

            loop()
            op = input("\nSELECCIONE UNA OPCION DE 1-5 ")

        print("¡Gracias por usar CommuniKen! Hasta luego.")
    else:
        print("¡Gracias por usar CommuniKen! Hasta luego.")

if __name__ == "__main__":
    main()
