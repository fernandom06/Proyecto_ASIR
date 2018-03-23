import Variables as vb
import Previsualizar as pr
import wx
from functools import partial

def valores_choice(e):
    vb.back_rep=ch_back_rep.GetString(ch_back_rep.GetCurrentSelection())
    vb.contorno=ch_back_con.GetString(ch_back_con.GetCurrentSelection())
    vb.background_gr=ch_back_gr.GetString(ch_back_gr.GetCurrentSelection())
    vb.color_linea_=ch_linea_gr.GetString(ch_linea_gr.GetCurrentSelection())
    vb.label=ch_label_gr.GetString(ch_label_gr.GetCurrentSelection())

def valores_texto(e):
    vb.titulo1=titulo1.GetValue()
    vb.titulo2=titulo2.GetValue()

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


colores=["aqua","aquamarine","azure","beige","black","blue","brown","chartreuse","chocolate","coral","crimson","white"]
app = wx.App()
menu_principal = wx.Frame(None,size=(400,600))
menu_principal.Bind(wx.EVT_CLOSE, vb.cerrar)

panel_principal = wx.Panel(menu_principal)

texto1 = wx.StaticText(panel_principal, label="Video", pos=(20, 40))
texto2 = wx.StaticText(panel_principal, label="CSV", pos=(20, 80))

cuadro1 = wx.TextCtrl(panel_principal, value=vb.video, pos=(70, 38), size=(175, -1))
cuadro2 = wx.TextCtrl(panel_principal, value=vb.csv, pos=(70, 78), size=(175, -1))

boton1 = wx.Button(panel_principal, label="Cargar video", pos=(260, 37))
boton2 = wx.Button(panel_principal, label="Cargar CSV", pos=(260, 77))
boton_salir=wx.Button(panel_principal,label="Salir",pos=(150,500))
boton_previsualizar = wx.Button(panel_principal, label="Previsualizar video", pos=(20, 500))
# boton_gen = wx.Button(panel_principal, label="Generar video", pos=(250, 120))

boton1.Bind(wx.EVT_BUTTON, partial(cargar_archivo, texto="Carga el video", numero=1))
boton2.Bind(wx.EVT_BUTTON, partial(cargar_archivo, texto="Carga el CSV", numero=2))
boton_salir.Bind(wx.EVT_BUTTON,vb.cerrar)
boton_previsualizar.Bind(wx.EVT_BUTTON,pr.previsualizar)

texto_back_rep = wx.StaticText(panel_principal, label="Color de fondo", pos=(20, 130))
ch_back_rep=wx.Choice(panel_principal,choices=colores,pos=(120,125))
ch_back_rep.SetSelection(11)
ch_back_rep.Bind(wx.EVT_CHOICE,valores_choice)

texto_back_con=wx.StaticText(panel_principal, label="Color del contorno d las gráficas", pos=(20, 170))
ch_back_con=wx.Choice(panel_principal,choices=colores,pos=(200,165))
ch_back_con.SetSelection(11)
ch_back_con.Bind(wx.EVT_CHOICE,valores_choice)

texto_back_gr=wx.StaticText(panel_principal, label="Color de fondo de la gráfica", pos=(20, 210))
ch_back_gr=wx.Choice(panel_principal,choices=colores,pos=(180,205))
ch_back_gr.SetSelection(11)
ch_back_gr.Bind(wx.EVT_CHOICE,valores_choice)

texto_linea_gr=wx.StaticText(panel_principal, label="Color de las líneas de la gráfica", pos=(20, 250))
ch_linea_gr=wx.Choice(panel_principal,choices=colores,pos=(190,245))
ch_linea_gr.SetSelection(11)
ch_linea_gr.Bind(wx.EVT_CHOICE,valores_choice)

texto_label_gr=wx.StaticText(panel_principal, label="Color de las etiquetas de la gráfica", pos=(20, 290))
ch_label_gr=wx.Choice(panel_principal,choices=colores,pos=(210,285))
ch_label_gr.SetSelection(11)
ch_label_gr.Bind(wx.EVT_CHOICE,valores_choice)

texto_titulo1=wx.StaticText(panel_principal, label="Titulo 1", pos=(20, 335))
titulo1 = wx.TextCtrl(panel_principal, value=vb.titulo1, pos=(70, 332), size=(175, -1))
titulo1.Bind(wx.EVT_TEXT,valores_texto)

texto_titulo2=wx.StaticText(panel_principal, label="Titulo 2", pos=(20, 375))
titulo2 = wx.TextCtrl(panel_principal, value=vb.titulo2, pos=(70, 372), size=(175, -1))
titulo2.Bind(wx.EVT_TEXT,valores_texto)

menu_principal.Show()
menu_principal.Centre()
app.MainLoop()
