from settings import *
from restart_window import *
class button:
    isbusy = False
    type_of_figure = None
    isqeen = False


class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

class RestartWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog_restart()
        self.ui.setupUi(self)
        # модальное окно
        self.setModal(True)
        # отключение кнопки закрытия
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)