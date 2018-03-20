import wx
import wx.media
import interfaz
import sys
import csv
import matplotlib.pyplot as plt
from datetime import datetime

app = wx.App()


def cerrar(e):
    # Funcion para cerrar el programa
    sys.exit(0)


def cargar_archivo(texto):
    # Funcion que se encarga de cargar la ruta de un archivo del SO
    cargar = wx.Frame(None, -1, 'win.py')
    cargar.SetSize(0, 0, 200, 50)

    dlg = wx.FileDialog(cargar, texto)

    if dlg.ShowModal() == wx.ID_OK:
        return dlg.GetPath()


def medio(e, barra_tiempo):
    # Cambiar por la variable csv y video
    previsualizar("imagen2.jpg", barra_tiempo=barra_tiempo)


def previsualizar(video, barra_tiempo):
    def cargado(e):
        print("cargado")
        reproductor.player.Play()
        timer.Start(1000)
        print(timer.IsRunning())


    def pause(e):
        print("pause")
        reproductor.player.Pause()
        timer.Stop()
        print(reproductor.player.Tell())

    def actualizar(e):
        print("actualizar")
        #reproductor.player.Tell()
        #Establezco el valor del slider segun la posicion del video
        slider.SetValue(reproductor.player.Tell()/1000)

        tiempo=568/len(barra_tiempo)
        movimiento=wx.Point(52+(slider.GetValue()*tiempo),30)
        barra_mover.SetPosition(movimiento)
        #print(slider.GetValue())


    # Destruir la ventana con el menu
    menu.Destroy()

    # Crear ventana para el video
    reproductor = interfaz.Menu(1500, 1000)
    reproductor.SetBackgroundColour("WHITE")
    # reproductor.Maximize()
    reproductor.Bind(wx.EVT_CLOSE, cerrar)

    # Creacion de sizers
    main_sizer = wx.GridSizer(2, 1, 0, 0)

    sizer_video = wx.GridSizer(1, 3, 0, 0)
    main_sizer.Add(sizer_video, 1, wx.EXPAND, 5)

    # sizer video
    izqvi = wx.BoxSizer(wx.VERTICAL)
    sizer_video.Add(izqvi, 1, wx.EXPAND, 5)
    centrovi = wx.BoxSizer(wx.VERTICAL)
    sizer_video.Add(centrovi, 1, wx.EXPAND, 5)
    dervi = wx.GridSizer(3, 1, 0, 0)
    # Aqui los sizer de dentro de Dervi
    sizer_video.Add(dervi, 1, wx.EXPAND, 5)

    # sizers grafica
    sizer_grafica = wx.GridSizer(1, 3, 0, 0)
    izqgr = wx.BoxSizer(wx.VERTICAL)

    sizer_grafica.Add(izqgr, 1, wx.EXPAND, 5)

    centrogr = wx.BoxSizer(wx.VERTICAL)

    sizer_grafica.Add(centrogr, 1, wx.EXPAND, 5)

    # dergr = wx.BoxSizer(wx.VERTICAL)

    # sizer_grafica.Add(dergr, 1, wx.EXPAND, 5)

    main_sizer.Add(sizer_grafica, 1, wx.EXPAND, 5)

    panel_video = wx.Panel(reproductor)
    centrovi.Add(panel_video)
    panel_izqvi = wx.Panel(reproductor)
    izqvi.Add(panel_izqvi)

    panel_grafica = wx.Panel(reproductor)
    centrogr.Add(panel_grafica)
    panel_izqgr=wx.Panel(reproductor)
    izqgr.Add(panel_izqgr)

    # Video
    boton_play = wx.Button(panel_izqvi, label="Play")
    boton_pause = wx.Button(panel_izqvi, label="Pause", pos=(30, 30))
    boton_play.Bind(wx.EVT_BUTTON,cargado)
    boton_pause.Bind(wx.EVT_BUTTON, pause)

    reproductor.player = wx.media.MediaCtrl(panel_video, pos=(0, 0), size=(500, 250))
    reproductor.player.ShowPlayerControls(flags=wx.media.MEDIACTRLPLAYERCONTROLS_VOLUME)
    # reproductor.Bind(wx.media.EVT_MEDIA_LOADED,cargado)
    reproductor.player.Load(r"madrid.mp4")
    # reproductor.player.Play()
    # print(reproductor.player.Length())

    # Barra y grafica

    # reproductor.Bind(wx.media.EVT_MEDIA_PAUSE,lambda e,ejex=ejex:barra(e,ejex))


    # Grafica

    wx.StaticBitmap(panel_grafica, -1, wx.Bitmap(name="grafico.png"), pos=(0, 0), size=(640, 480))

    # Slider
    timer=wx.Timer(reproductor.player)
    reproductor.player.Bind(wx.EVT_TIMER,actualizar,timer)


    slider=wx.Slider(reproductor,pos=(20,500),style=wx.SL_VALUE_LABEL)
    slider.SetRange(0,len(barra_tiempo))
    barra_mover=wx.StaticBitmap(panel_grafica, -1, wx.Bitmap(name="barra2.png"), pos=(52, 30))

    # Sizers

    reproductor.SetSizer(main_sizer)
    reproductor.Layout()

    reproductor.Centre(wx.BOTH)

    reproductor.Show()


