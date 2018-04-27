import Variables as vb
import Previsualizar as pr
import wx
from functools import partial
import Columnas as col
import json


def valores_choice(e):
    # Funcion que recoge los valores de los select
    vb.back_rep = ch_back_rep.GetString(ch_back_rep.GetCurrentSelection())
    vb.contorno = ch_back_con.GetString(ch_back_con.GetCurrentSelection())
    vb.background_gr = ch_back_gr.GetString(ch_back_gr.GetCurrentSelection())
    vb.color_linea = ch_linea_gr.GetString(ch_linea_gr.GetCurrentSelection())
    vb.label = ch_label_gr.GetString(ch_label_gr.GetCurrentSelection())
    vb.tamanno_tit = ch_titulo_tam.GetString(ch_titulo_tam.GetCurrentSelection())
    vb.titulo_gr = ch_titulo_gr.GetString(ch_titulo_gr.GetCurrentSelection())
    vb.fuente_tit = ch_titulo_fam.GetString(ch_titulo_fam.GetCurrentSelection())
    vb.fuente_label = ch_fuente_etiqueta.GetString(ch_fuente_etiqueta.GetCurrentSelection())
    vb.tamanno_label = ch_tamannos_etiqueta.GetString(ch_tamannos_etiqueta.GetCurrentSelection())


def valores_color(e):
    # Funcion que recoge los colores de los input de tipo color
    vb.back_rep = cl_back_rep.GetColour()
    vb.back_rep = vb.back_rep.GetAsString(flags=wx.C2S_HTML_SYNTAX)
    vb.contorno = cl_back_con.GetColour()
    vb.contorno = vb.contorno.GetAsString(flags=wx.C2S_HTML_SYNTAX)
    vb.background_gr = cl_back_gr.GetColour()
    vb.background_gr = vb.background_gr.GetAsString(flags=wx.C2S_HTML_SYNTAX)
    vb.color_linea = cl_linea_gr.GetColour()
    vb.color_linea = vb.color_linea.GetAsString(flags=wx.C2S_HTML_SYNTAX)
    vb.label = cl_label_gr.GetColour()
    vb.label = vb.label.GetAsString(flags=wx.C2S_HTML_SYNTAX)
    vb.titulo_gr = cl_titulo_gr.GetColour()
    vb.titulo_gr = vb.titulo_gr.GetAsString(flags=wx.C2S_HTML_SYNTAX)


def valores_texto(e):
    # Funcion que recoge los valores de los cuadros de texto
    vb.etiquetas = int(etiquetas_input.GetValue())
    vb.grosor = float(grosor_input.GetValue())
    vb.s_entrada = int(s_entrada_input.GetValue())
    vb.s_salida = int(s_salida_input.GetValue())
    vb.angulo_gr = int(angulo_input.GetValue())


def cambiar(e):
    # Funcion para cambiar entre los controles de lista para los colores o los input de tipo color
    if vb.checkbox == 1:
        ch_linea_gr.Hide()
        ch_label_gr.Hide()
        ch_back_con.Hide()
        ch_back_gr.Hide()
        ch_back_rep.Hide()
        ch_titulo_gr.Hide()
        cl_back_con.Show()
        cl_back_rep.Show()
        cl_back_gr.Show()
        cl_label_gr.Show()
        cl_linea_gr.Show()
        cl_titulo_gr.Show()
        vb.checkbox = 0
    else:
        ch_linea_gr.Show()
        ch_label_gr.Show()
        ch_back_con.Show()
        ch_back_gr.Show()
        ch_back_rep.Show()
        ch_titulo_gr.Show()
        cl_back_con.Hide()
        cl_back_rep.Hide()
        cl_back_gr.Hide()
        cl_label_gr.Hide()
        cl_linea_gr.Hide()
        cl_titulo_gr.Hide()
        vb.checkbox = 1


def cambiar_titulos(e, lista):
    # Funcion que guarda los titulos que se introducen en los cuadros de texto creados dinamicamente
    for titu in range(len(lista)):
        vb.titulos[titu] = lista[titu].GetValue()


def predeterminados(widget, texto, lista):
    widget.SetSelection(lista.index(texto))


def cambiar_ytick_entrada(e, entrada):
    for ytick in range(len(entrada)):
        vb.ytick_entrada_fin[ytick] = float(entrada[ytick].GetValue())


