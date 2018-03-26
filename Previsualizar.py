import wx
import wx.media
import Graficas as gr
import Variables as vb


def previsualizar(e):
    def cargado(e):
        player.Play()
        timer.Start(250)

    def pause(e):
        player.Pause()
        timer.Stop()

    def actualizar(e):
        # Establezco el valor del slider segun la posicion del video
        slider_player.SetValue(player.Tell() / 1000)

        tiempo = 568 / len(barra_tiempo)
        movimiento = wx.Point(52 + (player.Tell() / 1000 * tiempo), 30)
        barra_mover.SetPosition(movimiento)
        # print(slider.GetValue())

    def par_slider(e):
        timer.Stop()

    def mov_slider(e):
        player.Seek(slider_player.GetValue()*1000)
        timer.Start(250)

    def atras(e):
        reproductor.Destroy()

    barra_tiempo = gr.grafica()

    # Crear ventana para el video
    reproductor = wx.Frame(None,size=(1500,1000))
    reproductor.SetBackgroundColour(vb.back_rep)
    reproductor.Maximize()
    # reproductor.Bind(wx.EVT_CLOSE, vb.cerrar)

    main_sizer = wx.GridSizer(2, 1, 0, 0)

    sizer_video = wx.GridSizer(1, 3, 0, 0)
    main_sizer.Add(sizer_video, 1, wx.EXPAND, 5)

    sizer_grafica = wx.GridSizer(1, 3, 0, 0)
    main_sizer.Add(sizer_grafica, 1, wx.EXPAND, 5)

    panel_botones = wx.Panel(reproductor)
    sizer_video.Add(panel_botones)
    panel_video = wx.Panel(reproductor)
    sizer_video.Add(panel_video)
    # sizer_dervi= wx.GridSizer(3, 1, 0, 0)
    # sizer_video.Add(sizer_dervi)
    panel_dervi = wx.Panel(reproductor)
    sizer_video.Add(panel_dervi)
    # sizer_dervi.Add(panel_dervi)
    wx.StaticBitmap(panel_dervi, -1, wx.Bitmap(name="socio2.png"), pos=(0, 0), size=wx.DefaultSize)

    panel_izqgr = wx.Panel(reproductor)
    sizer_grafica.Add(panel_izqgr)
    panel_grafica = wx.Panel(reproductor)
    sizer_grafica.Add(panel_grafica)

    # Video
    boton_play = wx.BitmapButton(panel_botones, bitmap=wx.Bitmap("player_play.png"))
    boton_pause = wx.BitmapButton(panel_botones, bitmap=wx.Bitmap("player_pause.png"), pos=(30, 30))
    boton_atras = wx.Button(panel_botones, label="Atrás", pos=(60, 60))
    boton_play.Bind(wx.EVT_BUTTON, cargado)
    boton_pause.Bind(wx.EVT_BUTTON, pause)
    boton_atras.Bind(wx.EVT_BUTTON, atras)

    player = wx.media.MediaCtrl(panel_video, pos=(0, 0), size=(640, 400))
    #player.ShowPlayerControls(flags=wx.media.MEDIACTRLPLAYERCONTROLS_VOLUME)
    player.Load(vb.video)

    # Slider que llevara el tiempo del video
    slider_player=wx.Slider(panel_video, pos=(0,420),size=(640,-1))
    slider_player.SetRange(0, len(barra_tiempo))
    slider_player.Bind(wx.EVT_SCROLL_THUMBTRACK,par_slider)
    slider_player.Bind(wx.EVT_SCROLL_THUMBRELEASE,mov_slider)

    # Grafica

    wx.StaticBitmap(panel_grafica, -1, wx.Bitmap(name="grafico.png"), pos=(0, 0), size=(640, 480))

    # Timer que se lanza cada 250 ms para actualizar la barra que se mueve por el gráfico
    timer = wx.Timer(player)
    player.Bind(wx.EVT_TIMER, actualizar, timer)
    # Introducir la barra encima del gráfico
    barra_mover = wx.StaticBitmap(panel_grafica, -1, wx.Bitmap(name="barra2.png"), pos=(52, 30))

    # Sizers

    reproductor.SetSizer(main_sizer)
    reproductor.Layout()

    reproductor.Show()
    reproductor.Centre(wx.BOTH)
