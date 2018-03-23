import Variables as vb
import Previsualizar as pr
import wx
import matplotlib.pyplot as plt
from functools import partial


def valores_choice(e):
    vb.back_rep = ch_back_rep.GetString(ch_back_rep.GetCurrentSelection())
    vb.contorno = ch_back_con.GetString(ch_back_con.GetCurrentSelection())
    vb.background_gr = ch_back_gr.GetString(ch_back_gr.GetCurrentSelection())
    vb.color_linea_ = ch_linea_gr.GetString(ch_linea_gr.GetCurrentSelection())
    vb.label = ch_label_gr.GetString(ch_label_gr.GetCurrentSelection())

    # Conseguir el color en formato hexadecimal
    # vb.color_prueba = elegir_color.GetColour()
    # vb.color_prueba = vb.color_prueba.GetAsString(flags=wx.C2S_HTML_SYNTAX)


def valores_texto(e):
    vb.titulo1 = titulo1.GetValue()
    vb.titulo2 = titulo2.GetValue()


def cambiar(e):
    if vb.numero == 1:
        ch_linea_gr.Hide()
        ch_label_gr.Hide()
        ch_back_con.Hide()
        ch_back_gr.Hide()
        ch_back_rep.Hide()
        cl_back_con.Show()
        cl_back_rep.Show()
        cl_back_gr.Show()
        cl_label_gr.Show()
        cl_linea_gr.Show()
        vb.numero = 0
    else:
        ch_linea_gr.Show()
        ch_label_gr.Show()
        ch_back_con.Show()
        ch_back_gr.Show()
        ch_back_rep.Show()
        cl_back_con.Hide()
        cl_back_rep.Hide()
        cl_back_gr.Hide()
        cl_label_gr.Hide()
        cl_linea_gr.Hide()
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
numero = 1
app = wx.App()
menu_principal = wx.Frame(None, size=(400, 600))
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
check = wx.CheckBox(panel_principal, label="Elegir lo colores a mano", pos=(20, 115))
check.Bind(wx.EVT_CHECKBOX, cambiar)

# Colores
texto_back_rep = wx.StaticText(panel_principal, label="Color de fondo", pos=(20, 150))
ch_back_rep = wx.Choice(panel_principal, choices=colores, pos=(120, 145))
cl_back_rep = wx.ColourPickerCtrl(panel_principal, pos=(120, 145))
cl_back_rep.Hide()
ch_back_rep.SetSelection(11)
ch_back_rep.Bind(wx.EVT_CHOICE, valores_choice)

texto_back_con = wx.StaticText(panel_principal, label="Color del contorno d las gráficas", pos=(20, 190))
ch_back_con = wx.Choice(panel_principal, choices=colores, pos=(200, 185))
cl_back_con = wx.ColourPickerCtrl(panel_principal, pos=(200, 185))
cl_back_con.Hide()
ch_back_con.SetSelection(11)
ch_back_con.Bind(wx.EVT_CHOICE, valores_choice)

texto_back_gr = wx.StaticText(panel_principal, label="Color de fondo de la gráfica", pos=(20, 230))
ch_back_gr = wx.Choice(panel_principal, choices=colores, pos=(180, 225))
cl_back_gr = wx.ColourPickerCtrl(panel_principal, pos=(180, 225))
cl_back_gr.Hide()
ch_back_gr.SetSelection(11)
ch_back_gr.Bind(wx.EVT_CHOICE, valores_choice)

texto_linea_gr = wx.StaticText(panel_principal, label="Color de las líneas de la gráfica", pos=(20, 270))
ch_linea_gr = wx.Choice(panel_principal, choices=colores, pos=(190, 265))
cl_linea_gr = wx.ColourPickerCtrl(panel_principal, pos=(190, 265))
cl_linea_gr.Hide()
ch_linea_gr.SetSelection(11)
ch_linea_gr.Bind(wx.EVT_CHOICE, valores_choice)

texto_label_gr = wx.StaticText(panel_principal, label="Color de las etiquetas de la gráfica", pos=(20, 310))
ch_label_gr = wx.Choice(panel_principal, choices=colores, pos=(210, 305))
cl_label_gr = wx.ColourPickerCtrl(panel_principal, pos=(210, 305))
cl_label_gr.Hide()
ch_label_gr.SetSelection(11)
ch_label_gr.Bind(wx.EVT_CHOICE, valores_choice)

texto_titulo1 = wx.StaticText(panel_principal, label="Titulo 1", pos=(20, 355))
titulo1 = wx.TextCtrl(panel_principal, value=vb.titulo1, pos=(70, 352), size=(175, -1))
titulo1.Bind(wx.EVT_TEXT, valores_texto)

texto_titulo2 = wx.StaticText(panel_principal, label="Titulo 2", pos=(20, 395))
titulo2 = wx.TextCtrl(panel_principal, value=vb.titulo2, pos=(70, 392), size=(175, -1))
titulo2.Bind(wx.EVT_TEXT, valores_texto)

menu_principal.Show()
menu_principal.Centre()
app.MainLoop()
