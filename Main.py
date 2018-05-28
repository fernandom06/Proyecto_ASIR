import Variables as vb
import Previsualizar as pr
import wx
from functools import partial
import Columnas as col
import json


def valores_choice(e):
    # Funcion que recoge los valores de los select
    vb.back_rep = ch_back_rep.GetString(ch_back_rep.GetCurrentSelection())
    vb.background_gr = ch_back_gr.GetString(ch_back_gr.GetCurrentSelection())


def valores_color(e):
    # Funcion que recoge los colores de los input de tipo color
    vb.back_rep = cl_back_rep.GetColour()
    vb.back_rep = vb.back_rep.GetAsString(flags=wx.C2S_HTML_SYNTAX)
    vb.background_gr = cl_back_gr.GetColour()
    vb.background_gr = vb.background_gr.GetAsString(flags=wx.C2S_HTML_SYNTAX)


def valores_texto(e):
    # Funcion que recoge los valores de los cuadros de texto
    vb.etiquetas = int(etiquetas_input.GetValue())
    vb.s_entrada = int(s_entrada_input.GetValue())
    vb.s_salida = int(s_salida_input.GetValue())
    vb.angulo_gr = int(angulo_input.GetValue())


def cambiar(e):
    # Funcion para cambiar entre los controles de lista para los colores o los input de tipo color
    if vb.checkbox == 1:
        ch_back_gr.Hide()
        ch_back_rep.Hide()
        cl_back_rep.Show()
        cl_back_gr.Show()
        vb.checkbox = 0
    else:
        ch_back_gr.Show()
        ch_back_rep.Show()
        cl_back_rep.Hide()
        cl_back_gr.Hide()
        vb.checkbox = 1


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
                wx.StaticText(panel_principal, label=f"Columna {i+1}", pos=(400, 475 + i * 40)))
            vb.ytick_entrada.append(wx.TextCtrl(panel_principal, pos=(465, 470 + i * 40), size=(40, -1)))
            vb.ytick_entrada[i].Bind(wx.EVT_TEXT, partial(cambiar_ytick_entrada, entrada=vb.ytick_entrada))
            vb.ytick_entrada[i].Bind(wx.EVT_ENTER_WINDOW, dentro)
            vb.ytick_entrada[i].Bind(wx.EVT_LEAVE_WINDOW, fuera)
            vb.ytick_entrada_fin.append(0)
            vb.ytick_salida.append(wx.TextCtrl(panel_principal, pos=(535, 470 + i * 40), size=(40, -1)))
            vb.ytick_salida[i].Bind(wx.EVT_TEXT, partial(cambiar_ytick_salida, entrada=vb.ytick_salida))
            vb.ytick_salida[i].Bind(wx.EVT_ENTER_WINDOW, dentro)
            vb.ytick_salida[i].Bind(wx.EVT_LEAVE_WINDOW, fuera)
            vb.ytick_salida_fin.append(0)
            vb.ytick_salto.append(wx.TextCtrl(panel_principal, pos=(610, 470 + i * 40), size=(40, -1)))
            vb.ytick_salto[i].Bind(wx.EVT_TEXT, partial(cambiar_ytick_salto, entrada=vb.ytick_salto))
            vb.ytick_salto[i].Bind(wx.EVT_ENTER_WINDOW, dentro)
            vb.ytick_salto[i].Bind(wx.EVT_LEAVE_WINDOW, fuera)
            vb.ytick_salto_fin.append(0)
        inicio_ytick.Show()
        fin_ytick.Show()
        saltos_ytick.Show()
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
        inicio_ytick.Hide()
        fin_ytick.Hide()
        saltos_ytick.Hide()
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
        vb.titulos_col = wx.CheckListBox(panel_principal, pos=(25, 460), choices=list_col)
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
            try:
                vb.csv = dlg.GetPath()
                # Obtenemos el numero de columnas del csv
                vb.contador_col = col.columnas()
                cuadro2.SetValue(dlg.GetPath())
            except:
                error = wx.MessageDialog(menu_principal, "Archivo no valido", "Error",
                                         wx.OK | wx.ICON_EXCLAMATION)
                error.ShowModal()
                error.Centre()


def dentro(e):
    vb.cursor = wx.Cursor(wx.CURSOR_IBEAM)
    menu_principal.SetCursor(vb.cursor)


def fuera(e):
    vb.cursor = wx.Cursor(wx.CURSOR_ARROW)
    menu_principal.SetCursor(vb.cursor)


