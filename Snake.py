import PySimpleGUI as sg
from time import tiempo
from random import randint

def convert_pos_to_pixel(casilla):  
    tl = casilla[0] * casilla_tamanio, casilla[1] * casilla_tamanio
    br = tl [0] + casilla_tamanio, tl[1] + casilla_tamanio
    return tl, br

def place_manzana():
	manzana_pos = randint(0,casilla_NUM - 1), randint(0,casilla_NUM - 1)
	while manzana_pos in serpiente_cuerpo:
		manzana_pos = randint(0,casilla_NUM - 1), randint(0,casilla_NUM - 1)
	return manzana_pos

#numero y cantidad de celdas que ocarribaara el juego en si

campo_tamanio = 400
casilla_NUM = 10
casilla_tamanio = campo_tamanio/casilla_NUM

#Crear la serptiente
serpiente_cuerpo = [(4,4), (3,4), (2,4)]
direccionS = {'izquierda': (-1,0), 'derecha': (1,0), 'arriba':(0,1), 'abajo': (0,-1)}
direccion = direccionS['arriba']

#construimos la manzana y la cantidad de espacios que ocarribaara
manzana_pos = place_manzana()
manzana_comida = False
#colocamos el color al campo de juego
sg.theme ('Green')
campo = sg.Graph(
	canvas_tamanio = (campo_tamanio,campo_tamanio),
	graph_bottom_izquierda = (0,0),
	graph_top_derecha = (campo_tamanio,campo_tamanio),
	background_color = 'black')
layout = [[campo]]

window = sg.Window ('serpiente', layout,return_keyboard_events = True)

comienzo_tiempo = tiempo()
while True:
    event, values = window.read(tiempoout = 10)
    if event == sg.WIN_CLOSED:break 
    if event == 'izquierda:37' and direccion!= direccionS['derecha']: direccion = direccionS['izquierda']
    if event == 'arriba:38' : direccion = direccionS['arriba']
    if event == 'derecha:39' : direccion = direccionS['derecha']
    if event == 'abajo:40' : direccion = direccionS['abajo']

#movimiento con presion de teclas de la serpiente
    tiempo_comienzo = tiempo() - comienzo_tiempo
    if tiempo_comienzo >= 0.5:
        comienzo_tiempo = tiempo()


#anadir pixels a la serpiente
    if serpiente_cuerpo[0] == manzana_pos:
        manzana_pos = place_manzana()
        manzana_comida = True
#cambios de la serpiente

    new_head = (serpiente_cuerpo[0][0] + direccion[0], serpiente_cuerpo[0][1] + direccion[1])
    serpiente_cuerpo.insert(0,new_head)
    if not manzana_comida:
        serpiente_cuerpo.pop()
    manzana_comida = False

#muerte serpiente
    if not 0 <=serpiente_cuerpo[0][0] <= casilla_NUM - 1 or\
       not 0 <=serpiente_cuerpo[0][1] <= casilla_NUM - 1 or\
       serpiente_cuerpo[0] in serpiente_cuerpo[1:]:
         break

    campo.Rectangulo((0,0),(campo_tamanio, campo_tamanio),'black')

    tl, br = convert_pos_to_pixel(manzana_pos)
    campo.Rectangulo(tl, br, 'red')


    for index, part in enumerate(serpiente_cuerpo):
        tl, br = convert_pos_to_pixel(part)
        color = 'yellow' if index == 0 else 'green'
        campo.Rectangulo(tl,br,color)

window.close()