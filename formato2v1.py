import wx
import wx.media
import interfaz
import sys
import csv
import matplotlib.pyplot as plt

app=wx.App()
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

def medio(e):
    # Cambiar por la variable csv y video
    previsualizar("imagen2.jpg")



def previsualizar(video):

    def cargado(e):
        print("cargado")
        reproductor.player.Play()

    def barra(e):
        print("hola")

    def pause(e):
        reproductor.player.Pause()

    #Destruir la ventana con el menu
    menu.Destroy()

    #Crear ventana para el video
    reproductor=interfaz.Menu(1500,1000)
    reproductor.SetBackgroundColour("WHITE")
    reproductor.Bind(wx.EVT_CLOSE,cerrar)

    # Creacion de sizers
    main_sizer = wx.GridSizer(2, 1, 0, 0)

    sizer_video = wx.GridSizer(0, 2, 0, 0)
    main_sizer.Add(sizer_video, 1, wx.EXPAND, 5)

    sizer_grafica = wx.GridSizer(0, 2, 0, 0)
    main_sizer.Add(sizer_grafica, 1, wx.EXPAND, 5)

    panel_video = wx.Panel(reproductor)
    sizer_video.Add(panel_video)

    panel_grafica = wx.Panel(reproductor)
    sizer_grafica.Add(panel_grafica)

    #Video
    boton_play=wx.Button(panel_video,label="Play")
    boton_pause=wx.Button(panel_grafica,label="Pause")
    boton_play.Bind(wx.EVT_BUTTON,cargado)
    boton_pause.Bind(wx.EVT_BUTTON,pause)

    reproductor.player = wx.media.MediaCtrl(panel_video, pos=(250, 0), size=(500, 250))
    #reproductor.Bind(wx.media.EVT_MEDIA_LOADED,cargado)
    reproductor.player.Load(r"Cabecera.mp4")
    #reproductor.player.Play()
    #print(reproductor.player.Length())



    #Barra y grafica

    reproductor.Bind(wx.media.EVT_MEDIA_PAUSE,barra)

    #Grafica

    wx.StaticBitmap(panel_grafica,-1,wx.Bitmap(name="grafico.png"),pos=(420,0),size=(640,480))

    #Slider

    #slider=wx.Slider(panel_grafica)
    wx.StaticBitmap(panel_grafica,-1,wx.Bitmap(name="barra.png"),pos=(420,30))

    #Sizers

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

        for line in leido:
            tiempo.append(line[0])
            y.append(float(line[1]))
            z.append(float(line[2]))

    # tiempo tiene todos los valores del tiempo del csv

    # Elegir cada cuanto quieres las etiquetas en la grafica
    usuario = 10

    # for para guardar solo los tiempos que interesan
    for i in range(0, len(tiempo), usuario):
        x.append(tiempo[i])

    # Cambia el color del fondo de la figura
    # fig = plt.figure(facecolor='red')
    fig = plt.figure()
    fig.subplots_adjust(top=0.96, bottom=0.15, left=0.08, right=0.97, hspace=0.47)

    gra1 = fig.add_subplot(2, 1, 1)
    gra1.plot(tiempo, y)
    # Establece donde empieza y donde acaba el eje x, con esa formula ajusta la grafica perfectamente
    gra1.set_xlim(0, x[len(x) - 1])
    gra1.set_xticks(x)
    plt.xticks(rotation=70)

    gra2 = fig.add_subplot(2, 1, 2)
    gra2.plot(tiempo, z)
    gra2.set_xlim(0, x[len(x) - 1])
    gra2.set_xticks(x)

    plt.xticks(rotation=70)
    # plt.show()
    #print(fig.get_facecolor())
    # Guarda el grafico con los colores especificados
    # plt.savefig("grafico.png",facecolor=fig.get_facecolor())
    plt.savefig("grafico.png")

print("bienvenido al programa")
print("Carga el archivo CSV")

#csvp=cargar_archivo("Cargar el CSV")
csvp="real_madrid.csv" # Para no tener que elegir siempre
#video=cargar_archivo("Cargar el video")


menu=interfaz.Menu(400,300)

graficas(csvp)
panel=interfaz.Panel(menu,0,0,400,300)
texto1=interfaz.Texto(panel,"Video",20,40)
texto2=interfaz.Texto(panel,"CSV",20,80)

# Cambiar el cuadro de texto por el path
cuadro1=interfaz.CuadroTexto(panel,"video",70,38,175,-1)
cuadro2=interfaz.CuadroTexto(panel,"csv",70,78,175,-1)

btn_salir=interfaz.Boton(panel,"salir",20,120)
btn_salir.Bind(wx.EVT_BUTTON,cerrar,btn_salir)

btn_previsualizar=interfaz.Boton(panel,"Previsualizar video",120,120)
btn_previsualizar.Bind(wx.EVT_BUTTON,medio,btn_previsualizar)

btn_gen=interfaz.Boton(panel,"Generar video",240,120)

menu.Bind(wx.EVT_CLOSE, cerrar)
menu.Show()
app.MainLoop()