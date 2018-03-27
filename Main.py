import Variables as vb
import Previsualizar as pr
import wx
from functools import partial


def valores_choice(e):
    vb.back_rep = ch_back_rep.GetString(ch_back_rep.GetCurrentSelection())
    vb.contorno = ch_back_con.GetString(ch_back_con.GetCurrentSelection())
    vb.background_gr = ch_back_gr.GetString(ch_back_gr.GetCurrentSelection())
    vb.color_linea = ch_linea_gr.GetString(ch_linea_gr.GetCurrentSelection())
    vb.label = ch_label_gr.GetString(ch_label_gr.GetCurrentSelection())
    vb.tamanno_tit = ch_titulo_tam.GetString(ch_titulo_tam.GetCurrentSelection())
    vb.titulo_gr = ch_titulo_gr.GetString(ch_titulo_gr.GetCurrentSelection())


def valores_color(e):
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

    # Conseguir el color en formato hexadecimal
    # vb.color_prueba = elegir_color.GetColour()
    # vb.color_prueba = vb.color_prueba.GetAsString(flags=wx.C2S_HTML_SYNTAX)


def valores_texto(e):
    vb.titulo1 = titulo1.GetValue()
    vb.titulo2 = titulo2.GetValue()
    vb.etiquetas = int(etiquetas_input.GetValue())
    vb.grosor = float(grosor_input.GetValue())
    vb.fuente_tit = ch_titulo_fam.GetValue()
    vb.l_gr = int(l_gr_input.GetValue())
    vb.t_gr = int(t_gr_input.GetValue())
    vb.l_rep = int(l_rep_input.GetValue())
    vb.t_rep = int(t_rep_input.GetValue())
    vb.l_log = int(l_log_input.GetValue())
    vb.t_log = int(t_log_input.GetValue())
    vb.s_entrada=int(s_entrada_input.GetValue())
    vb.s_salida=int(s_salida_input.GetValue())


def cambiar(e):
    if vb.numero == 1:
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
        vb.numero = 0
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
        vb.numero = 1


def cargar_archivo(e, numero, texto):
    cargar = wx.Frame(None, -1, 'win.py')
    cargar.SetSize(0, 0, 200, 50)

    dlg = wx.FileDialog(cargar, texto)

    if dlg.ShowModal() == wx.ID_OK:
        # return dlg.GetPath()
        if numero == 1:
            vb.video = dlg.GetPath()
            print(vb.video)
            cuadro1.write(dlg.GetPath())
        else:
            vb.csv = dlg.GetPath()
            cuadro2.write(dlg.GetPath())


colores = ["aqua", "aquamarine", "azure", "beige", "black", "blue", "brown", "chartreuse", "chocolate", "coral",
           "crimson", "white"]
