import wx
import wx.media
import Graficas as gr
import Variables as vb



def previsualizar(e):
    def cargado(e):
        print("cargado")
        reproductor.player.Play()
        timer.Start(250)
        print(timer.IsRunning())

    def pause(e):
        print("pause")
        reproductor.player.Pause()
        timer.Stop()
        print(reproductor.player.Tell())

    def actualizar(e):
        # Establezco el valor del slider segun la posicion del video
        slider.SetValue(reproductor.player.Tell() / 1000)

        tiempo = 568 / len(barra_tiempo)
        movimiento = wx.Point(52 + (slider.GetValue() * tiempo), 30)
        barra_mover.SetPosition(movimiento)
        # print(slider.GetValue())

    def atras(e):
        reproductor.Destroy()

    barra_tiempo = gr.grafica()
    print(vb.background_rep)

    # Crear ventana para el video
    reproductor = wx.Frame(None)
    reproductor.SetBackgroundColour(vb.background_rep)
    reproductor.Maximize()
    reproductor.Bind(wx.EVT_CLOSE, vb.cerrar)

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
    boton_play = wx.Button(panel_botones, label="Play")
    boton_pause = wx.Button(panel_botones, label="Pause", pos=(30, 30))
    boton_atras = wx.Button(panel_botones, label="Atrás", pos=(60, 60))
    boton_play.Bind(wx.EVT_BUTTON, cargado)
    boton_pause.Bind(wx.EVT_BUTTON, pause)
    boton_atras.Bind(wx.EVT_BUTTON, atras)

    reproductor.player = wx.media.MediaCtrl(panel_video, pos=(0, 0), size=(640, 400))
    reproductor.player.ShowPlayerControls(flags=wx.media.MEDIACTRLPLAYERCONTROLS_VOLUME)
    reproductor.player.Load(vb.video)

    # Grafica

    wx.StaticBitmap(panel_grafica, -1, wx.Bitmap(name="grafico.png"), pos=(0, 0), size=(640, 480))

    # Slider
    timer = wx.Timer(reproductor.player)
    reproductor.player.Bind(wx.EVT_TIMER, actualizar, timer)

    slider = wx.Slider(reproductor, pos=(20, 500), style=wx.SL_VALUE_LABEL)
    slider.Hide()
    slider.SetRange(0, len(barra_tiempo))
    barra_mover = wx.StaticBitmap(panel_grafica, -1, wx.Bitmap(name="barra2.png"), pos=(52, 30))

    # Sizers

    reproductor.SetSizer(main_sizer)
    reproductor.Layout()

    reproductor.Show()
    reproductor.Centre(wx.BOTH)
