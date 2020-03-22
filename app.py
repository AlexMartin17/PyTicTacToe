import arcade
import random

win = "0"
p = "x"
c = "o"

WIDTH = 600
HEIGHT = 600

class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.AZURE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Tic Tac Toe", WIDTH/2, 300, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Press X or O to choose a sign..", WIDTH/2, 250, arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        global p, c
        if key == arcade.key.X:
            p = "X"
            c = "O"
            game_view = GameView()
            self.window.show_view(game_view)
        elif key == arcade.key.O:
            p = "O"
            c = "X"
            game_view = GameView()
            self.window.show_view(game_view)

class GameView(arcade.View):

    def __init__(self):
        super().__init__()
        self.board = [0,0,0,0,0,0,0,0,0]

    def CheckBoard(self):
        global win, p, c
        if self.board[0] == 'x' and self.board[1] == 'x' and self.board[2] == 'x':
            if p == "X":
                win = "p"
            else:
                win = "c"
        elif self.board[3] == 'x' and self.board[4] == 'x' and self.board[5] == 'x':
            if p == "X":
                win = "p"
            else:
                win = "c"
        elif self.board[6] == 'x' and self.board[7] == 'x' and self.board[8] == 'x':
            if p == "X":
                win = "p"
            else:
                win = "c"
        elif self.board[0] == 'x' and self.board[3] == 'x' and self.board[6] == 'x':
            if p == "X":
                win = "p"
            else:
                win = "c"
        elif self.board[1] == 'x' and self.board[4] == 'x' and self.board[7] == 'x':
            if p == "X":
                win = "p"
            else:
                win = "c"
        elif self.board[2] == 'x' and self.board[5] == 'x' and self.board[8] == 'x':
            if p == "X":
                win = "p"
            else:
                win = "c"
        elif self.board[0] == 'x' and self.board[4] == 'x' and self.board[8] == 'x':
            if p == "X":
                win = "p"
            else:
                win = "c"
        elif self.board[2] == 'x' and self.board[4] == 'x' and self.board[6] == 'x':
            if p == "X":
                win = "p"
            else:
                win = "c"
        elif self.board[0] == 'o' and self.board[1] == 'o' and self.board[2] == 'o':
              if p == "O":
                  win = "p"
              else:
                  win = "c"
        elif self.board[3] == 'o' and self.board[4] == 'o' and self.board[5] == 'o':
              if p == "O":
                  win = "p"
              else:
                  win = "c"
        elif self.board[6] == 'o' and self.board[7] == 'o' and self.board[8] == 'o':
              if p == "O":
                  win = "p"
              else:
                  win = "c"
        elif self.board[0] == 'o' and self.board[3] == 'o' and self.board[6] == 'o':
              if p == "O":
                  win = "p"
              else:
                  win = "c"
        elif self.board[1] == 'o' and self.board[4] == 'o' and self.board[7] == 'o':
              if p == "O":
                  win = "p"
              else:
                  win = "c"
        elif self.board[2] == 'o' and self.board[5] == 'o' and self.board[8] == 'o':
              if p == "O":
                  win = "p"
              else:
                  win = "c"
        elif self.board[0] == 'o' and self.board[4] == 'o' and self.board[8] == 'o':
              if p == "O":
                  win = "p"
              else:
                  win = "c"
        elif self.board[2] == 'o' and self.board[4] == 'o' and self.board[6] == 'o':
              if p == "O":
                  win = "p"
              else:
                  win = "c"
        elif all(self.board):
            win = "d"

        if win != "0":
            game_view = GameOverView()
            self.window.show_view(game_view)

    def PcMove(self):
          global p, c
          try:
              if c == "X":
                  self.temp = []
                  for x in range(len(self.board)):
                      if self.board[x] == 0 and self.board[x] == 0:
                          self.temp.append(x)
                  self.cm = random.choice(self.temp)
                  self.board[self.cm] = "x"

              if c == "O":
                  self.temp = []
                  for o in range(len(self.board)):
                      if self.board[o] == 0 and self.board[o] == 0:
                          self.temp.append(o)
                  self.cm = random.choice(self.temp)
                  self.board[self.cm] = "o"
          except IndexError:
              pass

    def on_show(self):
        arcade.set_background_color(arcade.color.AZURE)
        if p == "O":
            self.PcMove()
        else:
            pass

    def on_draw(self):
        global p, c
        arcade.start_render()
        self.shape_list = arcade.ShapeElementList()
        arcade.draw_line(0, 400, 600, 400, arcade.color.WHITE, 5)
        arcade.draw_line(0, 200, 600, 200, arcade.color.WHITE, 5)
        arcade.draw_line(400, 0, 400, 600, arcade.color.WHITE, 5)
        arcade.draw_line(200, 0, 200, 600, arcade.color.WHITE, 5)

        for circle in self.board:
            if circle == "o":
                if self.board[0] == "o":
                    self.shape = arcade.create_ellipse(100,500,100,100,arcade.color.WHITE)
                    self.shape_list.append(self.shape)
                    self.shape = arcade.create_ellipse(100,500,95,95,arcade.color.AZURE)
                    self.shape_list.append(self.shape)
                if self.board[1] == "o":
                    self.shape = arcade.create_ellipse(300,500,100,100,arcade.color.WHITE)
                    self.shape_list.append(self.shape)
                    self.shape = arcade.create_ellipse(300,500,95,95,arcade.color.AZURE)
                    self.shape_list.append(self.shape)
                if self.board[2] == "o":
                    self.shape = arcade.create_ellipse(500,500,100,100,arcade.color.WHITE)
                    self.shape_list.append(self.shape)
                    self.shape = arcade.create_ellipse(500,500,95,95,arcade.color.AZURE)
                    self.shape_list.append(self.shape)
                if self.board[3] == "o":
                    self.shape = arcade.create_ellipse(100,300,100,100,arcade.color.WHITE)
                    self.shape_list.append(self.shape)
                    self.shape = arcade.create_ellipse(100,300,95,95,arcade.color.AZURE)
                    self.shape_list.append(self.shape)
                if self.board[4] == "o":
                    self.shape = arcade.create_ellipse(300,300,100,100,arcade.color.WHITE)
                    self.shape_list.append(self.shape)
                    self.shape = arcade.create_ellipse(300,300,95,95,arcade.color.AZURE)
                    self.shape_list.append(self.shape)
                if self.board[5] == "o":
                    self.shape = arcade.create_ellipse(500,300,100,100,arcade.color.WHITE)
                    self.shape_list.append(self.shape)
                    self.shape = arcade.create_ellipse(500,300,95,95,arcade.color.AZURE)
                    self.shape_list.append(self.shape)
                if self.board[6] == "o":
                    self.shape = arcade.create_ellipse(100,100,100,100,arcade.color.WHITE)
                    self.shape_list.append(self.shape)
                    self.shape = arcade.create_ellipse(100,100,95,95,arcade.color.AZURE)
                    self.shape_list.append(self.shape)
                if self.board[7] == "o":
                    self.shape = arcade.create_ellipse(300,100,100,100,arcade.color.WHITE)
                    self.shape_list.append(self.shape)
                    self.shape = arcade.create_ellipse(300,100,95,95,arcade.color.AZURE)
                    self.shape_list.append(self.shape)
                if self.board[8] == "o":
                    self.shape = arcade.create_ellipse(500,100,100,100,arcade.color.WHITE)
                    self.shape_list.append(self.shape)
                    self.shape = arcade.create_ellipse(500,100,95,95,arcade.color.AZURE)
                    self.shape_list.append(self.shape)

        for cross in self.board:
                if cross == "x":
                    if self.board[0] == "x":
                        self.shape = arcade.create_line(0, 600, 200, 400, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                        self.shape = arcade.create_line(200, 600, 0, 400, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                    if self.board[1] == "x":
                        self.shape = arcade.create_line(200, 600, 400, 400, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                        self.shape = arcade.create_line(400, 600, 200, 400, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                    if self.board[2] == "x":
                        self.shape = arcade.create_line(400, 600, 600, 400, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                        self.shape = arcade.create_line(600, 600, 400, 400, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                    if self.board[3] == "x":
                        self.shape = arcade.create_line(0, 400, 200, 200, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                        self.shape = arcade.create_line(200, 400, 0, 200, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                    if self.board[4] == "x":
                        self.shape = arcade.create_line(200, 400, 400, 200, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                        self.shape = arcade.create_line(400, 400, 200, 200, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                    if self.board[5] == "x":
                        self.shape = arcade.create_line(400, 400, 600, 200, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                        self.shape = arcade.create_line(600, 400, 400, 200, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                    if self.board[6] == "x":
                        self.shape = arcade.create_line(0, 200, 200, 0, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                        self.shape = arcade.create_line(200, 200, 0, 0, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                    if self.board[7] == "x":
                        self.shape = arcade.create_line(200, 200, 400, 0, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                        self.shape = arcade.create_line(400, 200, 200, 0, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                    if self.board[8] == "x":
                        self.shape = arcade.create_line(400, 200, 600, 0, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                        self.shape = arcade.create_line(600, 200, 400, 0, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                self.shape_list.draw()

    def on_mouse_press(self, x, y, _button, _modifiers): #Player move
        global p, c
        if p == "O":
            self.CheckBoard()
            try:
                if 0 <= x <= 200 and 400 <= y <= 600:
                    if self.board[0] == 0:
                        self.board[0] = "o"
                    else:
                        raise Exception("Not allowed")
                elif 200 <= x <= 400 and 400 <= y <= 600:
                    if self.board[1] == 0:
                        self.board[1] = "o"
                    else:
                        raise Exception("Not allowed")
                elif 400 <= x <= 600 and 400 <= y <= 600:
                    if self.board[2] == 0:
                        self.board[2] = "o"
                    else:
                        raise Exception("Not allowed")
                elif 0 <= x <= 200 and 200 <= y <= 400:
                    if self.board[3] == 0:
                        self.board[3] = "o"
                    else:
                        raise Exception("Not allowed")
                elif 200 <= x <= 400 and 200 <= y <= 400:
                    if self.board[4] == 0:
                        self.board[4] = "o"
                    else:
                        raise Exception("Not allowed")
                elif 400 <= x <= 600 and 200 <= y <= 400:
                    if self.board[5] == 0:
                        self.board[5] = "o"
                    else:
                        raise Exception("Not allowed")
                elif 0 <= x <= 200 and 0 <= y <= 200:
                    if self.board[6] == 0:
                        self.board[6] = "o"
                    else:
                        raise Exception("Not allowed")
                elif 200 <= x <= 400 and 0 <= y <= 200:
                    if self.board[7] == 0:
                        self.board[7] = "o"
                    else:
                        raise Exception("Not allowed")
                elif 400 <= x <= 600 and 0 <= y <= 200:
                    if self.board[8] == 0:
                        self.board[8] = "o"
                    else:
                        raise Exception("Not allowed")
                self.CheckBoard()
                self.PcMove()
                self.CheckBoard()
            except Exception:
                pass

        elif p == "X":
                self.CheckBoard()
                try:
                    if 0 <= x <= 200 and 400 <= y <= 600:
                        if self.board[0] == 0:
                            self.board[0] = "x"
                        else:
                            raise Exception("Not allowed")
                    elif 200 <= x <= 400 and 400 <= y <= 600:
                        if self.board[1] == 0:
                            self.board[1] = "x"
                        else:
                            raise Exception("Not allowed")
                    elif 400 <= x <= 600 and 400 <= y <= 600:
                        if self.board[2] == 0:
                            self.board[2] = "x"
                        else:
                            raise Exception("Not allowed")
                    elif 0 <= x <= 200 and 200 <= y <= 400:
                        if self.board[3] == 0:
                            self.board[3] = "x"
                        else:
                            raise Exception("Not allowed")
                    elif 200 <= x <= 400 and 200 <= y <= 400:
                        if self.board[4] == 0:
                            self.board[4] = "x"
                        else:
                            raise Exception("Not allowed")
                    elif 400 <= x <= 600 and 200 <= y <= 400:
                        if self.board[5] == 0:
                            self.board[5] = "x"
                        else:
                            raise Exception("Not allowed")
                    elif 0 <= x <= 200 and 0 <= y <= 200:
                        if self.board[6] == 0:
                            self.board[6] = "x"
                        else:
                            raise Exception("Not allowed")
                    elif 200 <= x <= 400 and 0 <= y <= 200:
                        if self.board[7] == 0:
                            self.board[7] = "x"
                        else:
                            raise Exception("Not allowed")
                    elif 400 <= x <= 600 and 0 <= y <= 200:
                        if self.board[8] == 0:
                            self.board[8] = "x"
                        else:
                            raise Exception("Not allowed")
                    self.CheckBoard()
                    self.PcMove()
                    self.CheckBoard()
                except Exception:
                    pass

class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show(self):
        arcade.set_background_color(arcade.color.AZURE)

    def on_draw(self):
        global win
        arcade.start_render()
        if win == "p":
            arcade.draw_text("Congratulations, you won !", WIDTH/2, 300, arcade.color.WHITE, font_size=40, anchor_x="center")
            arcade.draw_text("Click to continue", WIDTH/2, 250, arcade.color.WHITE, font_size=20, anchor_x="center")
        elif win == "c":
            arcade.draw_text("Computer wins :(", WIDTH/2, 300, arcade.color.WHITE, font_size=50, anchor_x="center")
            arcade.draw_text("Click to continue", WIDTH/2, 250, arcade.color.WHITE, font_size=20, anchor_x="center")
        elif win == "d":
            arcade.draw_text("It's a draw..", WIDTH/2, 300, arcade.color.WHITE, font_size=50, anchor_x="center")
            arcade.draw_text("Click to continue", WIDTH/2, 250, arcade.color.WHITE, font_size=20, anchor_x="center")
        else:
            pass

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        global win
        win = "0"
        game_view = MenuView()
        self.window.show_view(game_view)

def main():
    window = arcade.Window(WIDTH, HEIGHT, "Tic Tac Toe A-M 2020")
    window.total_score = 0
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()
