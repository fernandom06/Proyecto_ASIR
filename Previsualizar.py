from functools import partial
import wx
import wx.media
from PIL import Image
import Graficas as gr
import Variables as vb


def previsualizar(e):
    def cargado(e):
        # Lanza el video y si es la primera vez posiciona el video donde el usuario desea
        barra_mover.Show()
        if vb.c_segundos == 0:
            player.Seek(vb.s_entrada * 1000)
        player.Play()
        timer.Start(50)
        vb.c_segundos = 1

    def pause(e):
        # Para el video y el timer que mueve la barra
        player.Pause()
        timer.Stop()

    def actualizar(e):
        # Funcion que actualiza la posicion de la barra en la grafica dependiendo del momento del video
        barra_mover.Show()
        # Si slider valor maximo se para el video
        # Establecer el valor del slider segun la posicion del video
        tiempo = vb.pixeles_grafica / (vb.s_salida - vb.s_entrada)
        slider_player.SetValue((player.Tell() / 1000))
        movimiento = wx.Point(vb.l_grafica + vb.l_barra + ((player.Tell() / 1000 - vb.s_entrada) * tiempo),
                              vb.t_grafica + vb.t_barra)
        barra_mover.SetPosition(movimiento)
        if slider_player.GetMax() == int(player.Tell() / 1000):
            parar_video()

    def par_slider(e):
        # Cuando se quiere mover el slider se para el timer
        timer.Stop()

    def mov_slider(e):
        # Cuando se suelta para reubicar el slider hay que avanzar o retroceder el video y volver a lanzar el timer
        player.Seek(slider_player.GetValue() * 1000)
        timer.Start(50)
        reproductor.SetFocus()

    def parar_video():
        # Cuando se llega al final del video se para el video y se para el timer
        player.Pause()
        timer.Stop()
        vb.c_segundos = 0

    def grabar_video(e):
        # Esconde los controles no permite redimensionar la pantalla y
        # lanza el video desde el principio a los 5 segundos para grabar la pantalla
        reproductor.SetWindowStyleFlag(style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        reproductor.SetSize(reproductor.GetSize())
        panel_player.SetBackgroundColour(vb.back_rep)
        panel_grafica.SetBackgroundColour(vb.back_rep)
        reproductor.Refresh()
        player.Stop()
        boton_play.Hide()
        boton_pause.Hide()
        boton_atras.Hide()
        boton_grafica.Hide()
        boton_grabar.Hide()
        slider_player.Hide()
        timer_grabar.Start(5000, True)
        barra_mover.SetPosition((vb.l_grafica + vb.l_barra, vb.t_grafica + vb.t_barra))
        vb.c_segundos = 0

    def pincharw(e, widget):
        if widget.HasCapture():
            widget.ReleaseMouse()
        widget.CaptureMouse()
        x, y = reproductor.ScreenToClient(widget.ClientToScreen(e.GetPosition()))
        originx, originy = widget.GetPosition()
        dx = x - originx
        vb.delta = (dx, originy)
        widget.Bind(wx.EVT_MOTION, partial(arrastrarw, widget=widget))

    def arrastrarw(e, widget):
        if e.Dragging():
            cursor = wx.Cursor(wx.CURSOR_SIZEWE)
            reproductor.SetCursor(cursor)
            x, y = reproductor.ScreenToClient(widget.ClientToScreen(e.GetPosition()))
            fp = (x - vb.delta[0], vb.delta[1])
            widget.Bind(wx.EVT_LEFT_UP, partial(soltar, widget=widget, cuadrado=True))
            widget.Move(fp)

    def pincharh(e, widget):
        if widget.HasCapture():
            widget.ReleaseMouse()
        widget.CaptureMouse()
        x, y = reproductor.ScreenToClient(widget.ClientToScreen(e.GetPosition()))
        originx, originy = widget.GetPosition()
        dy = y - originy
        vb.delta = (originx, dy)
        widget.Bind(wx.EVT_MOTION, partial(arrastrarh, widget=widget))

    def arrastrarh(e, widget):
        if e.Dragging():
            cursor = wx.Cursor(wx.CURSOR_SIZENS)
            reproductor.SetCursor(cursor)
            x, y = reproductor.ScreenToClient(widget.ClientToScreen(e.GetPosition()))
            fp = (vb.delta[0], y - vb.delta[1])
            widget.Bind(wx.EVT_LEFT_UP, partial(soltar, widget=widget, cuadrado=True))
            widget.Move(fp)

    def pinchar(e, widget):
        if widget.HasCapture():
            widget.ReleaseMouse()
        widget.CaptureMouse()
        x, y = reproductor.ScreenToClient(widget.ClientToScreen(e.GetPosition()))
        originx, originy = widget.GetPosition()
        dx = x - originx
        dy = y - originy
        vb.delta = (dx, dy)
        widget.Bind(wx.EVT_MOTION, partial(arrastrar, widget=widget))

    def arrastrar(e, widget):
        if e.Dragging():
            x, y = reproductor.ScreenToClient(widget.ClientToScreen(e.GetPosition()))
            fp = (x - vb.delta[0], y - vb.delta[1])
            widget.Bind(wx.EVT_LEFT_UP, partial(soltar, widget=widget, cuadrado=False))
            widget.Move(fp)
            if widget.Name == "player":
                vb.l_panel_player, vb.t_panel_player = widget.GetPosition()
            elif widget.Name == "grafica":
                vb.l_panel_grafica, vb.t_panel_grafica = widget.GetPosition()
            reposicionar_cuadrados()

    def soltar(e, widget, cuadrado):
        cursor = wx.Cursor(wx.CURSOR_ARROW)
        reproductor.SetCursor(cursor)
        if widget.HasCapture():
            widget.ReleaseMouse()
        reproductor.Refresh()
        if cuadrado:
            reposicionar_paneles()
            reposicionar_cuadrados()

    def reposicionar_paneles():
        # Player
        w_panel_player, h_panel_player = panel_player.GetSize()
        w_panel_grafica, h_panel_grafica = panel_grafica.GetSize()
        vb.l_panel_player = izq_video.GetPosition()[0]
        vb.t_panel_player = top_video.GetPosition()[1]
        vb.w_panel_player = der_video.GetPosition()[0] - vb.l_panel_player
        vb.h_panel_player = bottom_video.GetPosition()[1] - vb.t_panel_player
        panel_player.SetSize(vb.w_panel_player, vb.h_panel_player)
        panel_player.SetPosition(pt=(vb.l_panel_player, vb.t_panel_player))

        # Grafica
        vb.l_panel_grafica = izq_grafica.GetPosition()[0]
        vb.t_panel_grafica = top_grafica.GetPosition()[1]
        vb.w_panel_grafica = der_grafica.GetPosition()[0] - vb.l_panel_grafica
        vb.h_panel_grafica = bottom_grafica.GetPosition()[1] - vb.t_panel_grafica
        panel_grafica.SetSize(vb.w_panel_grafica, vb.h_panel_grafica)
        panel_grafica.SetPosition(pt=(vb.l_panel_grafica, vb.t_panel_grafica))
        reposicionar_elementos(w_panel_player, h_panel_player, w_panel_grafica, h_panel_grafica)

    def reposicionar_elementos(w_panel_player, h_panel_player, w_panel_grafica, h_panel_grafica):
        # Se obtiene la relacion de tamaño entre el panel y la vetana
        boton_play.SetPosition(
            pt=(
                boton_play.GetPosition()[0],
                boton_play.GetPosition()[1] + (panel_player.GetSize()[1] - h_panel_player)))

        boton_pause.SetPosition(
            pt=(
                boton_pause.GetPosition()[0],
                boton_pause.GetPosition()[1] + (panel_player.GetSize()[1] - h_panel_player)))

        boton_atras.SetPosition(
            pt=(
                boton_atras.GetPosition()[0],
                boton_atras.GetPosition()[1] + (panel_player.GetSize()[1] - h_panel_player)))

        boton_grabar.SetPosition(
            pt=(
                boton_grabar.GetPosition()[0],
                boton_grabar.GetPosition()[1] + (panel_player.GetSize()[1] - h_panel_player)))

        boton_grafica.SetPosition(
            pt=(
                boton_grafica.GetPosition()[0],
                boton_grafica.GetPosition()[1] + (panel_player.GetSize()[1] - h_panel_player)))

        vb.w_slider = vb.w_slider * panel_player.GetSize()[0] / w_panel_player
        slider_player.SetSize(vb.w_slider, vb.h_slider)
        slider_player.SetPosition(
            pt=(
                slider_player.GetPosition()[0],
                slider_player.GetPosition()[1] + (panel_player.GetSize()[1] - h_panel_player)))

        vb.w_player = vb.w_player * panel_player.GetSize()[0] / w_panel_player
        vb.h_player = vb.h_player * panel_player.GetSize()[1] / h_panel_player
        player.SetSize(vb.w_player, vb.h_player)

        # Grafica

        w_grafica_ant = vb.w_grafica
        vb.w_grafica = vb.w_grafica * panel_grafica.GetSize()[0] / w_panel_grafica
        vb.h_grafica = vb.h_grafica * panel_grafica.GetSize()[1] / h_panel_grafica
        vb.w_inch = vb.w_grafica / 100
        vb.h_inch = vb.h_grafica / 100
        imagen = Image.open("grafico.png")
        guardar = imagen.resize((int(vb.w_panel_grafica) - 40, int(vb.h_panel_grafica) - 50))
        guardar.save("otra.png")
        grafica.SetBitmap(wx.Bitmap(name="otra.png"))

        vb.w_barra = vb.w_barra * panel_grafica.GetSize()[0] / w_panel_grafica
        vb.h_barra = vb.h_barra * panel_grafica.GetSize()[1] / h_panel_grafica
        vb.l_barra = vb.l_barra * panel_grafica.GetSize()[0] / w_panel_grafica
        vb.t_barra = vb.t_barra * panel_grafica.GetSize()[1] / h_panel_grafica
        barra_mover.SetPosition(pt=(vb.l_grafica + vb.l_barra, vb.t_grafica + vb.t_barra))
        imagen = Image.open("barra2.png")
        guardar = imagen.resize((int(vb.w_barra), int(vb.h_barra)))
        guardar.save("otra.png")
        barra_mover.SetBitmap(wx.Bitmap(name="otra.png"))

        vb.pixeles_grafica = vb.pixeles_grafica * vb.w_grafica / w_grafica_ant

    def reposicionar_cuadrados():
        # Player
        vb.t_izq_video = panel_player.GetPosition()[1] + (panel_player.GetSize()[1] / 2)
        izq_video.SetPosition(pt=(vb.l_panel_player - 5 + vb.l_izq_video, vb.t_izq_video))

        vb.l_der_video = panel_player.GetPosition()[0] + (panel_player.GetSize()[0])
        vb.t_der_video = panel_player.GetPosition()[1] + (panel_player.GetSize()[1] / 2)
        der_video.SetPosition(pt=(vb.l_der_video, vb.t_der_video))

        vb.l_top_video = panel_player.GetPosition()[0] + (panel_player.GetSize()[0] / 2)
        top_video.SetPosition(pt=(vb.l_top_video, vb.t_panel_player + vb.t_top_video - 5))

        vb.l_bottom_video = panel_player.GetPosition()[0] + (panel_player.GetSize()[0] / 2)
        vb.t_bottom_video = panel_player.GetPosition()[1] + (panel_player.GetSize()[1])
        bottom_video.SetPosition(pt=(vb.l_bottom_video, vb.t_bottom_video))

        # Grafica
        vb.t_izq_grafica = panel_grafica.GetPosition()[1] + (panel_grafica.GetSize()[1] / 2)
        izq_grafica.SetPosition(pt=(vb.l_panel_grafica - 5 + vb.l_izq_grafica, vb.t_izq_grafica))

        vb.l_der_grafica = panel_grafica.GetPosition()[0] + (panel_grafica.GetSize()[0])
        vb.t_der_grafica = panel_grafica.GetPosition()[1] + (panel_grafica.GetSize()[1] / 2)
        der_grafica.SetPosition(pt=(vb.l_der_grafica, vb.t_der_grafica))

        vb.l_top_grafica = panel_grafica.GetPosition()[0] + (panel_grafica.GetSize()[0] / 2)
        top_grafica.SetPosition(pt=(vb.l_top_grafica, vb.t_panel_grafica + vb.t_top_grafica - 10))

        vb.l_bottom_grafica = panel_grafica.GetPosition()[0] + (panel_grafica.GetSize()[0] / 2)
        vb.t_bottom_grafica = panel_grafica.GetPosition()[1] + (panel_grafica.GetSize()[1])
        bottom_grafica.SetPosition(pt=(vb.l_bottom_grafica, vb.t_bottom_grafica))

    def entrar_paneles_w(e):
        cursor = wx.Cursor(wx.CURSOR_SIZEWE)
        reproductor.SetCursor(cursor)

    def entrar_paneles_h(e):
        cursor = wx.Cursor(wx.CURSOR_SIZENS)
        reproductor.SetCursor(cursor)

    def salir_paneles(e):
        cursor = wx.Cursor(wx.CURSOR_ARROW)
        reproductor.SetCursor(cursor)

    def atras(e):
        # Funcion para volver al formulario principal
        timer.Stop()
        vb.c_segundos = 0
        vb.c_grafica = 0
        vb.w_player = 640
        vb.h_player = 400
        vb.w_slider = 640
        vb.h_slider = 24
        vb.w_panel_player = 640
        vb.h_panel_player = 500
        vb.w_panel_grafica = 930
        vb.h_panel_grafica = 580
        panel_grafica.SetSize(930, 580)
        vb.w_grafica = 830
        vb.h_grafica = 480
        vb.l_barra = 151
        vb.t_barra = 15
        vb.w_barra = 4
        vb.h_barra = 350
        vb.l_grafica = 25
        vb.t_grafica = 25
        vb.pixeles_grafica = 650
        grafica.SetBitmap(wx.Bitmap(name="grafico.png"))
        barra_mover.SetBitmap(wx.Bitmap(name="barra2.png"))
        barra_mover.SetPosition(pt=(vb.l_grafica + vb.l_barra, vb.t_grafica + vb.t_barra))
        reproductor.Maximize()
        reproductor.Destroy()

    def regrafica(e):
        barra_mover.Hide()
        cursor = wx.Cursor(wx.CURSOR_WAIT)
        reproductor.SetCursor(cursor)
        gr.grafica(numero=1)
        grafica.SetBitmap(wx.Bitmap(name="otra.png"))
        cursor = wx.Cursor(wx.CURSOR_ARROW)
        reproductor.Refresh()
        reproductor.SetCursor(cursor)
        reproductor.SetFocus()

    def dentro(e, widget):
        if widget.Name == "grafica":
            vb.c_resize_grafica = 1
        elif widget.Name == "player":
            vb.c_resize_player = 1
        else:
            vb.c_resize_logo = 1

    def fuera(e, widget):
        if widget.Name == "grafica":
            vb.c_resize_grafica = 0
        elif widget.Name == "player":
            vb.c_resize_player = 0
        else:
            vb.c_resize_logo = 0

    def resize_componentes(e):
        if vb.c_resize_player == 1:
            # Se obtiene la relacion de tamaño entre el panel y la vetana
            w_panel, h_panel = panel_player.GetSize()
            relacion_w = vb.w_ant / w_panel
            relacion_h = vb.h_ant / h_panel
            # Se redimensioa en panel
            if e.WheelRotation > 0:
                panel_player.SetSize(panel_player.GetSize()[0] + (10 * relacion_w),
                                     panel_player.GetSize()[1] + (10 * relacion_h))
            else:
                panel_player.SetSize(panel_player.GetSize()[0] - (10 * relacion_w),
                                     panel_player.GetSize()[1] - (10 * relacion_h))
            # Se redimensionan los elementos que estan dentro del panel (player,play,pause,atras,grabar,grafica,slider)
            vb.w_player = vb.w_player * panel_player.GetSize()[0] / w_panel
            vb.h_player = vb.h_player * panel_player.GetSize()[1] / h_panel
            player.SetSize(vb.w_player, vb.h_player)

            boton_play.SetPosition(
                pt=(boton_play.GetPosition()[0], boton_play.GetPosition()[1] + (panel_player.GetSize()[1] - h_panel)))

            boton_pause.SetPosition(
                pt=(boton_pause.GetPosition()[0], boton_pause.GetPosition()[1] + (panel_player.GetSize()[1] - h_panel)))

            boton_atras.SetPosition(
                pt=(boton_atras.GetPosition()[0], boton_atras.GetPosition()[1] + (panel_player.GetSize()[1] - h_panel)))

            boton_grabar.SetPosition(
                pt=(
                    boton_grabar.GetPosition()[0],
                    boton_grabar.GetPosition()[1] + (panel_player.GetSize()[1] - h_panel)))

            boton_grafica.SetPosition(
                pt=(
                    boton_grafica.GetPosition()[0],
                    boton_grafica.GetPosition()[1] + (panel_player.GetSize()[1] - h_panel)))

            vb.w_slider = vb.w_slider * panel_player.GetSize()[0] / w_panel
            slider_player.SetSize(vb.w_slider, vb.h_slider)
            slider_player.SetPosition(
                pt=(
                    slider_player.GetPosition()[0],
                    slider_player.GetPosition()[1] + (panel_player.GetSize()[1] - h_panel)))
            reposicionar_cuadrados()
        elif vb.c_resize_grafica == 1:
            w_grafica_ant = vb.w_grafica
            # Se obtiene la relacion de tamaño entre el panel y la vetana
            w_panel, h_panel = panel_grafica.GetSize()
            relacion_w = vb.w_ant / w_panel
            relacion_h = vb.h_ant / h_panel
            # Se redimensioa en panel
            if e.WheelRotation > 0:
                panel_grafica.SetSize(panel_grafica.GetSize()[0] + (10 * relacion_w),
                                      panel_grafica.GetSize()[1] + (10 * relacion_h))
            else:
                panel_grafica.SetSize(panel_grafica.GetSize()[0] - (10 * relacion_w),
                                      panel_grafica.GetSize()[1] - (10 * relacion_h))
            # Se redimensionan los elementos que estan dentro del panel (grafica,barra)
            vb.w_grafica = vb.w_grafica * panel_grafica.GetSize()[0] / w_panel
            vb.h_grafica = vb.h_grafica * panel_grafica.GetSize()[1] / h_panel
            grafica.SetSize(vb.w_grafica, vb.h_grafica)
            vb.w_inch = vb.w_grafica / 100
            vb.h_inch = vb.h_grafica / 100
            imagen = Image.open("grafico.png")
            guardar = imagen.resize((int(vb.w_grafica), int(vb.h_grafica)))
            guardar.save("otra.png")
            grafica.SetBitmap(wx.Bitmap(name="otra.png"))

            vb.w_barra = vb.w_barra * panel_grafica.GetSize()[0] / w_panel
            vb.h_barra = vb.h_barra * panel_grafica.GetSize()[1] / h_panel
            vb.l_barra = vb.l_barra * panel_grafica.GetSize()[0] / w_panel
            barra_mover.SetPosition(pt=(vb.l_grafica + vb.l_barra, vb.t_grafica + vb.t_barra))
            imagen = Image.open("barra2.png")
            guardar = imagen.resize((int(vb.w_barra), int(vb.h_barra)))
            guardar.save("otra.png")
            barra_mover.SetBitmap(wx.Bitmap(name="otra.png"))

            vb.pixeles_grafica = vb.pixeles_grafica * vb.w_grafica / w_grafica_ant
            reposicionar_cuadrados()

    def resize(e):
        # Funcion para redimensionar la imagen ajustandolo al tamaño de la ventana
        imagen = Image.open("grafico.png")
        guardar = imagen.resize((int(vb.w_grafica), int(vb.h_grafica)))
        guardar.save("otra.png")
        grafica.SetBitmap(wx.Bitmap(name="otra.png"))
        imagen = Image.open("socio2.png")
        guardar = imagen.resize((int(vb.w_logo), int(vb.h_logo)))
        guardar.save("logo.png")
        logo.SetBitmap(wx.Bitmap(name="logo.png"))

    def responsive(e):
        # Funcion para redimensionar todos los elementos y ajustarlos al tamaño de la ventana
        barra_mover.Hide()

        reproductor.Freeze()
        # Obtener ancho y alto de la ventana
        w, h = reproductor.GetSize()
        if reproductor.IsMaximized():
            grafica.SetBitmap(wx.Bitmap(name="grafico.png"))
            logo.SetBitmap(wx.Bitmap(name="socio2.png"))
        # Calcular los pixeles solo de la grafica
        vb.pixeles_grafica = vb.pixeles_grafica * w / vb.w_ant

        # Cambios al player y a su Panel
        vb.w_player = vb.w_player * w / vb.w_ant
        vb.h_player = vb.h_player * h / vb.h_ant
        vb.w_panel_player = vb.w_panel_player * w / vb.w_ant
        vb.h_panel_player = vb.h_panel_player * h / vb.h_ant
        vb.l_panel_player = vb.l_panel_player * w / vb.w_ant
        vb.t_panel_player = vb.t_panel_player * h / vb.h_ant
        player.SetSize(vb.w_player, vb.h_player)
        panel_player.SetSize(vb.w_panel_player, vb.h_panel_player)
        panel_player.SetPosition(pt=(vb.l_panel_player, vb.t_panel_player))

        # Cambios al logo
        vb.w_logo = vb.w_logo * w / vb.w_ant
        vb.h_logo = vb.h_logo * h / vb.h_ant
        vb.l_logo = vb.l_logo * w / vb.w_ant
        vb.t_logo = vb.t_logo * h / vb.h_ant
        logo.SetSize(vb.w_logo, vb.h_logo)
        logo.SetPosition(pt=(vb.l_logo, vb.t_logo))

        # Camios Slider
        vb.w_slider = vb.w_slider * w / vb.w_ant
        vb.h_slider = vb.h_slider * h / vb.h_ant
        vb.t_slider = vb.t_slider * h / vb.h_ant
        slider_player.SetSize(vb.w_slider, vb.h_slider)
        slider_player.SetPosition(pt=(vb.l_player, vb.t_player + vb.t_slider))

        # Cambios Botones
        vb.w_play = vb.w_play * w / vb.w_ant
        vb.h_play = vb.h_play * h / vb.h_ant
        vb.t_play = vb.t_play * h / vb.h_ant
        boton_play.SetSize(vb.w_play, vb.h_play)
        boton_play.SetPosition(pt=(vb.l_player, vb.t_player + vb.t_play))

        vb.w_pause = vb.w_pause * w / vb.w_ant
        vb.h_pause = vb.h_pause * h / vb.h_ant
        vb.l_pause = vb.l_pause * w / vb.w_ant
        vb.t_pause = vb.t_pause * h / vb.h_ant
        boton_pause.SetSize(vb.w_pause, vb.h_pause)
        boton_pause.SetPosition(pt=(vb.l_player + vb.l_pause, vb.t_player + vb.t_pause))

        vb.w_atras = vb.w_atras * w / vb.w_ant
        vb.h_atras = vb.h_atras * h / vb.h_ant
        vb.l_atras = vb.l_atras * w / vb.w_ant
        vb.t_atras = vb.t_atras * h / vb.h_ant
        boton_atras.SetSize(vb.w_atras, vb.h_atras)
        boton_atras.SetPosition(pt=(vb.l_player + vb.l_atras, vb.t_player + vb.t_atras))

        vb.w_grabar = vb.w_grabar * w / vb.w_ant
        vb.h_grabar = vb.h_grabar * h / vb.h_ant
        vb.l_grabar = vb.l_grabar * w / vb.w_ant
        vb.t_grabar = vb.t_grabar * h / vb.h_ant
        boton_grabar.SetSize(vb.w_grabar, vb.h_grabar)
        boton_grabar.SetPosition(pt=(vb.l_player + vb.l_grabar, vb.t_player + vb.t_grabar))

        # Mover el boton de regrafica
        vb.w_regrafica = vb.w_regrafica * w / vb.w_ant
        vb.h_regrafica = vb.h_regrafica * h / vb.h_ant
        vb.l_regrafica = vb.l_regrafica * w / vb.w_ant
        vb.t_regrafica = vb.t_regrafica * h / vb.h_ant
        boton_grafica.SetSize(vb.w_regrafica, vb.h_regrafica)
        boton_grafica.SetPosition(pt=(vb.l_player + vb.l_regrafica, vb.t_player + vb.t_regrafica))

        # Grafica
        vb.w_grafica = vb.w_grafica * w / vb.w_ant
        vb.h_grafica = vb.h_grafica * h / vb.h_ant
        vb.w_panel_grafica = vb.w_panel_grafica * w / vb.w_ant
        vb.h_panel_grafica = vb.h_panel_grafica * h / vb.h_ant
        vb.l_panel_grafica = vb.l_panel_grafica * w / vb.w_ant
        vb.t_panel_grafica = vb.t_panel_grafica * h / vb.h_ant
        grafica.SetSize(vb.w_grafica, vb.h_grafica)
        panel_grafica.SetSize(vb.w_panel_grafica, vb.h_panel_grafica)
        panel_grafica.SetPosition(pt=(vb.l_panel_grafica, vb.t_panel_grafica))

        # Barra
        vb.w_barra = vb.w_barra * w / vb.w_ant
        vb.h_barra = vb.h_barra * h / vb.h_ant
        vb.l_barra = vb.l_barra * w / vb.w_ant
        vb.t_barra = vb.t_barra * h / vb.h_ant
        barra_mover.SetSize(vb.w_barra, vb.h_barra)
        barra_mover.SetPosition(pt=(vb.l_grafica + vb.l_barra, vb.t_grafica + vb.t_barra))

        # Calcular pulgadas para la grafica
        vb.w_inch = vb.w_grafica / 100
        vb.h_inch = vb.h_grafica / 100

        # Guaradar los nuevos valores de ancho y alto de la ventana
        vb.w_ant = w
        vb.h_ant = h
        vb.w_ant_grafica = vb.w_grafica
        vb.h_ant_grafica = vb.h_grafica

        reposicionar_cuadrados()

        reproductor.Thaw()

    # LLamar a la funcion grafica para crear la grafica
    vb.barra_tiempo = gr.grafica(numero=0)

    # Crear ventana para el video
    reproductor = wx.Frame(None, size=(1440, 900))
    reproductor.SetBackgroundColour(vb.back_rep)
    reproductor.Maximize()
    reproductor.Bind(wx.EVT_SIZE, responsive)
    reproductor.Bind(wx.EVT_CLOSE, atras)
    reproductor.Bind(wx.EVT_MOUSE_CAPTURE_CHANGED, resize)
    reproductor.Bind(wx.EVT_MOUSEWHEEL, resize_componentes)

    # main_sizer = wx.BoxSizer()
    panel_player = wx.Panel(reproductor, size=(vb.w_panel_player, vb.h_panel_player), pos=(640, 0), name="player")
    panel_player.Layout()
    panel_player.SetBackgroundColour(wx.YELLOW)
    panel_player.Bind(wx.EVT_LEFT_DOWN, partial(pinchar, widget=panel_player))
    panel_player.Bind(wx.EVT_ENTER_WINDOW, partial(dentro, widget=panel_player))
    panel_player.Bind(wx.EVT_LEAVE_WINDOW, partial(fuera, widget=panel_player))

    panel_grafica = wx.Panel(reproductor, size=(vb.w_panel_grafica, vb.h_panel_grafica), pos=(445, 530), name="grafica")
    panel_grafica.Layout()
    panel_grafica.SetBackgroundColour(wx.YELLOW)
    panel_grafica.Bind(wx.EVT_LEFT_DOWN, partial(pinchar, widget=panel_grafica))
    panel_grafica.Bind(wx.EVT_ENTER_WINDOW, partial(dentro, widget=panel_grafica))
    panel_grafica.Bind(wx.EVT_LEAVE_WINDOW, partial(fuera, widget=panel_grafica))

    # main_sizer.Add(panel_reproductor)

    # Video
    boton_play = wx.BitmapButton(panel_player, bitmap=wx.Bitmap("player_play.png"),
                                 pos=(vb.l_player, vb.t_player + vb.t_play), size=(vb.w_play, vb.h_play))
    boton_play.Bind(wx.EVT_BUTTON, cargado)
    boton_pause = wx.BitmapButton(panel_player, bitmap=wx.Bitmap("player_pause.png"),
                                  pos=(vb.l_player + vb.l_pause, vb.t_player + vb.t_pause),
                                  size=(vb.w_pause, vb.h_pause))
    boton_pause.Bind(wx.EVT_BUTTON, pause)
    boton_atras = wx.Button(panel_player, label="Atrás", pos=(vb.l_player + vb.l_atras, vb.t_player + vb.t_atras),
                            size=(vb.w_grabar, vb.h_grabar))
    boton_atras.Bind(wx.EVT_BUTTON, atras)
    boton_grabar = wx.Button(panel_player, label="Grabar Video",
                             pos=(vb.l_player + vb.l_grabar, vb.t_player + vb.t_grabar),
                             size=(vb.w_grabar, vb.h_grabar))
    boton_grabar.Bind(wx.EVT_BUTTON, grabar_video)
    boton_grafica = wx.Button(panel_player, label="Recalcular Grafica",
                              pos=(vb.l_player + vb.l_regrafica, vb.t_player + vb.t_regrafica),
                              size=(vb.w_regrafica, vb.h_regrafica))
    boton_grafica.Bind(wx.EVT_BUTTON, regrafica)

    player = wx.media.MediaCtrl(panel_player, pos=(vb.l_player, vb.t_player), size=(vb.w_player, vb.h_player))
    player.Load(vb.video)

    # Slider que llevara el tiempo del video
    slider_player = wx.Slider(panel_player, pos=(vb.l_player, vb.t_player + vb.t_slider),
                              size=(vb.w_slider, vb.h_slider))
    if vb.s_salida != 0:
        slider_player.SetRange(vb.s_entrada, vb.s_salida)
    else:
        slider_player.SetRange(vb.s_entrada, len(vb.barra_tiempo))

    slider_player.Bind(wx.EVT_SCROLL_THUMBTRACK, par_slider)
    slider_player.Bind(wx.EVT_SCROLL_THUMBRELEASE, mov_slider)

    # Grafica

    grafica = wx.StaticBitmap(panel_grafica, -1, wx.Bitmap(name="grafico.png"), pos=(vb.l_grafica, vb.t_grafica),
                              size=(vb.w_grafica, vb.h_grafica))

    logo = wx.StaticBitmap(reproductor, -1, wx.Bitmap(name="socio2.png"), pos=(vb.l_logo, vb.t_logo),
                           size=(vb.w_logo, vb.h_logo), name="logo")
    logo.Bind(wx.EVT_LEFT_DOWN, partial(pinchar, widget=logo))
    logo.Bind(wx.EVT_ENTER_WINDOW, partial(dentro, widget=logo))
    logo.Bind(wx.EVT_LEAVE_WINDOW, partial(fuera, widget=logo))

    # Timer que se lanza cada 250 ms para actualizar la barra que se mueve por el gráfico
    timer = wx.Timer(player)
    player.Bind(wx.EVT_TIMER, actualizar, timer)

    # Timer que al dar al boton de grabar tendra que lanzar el video para grabar
    timer_grabar = wx.Timer(player)
    player.Bind(wx.EVT_TIMER, cargado, timer_grabar)

    # Introducir la barra encima del gráfico
    barra_mover = wx.StaticBitmap(panel_grafica, -1, wx.Bitmap(name="barra2.png"),
                                  pos=(vb.l_grafica + vb.l_barra, vb.t_grafica + vb.t_barra),
                                  size=(vb.w_barra, vb.h_barra))
    barra_mover.Hide()

    # Paneles para redimensionar el panel del player
    izq_video = wx.Panel(reproductor, size=(10, 10),
                         pos=(vb.l_panel_player + vb.l_izq_video, vb.t_panel_player + vb.t_izq_video))
    izq_video.SetBackgroundColour(wx.BLUE)
    izq_video.Bind(wx.EVT_LEFT_DOWN, partial(pincharw, widget=izq_video))
    izq_video.Bind(wx.EVT_ENTER_WINDOW, entrar_paneles_w)
    izq_video.Bind(wx.EVT_LEAVE_WINDOW, salir_paneles)

    der_video = wx.Panel(reproductor, size=(10, 10), pos=(
        vb.l_panel_player + vb.w_panel_player + vb.l_der_video, vb.t_panel_player + vb.t_der_video))
    der_video.SetBackgroundColour(wx.BLUE)
    der_video.Bind(wx.EVT_LEFT_DOWN, partial(pincharw, widget=der_video))
    der_video.Bind(wx.EVT_ENTER_WINDOW, entrar_paneles_w)
    der_video.Bind(wx.EVT_LEAVE_WINDOW, salir_paneles)

    top_video = wx.Panel(reproductor, size=(10, 10),
                         pos=(vb.l_panel_player + vb.l_top_video, vb.t_panel_player + vb.t_top_video))
    top_video.SetBackgroundColour(wx.BLUE)
    top_video.Bind(wx.EVT_LEFT_DOWN, partial(pincharh, widget=top_video))
    top_video.Bind(wx.EVT_ENTER_WINDOW, entrar_paneles_h)
    top_video.Bind(wx.EVT_LEAVE_WINDOW, salir_paneles)

    bottom_video = wx.Panel(reproductor, size=(10, 10), pos=(
        vb.l_panel_player + vb.l_bottom_video, vb.t_panel_player + vb.h_panel_player + vb.t_bottom_video))
    bottom_video.SetBackgroundColour(wx.BLUE)
    bottom_video.Bind(wx.EVT_LEFT_DOWN, partial(pincharh, widget=bottom_video))
    bottom_video.Bind(wx.EVT_ENTER_WINDOW, entrar_paneles_h)
    bottom_video.Bind(wx.EVT_LEAVE_WINDOW, salir_paneles)

    # Paneles para redimensionar el panel del player
    izq_grafica = wx.Panel(reproductor, size=(10, 10),
                           pos=(vb.l_panel_grafica + vb.l_izq_grafica, vb.t_panel_grafica + vb.t_izq_grafica))
    izq_grafica.SetBackgroundColour(wx.BLUE)
    izq_grafica.Bind(wx.EVT_LEFT_DOWN, partial(pincharw, widget=izq_grafica))
    izq_grafica.Bind(wx.EVT_ENTER_WINDOW, entrar_paneles_w)
    izq_grafica.Bind(wx.EVT_LEAVE_WINDOW, salir_paneles)

    der_grafica = wx.Panel(reproductor, size=(10, 10), pos=(
        vb.l_panel_grafica + vb.w_panel_grafica + vb.l_der_grafica, vb.t_panel_grafica + vb.t_der_grafica))
    der_grafica.SetBackgroundColour(wx.BLUE)
    der_grafica.Bind(wx.EVT_LEFT_DOWN, partial(pincharw, widget=der_grafica))
    der_grafica.Bind(wx.EVT_ENTER_WINDOW, entrar_paneles_w)
    der_grafica.Bind(wx.EVT_LEAVE_WINDOW, salir_paneles)

    top_grafica = wx.Panel(reproductor, size=(10, 10),
                           pos=(vb.l_panel_grafica + vb.l_top_grafica, vb.t_panel_grafica + vb.t_top_grafica))
    top_grafica.SetBackgroundColour(wx.BLUE)
    top_grafica.Bind(wx.EVT_LEFT_DOWN, partial(pincharh, widget=top_grafica))
    top_grafica.Bind(wx.EVT_ENTER_WINDOW, entrar_paneles_h)
    top_grafica.Bind(wx.EVT_LEAVE_WINDOW, salir_paneles)

    bottom_grafica = wx.Panel(reproductor, size=(10, 10), pos=(
        vb.l_panel_grafica + vb.l_bottom_grafica, vb.t_panel_grafica + vb.h_panel_grafica + vb.t_top_grafica))
    bottom_grafica.SetBackgroundColour(wx.BLUE)
    bottom_grafica.Bind(wx.EVT_LEFT_DOWN, partial(pincharh, widget=bottom_grafica))
    bottom_grafica.Bind(wx.EVT_ENTER_WINDOW, entrar_paneles_h)
    bottom_grafica.Bind(wx.EVT_LEAVE_WINDOW, salir_paneles)

    reproductor.Show()
    reproductor.Centre(wx.BOTH)
