# Objetivo é transformar a narrativa do BAT em inserção de dados

# from text import situation_singular, situation_plural
import impression
import os

# Data insertion
date = input('Qual o dia do ocorrido? ')
hour = input('Qual a hora do ocorrido? ')
br = input('Qual a BR? ')
km = input('Qual o Km? ')
way = input('Qual sentido? ')
municipality = input('Qual o Município e Estado? ')
type_of_accident = input('Qual o tipo de acidente? ')
numbers_of_vehicles = input('Quantos veículos envolvidos? ')
numbers_of_vehicles_int = int(numbers_of_vehicles)
os.system('cls')
impression.erase_file()


# Vehicle insertion

vehicles = []
for i in range(1, numbers_of_vehicles_int+1):
    insert_vehicle = input(
        f'Placa e modelo de V{i}: '
    )
    vehicles.append(insert_vehicle)
print()

# People insertion

drivers = []
for i in range(1, numbers_of_vehicles_int+1):
    insert_drivers = input(
        f'Insira o condutor de V{i} - {vehicles[i-1]}: '
    ).upper()
    drivers.append(insert_drivers)
print()


# Moments of the accident

moments = input(
    'Em quantos momentos ocorreram no acidente? '
)
moments_int = int(moments)
cinematic = []

for i in range(moments_int):
    insert_moments = input(f'No momento {i+1}, ')
    cinematic.append(insert_moments)
print()
os.system('cls')


# Scene situation:
scene = input(
    'A cena encontrava-se: \n'
    '[0] - Desfeita \n'
    '[1] Parcialmente Desfeita \n'
    '[2] Preservada: \n'
)
if scene == '0':
    scene_situation = 'Desfeita'
elif scene == '1':
    scene_situation = 'Parcialmente Desfeita'
elif scene == '2':
    scene_situation = 'Preservada'
print()

interdition_input = input(
    'Houve interdição da via? '
).lower()

if interdition_input == 'sim':
    interdition_situation = input(
        '[0] Total ou [1] Parcial? '
    )
    if scene == '0':
        interdition_situation = 'Total'
    elif scene == '1':
        interdition_situation = 'Parcialmente obstruída'
    os.system('cls')
else:
    interdition_situation = None

# Introduction and Display of drivers and vehicles


def vehicles_func(x):
    global vehicles
    global drivers
    for i in range(x):
        return (f'V{i+1} - {vehicles[i]} - Conduzido por {drivers[i]}. ')


# Singular
if numbers_of_vehicles_int == 1:
    introduction_singular = (
        f'No dia {date}, por volta das {hour}, esta equipe compareceu no km '
        f'{km}, {way}, da BR {br}, no município de {municipality}, onde '
        f'ocorreu um acidente do tipo {type_of_accident}, envolvendo o '
        'veículo: '
    )
    impression.write_file(introduction_singular)
    print()
# Plural
else:
    introduction_plural = (
        f'No dia {date}, por volta das {hour}, esta equipe compareceu no km '
        f'{km}, {way}, da BR {br}, no município de {municipality}, onde '
        f'ocorreu um acidente do tipo {type_of_accident}, envolvendo os '
        'veículos:'
    )
    impression.write_file(introduction_plural)
    print()

impression.write_file(vehicles_func(numbers_of_vehicles_int))
print()

# Moments of the accident

for i in range(moments_int):
    impression.write_file(f'No momento {i+1}, {cinematic[i]}. ')
print()

# Road situation

if numbers_of_vehicles_int == 1:
    impression.write_file_singular(scene_situation, interdition_situation)
else:
    impression.write_file_plural(scene_situation, interdition_situation)

# Observações

speed = input('Velocidade Máxima da via: ')
speed_print = f'A velocidade máxima da via é {speed} km/h. '
impression.write_file(speed_print)

remotion = input('Houve remoção? ').lower()

if remotion == 'sim':
    pacient = input('Quem foi removido? ')
    bam = input('Número do BAM: ')
    remotion_print = (
        f'{pacient} necessitou de atendimento médico. BAM - {bam}. '
    )
    impression.write_file(remotion_print)

criminal = input('Houve abertura de RO? ')
if criminal == 'sim':
    ro = input('Número do RO: ')
    bop = input('Número do BOP: ')
    criminal_print = (
        f'Foi lavrado o RO de nº {ro} e confeccionado o BOP nº {bop}. '
        'nos sistemas da PRF.'
    )
    impression.write_file(criminal_print)