def previsualizar(e):
    if vb.video == "":
        error = wx.MessageDialog(menu_principal, "No se ha cargado ningun video", "Error", wx.OK | wx.ICON_EXCLAMATION)
        error.ShowModal()
        error.Centre()
    try:
        vb.cursor = wx.Cursor(wx.CURSOR_WAIT)
        menu_principal.SetCursor(vb.cursor)
        pr.previsualizar(e)
        vb.cursor = wx.Cursor(wx.CURSOR_DEFAULT)
        menu_principal.SetCursor(vb.cursor)
    except FileNotFoundError:
        vb.cursor = wx.Cursor(wx.CURSOR_ARROW)
        menu_principal.SetCursor(vb.cursor)
        error = wx.MessageDialog(menu_principal, "No se ha cargado el CSV", "Error", wx.OK | wx.ICON_ERROR)
        error.ShowModal()
        error.Centre()
    except ValueError:
        vb.cursor = wx.Cursor(wx.CURSOR_ARROW)
        menu_principal.SetCursor(vb.cursor)
        error = wx.MessageDialog(menu_principal, "Las etiquetas del eje Y no estan bien definidas", "Error", wx.OK | wx.ICON_ERROR)
        error.ShowModal()
        error.Centre()
    except ZeroDivisionError:
        vb.cursor = wx.Cursor(wx.CURSOR_ARROW)
        menu_principal.SetCursor(vb.cursor)
        error = wx.MessageDialog(menu_principal, "Las etiquetas del eje Y no estan bien definidas", "Error", wx.OK | wx.ICON_ERROR)
        error.ShowModal()
        error.Centre()
    except IndexError:
        vb.cursor = wx.Cursor(wx.CURSOR_ARROW)
        menu_principal.SetCursor(vb.cursor)
        error = wx.MessageDialog(menu_principal, "El archivo JSON no esta bien editado", "Error", wx.OK | wx.ICON_ERROR)
        error.ShowModal()
        error.Centre()


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
menu_principal = wx.Frame(None, size=(800, 700), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
menu_principal.Bind(wx.EVT_CLOSE, vb.cerrar)

panel_principal = wx.Panel(menu_principal)

#Bienvenida
wx.StaticLine(panel_principal,pos=(20,80),size=(740,-1))
bienvenida=wx.StaticText(panel_principal,pos=(220,20),label="Selección de Parámetros")
font_bienvenida = wx.Font(20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
font_titulo = wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
bienvenida.SetFont(wx.Font(font_bienvenida))
bienvenida.SetForegroundColour("#244ABF")

# Elegir video y CSV
titulo_archivos=wx.StaticText(panel_principal,pos=(25,120),label="Archivos   ")
titulo_archivos.SetFont(font_titulo)
titulo_archivos.SetForegroundColour("#3982E8")
wx.StaticLine(panel_principal,pos=(25,140),size=(80,-1))
texto1 = wx.StaticText(panel_principal, label="Video", pos=(20, 160))
texto2 = wx.StaticText(panel_principal, label="CSV", pos=(20, 200))

cuadro1 = wx.TextCtrl(panel_principal, value=vb.video, pos=(70, 158), size=(175, -1), style=wx.TE_READONLY)
cuadro1.Bind(wx.EVT_TEXT, valores_texto)
cuadro2 = wx.TextCtrl(panel_principal, value=vb.csv, pos=(70, 198), size=(175, -1), style=wx.TE_READONLY)
cuadro2.Bind(wx.EVT_TEXT, valores_texto)

boton1 = wx.Button(panel_principal, label="Cargar video", pos=(260, 157))
boton2 = wx.Button(panel_principal, label="Cargar CSV", pos=(260, 197))
boton_salir = wx.Button(panel_principal, label="Salir", pos=(150, 580))
boton_previsualizar = wx.Button(panel_principal, label="Previsualizar video", pos=(20, 580))

boton1.Bind(wx.EVT_BUTTON, partial(cargar_archivo, texto="Carga el video", numero=1, tipo=""))
boton2.Bind(wx.EVT_BUTTON, partial(cargar_archivo, texto="Carga el CSV", numero=2, tipo="CSV files (.csv)|*.csv"))
boton_salir.Bind(wx.EVT_BUTTON, vb.cerrar)
boton_previsualizar.Bind(wx.EVT_BUTTON, previsualizar)

# Checkbox
titulo_colores=wx.StaticText(panel_principal,pos=(25,250),label="Colores   ")
titulo_colores.SetFont(font_titulo)
titulo_colores.SetForegroundColour("#3982E8")
wx.StaticLine(panel_principal,pos=(25,270),size=(80,-1))
check = wx.CheckBox(panel_principal, label="Elegir colores personalizados", pos=(20, 285))
check.SetValue(True)
check.Bind(wx.EVT_CHECKBOX, cambiar)

# Colores
texto_back_rep = wx.StaticText(panel_principal, label="Color de fondo", pos=(20, 320))
ch_back_rep = wx.Choice(panel_principal, choices=colores_wx, pos=(120, 315))
cl_back_rep = wx.ColourPickerCtrl(panel_principal, pos=(120, 315), colour=(wx.WHITE))
ch_back_rep.Hide()
ch_back_rep.SetSelection(0)
cl_back_rep.SetColour(data["colores"]["color_fondo"])
ch_back_rep.Bind(wx.EVT_CHOICE, valores_choice)
cl_back_rep.Bind(wx.EVT_COLOURPICKER_CHANGED, valores_color)

texto_back_gr = wx.StaticText(panel_principal, label="Color de fondo de la gráfica", pos=(20, 350))
ch_back_gr = wx.Choice(panel_principal, choices=colores_mat, pos=(180, 345))
cl_back_gr = wx.ColourPickerCtrl(panel_principal, pos=(180, 345), colour=(wx.WHITE))
ch_back_gr.Hide()
ch_back_gr.SetSelection(0)
cl_back_gr.SetColour(data["colores"]["color_fondo_grafica"])
ch_back_gr.Bind(wx.EVT_CHOICE, valores_choice)
cl_back_gr.Bind(wx.EVT_COLOURPICKER_CHANGED, valores_color)

# Checkbox para si se quieren todas las columnas del CSV
titulo_columnas=wx.StaticText(panel_principal,pos=(25,380),label="Columnas   ")
titulo_columnas.SetFont(font_titulo)
titulo_columnas.SetForegroundColour("#3982E8")
wx.StaticLine(panel_principal,pos=(25,400),size=(85,-1))
check_col = wx.CheckBox(panel_principal, label="Elegir Columnas", pos=(25, 420))
check_col.Bind(wx.EVT_CHECKBOX, ck_col)

vb.titulos_col = wx.CheckListBox(panel_principal, pos=(25, 540), choices=list_col)
vb.titulos_col.Hide()

# Intervalos de etiquetas
titulo_xticks=wx.StaticText(panel_principal,pos=(405,120),label="Etiquetas eje X   ")
titulo_xticks.SetFont(font_titulo)
titulo_xticks.SetForegroundColour("#3982E8")
wx.StaticLine(panel_principal,pos=(405,140),size=(127,-1))
etiquetas = wx.StaticText(panel_principal, label="Intervalos de etiquetas", pos=(400, 160))
etiquetas_input = wx.TextCtrl(panel_principal, value=str(data["etiquetas"]["intervalos"]), pos=(540, 158),
                              size=(80, -1))
etiquetas_input.Bind(wx.EVT_TEXT, valores_texto)
etiquetas_input.Bind(wx.EVT_ENTER_WINDOW, dentro)
etiquetas_input.Bind(wx.EVT_LEAVE_WINDOW, fuera)

# Angulo de rotacion de las etiquetas
angulo = wx.StaticText(panel_principal, label="Angulo de rotacion de las etiquetas", pos=(400, 200))
angulo_input = wx.TextCtrl(panel_principal, value=str(data["etiquetas"]["rotacion"]), pos=(600, 198), size=(80, -1))
angulo_input.Bind(wx.EVT_TEXT, valores_texto)
angulo_input.Bind(wx.EVT_ENTER_WINDOW, dentro)
angulo_input.Bind(wx.EVT_LEAVE_WINDOW, fuera)

# Tiempo entrada y salida
titulo_tiempo=wx.StaticText(panel_principal,pos=(405,250),label="Tiempo de entrada   ")
titulo_tiempo.SetForegroundColour("#3982E8")
titulo_tiempo.SetFont(font_titulo)
wx.StaticLine(panel_principal,pos=(405,270),size=(152,-1))
s_entrada = wx.StaticText(panel_principal, label="Tiempo entrada del video (segundos)", pos=(400, 285))
s_entrada_input = wx.TextCtrl(panel_principal, value="0", pos=(600, 285), size=(80, -1))
s_entrada_input.Bind(wx.EVT_TEXT, valores_texto)
s_entrada_input.Bind(wx.EVT_ENTER_WINDOW, dentro)
s_entrada_input.Bind(wx.EVT_LEAVE_WINDOW, fuera)

s_salida = wx.StaticText(panel_principal, label="Tiempo salida del video (segundos)", pos=(400, 325))
s_salida_input = wx.TextCtrl(panel_principal, value="0", pos=(590, 325), size=(80, -1))
s_salida_input.Bind(wx.EVT_TEXT, valores_texto)
s_salida_input.Bind(wx.EVT_ENTER_WINDOW, dentro)
s_salida_input.Bind(wx.EVT_LEAVE_WINDOW, fuera)

# Etiquetas eje Y
titulo_yticks=wx.StaticText(panel_principal,pos=(405,360),label="Etiquetas eje Y   ")
titulo_yticks.SetFont(font_titulo)
titulo_yticks.SetForegroundColour("#3982E8")
wx.StaticLine(panel_principal,pos=(405,380),size=(127,-1))
check_ytick = wx.CheckBox(panel_principal, label="Elegir etiquetas del eje y", pos=(400, 400))
check_ytick.Bind(wx.EVT_CHECKBOX, ck_ytick)

inicio_ytick = wx.StaticText(panel_principal, label="(inicio)", pos=(460, 435))
inicio_ytick.Hide()
fin_ytick = wx.StaticText(panel_principal, label="(final)", pos=(530, 435))
fin_ytick.Hide()
saltos_ytick = wx.StaticText(panel_principal, label="(longitud del salto)", pos=(585, 435))
saltos_ytick.Hide()

menu_principal.Show()
menu_principal.Centre()
app.MainLoop()
