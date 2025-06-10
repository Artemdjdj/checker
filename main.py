from PySide6 import *
import sys
import os
from form import *
from settings import *
from form_settings import *
from game import *
from utils import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.temp = self.ui.first_cenral_widget
        self.settings_window = None
        # Явно устанавливаем состояние окна
        self.setWindowState(Qt.WindowNoState)
        # Разрешаем все операции с окном
        self.setWindowFlags(
            self.windowFlags() | 
            Qt.WindowMaximizeButtonHint |
            Qt.CustomizeWindowHint |
            Qt.WindowTitleHint |
            Qt.WindowSystemMenuHint |
            Qt.WindowMinimizeButtonHint |
            Qt.WindowCloseButtonHint
        )
        self.type_of_figure = "white"
        self.count_of_white_figure = 12
        self.count_of_black_figure = 12
        self.name_parent_button =""
        self.parent_r = -1
        self.parent_c = -1
        self.cut_figures = []
        self.board = [[button() for j in range(8)] for i in range(8)]
        self.all_buttons = [self.ui.button_00, self.ui.button_01, self.ui.button_02, self.ui.button_03, self.ui.button_04, self.ui.button_05,self.ui.button_06, self.ui.button_07,
                            self.ui.button_10, self.ui.button_11, self.ui.button_12, self.ui.button_13, self.ui.button_14, self.ui.button_15,self.ui.button_16, self.ui.button_17,
                            self.ui.button_20, self.ui.button_21, self.ui.button_22, self.ui.button_23, self.ui.button_24, self.ui.button_25,self.ui.button_26, self.ui.button_27,
                            self.ui.button_30, self.ui.button_31, self.ui.button_32, self.ui.button_33, self.ui.button_34, self.ui.button_35,self.ui.button_36, self.ui.button_37,
                            self.ui.button_40, self.ui.button_41, self.ui.button_42, self.ui.button_43, self.ui.button_44, self.ui.button_45,self.ui.button_46, self.ui.button_47,
                            self.ui.button_50, self.ui.button_51, self.ui.button_52, self.ui.button_53, self.ui.button_54, self.ui.button_55,self.ui.button_56, self.ui.button_57,
                            self.ui.button_60, self.ui.button_61, self.ui.button_62, self.ui.button_63, self.ui.button_64, self.ui.button_65,self.ui.button_66, self.ui.button_67,
                            self.ui.button_70, self.ui.button_71, self.ui.button_72, self.ui.button_73, self.ui.button_74, self.ui.button_75,self.ui.button_76, self.ui.button_77,]
        self.all_lines = [
            [[6,0],[7,1]],
            [[4,0],[5,1],[6,2],[7,3]],
            [[2,0],[3,1],[4,2],[5,3],[6,4],[7,5]],
            [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6], [7,7]],
            [[0,2],[1,3],[2,4],[3,5],[4,6],[5,7]],
            [[0,4],[1,5],[2,6],[3,7]],
            [[0,6],[1,7]],
        ]      
        self.add_functions()
        self.start_settings()
        self.ui.left_widget.setCurrentWidget(self.ui.first_tab_left)
        self.ui.left_widget.tabBar().hide()
        self.ui.central_widget.tabBar().hide()
        self.ui.right_widget.tabBar().hide()
        self.ui.central_widget.setCurrentWidget(self.ui.first_cenral_widget)
        self.ui.right_widget.setCurrentWidget(self.ui.first_widget_right)
        self.style_buttons = style_classic
        self.style_around_buttons = style_around_classic
    def start_settings(self):
        for i in range(0,3):
            if i%2 == 0: 
                for j in range(0,8,2):
                    self.board[i][j].isbusy = True
                    self.board[i][j].type_of_figure = "white"
                    if j == 0 or j == 7:
                        self.board[i][j].isextreme = True
            else:
                for j in range(1,8,2):
                    self.board[i][j].isbusy = True
                    self.board[i][j].type_of_figure = "white"
                    if j == 0 or j == 7:
                        self.board[i][j].isextreme = True
        for i in range(5,8):
            if i%2 == 0: 
                for j in range(0,8,2):
                    self.board[i][j].isbusy = True
                    self.board[i][j].type_of_figure = "black"
                    if j == 0 or j == 7:
                        self.board[i][j].isextreme = True
            else:
                for j in range(1,8,2):
                    self.board[i][j].isbusy = True
                    self.board[i][j].type_of_figure = "black"
                    if j == 0 or j == 7:
                        self.board[i][j].isextreme = True
     
                    
    def add_functions(self):
        self.ui.start_the_game.clicked.connect(lambda:self.start_game())
        self.ui.rules_of_play.clicked.connect(lambda:self.read_rules())
        self.ui.back_to_game.clicked.connect(lambda:self.backs_to_game())
        self.ui.statistics.clicked.connect(lambda:self.read_statistic())
        self.ui.back_to_report.clicked.connect(lambda:self.back_rep())
        self.ui.leave_the_game.clicked.connect(lambda:self.get_away())
        self.ui.stop_game.clicked.connect(lambda:self.go_to_preview())
        self.ui.settings.clicked.connect(lambda:self.open_settings())
        for button in self.all_buttons:
            button.clicked.connect(lambda ch, b=button: self.choose_start_position(b))

    def get_button_by_name(self, name):
        for button in self.all_buttons:
            if button.objectName() == name:
                return button

    def choose_start_position(self, button):
        index_of_row = int(button.objectName()[-2])
        index_of_col = int(button.objectName()[-1])
        figure_type = self.board[index_of_row][index_of_col].type_of_figure
        
        
        if figure_type == self.type_of_figure: 
            button.setStyleSheet(self.style_around_buttons)
            self.name_parent_button = button.objectName()
            if self.parent_r != -1 and self.parent_c != -1:
                name = f"button_{self.parent_r}{self.parent_c}"
                parent_button = self.get_button_by_name(name)
                parent_button.setStyleSheet(self.style_buttons)
            self.parent_r = index_of_row
            self.parent_c = index_of_col
        
        else:
            
            if self.parent_r == -1 or self.parent_c == -1 or self.board[self.parent_r][self.parent_c].type_of_figure != self.type_of_figure:
                return
                
            check_is_qeen = self.board[self.parent_r][self.parent_c].isqeen
            ways = []
            more_important_ways = []
            list_buttons_that_must_to_cut_ohter = []
            result = []
           
            self.get_buttons_that_should_cut_others(list_buttons_that_must_to_cut_ohter, self.type_of_figure)  
            
            self.get_all_ways(self.parent_r, self.parent_c, ways, more_important_ways, check_is_qeen, self.type_of_figure,-1,-1) 
            
            if check_is_qeen:
                if self.pos_which_can_cut_figure(more_important_ways, result, self.type_of_figure): 
                    more_important_ways.clear()
                    for i in result:
                        more_important_ways.append(i)
            
            
            if figure_type is not None:
                return
                
            if len(list_buttons_that_must_to_cut_ohter) == 0:
                if len(more_important_ways) == 0 and len(ways) > 0:
                    self.change_position(ways, figure_type, index_of_row, index_of_col, self.type_of_figure, is_capture=False)
            else:
                
                if [self.parent_r, self.parent_c] in list_buttons_that_must_to_cut_ohter:
                    if [index_of_row, index_of_col] in more_important_ways:
                        name = f"button_{index_of_row}{index_of_col}"
                        new_button = self.get_button_by_name(name)
                        parent_button = self.get_button_by_name(self.name_parent_button)
                        icon = parent_button.icon()
                        
                        d_row = 1 if index_of_row > self.parent_r else -1
                        d_col = 1 if index_of_col > self.parent_c else -1
                        cut_row, cut_col = self.parent_r, self.parent_c
                        time_r, time_c = self.parent_r + d_row, self.parent_c + d_col
                        
                        
                        while (time_r, time_c) != (index_of_row, index_of_col) and 0 <= time_r < 8 and 0 <= time_c < 8:
                            if self.board[time_r][time_c].type_of_figure is not None:
                                if self.board[time_r][time_c].type_of_figure != self.type_of_figure:
                                    cut_row, cut_col = time_r, time_c
                                else:
                                    return  
                            time_r += d_row
                            time_c += d_col
                            
                        name_of_cut = f"button_{cut_row}{cut_col}"
                        cut_button = self.get_button_by_name(name_of_cut)
                        if self.board[cut_row][cut_col].type_of_figure == self.type_of_figure:
                            return
                            
                        self.board[cut_row][cut_col].type_of_figure = None
                        self.board[cut_row][cut_col].isbusy = False
                        self.cut_figures.append(cut_button.objectName())
                        
                        types = "black" if self.type_of_figure == "white" else "white"
                        if types == "black":
                            self.count_of_black_figure -= 1
                        else:
                            self.count_of_white_figure -= 1
                        
                        self.change_position(more_important_ways, figure_type, index_of_row, index_of_col, self.type_of_figure, is_capture=True)

    def remove_cut_figures(self):
        for n in self.cut_figures:
            button = self.get_button_by_name(n)
            button.setIcon(QIcon())
        self.cut_figures.clear()

    def find_cut_figure(self, index_of_row, index_of_col):
        d_row = 1 if index_of_row > self.parent_r else -1
        d_col = 1 if index_of_col > self.parent_c else -1
        cut_row, cut_col = self.parent_r, self.parent_c
        time_r, time_c = self.parent_r + d_row, self.parent_c + d_col               
        while (time_r, time_c) != (index_of_row, index_of_col) and 0 <= time_r < 8 and 0 <= time_c < 8:
            if self.board[time_r][time_c].type_of_figure is not None:
                if self.board[time_r][time_c].type_of_figure != self.type_of_figure:
                    cut_row, cut_col = time_r, time_c
                else:
                    return  
            time_r += d_row
            time_c += d_col
        return [cut_row, cut_col]


    def change_position(self, ways, figure_type, index_of_row, index_of_col, types,is_capture):
        if figure_type == None and [index_of_row, index_of_col] in ways:
            name = f"button_{index_of_row}{index_of_col}"
            new_button = self.get_button_by_name(name)
            parent_button = self.get_button_by_name(self.name_parent_button)
            icon = parent_button.icon()
            new_button.setIcon(icon)
            parent_button.setIcon(QIcon())
            parent_button.setStyleSheet(self.style_buttons)
            
            is_queen = self.board[self.parent_r][self.parent_c].isqeen
            self.board[index_of_row][index_of_col].type_of_figure = self.board[self.parent_r][self.parent_c].type_of_figure
            self.board[index_of_row][index_of_col].isqeen = is_queen
            self.board[self.parent_r][self.parent_c].type_of_figure = None
            self.board[self.parent_r][self.parent_c].isbusy = False
            self.board[self.parent_r][self.parent_c].isqeen = False  
            self.board[index_of_row][index_of_col].isbusy = True
            self.check_is_figure_qeen(index_of_row, index_of_col)

            if is_capture:
                ways = []
                more_important_ways = []
                current_type = self.board[index_of_row][index_of_col].type_of_figure
                self.get_all_ways(index_of_row, index_of_col, ways, more_important_ways, self.board[index_of_row][index_of_col].isqeen,current_type,-1,-1)
                if len(more_important_ways) > 0:
                    self.name_parent_button = name
                    self.parent_r = index_of_row
                    self.parent_c = index_of_col
                    new_button.setStyleSheet(self.style_around_buttons)
                    return
            
                self.remove_cut_figures()
            
            self.name_parent_button = ""
            self.type_of_figure = "black" if self.type_of_figure == "white" else "white"


    def get_buttons_that_should_cut_others(self, lists, types):
        for button in self.all_buttons:
            row = int(button.objectName()[-2])
            col = int(button.objectName()[-1])
            if self.board[row][col].type_of_figure == self.type_of_figure:
                ways = []
                more_important_ways = []
                self.get_all_ways(row, col, ways, more_important_ways, self.board[row][col].isqeen,types)
                if len(more_important_ways)>0:
                    lists.append([row, col])

    def get_all_ways(self, row, col, ways, more_important_ways, is_qeen, types, nerow=-1, necol=-1):
        figure = self.board[row][col]
        if not is_qeen:
            if types=="white":
                if row+1<8 and col-1>-1 and self.board[row+1][col-1].type_of_figure==None:
                    ways.append([row+1, col-1])
                if row+1<8 and col-1>-1 and self.board[row+1][col-1].type_of_figure == "black" and row+2<8 and col-2>-1 and self.board[row+2][col-2].type_of_figure==None:
                    more_important_ways.append([row+2, col-2])
                if row-1>-1 and self.board[row-1][col-1].type_of_figure =="black" and row-2>-1 and col-2>-1 and self.board[row-2][col-2].type_of_figure==None:
                    more_important_ways.append([row-2, col-2])
                if row+1<8 and col+1<8 and self.board[row+1][col+1].type_of_figure==None:
                    ways.append([row+1, col+1])
                if row+1<8 and col+1<8 and self.board[row+1][col+1].type_of_figure =="black" and row+2<8 and col+2<8 and self.board[row+2][col+2].type_of_figure==None:
                    more_important_ways.append([row+2, col+2])
                if row-1>-1 and col+1<8 and self.board[row-1][col+1].type_of_figure =="black" and row-2>-1 and col+2<8 and self.board[row-2][col+2].type_of_figure==None:
                    more_important_ways.append([row-2, col+2])
            else:
                if row-1>-1 and col-1>-1 and self.board[row-1][col-1].type_of_figure==None:
                    ways.append([row-1, col-1])
                if row-1>-1 and col-1>-1 and self.board[row-1][col-1].type_of_figure == "white" and row-2>-1 and col-2>-1 and self.board[row-2][col-2].type_of_figure==None:
                    more_important_ways.append([row-2, col-2])
                if row+1<8 and col-1>-1 and self.board[row+1][col-1].type_of_figure == "white" and row+2<8 and col-2>-1 and self.board[row+2][col-2].type_of_figure==None:
                    more_important_ways.append([row+2, col-2])
                if row-1>-1 and col+1<8 and self.board[row-1][col+1].type_of_figure==None:
                    ways.append([row-1, col+1])
                if row-1> -1 and col+1<8 and self.board[row-1][col+1].type_of_figure == "white" and row-2>-1 and col+2<8 and self.board[row-2][col+2].type_of_figure==None:
                    more_important_ways.append([row-2, col+2])
                if row+1<8  and col+1<8 and self.board[row+1][col+1].type_of_figure =="white" and row+2<8 and col+2<8 and self.board[row+2][col+2].type_of_figure==None:
                    more_important_ways.append([row+2, col+2])

        else:
            types_fig = None
            if nerow!=-1 or necol!=-1:
                print(f"{nerow}{necol}")
                types_fig = self.board[nerow][necol].type_of_figure
                self.board[nerow][necol].type_of_figure = None
            count=1    
            directions = [
                (-1, -1),  # левый низ
                (-1, 1),   # левый верх
                (1, -1),   # правый низ
                (1, 1)     # правый верх
            ]
            for dr, dc in directions:
                count = 1
                while True:
                    r = row + count * dr
                    c = col + count * dc
                    if not (0 <= r < 8 and 0 <= c < 8):
                        break
                    if self.board[r][c].type_of_figure is None:
                        ways.append([r,c])
                        count += 1
                    else:
                        break
                            
            for dr, dc in directions:
                count = 1
                found_enemy = False
                                
                while True:
                    r = row + count * dr
                    c = col + count * dc
                                    
                    if not (0 <= r < 8 and 0 <= c < 8):
                        break
                                    
                    current_cell = self.board[r][c]
                                    
                    if not found_enemy:
                        if current_cell.type_of_figure is None:
                            # Пустая клетка - продолжаем поиск
                            count += 1
                            continue
                        elif current_cell.type_of_figure == ("white" if types == "black" else "black"):
                            # Нашли вражескую фигуру
                            found_enemy = True
                            count += 1
                            continue
                        else:
                            # Своя фигура - остановка
                            break
                    else:
                        if current_cell.type_of_figure is None:
                            # Пустая клетка за вражеской фигурой - добавляем
                            more_important_ways.append([r, c])
                            count += 1
                        else:
                            # Любая фигура за врагом - остановка
                            break
            if types_fig is not None:
                self.board[nerow][necol].type_of_figure = types_fig
                     
                    
           
    def pos_which_can_cut_figure(self, more_important_ways, result, types):
        
        # for r, c in more_important_ways:
        #     new_more_important_ways = []
        #     new_ways = []
        #     self.get_all_ways(r, c, new_ways, new_more_important_ways, True, types)
        #     if len(new_more_important_ways) > max_captures:
        #         max_captures = len(new_more_important_ways)
        print("\n more_important_ways:")
        print(more_important_ways)
        for r, c in more_important_ways:
            new_more_important_ways = []
            new_ways = []
            arr = self.find_cut_figure(r, c)
            nerow, necol = arr[0], arr[1]
            self.get_all_ways(r, c, new_ways, new_more_important_ways, True, types, nerow, necol)
            if len(new_more_important_ways) >0:
                print(f"\nДля позиции {r}{c} след ходы")
                print(new_more_important_ways)
                result.append([r, c])
        print("\n result:")
        print(result)
       
        return len(result) > 0


        
    
    def check_is_figure_qeen(self, row, col):
        figure = self.board[row][col]
        name = f"button_{row}{col}"
        button = self.get_button_by_name(name)
        if row ==7 and figure.type_of_figure =="white":
            button.setIcon(QIcon(qeen_icon_white))
        elif row == 0 and figure.type_of_figure =="black":
            button.setIcon(QIcon(qeen_icon_black))
        else:
            return
        self.board[row][col].isqeen = True
        

                
    def start_game(self):
        self.ui.central_widget.setCurrentWidget(self.ui.second_central_widget)
        self.ui.left_widget.setCurrentWidget(self.ui.second_tab_left)
        self.ui.right_widget.setCurrentWidget(self.ui.second_widget_right)  
        self.temp = self.ui.second_central_widget
    def read_rules(self):
        self.ui.central_widget.setCurrentWidget(self.ui.third_central_widget)
    def backs_to_game(self):
        if self.temp == self.ui.second_central_widget:
            self.ui.central_widget.setCurrentWidget(self.ui.second_central_widget)
        else:
            self.ui.central_widget.setCurrentWidget(self.ui.first_cenral_widget)
    def read_statistic(self):
        self.ui.right_widget.setCurrentWidget(self.ui.third_widget_right)
    def back_rep(self):
        self.ui.right_widget.setCurrentWidget(self.ui.second_widget_right)
    def get_away(self):
        self.close()
    def go_to_preview(self):
        self.ui.central_widget.setCurrentWidget(self.ui.first_cenral_widget)
        self.ui.right_widget.setCurrentWidget(self.ui.first_widget_right)
        self.ui.left_widget.setCurrentWidget(self.ui.first_tab_left)
        self.temp = self.ui.first_cenral_widget
        self.start_settings()
        self.start_settings_for_game()

    def start_settings_for_game(self):
        self.type_of_figure = "white"
        self.count_of_white_figure = 12
        self.count_of_black_figure = 12
        self.name_parent_button =""
        self.parent_r = -1
        self.parent_c = -1
    
    
    def set_theme_for_board(self, theme):
        for button in self.all_buttons:
            row = int(button.objectName()[-2])
            col = int(button.objectName()[-1])
            if (row%2 == 0 and col%2==0) or (row%2==1 and col%2==1):
                if theme=="Темно-зеленая":
                    button.setStyleSheet(style_for_dark_green_board)
                    self.style_buttons = style_for_dark_green_board
                    self.style_around_buttons = style_around_green
                elif theme == "Светлая":
                    button.setStyleSheet(style_for_light_yellow_board)
                    self.style_buttons = style_for_light_yellow_board
                    self.style_around_buttons = style_around_yellow
                    

    def open_settings(self):
        if self.settings_window is None:
            self.settings_window = SettingsWindow()
            
            self.settings_window.ui.pushButton.clicked.connect(lambda:self.on_settings_closed())
            
            self.settings_window.ui.pushButton_2.clicked.connect(
                lambda: self.set_theme_for_board(self.settings_window.ui.comboBox_2.currentText())
            )
        self.settings_window.show()

    def on_settings_closed(self):
        self.settings_window = None
        
class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    
        
      

if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    # for i in range(8):
    #     for j in range(8):
    #         print(window.board[i][j].type_of_figure, sep=" ")
    #     print("\n")
    window.show()
    sys.exit(app.exec())




                   



                   