def graficas(csvp):
    # Aqui se genera la imagen con la grafica

    with open(csvp) as fichero:
        leido = csv.reader(fichero, delimiter=';')

        tiempo = []
        x = []
        y = []
        z = []
        barra_tiempo = []

        for line in leido:
            tiempo.append(line[0])
            barra_tiempo.append(datetime.strptime(line[0], '%H:%M:%S'))
            y.append(float(line[1]))
            z.append(float(line[2]))

    # tiempo tiene todos los valores del tiempo del csv

    # Elegir cada cuanto quieres las etiquetas en la grafica
    usuario = 20

    # for para guardar solo los tiempos que interesan
    for i in range(0, len(tiempo), usuario):
        x.append(tiempo[i])

    # Cambia el color del fondo de la figura
    # fig = plt.figure(facecolor='red')
    fig = plt.figure()
    fig.subplots_adjust(top=0.95, bottom=0.15, left=0.08, right=0.97, hspace=0.60)

    gra1 = fig.add_subplot(2, 1, 1)
    gra1.plot(tiempo, y)
    # Establece donde empieza y donde acaba el eje x, con esa formula ajusta la grafica
    gra1.set_xlim(0, tiempo[len(tiempo) - 1])
    gra1.set_xticks(x)
    gra1.set_title('Atención')
    plt.xticks(rotation=70)

    gra2 = fig.add_subplot(2, 1, 2)
    gra2.plot(tiempo, z)
    gra2.set_xlim(0, tiempo[len(tiempo) - 1])
    gra2.set_xticks(x)
    gra2.set_title('Emoción')
    plt.xticks(rotation=70)
    # plt.show()
    # print(fig.get_facecolor())
    # Guarda el grafico con los colores especificados
    # plt.savefig("grafico.png",facecolor=fig.get_facecolor())
    plt.savefig("grafico.png")
    return barra_tiempo


print("bienvenido al programa")
print("Carga el archivo CSV")

# csvp=cargar_archivo("Cargar el CSV")
csvp = "real_madrid.csv"  # Para no tener que elegir siempre
# video=cargar_archivo("Cargar el video")


menu = interfaz.Menu(400, 300)

barra_tiempo = graficas(csvp)
panel = interfaz.Panel(menu, 0, 0, 400, 300)
texto1 = interfaz.Texto(panel, "Video", 20, 40)
texto2 = interfaz.Texto(panel, "CSV", 20, 80)

# Cambiar el cuadro de texto por el path
cuadro1 = interfaz.CuadroTexto(panel, "video", 70, 38, 175, -1)
cuadro2 = interfaz.CuadroTexto(panel, "csv", 70, 78, 175, -1)

btn_salir = interfaz.Boton(panel, "salir", 20, 120)
btn_salir.Bind(wx.EVT_BUTTON, cerrar, btn_salir)

btn_previsualizar = interfaz.Boton(panel, "Previsualizar video", 120, 120)
btn_previsualizar.Bind(wx.EVT_BUTTON, lambda e, tiempo=barra_tiempo: medio(e, tiempo))

btn_gen = interfaz.Boton(panel, "Generar video", 240, 120)

menu.Bind(wx.EVT_CLOSE, cerrar)
menu.Show()
app.MainLoop()
