from .baseWindow import baseWindow
from twitter import Api


class mainWindow(baseWindow):

    def init_gui(self):
        self.app.setTitle("Twitter Sentiment Analysis")
        self.app.addLabel(
            "Twitter_Url",
            "Please paste a URL from an Twitter Post or an Twitter Profile in here")
        self.app.addLabelEntry("twitterURL")
        self.app.addButton("Send", self.send_clicked)
        self.app.go()

    # button send clicked
    def send_clicked(self, button):
        if self.app.getEntry("twitterURL") != "":
            # continue to check link
            pass
        pass
