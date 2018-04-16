import wx
import wx.media
import Graficas as gr
import Variables as vb
from PIL import Image


def previsualizar(e):
    def cargado(e):
        barra_mover.Show()
        if vb.c_segundos == 0:
            player.Seek(vb.s_entrada * 1000)
        player.Play()
        timer.Start(250)
        vb.c_segundos = 1

    def pause(e):
        player.Pause()
        timer.Stop()

    def grabar_video(e):
        player.Stop()
        boton_play.Hide()
        boton_pause.Hide()
        boton_atras.Hide()
        boton_grabar.Hide()
        slider_player.Hide()
        timer_grabar.Start(5000, True)
        barra_mover.SetPosition((vb.l_gr + 116, vb.t_gr + 30))
        vb.c_segundos = 0

    def actualizar(e):
        # Si slider valor maximo se para el video
        if slider_player.GetMax() == slider_player.GetValue():
            parar_video()
        # Establecer el valor del slider segun la posicion del video
        tiempo = 504 / (vb.s_salida - vb.s_entrada)
        slider_player.SetValue((player.Tell() / 1000))
        movimiento = wx.Point(vb.l_gr + 116 + ((slider_player.GetValue() - vb.s_entrada) * tiempo), vb.t_gr + 30)
        barra_mover.SetPosition(movimiento)

    def par_slider(e):
        timer.Stop()

    def mov_slider(e):
        player.Seek(slider_player.GetValue() * 1000)
        timer.Start(250)

    def parar_video():
        player.Pause()
        timer.Stop()
        vb.c_segundos = 0

    def atras(e):
        timer.Stop()
        vb.c_segundos = 0
        vb.c_grafica= 0
        reproductor.Destroy()

    def resize(e):
        print("aqui")
        imagen = Image.open("grafico.png")
        guardar = imagen.resize((vb.w_otra, vb.h_otra))
        guardar.save("otra.png")
        grafica.SetBitmap(wx.Bitmap(name="otra.png"))
        imagen = Image.open("socio2.png")
        guardar = imagen.resize((int(vb.w_logo), int(vb.h_logo)))
        guardar.save("logo.png")
        logo.SetBitmap(wx.Bitmap(name="logo.png"))



    def responsive(e):
        # Obtener ancho y alto de la ventana
        w, h = reproductor.GetSize()

        # Cambios al player
        vb.w_player = vb.w_player * w / vb.w_ant
        vb.h_player = vb.h_player * h / vb.h_ant
        vb.l_rep = vb.l_rep * w / vb.w_ant
        vb.t_rep = vb.t_rep * h / vb.h_ant
        player.SetSize(vb.w_player, vb.h_player)
        player.SetPosition(pt=(vb.l_rep, vb.t_rep))

        # Cambios al logo
        vb.w_logo = vb.w_logo * w / vb.w_ant
        vb.h_logo = vb.h_logo * h / vb.h_ant
        vb.l_soc = vb.l_soc * w / vb.w_ant
        vb.t_soc = vb.t_soc * h / vb.h_ant
        logo.SetSize(vb.w_logo, vb.h_logo)
        logo.SetPosition(pt=(vb.l_soc, vb.t_soc))

        # Camios Slider
        vb.w_slider = vb.w_slider * w / vb.w_ant
        vb.t_slider = vb.t_slider * h / vb.h_ant
        slider_player.SetSize(vb.w_slider, -1)
        slider_player.SetPosition(pt=(vb.l_rep, vb.t_rep + vb.t_slider))

        # Cambios Botones
        vb.w_play = vb.w_play * w / vb.w_ant
        vb.h_play = vb.h_play * h / vb.h_ant
        vb.t_play = vb.t_play * h / vb.h_ant
        boton_play.SetSize(vb.w_play, vb.h_play)
        boton_play.SetPosition(pt=(vb.l_rep, vb.t_rep + vb.t_play))

        vb.w_pause = vb.w_pause * w / vb.w_ant
        vb.h_pause = vb.h_pause * h / vb.h_ant
        vb.l_pause = vb.l_pause * w / vb.w_ant
        vb.t_pause = vb.t_pause * h / vb.h_ant
        boton_pause.SetSize(vb.w_pause, vb.h_pause)
        boton_pause.SetPosition(pt=(vb.l_rep + vb.l_pause, vb.t_rep + vb.t_pause))

        vb.w_atras = vb.w_atras * w / vb.w_ant
        vb.h_atras = vb.h_atras * h / vb.h_ant
        vb.l_atras = vb.l_atras * w / vb.w_ant
        vb.t_atras = vb.t_atras * h / vb.h_ant
        boton_atras.SetSize(vb.w_atras, vb.h_atras)
        boton_atras.SetPosition(pt=(vb.l_rep + vb.l_atras, vb.t_rep + vb.t_atras))

        vb.w_grabar = vb.w_grabar * w / vb.w_ant
        vb.h_grabar = vb.h_grabar * h / vb.h_ant
        vb.l_grabar = vb.l_grabar * w / vb.w_ant
        vb.t_grabar = vb.t_grabar * h / vb.h_ant
        boton_grabar.SetSize(vb.w_grabar, vb.h_grabar)
        boton_grabar.SetPosition(pt=(vb.l_rep + vb.l_grabar, vb.t_rep + vb.t_grabar))

        # Grafica
        vb.w_grafica = vb.w_grafica * w / vb.w_ant
        vb.h_grafica = vb.h_grafica * h / vb.h_ant
        vb.w_otra=int(vb.w_grafica)
        vb.h_otra=int(vb.h_grafica)
        vb.l_gr = vb.l_gr * w / vb.w_ant
        vb.t_gr = vb.t_gr * h / vb.h_ant
        grafica.SetSize(vb.w_grafica, vb.h_grafica)
        grafica.SetPosition(pt=(vb.l_gr, vb.t_gr))

        # Barra
        vb.w_barra = vb.w_barra * w / vb.w_ant
        vb.h_barra = vb.h_barra * h / vb.h_ant
        vb.l_barra = vb.l_barra * w / vb.w_ant
        vb.t_barra = vb.t_barra * h / vb.h_ant
        barra_mover.SetSize(vb.w_barra, vb.h_barra)
        barra_mover.SetPosition(pt=(vb.l_gr + vb.l_barra, vb.t_gr + vb.t_barra))

        # Guaradar los nuevos valores de ancho y alto de la ventana
        vb.w_ant = w
        vb.h_ant = h

    # LLamar a la funcion grafica para crear la grafica
    vb.barra_tiempo = gr.grafica()

    # Crear ventana para el video
    reproductor = wx.Frame(None, size=(1920, 1040))
    reproductor.SetBackgroundColour(vb.back_rep)
    # reproductor.Maximize()
    reproductor.Bind(wx.EVT_SIZE, responsive)
    reproductor.Bind(wx.EVT_CLOSE, atras)
    reproductor.Bind(wx.EVT_MOUSE_CAPTURE_CHANGED, resize)

    main_sizer = wx.BoxSizer()
    panel_reproductor = wx.Panel(reproductor)
    main_sizer.Add(panel_reproductor)

    # Video
    boton_play = wx.BitmapButton(panel_reproductor, bitmap=wx.Bitmap("player_play.png"),
                                 pos=(vb.l_rep, vb.t_rep + vb.t_play), size=(vb.w_play, vb.h_play))
    boton_pause = wx.BitmapButton(panel_reproductor, bitmap=wx.Bitmap("player_pause.png"),
                                  pos=(vb.l_rep + vb.l_pause, vb.t_rep + vb.t_pause), size=(vb.w_pause, vb.h_pause))
    boton_atras = wx.Button(panel_reproductor, label="Atrás", pos=(vb.l_rep + vb.l_atras, vb.t_rep + vb.t_atras),
                            size=(vb.w_grabar, vb.h_grabar))
    boton_play.Bind(wx.EVT_BUTTON, cargado)
    boton_pause.Bind(wx.EVT_BUTTON, pause)
    boton_atras.Bind(wx.EVT_BUTTON, atras)
    boton_grabar = wx.Button(panel_reproductor, label="Grabar Video",
                             pos=(vb.l_rep + vb.l_grabar, vb.t_rep + vb.t_grabar), size=(vb.w_grabar, vb.h_grabar))
    boton_grabar.Bind(wx.EVT_BUTTON, grabar_video)

    player = wx.media.MediaCtrl(panel_reproductor, pos=(vb.l_rep, vb.t_rep), size=(vb.w_player, vb.h_player))
    # player.ShowPlayerControls(flags=wx.media.MEDIACTRLPLAYERCONTROLS_VOLUME)
    player.Load(vb.video)

    # Slider que llevara el tiempo del video
    slider_player = wx.Slider(panel_reproductor, pos=(vb.l_rep, vb.t_rep + vb.t_slider), size=(vb.w_slider, -1))
    if vb.s_salida != 0:
        slider_player.SetRange(vb.s_entrada, vb.s_salida)
    else:
        slider_player.SetRange(vb.s_entrada, len(vb.barra_tiempo))

    slider_player.Bind(wx.EVT_SCROLL_THUMBTRACK, par_slider)
    slider_player.Bind(wx.EVT_SCROLL_THUMBRELEASE, mov_slider)

    # Grafica

    grafica = wx.StaticBitmap(panel_reproductor, -1, wx.Bitmap(name="grafico.png"), pos=(vb.l_gr, vb.t_gr),
                              size=(vb.w_grafica, vb.h_grafica))
    logo = wx.StaticBitmap(panel_reproductor, -1, wx.Bitmap(name="socio2.png"), pos=(vb.l_soc, vb.t_soc),
                           size=(vb.w_logo, vb.h_logo))

    # Timer que se lanza cada 250 ms para actualizar la barra que se mueve por el gráfico
    timer = wx.Timer(player)
    player.Bind(wx.EVT_TIMER, actualizar, timer)

    # Timer que al dar al boton de grabar tendra que lanzar el video para grabar
    timer_grabar = wx.Timer(player)
    player.Bind(wx.EVT_TIMER, cargado, timer_grabar)

    # Introducir la barra encima del gráfico
    barra_mover = wx.StaticBitmap(panel_reproductor, -1, wx.Bitmap(name="barra2.png"),
                                  pos=(vb.l_gr + 116, vb.t_gr + 30), size=(vb.w_barra, vb.h_barra))
    barra_mover.Hide()

    # Sizers

    reproductor.SetSizer(main_sizer)
    reproductor.Layout()

    reproductor.Show()
    reproductor.Centre(wx.BOTH)
