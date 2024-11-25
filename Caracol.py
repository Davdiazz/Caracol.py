def dias_para_subir(metros_totales):
    metros_subidos = 0
    dias = 0
    # Inicia en 0

#se hace un while para determinar cuando se cumpla la altura requerida 
    while metros_subidos < metros_totales:
        dias += 1  
        metros_subidos += 2  
        # aumenta 1 dia y 2 metros subidos

        if metros_subidos >= metros_totales:
            break  
        
        metros_subidos -= 1  
# disminuye 1 en la noche

    return dias

# Definir la altura total que el caracol quiere alcanzar
# Debera quedar 9 dias en 10 metros, ya que la logica indica que el dia 8 subira hasta el metro 10 lo cual es correcto si solo son 9 dias
metros_totales = 15
# Cambiar metros totales 
dias = dias_para_subir(metros_totales)
print(f"El caracol tarda {dias} días en subir {metros_totales} metros.")