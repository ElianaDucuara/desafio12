recordatorios = [
    ['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]
]

# 1. Agregar un evento el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar el Año”
recordatorios.append(['2021-02-02', '06:00', 'Empezar el año'])

# Ordenar los eventos después de agregar uno nuevo para mantener el orden cronológico
recordatorios.sort(key=lambda x: x[0] + ' ' + x[1])

# 2. Editar el evento del 15 de Julio ya que no es feriado y cambiarlo por el 16 de Julio
for evento in recordatorios:
    if evento[0] == '2021-07-15':
        evento[0] = '2021-07-16'
        break

# 3. Eliminar el evento del día del trabajo
recordatorios = [evento for evento in recordatorios if evento[0] != '2021-05-01']

# 4. Agregar cena de Navidad y de Año Nuevo
recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

# Ordenar nuevamente después de añadir más eventos
recordatorios.sort(key=lambda x: x[0] + ' ' + x[1])

for evento in recordatorios:
    print(evento)