tamannos = ["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"]
# familias=["serif","sans-serif","cursive","fantasy","monospace"]
app = wx.App()
# El estilo que se le aplica a la ventana es el de por defecto pero quitandole la posibilidad de modificar el tamaño
menu_principal = wx.Frame(None, size=(800, 600), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
menu_principal.Bind(wx.EVT_CLOSE, vb.cerrar)

panel_principal = wx.Panel(menu_principal)

# Elegir video y CSV
texto1 = wx.StaticText(panel_principal, label="Video", pos=(20, 40))
texto2 = wx.StaticText(panel_principal, label="CSV", pos=(20, 80))

cuadro1 = wx.TextCtrl(panel_principal, value=vb.video, pos=(70, 38), size=(175, -1))
cuadro2 = wx.TextCtrl(panel_principal, value=vb.csv, pos=(70, 78), size=(175, -1))

boton1 = wx.Button(panel_principal, label="Cargar video", pos=(260, 37))
boton2 = wx.Button(panel_principal, label="Cargar CSV", pos=(260, 77))
boton_salir = wx.Button(panel_principal, label="Salir", pos=(150, 500))
boton_previsualizar = wx.Button(panel_principal, label="Previsualizar video", pos=(20, 500))
# boton_gen = wx.Button(panel_principal, label="Generar video", pos=(250, 120))

boton1.Bind(wx.EVT_BUTTON, partial(cargar_archivo, texto="Carga el video", numero=1))
boton2.Bind(wx.EVT_BUTTON, partial(cargar_archivo, texto="Carga el CSV", numero=2))
boton_salir.Bind(wx.EVT_BUTTON, vb.cerrar)
boton_previsualizar.Bind(wx.EVT_BUTTON, pr.previsualizar)

# Checkbox
check = wx.CheckBox(panel_principal, label="Elegir colores personalizados", pos=(20, 115))
check.Bind(wx.EVT_CHECKBOX, cambiar)

# Colores
texto_back_rep = wx.StaticText(panel_principal, label="Color de fondo", pos=(20, 150))
ch_back_rep = wx.Choice(panel_principal, choices=colores, pos=(120, 145))
cl_back_rep = wx.ColourPickerCtrl(panel_principal, pos=(120, 145))
cl_back_rep.Hide()
ch_back_rep.SetSelection(11)
ch_back_rep.Bind(wx.EVT_CHOICE, valores_choice)
cl_back_rep.Bind(wx.EVT_COLOURPICKER_CHANGED, valores_color)

texto_back_con = wx.StaticText(panel_principal, label="Color del contorno de las gráficas", pos=(20, 190))
ch_back_con = wx.Choice(panel_principal, choices=colores, pos=(200, 185))
cl_back_con = wx.ColourPickerCtrl(panel_principal, pos=(200, 185))
cl_back_con.Hide()
ch_back_con.SetSelection(4)
ch_back_con.Bind(wx.EVT_CHOICE, valores_choice)
cl_back_con.Bind(wx.EVT_COLOURPICKER_CHANGED, valores_color)

texto_back_gr = wx.StaticText(panel_principal, label="Color de fondo de la gráfica", pos=(20, 230))
ch_back_gr = wx.Choice(panel_principal, choices=colores, pos=(180, 225))
cl_back_gr = wx.ColourPickerCtrl(panel_principal, pos=(180, 225))
cl_back_gr.Hide()
ch_back_gr.SetSelection(11)
ch_back_gr.Bind(wx.EVT_CHOICE, valores_choice)
cl_back_gr.Bind(wx.EVT_COLOURPICKER_CHANGED, valores_color)

texto_linea_gr = wx.StaticText(panel_principal, label="Color de las líneas de la gráfica", pos=(20, 270))
ch_linea_gr = wx.Choice(panel_principal, choices=colores, pos=(190, 265))
cl_linea_gr = wx.ColourPickerCtrl(panel_principal, pos=(190, 265))
cl_linea_gr.Hide()
ch_linea_gr.SetSelection(5)
ch_linea_gr.Bind(wx.EVT_CHOICE, valores_choice)
cl_linea_gr.Bind(wx.EVT_COLOURPICKER_CHANGED, valores_color)

texto_label_gr = wx.StaticText(panel_principal, label="Color de las etiquetas de la gráfica", pos=(20, 310))
ch_label_gr = wx.Choice(panel_principal, choices=colores, pos=(210, 305))
cl_label_gr = wx.ColourPickerCtrl(panel_principal, pos=(210, 305))
cl_label_gr.Hide()
ch_label_gr.SetSelection(4)
ch_label_gr.Bind(wx.EVT_CHOICE, valores_choice)
cl_label_gr.Bind(wx.EVT_COLOURPICKER_CHANGED, valores_color)

texto_titulo_gr = wx.StaticText(panel_principal, label="Color de los títulos de la gráfica", pos=(20, 350))
ch_titulo_gr = wx.Choice(panel_principal, choices=colores, pos=(210, 345))
cl_titulo_gr = wx.ColourPickerCtrl(panel_principal, pos=(210, 345))
cl_titulo_gr.Hide()
ch_titulo_gr.SetSelection(4)
ch_titulo_gr.Bind(wx.EVT_CHOICE, valores_choice)
cl_titulo_gr.Bind(wx.EVT_COLOURPICKER_CHANGED, valores_color)
# Intervalos de etiquetas

etiquetas = wx.StaticText(panel_principal, label="Intervalos de etiquetas", pos=(400, 40))
etiquetas_input = wx.TextCtrl(panel_principal, value="30", pos=(540, 38), size=(175, -1))
etiquetas_input.Bind(wx.EVT_TEXT, valores_texto)

# Grosor linea, fuente y tamaño del titulo de la grafica

grosor = wx.StaticText(panel_principal, label="Pixeles de tamaño de la línea del gráfico", pos=(400, 80))
grosor_input = wx.TextCtrl(panel_principal, value="1.5", pos=(630, 78), size=(80, -1))
grosor_input.Bind(wx.EVT_TEXT, valores_texto)

titulo_tam = wx.StaticText(panel_principal, label="Tamaño del título del gráfico", pos=(400, 120))
ch_titulo_tam = wx.Choice(panel_principal, choices=tamannos, pos=(630, 118))
ch_titulo_tam.SetSelection(4)
ch_titulo_tam.Bind(wx.EVT_CHOICE, valores_choice)

titulo_fam = wx.StaticText(panel_principal, label="Fuente para el titulo", pos=(400, 160))
ch_titulo_fam = wx.TextCtrl(panel_principal, pos=(530, 158), size=(80, -1))
ch_titulo_fam.Bind(wx.EVT_TEXT, valores_texto)
# ch_titulo_fam = wx.Choice(panel_principal, choices=familias, pos=(530, 158))

# Anchura y Altura de Grafica Reproductor y Logotipo

# Poner un titulo

# Grafica
l_gr = wx.StaticText(panel_principal, label="Distancia desde la izquierda (Grafica)", pos=(400, 200))
l_gr_input = wx.TextCtrl(panel_principal, value="640", pos=(600, 198), size=(80, -1))
l_gr_input.Bind(wx.EVT_TEXT, valores_texto)

t_gr = wx.StaticText(panel_principal, label="Distancia desde arriba(Grafica)", pos=(400, 240))
t_gr_input = wx.TextCtrl(panel_principal, value="530", pos=(565, 238), size=(80, -1))
t_gr_input.Bind(wx.EVT_TEXT, valores_texto)

# Reproductor
l_rep = wx.StaticText(panel_principal, label="Distancia desde la izquierda (Reproductor)", pos=(400, 280))
l_rep_input = wx.TextCtrl(panel_principal, value="640", pos=(630, 278), size=(80, -1))
l_rep_input.Bind(wx.EVT_TEXT, valores_texto)

t_rep = wx.StaticText(panel_principal, label="Distancia desde arriba (Reproductor)", pos=(400, 320))
t_rep_input = wx.TextCtrl(panel_principal, value="0", pos=(600, 318), size=(80, -1))
t_rep_input.Bind(wx.EVT_TEXT, valores_texto)

# Logotipo
l_log = wx.StaticText(panel_principal, label="Distancia desde la izquierda (Logotipo)", pos=(400, 360))
l_log_input = wx.TextCtrl(panel_principal, value="1400", pos=(610, 358), size=(80, -1))
l_log_input.Bind(wx.EVT_TEXT, valores_texto)

t_log = wx.StaticText(panel_principal, label="Distancia desde arriba (Logotipo)", pos=(400, 400))
t_log_input = wx.TextCtrl(panel_principal, value="0", pos=(580, 398), size=(80, -1))
t_log_input.Bind(wx.EVT_TEXT, valores_texto)

# Tiempo entrada y salida
s_entrada = wx.StaticText(panel_principal, label="Tiempo entrada del video (segundos)", pos=(400, 440))
s_entrada_input = wx.TextCtrl(panel_principal, value="0", pos=(600, 438), size=(80, -1))
s_entrada_input.Bind(wx.EVT_TEXT, valores_texto)


s_salida = wx.StaticText(panel_principal, label="Tiempo salida del video (segundos)", pos=(400, 480))
# Poner que si se deja a 0 se tomara el valor total del video
s_salida_input = wx.TextCtrl(panel_principal, value="0", pos=(590, 478), size=(80, -1))
s_salida_input.Bind(wx.EVT_TEXT, valores_texto)

# Titulos de las graficas
texto_titulo1 = wx.StaticText(panel_principal, label="Titulo 1", pos=(20, 395))
titulo1 = wx.TextCtrl(panel_principal, value=vb.titulo1, pos=(70, 392), size=(175, -1))
titulo1.Bind(wx.EVT_TEXT, valores_texto)

texto_titulo2 = wx.StaticText(panel_principal, label="Titulo 2", pos=(20, 435))
titulo2 = wx.TextCtrl(panel_principal, value=vb.titulo2, pos=(70, 432), size=(175, -1))
titulo2.Bind(wx.EVT_TEXT, valores_texto)

menu_principal.Show()
menu_principal.Centre()
app.MainLoop()