def cambiar_ytick_salida(e, entrada):
    for ytick in range(len(entrada)):
        vb.ytick_salida_fin[ytick] = float(entrada[ytick].GetValue())


def cambiar_ytick_salto(e, entrada):
    for ytick in range(len(entrada)):
        vb.ytick_salto_fin[ytick] = float(entrada[ytick].GetValue())


def ck_ytick(e):
    if vb.c_yticks == 0:
        for i in range(vb.contador_col - 1):
            vb.ytick_label.append(
                wx.StaticText(panel_principal, label=f"Columna {i+1}", pos=(800, 230 + i * 40)))
            vb.ytick_entrada.append(wx.TextCtrl(panel_principal, pos=(860, 230 + i * 40), size=(40, -1)))
            vb.ytick_entrada[i].Bind(wx.EVT_TEXT, partial(cambiar_ytick_entrada, entrada=vb.ytick_entrada))
            vb.ytick_entrada_fin.append(0)
            vb.ytick_salida.append(wx.TextCtrl(panel_principal, pos=(910, 230 + i * 40), size=(40, -1)))
            vb.ytick_salida[i].Bind(wx.EVT_TEXT, partial(cambiar_ytick_salida, entrada=vb.ytick_salida))
            vb.ytick_salida_fin.append(0)
            vb.ytick_salto.append(wx.TextCtrl(panel_principal, pos=(960, 230 + i * 40), size=(40, -1)))
            vb.ytick_salto[i].Bind(wx.EVT_TEXT, partial(cambiar_ytick_salto, entrada=vb.ytick_salto))
            vb.ytick_salto_fin.append(0)

        vb.c_yticks = 1
    else:
        for ytick in vb.ytick_label:
            ytick.Destroy()
        for ytick in vb.ytick_entrada:
            ytick.Destroy()
        for ytick in vb.ytick_salida:
            ytick.Destroy()
        for ytick in vb.ytick_salto:
            ytick.Destroy()
        vb.ytick_label = []
        vb.ytick_entrada = []
        vb.ytick_salida = []
        vb.ytick_salto = []
        vb.c_yticks = 0


def ck_col(e):
    # Funcion que modifica el checkbox que determina si se quieren todas las columnas del CSV o no
    if vb.c_titulos == 1:
        # Si se quieren todas
        vb.titulos_col.Hide()
        vb.c_titulos = 0
    else:
        # No se quieren todas
        vb.col_checked = []
        list_col = []
        vb.titulos_col.Clear()
        for i in range(vb.contador_col - 1):
            list_col.append(f"Columna {i+1}")
            vb.col_checked.append(True)
        vb.titulos_col = wx.CheckListBox(panel_principal, pos=(400, 240), choices=list_col)
        vb.titulos_col.Bind(wx.EVT_CHECKLISTBOX, lista_col)
        vb.c_titulos = 1


def lista_col(e):
    # Funcion para determinar que columnas se quieren del CSV
    for i in range(vb.contador_col - 1):
        vb.col_checked[i] = vb.titulos_col.IsChecked(i)


def cargar_archivo(e, numero, texto, tipo):
    # Funcion que abre una ventana para cargar o un video o un csv
    cargar = wx.Frame(None, -1, 'win.py')
    cargar.SetSize(0, 0, 200, 50)

    dlg = wx.FileDialog(cargar, texto, wildcard=tipo)

    if dlg.ShowModal() == wx.ID_OK:
        if numero == 1:
            vb.video = dlg.GetPath()
            cuadro1.SetValue(dlg.GetPath())
        else:
            # En el caso de que sea Un CSV se crearan los cuadros de texto dinamicamente y se eliminaran los anteriores
            for titu in vb.titulos_label:
                titu.Destroy()
            for titu in vb.titulos_input:
                titu.Destroy()
            vb.csv = dlg.GetPath()
            # Obtenemos el numero de columnas del csv
            vb.contador_col = col.columnas()
            vb.titulos_label = []
            vb.titulos_input = []

            for columna in range(vb.contador_col - 1):
                vb.titulos_label.append(
                    wx.StaticText(panel_principal, label=f"titulo {columna+1}", pos=(800, 40 + columna * 40)))
                vb.titulos_input.append(wx.TextCtrl(panel_principal, pos=(840, 40 + columna * 40)))
                vb.titulos_input[columna].Bind(wx.EVT_TEXT, partial(cambiar_titulos, lista=vb.titulos_input))
            cuadro2.SetValue(dlg.GetPath())


