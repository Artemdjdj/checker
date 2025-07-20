from settings import *
from restart_window import *
from form import *

class button:
    isbusy = False
    type_of_figure = None
    isqeen = False


class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(resource_path("icons/icon_for_windows.png")))

class RestartWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog_restart()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(resource_path("icons/icon_for_windows.png")))
        # модальное окно
        self.setModal(True)
        # отключение кнопки закрытия
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)

class Move:
    def __init__(self):
        self.parent_row = None
        self.parent_col = None
        self.row = None
        self.col = None

    def get_el(self, parent_r, parent_c, r, c):
        self.parent_row = parent_r
        self.parent_col = parent_c
        self.row = r
        self.col = c

    def __str__(self):
        return f"{self.parent_row} {self.parent_col} {self.row} {self.col}"