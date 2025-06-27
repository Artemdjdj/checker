from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl
from PySide6 import *
import sys
import os
from form import *
from settings import *
from game import *
from utils import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.temp = self.ui.first_cenral_widget
        self.settings_window = None
        self.restart_window = None
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.more_important_ways = []
        self.ways =[]
        self.result = []
        self.list_buttons = []
        # Загружаем музыку
        self.music_file = ""
        self.player.setSource(QUrl.fromLocalFile(self.music_file))
        
        # Устанавливаем зацикливание
        self.player.setLoops(QMediaPlayer.Loops.Infinite)  # или -1 для бесконечного повтора

        self.player.play()
        self.current_music = "Без музыки"  # Значение по умолчанию для музыки
        self.current_theme = "Классическая"
        self.icon_white = QIcon()
        self.icon_white.addFile(icon_white)
        self.icon_black = QIcon()
        self.icon_black.addFile(icon_black)
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
        self.not_cutting_figure = []
        self.add_functions()
        self.start_settings()
        self.ui.left_widget.setCurrentWidget(self.ui.first_tab_left)
        self.ui.left_widget.tabBar().hide()
        self.ui.central_widget.tabBar().hide()
        self.ui.right_widget.tabBar().hide()
        self.ui.central_widget.setCurrentWidget(self.ui.first_cenral_widget)
        self.ui.right_widget.setCurrentWidget(self.ui.first_widget_right)
        self.style_buttons = style_dark_blue
        self.style_around_buttons = style_around_dark_blue
        self.style_buttons_non_use = style_base   

    def start_settings(self):
        self.type_of_figure = "white"
        self.count_of_white_figure = 12
        self.count_of_black_figure = 12
        self.name_parent_button =""
        self.parent_r = -1
        self.parent_c = -1
        self.ui.start_game_2_players.setEnabled(True)
        self.cut_figures = []
        for i in range(0, 8):
            for j in range(0,8):
                self.board[i][j].isbusy = False
                self.board[i][j].type_of_figure = None
                self.board[i][j].isqeen = False
                name = f"button_{i}{j}"
                button = self.get_button_by_name(name)
                button.setIcon(QIcon())
        
        for i in range(0,3):
            if i%2 == 0: 
                for j in range(0,8,2):
                    self.board[i][j].isbusy = True
                    self.board[i][j].type_of_figure = "white"
                    name = f"button_{i}{j}"
                    button = self.get_button_by_name(name)
                    button.setIcon(self.icon_white)
                    if j == 0 or j == 7:
                        self.board[i][j].isextreme = True
            else:
                for j in range(1,8,2):
                    self.board[i][j].isbusy = True
                    self.board[i][j].type_of_figure = "white"
                    name = f"button_{i}{j}"
                    button = self.get_button_by_name(name)
                    button.setIcon(self.icon_white)
                    if j == 0 or j == 7:
                        self.board[i][j].isextreme = True
                
        for i in range(5,8):
            if i%2 == 0: 
                for j in range(0,8,2):
                    self.board[i][j].isbusy = True
                    self.board[i][j].type_of_figure = "black"
                    name = f"button_{i}{j}"
                    button = self.get_button_by_name(name)
                    button.setIcon(self.icon_black)
                    if j == 0 or j == 7:
                        self.board[i][j].isextreme = True
            else:
                for j in range(1,8,2):
                    self.board[i][j].isbusy = True
                    self.board[i][j].type_of_figure = "black"
                    name = f"button_{i}{j}"
                    button = self.get_button_by_name(name)
                    button.setIcon(self.icon_black)
                    if j == 0 or j == 7:
                        self.board[i][j].isextreme = True
        for button in self.all_buttons:
            button.setEnabled(False)

          
    def add_functions(self):
        self.ui.start_the_game.clicked.connect(lambda:self.start_game())
        self.ui.rules_of_play.clicked.connect(lambda:self.read_rules())
        self.ui.back_to_game.clicked.connect(lambda:self.backs_to_game())
        self.ui.statistics.clicked.connect(lambda:self.read_statistic())
        self.ui.back_to_report.clicked.connect(lambda:self.back_rep())
        self.ui.leave_the_game.clicked.connect(lambda:self.get_away())
        self.ui.stop_game.clicked.connect(lambda:self.go_to_preview())
        self.ui.settings.clicked.connect(lambda:self.open_settings())
        self.ui.start_game_2_players.clicked.connect(lambda:self.start_game_for_2_players(True))
        for button in self.all_buttons:
            button.clicked.connect(lambda ch, b=button: self.choose_start_position(b))

    def get_button_by_name(self, name):
        for button in self.all_buttons:
            if button.objectName() == name:
                return button
    def make_red_dot(self, more_important_ways):
         for temp in self.more_important_ways:
                i = temp[0]
                j = temp[-1]
                name_of_btn = f"button_{i}{j}"
                btn = self.get_button_by_name(name_of_btn)
                btn.setIcon(QIcon(icon_of_red_dot))
                btn.setIconSize(QSize(10,10))
                self.list_buttons.append(btn)
    def clear_red_dot(self):
        if len(self.list_buttons)>0:
            for butt in self.list_buttons:
                i = int(butt.objectName()[-2])
                j = int(butt.objectName()[-1])
                if self.board[i][j].type_of_figure == None:
                    butt.setIcon(QIcon())
                    butt.setIconSize(QSize(60,60))
        self.list_buttons.clear()

    def choose_start_position(self, button):
        index_of_row = int(button.objectName()[-2])
        index_of_col = int(button.objectName()[-1])
        figure_type = self.board[index_of_row][index_of_col].type_of_figure
        
        
        if figure_type == self.type_of_figure: 
            button.setStyleSheet(self.style_around_buttons)
            self.name_parent_button = button.objectName()
            if (self.parent_r != -1 and self.parent_c != -1):
                name = f"button_{self.parent_r}{self.parent_c}"
                parent_button = self.get_button_by_name(name)
                parent_button.setStyleSheet(self.style_buttons)
            self.parent_r = index_of_row
            self.parent_c = index_of_col
            self.not_cutting_figure.clear()
            
            # при многократном выборе родительской позиции
            if (self.parent_r == index_of_row and self.parent_c == index_of_col):
                button.setStyleSheet(self.style_around_buttons)
            self.clear_red_dot()
            self.more_important_ways.clear()
            self.result.clear()
            self.ways.clear()
            check_is_qeen = self.board[self.parent_r][self.parent_c].isqeen
            self.get_all_ways(self.parent_r, self.parent_c, self.ways, self.more_important_ways, check_is_qeen, self.type_of_figure,-1,-1)
            if check_is_qeen:
                if self.pos_which_can_cut_figure(self.more_important_ways, self.result, self.type_of_figure): 
                    self.more_important_ways.clear()
                    for i in self.result:
                        self.more_important_ways.append(i)
            self.make_red_dot(self.more_important_ways)
        
        else:
            
            if self.parent_r == -1 or self.parent_c == -1 or self.board[self.parent_r][self.parent_c].type_of_figure != self.type_of_figure:
                return
            
            
            check_is_qeen = self.board[self.parent_r][self.parent_c].isqeen
            self.more_important_ways.clear()
            self.result.clear()
            list_buttons_that_must_to_cut_ohter = []
            
           
            self.get_buttons_that_should_cut_others(list_buttons_that_must_to_cut_ohter, self.type_of_figure)  
            
            self.get_all_ways(self.parent_r, self.parent_c, self.ways, self.more_important_ways, check_is_qeen, self.type_of_figure,-1,-1) 
            if check_is_qeen:
                if self.pos_which_can_cut_figure(self.more_important_ways, self.result, self.type_of_figure): 
                    self.more_important_ways.clear()
                    for i in self.result:
                        self.more_important_ways.append(i)
            

            # for temp in more_important_ways:
            #     name_of_btn = f"button_{temp[0]}{temp[-1]}"
            #     button  = self.get_button_by_name(name_of_btn)
            #     self.arr_of_buttons.append(button)
            #     button.setIcon(QIcon("icons/red-dot.png"))
            #     button.setIconSize(QSize(15,15))
                
                # number_of_diogonal = -1
                # for i in range(len(self.all_lines)):
                #     if [self.parent_r, self.parent_c] in self.all_lines[i] and [index_of_row, index_of_col]in self.all_lines:
                #         number_of_diogonal = i
                #         break;
                # is_in_big_arr = False
                # small_arr = []
                # big_arr = []
                # print(f"номер родителя {self.parent_r}{self.parent_c}")
                # print(f" метка  {index_of_row}{index_of_col}")
                # print(f"гомер диогонпли --- {number_of_diogonal}")
                # for element in more_important_ways:
                #     if element in self.all_lines[number_of_diogonal] and element[0] < self.parent_r:
                #         small_arr.append(element)
                #     elif element in self.all_lines[number_of_diogonal] and element[0] > self.parent_r:
                #         if [index_of_row, index_of_col] == element:
                #             is_in_big_arr = True
                #         big_arr.append(element)
                # print("small")
                # print(small_arr)
                # print("big")
                # print(big_arr)
            
                # result_arr = (small_arr if is_in_big_arr else big_arr)
                # print("result_arr")
                # print(result_arr)
                # for element in result_arr:
                #     self.not_cutting_figure.append(element)

               
            if figure_type is not None:
                return
            
                
            if len(list_buttons_that_must_to_cut_ohter) == 0:
                if len(self.more_important_ways) == 0 and len(self.ways) > 0:
                    self.change_position(self.ways, figure_type, index_of_row, index_of_col, self.type_of_figure, is_capture=False)
            else:
                
                if [self.parent_r, self.parent_c] in list_buttons_that_must_to_cut_ohter:
                    if [index_of_row, index_of_col] in self.more_important_ways:
                        self.clear_red_dot()
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
                            
                        self.board[cut_row][cut_col].type_of_figure = self.type_of_figure
                        self.board[cut_row][cut_col].isbusy = True
                        self.cut_figures.append(cut_button.objectName())
                        
                        types = "black" if self.type_of_figure == "white" else "white"
                        if types == "black":
                            self.count_of_black_figure -= 1
                        else:
                            self.count_of_white_figure -= 1
                        
                        self.change_position(self.more_important_ways, figure_type, index_of_row, index_of_col, self.type_of_figure, is_capture=True)
                        restart = self.check_win()
                        if (restart != ""):
                            self.clear_red_dot()
                            self.open_restart_window(restart)
                    


    def check_win(self):
        result = ""
        if self.count_of_black_figure == 0:
            result = "white"
            return result
        elif self.count_of_white_figure ==0:
            result = "black"
            return result
        else:
            types = self.type_of_figure
            list_of_figures= []
            for i in range(8):
                for j in range(8):
                    if self.board[i][j].type_of_figure == types:
                        list_of_figures.append([i,j])
            if len(list_of_figures)==0:
                result = ("black" if types == "white" else "white")
                return result
            for i in list_of_figures:
                ways = []
                more_important_ways = []
                self.get_all_ways(i[0],i[1] , ways, more_important_ways, self.board[i[0]][i[1]].isqeen, types,-1,-1)
                if len(ways)>0 or len(more_important_ways)>0:
                    return result
                
            
        result = ("black" if types == "white" else "white")
        return result

        

    def remove_cut_figures(self):
        for n in self.cut_figures:
            button = self.get_button_by_name(n)
            button.setIcon(QIcon())
            row, col = int(button.objectName()[-2]), int(button.objectName()[-1])
            self.board[row][col].type_of_figure = None
            self.board[row][col].isbusy = False
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
            new_button.setIconSize(QSize(60,60))
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
                for buttons in self.all_buttons:
                    i = int(buttons.objectName()[-2])
                    j = int(buttons.objectName()[-1])
                    if self.board[i][j].type_of_figure == self.board[index_of_row][index_of_col].type_of_figure:
                        # buttons.setEnabled(False)
                        buttons.setAttribute(Qt.WA_TransparentForMouseEvents, True)  
                self.ways.clear()
                self.more_important_ways.clear()
                self.result.clear()
                current_type = self.board[index_of_row][index_of_col].type_of_figure
                self.clear_red_dot()
                self.get_all_ways(index_of_row, index_of_col, self.ways, self.more_important_ways, self.board[index_of_row][index_of_col].isqeen,current_type,-1,-1)
                # print("more_important_ways")
                # print(more_important_ways)
                # temp = self.block_ways_which_is_not_cutting(more_important_ways);
                # more_important_ways.clear()
                # more_important_ways = temp
                # print("new_more_important_ways")
                # print(temp)
                # print("несбиваемые")
                # print(self.not_cutting_figure)
                self.make_red_dot(self.more_important_ways)
                if len(self.more_important_ways) > 0:
                    self.name_parent_button = name
                    self.parent_r = index_of_row
                    self.parent_c = index_of_col
                    new_button.setStyleSheet(self.style_around_buttons)
                    return
            
                self.remove_cut_figures()

            self.name_parent_button = ""
            self.type_of_figure = "black" if self.type_of_figure == "white" else "white"
            self.not_cutting_figure.clear()
            self.clear_red_dot()
            for buttons in self.all_buttons:
                buttons.setAttribute(Qt.WA_TransparentForMouseEvents, False) 
            
 

    # def block_ways_which_is_not_cutting(self, arr):
    #     new_arr = []
    #     for element in arr:
    #         if element in self.not_cutting_figure:
    #             continue
    #         else:
    #             new_arr.append(element)
    #     return new_arr

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
        for r, c in more_important_ways:
            new_more_important_ways = []
            new_ways = []
            arr = self.find_cut_figure(r, c)
            nerow, necol = arr[0], arr[1]
            self.get_all_ways(r, c, new_ways, new_more_important_ways, True, types, nerow, necol)
            if len(new_more_important_ways) >0:
                result.append([r, c])
            
        result = self.get_elements_in_one_lines(more_important_ways, result)    

        return len(result) > 0
    

    def get_elements_in_one_lines(self, more_important_ways, result):
        for elements in self.all_lines:
            arr = []
            for pos in more_important_ways:
                if pos in elements:
                    arr.append(pos)
            if len(arr)>1:
                small = []
                big = []
                for el in arr:
                    if el[0] < self.parent_r:
                        small.append(el)
                    elif el[0]> self.parent_r:
                        big.append(el)
                new_big = []
                new_small = []
                for temp in result:
                    if temp in big:
                        new_big.append(temp)
                    elif temp in small:
                        new_small.append(temp)
                if len(new_big)>0:
                    big = new_big
                if len(new_small)> 0:
                    small = new_small
                if len(big)>0 and len(small)> 0:
                    for t in small:
                        if t not in result:
                            result.append(t)
                    for t in big:
                        if t not in result:
                            result.append(t)        
        return result
                
            
    
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
        self.current_music="Без музыки"
        self.music_file = ""
        self.player.stop()
        
        
        # self.start_settings_for_game()

    # def start_settings_for_game(self):
    #     self.type_of_figure = "white"
    #     self.count_of_white_figure = 12
    #     self.count_of_black_figure = 12
    #     self.name_parent_button =""
    #     self.parent_r = -1
    #     self.parent_c = -1
    
    
    def set_theme_for_board(self, theme):
        self.current_theme = theme
        style = "" 
        style2 = ""
        if theme=="Темно-зеленая":
            style =  style_for_dark_green_board
            style2 = style_base
            self.style_buttons = style_for_dark_green_board
            self.style_around_buttons =  style_around_green
            self.style_buttons_non_use = style_base
        elif theme == "Светлая":
            style =  style_for_light_blue_board
            style2 = style_base
            self.style_buttons = style_for_light_blue_board
            self.style_around_buttons = style_around_light_blue
            self.style_buttons_non_use = style_base
        elif theme =="Темно-синяя":
            style =  style_dark_blue
            style2 = style_base
            self.style_buttons = style_dark_blue
            self.style_around_buttons = style_around_dark_blue
            self.style_buttons_non_use = style_base
        elif theme == "Классическая":
            style =  style_for_classic_board_grey
            style2 = style_for_classic_board_orange
            self.style_buttons = style_for_classic_board_grey
            self.style_around_buttons = style_classic_around 
            self.style_buttons_non_use = style_for_classic_board_orange

        for button in self.all_buttons:
            row = int(button.objectName()[-2])
            col = int(button.objectName()[-1])
            if (row%2 == 0 and col%2==0) or (row%2==1 and col%2==1):
                button.setStyleSheet(style)
            else:
                button.setStyleSheet(style2)
        
            
    def set_music_for_board(self, music):
        if self.current_music == music:
            return
        else:
            self.current_music = music
        if music == "Классическая":
            self.music_file = classic_music
        elif music == "Спокойная":
            self.music_file = calm_music
        elif music =="Умеренная":
            self.music_file = moderate_music
        elif music == "Быстрая":
            self.music_file = fast_music
        else:
            self.music_file = ""
            self.player.stop()
        self.player.setSource(QUrl.fromLocalFile(self.music_file))
        self.player.setLoops(QMediaPlayer.Loops.Infinite)
        self.player.play()

    def open_settings(self):
        if self.settings_window is None:
            self.settings_window = SettingsWindow()
            music_index = self.settings_window.ui.comboBox.findText(self.current_music)
            if music_index >= 0:
                self.settings_window.ui.comboBox.setCurrentIndex(music_index)
                
            theme_index = self.settings_window.ui.comboBox_2.findText(self.current_theme)
            if theme_index >= 0:
                self.settings_window.ui.comboBox_2.setCurrentIndex(theme_index)
            temp_music = self.settings_window.ui.comboBox.currentText()
            temp_theme = self.settings_window.ui.comboBox_2.currentText()
            self.settings_window.ui.pushButton.clicked.connect(lambda:self.on_settings_closed())
            
            self.settings_window.ui.pushButton_2.clicked.connect(
                lambda: self.set_theme_for_board(self.settings_window.ui.comboBox_2.currentText())
            )
            self.settings_window.ui.pushButton_2.clicked.connect(lambda:self.set_music_for_board(self.settings_window.ui.comboBox.currentText()))
            self.settings_window.ui.pushButton_3.clicked.connect(lambda:self.on_settings_cancel(temp_theme, temp_music))
            
        self.settings_window.show()

    def on_settings_closed(self):
        self.settings_window = None

    def on_settings_cancel(self, theme, music):
        self.set_theme_for_board(theme)

    def open_restart_window(self, restart):
        if self.restart_window is None:
            self.restart_window = RestartWindow()
            if restart == "white":
                self.restart_window.ui.label_2.setStyleSheet(win_white)
                self.restart_window.ui.label_2.setText("Выиграли белые!")
            else:
                self.restart_window.ui.label_2.setStyleSheet(win_black)
                self.restart_window.ui.label_2.setText("Выиграли черные!")
            self.restart_window.ui.pushButton.clicked.connect(lambda:self.on_restart_closed())
            self.restart_window.ui.pushButton_2.clicked.connect(lambda:self.on_preview())
        self.restart_window.show()
    def on_preview(self):
        self.restart_window = None
        self.go_to_preview()

    def on_restart_closed(self):
        self.restart_window = None
        self.start_settings()
    
        
    def make_board_buttons_clicked_or_unklicked(self, is_enabled):
        for button in self.all_buttons:
            button.setEnabled(is_enabled)

    def start_game_for_2_players(self, is_enabled):
        self.make_board_buttons_clicked_or_unklicked(is_enabled)
        self.ui.start_game_2_players.setEnabled(False)
        
    

        
      

if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




                   



                   