data = json.load(open("settings.json"))
list_col = []
colores_mat = ["Aqua", "Aquamarine", "Azure", "Beige", "Black", "Blue", "Brown", "Chartreuse", "Chocolate", "Coral",
               "Crimson", "Cyan", "Darkblue", "Darkgreen", "Fuchsia", "Gold", "Goldenrod", "Green", "Grey", "Indigo",
               "Ivory", "Khaki", "Lavander", "Lightblue", "Lightfreen", "Lime", "Magenta", "Matoon", "Navy", "Olive",
               "Orange", "Orangered", "Orchid", "Pink", "Plum", "Purple", "Red", "Salmon", "Sienna", "Silver", "Tan",
               "Teal", "Tomato", "Turquoise", "Violet", "Wheat", "White", "Yellow", "Yellowgreen"]
colores_wx = ["Aquamarine", "Black", "Blue", "Blue Violet", "Brown", "Cadet Blue", "Coral", "Cyan", "Dark Grey",
              "Dark Green", "Dark Slate Blue", "Dark Slate Grey", "Dark Turquoise", "Dim Grey", "Firebrick",
              "Forest Green", "Gold", "Goldenrod", "Grey", "Green", "Green Yellow", "Indian Red", "Khakhi",
              "Light Blue", "Light Grey", "Light Steel Blue", "Lime Green", "Magenta", "Maroon", "Medium Aquamarine",
              "Medium Blue", "MidNight Blue", "Navy", "Orange", "Orange Red", "Orchif", "Pale Green", "Pink", "Plum",
              "Purple", "Red", "Salmon", "Sea Green", "Sienna", "Sky Blue", "Slate Blue", "Spring Green", "Steel Blue",
              "Tan", "Thistle", "Tuquoise", "Violet", "Violet Red", "Wheat", "White", "Yellow", "Yellow Green"]
tamannos = ["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"]
tamannos2 = ["xx-small", "x-small", "small", "medium"]
fonts = ["Arial", "Times New Roman", "Verdana", "Courier New", "Comic Sans MS", "Impact", "Tahoma", "Trebuchet MS",
         "Georgia", "Century Gothic", "Garamond", "Lucida Console", "Bookman Old Style", "Book Antiqua", "Lucida Sans",
         "Monotype Corsiva", "Palatino Linotype"]

