from appJar import gui


class baseWindow:

    app = None

    def __init__(self):
        self.app = gui()
        pass

    def show():
        if self.app is not None:
            self.app.show()
        pass

    def hide():
        if self.app is not None:
            self.app.hide()
        pass
