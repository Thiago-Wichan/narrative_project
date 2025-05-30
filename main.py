# Objetivo é transformar a narrativa do BAT em inserção de dados

import impression
import os
from text import open_text, FILE_PATH

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
impression.erase_text_file()
input_dict = dict(
    date=date,
    hour=hour,
    br=br,
    km=km,
    way=way,
    municipality=municipality,
    type_of_accident=type_of_accident,
    numbers_of_vehicles=numbers_of_vehicles,
)

# Vehicle insertion

vehicles = []
for i in range(1, numbers_of_vehicles_int+1):
    insert_vehicle = input(
        f'Placa e modelo de V{i}: '
    )
    vehicles.append(insert_vehicle)

# People insertion

drivers = []
for i in range(1, numbers_of_vehicles_int+1):
    insert_drivers = input(
        f'Insira o condutor de V{i} - {vehicles[i-1]}: '
    ).upper()
    drivers.append(insert_drivers)


# Moments of the accident

moments = input(
    'Em quantos momentos ocorreram no acidente? '
)
moments_int = int(moments)
cinematic = []

for i in range(moments_int):
    insert_moments = input(f'No momento {i+1}, ')
    cinematic.append(insert_moments)
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

interdition_input = input(
    'Houve interdição da via? '
).lower()

if interdition_input == 'sim':
    interdition_situation = input(
        '[0] Total ou [1] Parcial? '
    )
    if interdition_situation == '0':
        interdition_situation = 'Total'
    elif interdition_situation == '1':
        interdition_situation = 'Parcial'
    os.system('cls')
else:
    interdition_situation = ''

# Introduction and Display of drivers and vehicles


def vehicles_func(x):
    global vehicles
    global drivers
    print_vehicles = ''
    for i in range(x):
        print_vehicles += (
            f'\nV{i+1} - {vehicles[i]} - Conduzido por {drivers[i]}.'
        )
    return print_vehicles


# Singular
path_intro_sing = FILE_PATH / 'intro_singular.txt'
path_intro_plural = FILE_PATH / 'intro_plural.txt'

if numbers_of_vehicles_int == 1:
    introduction_singular = open_text(path_intro_sing, input_dict)
    impression.write_file(introduction_singular)

# Plural
else:
    introduction_plural = open_text(path_intro_plural, input_dict)
    impression.write_file(introduction_plural)

impression.write_file(vehicles_func(len(vehicles)))

# Moments of the accident


def moments_func(x, y):
    print_moments = ''
    for i in range(x):
        print_moments += (
            f'\nNo momento {i+1}, {y[i]}.'
        )
    return print_moments


impression.write_file(moments_func(moments_int, cinematic))

# Road situation

if numbers_of_vehicles_int == 1:
    impression.write_file_singular(scene_situation, interdition_situation)
else:
    impression.write_file_plural(scene_situation, interdition_situation)

# Observações

speed = input('Velocidade Máxima da via: ')
speed_print = f' A velocidade máxima da via é {speed} km/h. '
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

print(f'Your file is ready. Access: {impression.FILE_DESKTOP_PATH}')