app = wx.App()
# El estilo que se le aplica a la ventana es el de por defecto pero quitandole la posibilidad de modificar el tamaño
menu_principal = wx.Frame(None, size=(1200, 600), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
menu_principal.Bind(wx.EVT_CLOSE, vb.cerrar)

panel_principal = wx.Panel(menu_principal)

# Elegir video y CSV
texto1 = wx.StaticText(panel_principal, label="Video", pos=(20, 40))
texto2 = wx.StaticText(panel_principal, label="CSV", pos=(20, 80))

cuadro1 = wx.TextCtrl(panel_principal, value=vb.video, pos=(70, 38), size=(175, -1), style=wx.TE_READONLY)
cuadro1.Bind(wx.EVT_TEXT, valores_texto)
cuadro2 = wx.TextCtrl(panel_principal, value=vb.csv, pos=(70, 78), size=(175, -1), style=wx.TE_READONLY)
cuadro2.Bind(wx.EVT_TEXT, valores_texto)

boton1 = wx.Button(panel_principal, label="Cargar video", pos=(260, 37))
boton2 = wx.Button(panel_principal, label="Cargar CSV", pos=(260, 77))
boton_salir = wx.Button(panel_principal, label="Salir", pos=(150, 500))
boton_previsualizar = wx.Button(panel_principal, label="Previsualizar video", pos=(20, 500))

boton1.Bind(wx.EVT_BUTTON, partial(cargar_archivo, texto="Carga el video", numero=1, tipo=""))
boton2.Bind(wx.EVT_BUTTON, partial(cargar_archivo, texto="Carga el CSV", numero=2, tipo="CSV files (.csv)|*.csv"))
boton_salir.Bind(wx.EVT_BUTTON, vb.cerrar)
boton_previsualizar.Bind(wx.EVT_BUTTON, pr.previsualizar)

# Checkbox
check = wx.CheckBox(panel_principal, label="Elegir colores personalizados", pos=(20, 115))
check.Bind(wx.EVT_CHECKBOX, cambiar)

# Colores
texto_back_rep = wx.StaticText(panel_principal, label="Color de fondo", pos=(20, 150))
ch_back_rep = wx.Choice(panel_principal, choices=colores_wx, pos=(120, 145))
cl_back_rep = wx.ColourPickerCtrl(panel_principal, pos=(120, 145), colour=(wx.WHITE))
cl_back_rep.Hide()
predeterminados(ch_back_rep, data["colores"]["color_fondo"], colores_wx)
ch_back_rep.Bind(wx.EVT_CHOICE, valores_choice)
cl_back_rep.Bind(wx.EVT_COLOURPICKER_CHANGED, valores_color)

texto_back_con = wx.StaticText(panel_principal, label="Color del contorno de las gráficas", pos=(20, 190))
ch_back_con = wx.Choice(panel_principal, choices=colores_mat, pos=(200, 185))
cl_back_con = wx.ColourPickerCtrl(panel_principal, pos=(200, 185), colour=(wx.BLACK))
cl_back_con.Hide()
predeterminados(ch_back_con, data["colores"]["color_contorno_grafica"], colores_mat)
ch_back_con.Bind(wx.EVT_CHOICE, valores_choice)
cl_back_con.Bind(wx.EVT_COLOURPICKER_CHANGED, valores_color)

texto_back_gr = wx.StaticText(panel_principal, label="Color de fondo de la gráfica", pos=(20, 230))
ch_back_gr = wx.Choice(panel_principal, choices=colores_mat, pos=(180, 225))
cl_back_gr = wx.ColourPickerCtrl(panel_principal, pos=(180, 225), colour=(wx.WHITE))
cl_back_gr.Hide()
predeterminados(ch_back_gr, data["colores"]["color_fondo_grafica"], colores_mat)
ch_back_gr.Bind(wx.EVT_CHOICE, valores_choice)
cl_back_gr.Bind(wx.EVT_COLOURPICKER_CHANGED, valores_color)

texto_linea_gr = wx.StaticText(panel_principal, label="Color de las líneas de la gráfica", pos=(20, 270))
ch_linea_gr = wx.Choice(panel_principal, choices=colores_mat, pos=(190, 265))
cl_linea_gr = wx.ColourPickerCtrl(panel_principal, pos=(190, 265), colour=(wx.BLUE))
cl_linea_gr.Hide()
predeterminados(ch_linea_gr, data["colores"]["color_lineas_grafica"], colores_mat)
ch_linea_gr.Bind(wx.EVT_CHOICE, valores_choice)
cl_linea_gr.Bind(wx.EVT_COLOURPICKER_CHANGED, valores_color)

texto_label_gr = wx.StaticText(panel_principal, label="Color de las etiquetas de la gráfica", pos=(20, 310))
ch_label_gr = wx.Choice(panel_principal, choices=colores_mat, pos=(210, 305))
cl_label_gr = wx.ColourPickerCtrl(panel_principal, pos=(210, 305), colour=(wx.BLACK))
cl_label_gr.Hide()
predeterminados(ch_label_gr, data["colores"]["color_etiquetas"], colores_mat)
ch_label_gr.Bind(wx.EVT_CHOICE, valores_choice)
cl_label_gr.Bind(wx.EVT_COLOURPICKER_CHANGED, valores_color)

texto_titulo_gr = wx.StaticText(panel_principal, label="Color de los títulos de la gráfica", pos=(20, 350))
ch_titulo_gr = wx.Choice(panel_principal, choices=colores_mat, pos=(210, 345))
cl_titulo_gr = wx.ColourPickerCtrl(panel_principal, pos=(210, 345), colour=(wx.BLACK))
cl_titulo_gr.Hide()
predeterminados(ch_titulo_gr, data["colores"]["color_titulos"], colores_mat)
ch_titulo_gr.Bind(wx.EVT_CHOICE, valores_choice)
cl_titulo_gr.Bind(wx.EVT_COLOURPICKER_CHANGED, valores_color)

# Intervalos de etiquetas
etiquetas = wx.StaticText(panel_principal, label="Intervalos de etiquetas", pos=(400, 40))
etiquetas_input = wx.TextCtrl(panel_principal, value=str(data["etiquetas"]["intervalos"]), pos=(540, 38),
                              size=(175, -1))
etiquetas_input.Bind(wx.EVT_TEXT, valores_texto)

# Grosor linea, fuente y tamaño del titulo de la grafica

grosor = wx.StaticText(panel_principal, label="Pixeles de tamaño de la línea del gráfico", pos=(400, 80))
grosor_input = wx.TextCtrl(panel_principal, value=str(data["grafica"]["pixeles_linea"]), pos=(630, 78), size=(80, -1))
grosor_input.Bind(wx.EVT_TEXT, valores_texto)

titulo_tam = wx.StaticText(panel_principal, label="Tamaño del título del gráfico", pos=(400, 120))
ch_titulo_tam = wx.Choice(panel_principal, choices=tamannos, pos=(630, 118))
predeterminados(ch_titulo_tam, data["grafica"]["tamanno_titulo"], tamannos)
ch_titulo_tam.Bind(wx.EVT_CHOICE, valores_choice)

titulo_fam = wx.StaticText(panel_principal, label="Fuente para el titulo", pos=(400, 160))
ch_titulo_fam = wx.Choice(panel_principal, choices=fonts, pos=(530, 158))
predeterminados(ch_titulo_fam, data["grafica"]["fuente_titulo"], fonts)
ch_titulo_fam.Bind(wx.EVT_CHOICE, valores_choice)

# Checkbox para si se quieren todas las columnas del CSV
check_col = wx.CheckBox(panel_principal, label="Elegir Columnas", pos=(400, 198))
check_col.Bind(wx.EVT_CHECKBOX, ck_col)

# Tiempo entrada y salida
s_entrada = wx.StaticText(panel_principal, label="Tiempo entrada del video (segundos)", pos=(400, 440))
s_entrada_input = wx.TextCtrl(panel_principal, value="0", pos=(600, 438), size=(80, -1))
s_entrada_input.Bind(wx.EVT_TEXT, valores_texto)

s_salida = wx.StaticText(panel_principal, label="Tiempo salida del video (segundos)", pos=(400, 480))
# Poner que si se deja a 0 se tomara el valor total del video
s_salida_input = wx.TextCtrl(panel_principal, value="0", pos=(590, 478), size=(80, -1))
s_salida_input.Bind(wx.EVT_TEXT, valores_texto)

# Angulo de rotacion de las etiquetas
angulo = wx.StaticText(panel_principal, label="Angulo de rotacion de las etiquetas", pos=(750, 480))
angulo_input = wx.TextCtrl(panel_principal, value=str(data["etiquetas"]["rotacion"]), pos=(950, 478), size=(80, -1))
angulo_input.Bind(wx.EVT_TEXT, valores_texto)

# Fuente y Tamaño de las etiquetas
fuente_etiqueta = wx.StaticText(panel_principal, label="Fuente de las etiquetas", pos=(750, 400))
ch_fuente_etiqueta = wx.Choice(panel_principal, choices=fonts, pos=(880, 398))
predeterminados(ch_fuente_etiqueta, data["grafica"]["fuente_etiqueta"], fonts)
ch_fuente_etiqueta.Bind(wx.EVT_CHOICE, valores_choice)

tamannos_etiqueta = wx.StaticText(panel_principal, label="Tamaño de las etiquetas", pos=(750, 440))
ch_tamannos_etiqueta = wx.Choice(panel_principal, choices=tamannos2, pos=(885, 438))
predeterminados(ch_tamannos_etiqueta, data["grafica"]["tamanno_etiqueta"], tamannos)
ch_tamannos_etiqueta.Bind(wx.EVT_CHOICE, valores_choice)

vb.titulos_col = wx.CheckListBox(panel_principal, pos=(400, 240), choices=list_col)
vb.titulos_col.Hide()

check_ytick = wx.CheckBox(panel_principal, label="Elegir etiquetas del eje y", pos=(800, 198))
check_ytick.Bind(wx.EVT_CHECKBOX, ck_ytick)

menu_principal.Show()
menu_principal.Centre()
app.MainLoop()
