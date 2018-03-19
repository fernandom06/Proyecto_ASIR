#
# Single, Double click recognition for wxpython using
# a timer event -- should be very reliable --
#
import wx


class TrySingleDouble(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(350, 200))

        # Delay time of 500ms, is what's used by Microsoft, but this is too long
        # and can be a lot shorter (especially if used for gaming). Here I
        # use 300 ms.
        self.dbl_clk_delay = 250

        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.Bind(wx.EVT_LEFT_DCLICK, self.on_dbl_click)
        self.Bind(wx.EVT_TIMER, self.single_click)

    def on_dbl_click(self, e):
        self.stop_timer()
        print('Double click')

    def on_left_down(self, e):
        self.start_timer()

    def start_timer(self):
        self.timer1 = wx.Timer(self)
        self.timer1.Start(self.dbl_clk_delay)

    def stop_timer(self):
        self.timer1.Stop()
        del self.timer1

    def single_click(self, e):
        self.stop_timer()
        print('Single_click')


def tst_app():
    app = wx.App(redirect=True)
    win = TrySingleDouble("Single-Double Click Test")
    win.Show()
    app.MainLoop()


if __name__ == '__main__':
    tst_app()