import webbrowser

def convertir_precio_a_dolares(precio_ars, tipo_cambio):
    return precio_ars / tipo_cambio

def abrir_enlaces(enlaces):
    for enlace in enlaces:
        print(enlace)
        #webbrowser.open(enlace)
