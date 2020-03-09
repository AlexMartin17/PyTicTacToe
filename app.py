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
        self.cross = [0,0,0,0,0,0,0,0,0]
        self.circle = [0,0,0,0,0,0,0,0,0]
        self.draw = [0,0,0,0,0,0,0,0,0]

    def CheckBoard(self):
        global win, p, c

        if self.cross[0] == 'x' and self.cross[1] == 'x' and self.cross[2] == 'x':
            if p == "X":
                win = "p"
            else:
                print("Computer wins")
                win == "c"
        elif self.cross[3] == 'x' and self.cross[4] == 'x' and self.cross[5] == 'x':
            if p == "X":
                print("You win!!")
                win = "p"
            else:
                print("Computer wins")
                win == "c"
        elif self.cross[6] == 'x' and self.cross[7] == 'x' and self.cross[8] == 'x':
            if p == "X":
                print("You win!!")
                win = "p"
            else:
                print("Computer wins")
                win == "c"
        elif self.cross[0] == 'x' and self.cross[3] == 'x' and self.cross[6] == 'x':
            if p == "X":
                print("You win!!")
                win = "p"
            else:
                print("Computer wins")
                win = "c"
        elif self.cross[1] == 'x' and self.cross[4] == 'x' and self.cross[7] == 'x':
            if p == "X":
                print("You win!!")
                win = "p"
            else:
                print("Computer wins")
                win = "c"
        elif self.cross[2] == 'x' and self.cross[5] == 'x' and self.cross[8] == 'x':
            if p == "X":
                print("You win!!")
                win = "p"
            else:
                print("Computer wins")
                win = "c"
        elif self.cross[0] == 'x' and self.cross[4] == 'x' and self.cross[8] == 'x':
            if p == "X":
                print("You win!!")
                win = "p"
            else:
                print("Computer wins")
                win == "c"
        elif self.cross[2] == 'x' and self.cross[4] == 'x' and self.cross[6] == 'x':
            if p == "X":
                print("You win!!")
                win = "p"
            else:
                print("Computer wins")
                win = "c"
        elif self.circle[0] == 'o' and self.circle[1] == 'o' and self.circle[2] == 'o':
              if p == "O":
                  print("You win!!")
                  win = "p"
              else:
                  print("Computer wins")
                  win = "c"
        elif self.circle[3] == 'o' and self.circle[4] == 'o' and self.circle[5] == 'o':
              if p == "O":
                  print("You win!!")
                  win = "p"
              else:
                  print("Computer wins")
                  win = "c"
        elif self.circle[6] == 'o' and self.circle[7] == 'o' and self.circle[8] == 'o':
              if p == "O":
                  print("You win!!")
                  win = "p"
              else:
                  print("Computer wins")
                  win = "c"
        elif self.circle[0] == 'o' and self.circle[3] == 'o' and self.circle[6] == 'o':
              if p == "O":
                  print("You win!!")
                  win = "p"
              else:
                  print("Computer wins")
                  win = "c"
        elif self.circle[1] == 'o' and self.circle[4] == 'o' and self.circle[7] == 'o':
              if p == "O":
                  print("You win!!")
                  win = "p"
              else:
                  print("Computer wins")
                  win = "c"
        elif self.circle[2] == 'o' and self.circle[5] == 'o' and self.circle[8] == 'o':
              if p == "O":
                  print("You win!!")
                  win = "p"
              else:
                  print("Computer wins")
                  win = "c"
        elif self.circle[0] == 'o' and self.circle[4] == 'o' and self.circle[8] == 'o':
              if p == "O":
                  print("You win!!")
                  win = "p"
              else:
                  print("Computer wins")
                  win = "c"
        elif self.circle[2] == 'o' and self.circle[4] == 'o' and self.circle[6] == 'o':
              if p == "O":
                  print("You win!!")
                  win = "p"
              else:
                  print("Computer wins")
                  win = "c"
        elif self.circle[0] != 0 and self.circle[1] != 0 and self.circle[2] != 0 and self.circle[3] != 0 and self.circle[4] != 0 and self.circle[5] != 0 and self.circle[6] != 0 and self.circle[7] != 0 and self.circle[8] != 0 and self.cross[0] != 0 and self.cross[1] != 0 and self.cross[2] != 0 and self.cross[3] != 0 and self.cross[4] != 0 and self.cross[5] != 0 and self.cross[6] != 0 and self.cross[7] != 0 and self.cross[8] != 0:
            print("Its a draw") #Currently bugged
        else:
            pass
            
        if win != "0":
            game_view = GameOverView()
            self.window.show_view(game_view)

    def PcMove(self):
        global p, c
        self.cm = random.randrange(9)
        if c == "X":
            for x in range(0,9):
                if int(self.cm) == x:
                    if self.cross[x] == 0 and self.circle[x] == 0:
                        self.cross[x] = "x"
                    else:
                        self.PcMove()
                        self.CheckBoard()
                        for a in self.cross: #for debugging
                            print(a, end=="")

        elif c == "O":
            for x in range(0,9):
                if int(self.cm) == x:
                    if self.circle[x] == 0 and self.cross[x] == 0:
                        self.circle[x] = "o"
                    else:
                        self.PcMove()
                        self.CheckBoard()
                        for a in self.circle: #for debugging
                            print(a, end=="")

    def on_show(self):
        arcade.set_background_color(arcade.color.AZURE)
        if p == "O":
            GameView.PcMove(self)
        else:
            pass

    def on_draw(self):
        global p, c
        arcade.start_render()
        self.shape_list = arcade.ShapeElementList()
        #tic tac toe lines
        arcade.draw_line(0, 400, 600, 400, arcade.color.WHITE, 5)
        arcade.draw_line(0, 200, 600, 200, arcade.color.WHITE, 5)
        arcade.draw_line(400, 0, 400, 600, arcade.color.WHITE, 5)
        arcade.draw_line(200, 0, 200, 600, arcade.color.WHITE, 5)

        for circle in self.circle:
            if circle == "o":
                if self.circle[0] == "o":
                    self.shape = arcade.create_ellipse(100,500,100,100,arcade.color.WHITE)
                    self.shape_list.append(self.shape)
                    self.shape = arcade.create_ellipse(100,500,95,95,arcade.color.AZURE)
                    self.shape_list.append(self.shape)
                if self.circle[1] == "o":
                    self.shape = arcade.create_ellipse(300,500,100,100,arcade.color.WHITE)
                    self.shape_list.append(self.shape)
                    self.shape = arcade.create_ellipse(300,500,95,95,arcade.color.AZURE)
                    self.shape_list.append(self.shape)
                if self.circle[2] == "o":
                    self.shape = arcade.create_ellipse(500,500,100,100,arcade.color.WHITE)
                    self.shape_list.append(self.shape)
                    self.shape = arcade.create_ellipse(500,500,95,95,arcade.color.AZURE)
                    self.shape_list.append(self.shape)
                if self.circle[3] == "o":
                    self.shape = arcade.create_ellipse(100,300,100,100,arcade.color.WHITE)
                    self.shape_list.append(self.shape)
                    self.shape = arcade.create_ellipse(100,300,95,95,arcade.color.AZURE)
                    self.shape_list.append(self.shape)
                if self.circle[4] == "o":
                    self.shape = arcade.create_ellipse(300,300,100,100,arcade.color.WHITE)
                    self.shape_list.append(self.shape)
                    self.shape = arcade.create_ellipse(300,300,95,95,arcade.color.AZURE)
                    self.shape_list.append(self.shape)
                if self.circle[5] == "o":
                    self.shape = arcade.create_ellipse(500,300,100,100,arcade.color.WHITE)
                    self.shape_list.append(self.shape)
                    self.shape = arcade.create_ellipse(500,300,95,95,arcade.color.AZURE)
                    self.shape_list.append(self.shape)
                if self.circle[6] == "o":
                    self.shape = arcade.create_ellipse(100,100,100,100,arcade.color.WHITE)
                    self.shape_list.append(self.shape)
                    self.shape = arcade.create_ellipse(100,100,95,95,arcade.color.AZURE)
                    self.shape_list.append(self.shape)
                if self.circle[7] == "o":
                    self.shape = arcade.create_ellipse(300,100,100,100,arcade.color.WHITE)
                    self.shape_list.append(self.shape)
                    self.shape = arcade.create_ellipse(300,100,95,95,arcade.color.AZURE)
                    self.shape_list.append(self.shape)
                if self.circle[8] == "o":
                    self.shape = arcade.create_ellipse(500,100,100,100,arcade.color.WHITE)
                    self.shape_list.append(self.shape)
                    self.shape = arcade.create_ellipse(500,100,95,95,arcade.color.AZURE)
                    self.shape_list.append(self.shape)

        for cross in self.cross:
                if cross == "x":
                    if self.cross[0] == "x":
                        self.shape = arcade.create_line(0, 600, 200, 400, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                        self.shape = arcade.create_line(200, 600, 0, 400, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                    if self.cross[1] == "x":
                        self.shape = arcade.create_line(200, 600, 400, 400, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                        self.shape = arcade.create_line(400, 600, 200, 400, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                    if self.cross[2] == "x":
                        self.shape = arcade.create_line(400, 600, 600, 400, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                        self.shape = arcade.create_line(600, 600, 400, 400, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                    if self.cross[3] == "x":
                        self.shape = arcade.create_line(0, 400, 200, 200, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                        self.shape = arcade.create_line(200, 400, 0, 200, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                    if self.cross[4] == "x":
                        self.shape = arcade.create_line(200, 400, 400, 200, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                        self.shape = arcade.create_line(400, 400, 200, 200, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                    if self.cross[5] == "x":
                        self.shape = arcade.create_line(400, 400, 600, 200, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                        self.shape = arcade.create_line(600, 400, 400, 200, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                    if self.cross[6] == "x":
                        self.shape = arcade.create_line(0, 200, 200, 0, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                        self.shape = arcade.create_line(200, 200, 0, 0, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                    if self.cross[7] == "x":
                        self.shape = arcade.create_line(200, 200, 400, 0, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                        self.shape = arcade.create_line(400, 200, 200, 0, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                    if self.cross[8] == "x":
                        self.shape = arcade.create_line(400, 200, 600, 0, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                        self.shape = arcade.create_line(600, 200, 400, 0, arcade.color.WHITE, 5)
                        self.shape_list.append(self.shape)
                self.shape_list.draw()

    def on_mouse_press(self, x, y, _button, _modifiers): #Player move
        global p, c
        if p == "O":
            self.CheckBoard()
            if 0 <= x <= 200 and 400 <= y <= 600:
                self.circle[0] = "o"
            elif 200 <= x <= 400 and 400 <= y <= 600:
                self.circle[1] = "o"
            elif 400 <= x <= 600 and 400 <= y <= 600:
                self.circle[2] = "o"
            elif 0 <= x <= 200 and 200 <= y <= 400:
                self.circle[3] = "o"
            elif 200 <= x <= 400 and 200 <= y <= 400:
                self.circle[4] = "o"
            elif 400 <= x <= 600 and 200 <= y <= 400:
                self.circle[5] = "o"
            elif 0 <= x <= 200 and 0 <= y <= 200:
                self.circle[6] = "o"
            elif 200 <= x <= 400 and 0 <= y <= 200:
                self.circle[7] = "o"
            elif 400 <= x <= 600 and 0 <= y <= 200:
                self.circle[8] = "o"
            self.CheckBoard()
            self.PcMove()
            self.CheckBoard()

        elif p == "X":
            self.CheckBoard()
            if 0 <= x <= 200 and 400 <= y <= 600:
                self.cross[0] = "x"
            elif 200 <= x <= 400 and 400 <= y <= 600:
                self.cross[1] = "x"
            elif 400 <= x <= 600 and 400 <= y <= 600:
                self.cross[2] = "x"
            elif 0 <= x <= 200 and 200 <= y <= 400:
                self.cross[3] = "x"
            elif 200 <= x <= 400 and 200 <= y <= 400:
                self.cross[4] = "x"
            elif 400 <= x <= 600 and 200 <= y <= 400:
                self.cross[5] = "x"
            elif 0 <= x <= 200 and 0 <= y <= 200:
                self.cross[6] = "x"
            elif 200 <= x <= 400 and 0 <= y <= 200:
                self.cross[7] = "x"
            elif 400 <= x <= 600 and 0 <= y <= 200:
                self.cross[8] = "x"
            self.CheckBoard()
            self.PcMove()
            self.CheckBoard()

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
