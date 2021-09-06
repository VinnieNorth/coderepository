from pyglet import app
from pyglet import image
from pyglet.window import Window
def redsquare():
    window = Window(500,500)
    @window.event
    def on_draw():
        window.clear()
        draw_square(snk_x, snk_y, cell_size)
    def draw_square(x, y, size, colour =(255,0,0, 0)):
        img = image.create(size,size, image.SolidColorImagePattern(colour))
        img.blit(x,y)
    cell_size = 20
    snk_x = window.width // cell_size // 2*cell_size
    snk_y = window.height // cell_size // 2*cell_size
    app.run()






redsquare()