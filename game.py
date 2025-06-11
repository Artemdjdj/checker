from settings import *
class button:
    isbusy = False
    type_of_figure = None
    isqeen = False
    is_cutting = True


class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)