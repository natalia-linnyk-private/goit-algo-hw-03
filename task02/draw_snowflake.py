from koh_snowflake_helper import koch_snowflake
import turtle
import consts
import random

def draw_snowflake(depth: int):
    color = random.choice(consts.AVAILABLE_COLORS)
    
    # Setup screen
    screen = turtle.Screen()
    screen.setup(consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT)
    screen.title(consts.SCREEN_TITLE)
    screen.bgcolor(consts.BACKGROUND_COLOR)
    
    canvas = screen.getcanvas()
    root = canvas.winfo_toplevel()
    root.attributes('-topmost', True)
    root.lift()
    root.focus_force()  
    
    # Draw snowflake
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-150, 150)
    t.pendown()
    t.color(color)
    t.begin_fill()
    
    koch_snowflake(t, consts.SNOWFLAKE_SIZE, depth)
    
    t.end_fill()
    
    # Write info text
    t.penup()
    t.goto(0, -200)
    t.color(consts.FONT_COLOR)
    t.write(f"Level of resursion: {depth}\n"
            f"Count of segment: {3 * (4 ** depth)}", 
            align=consts.FONT_ALLIGN, font=(consts.FONT_FAMILY, consts.FONT_SIZE))
    
    screen.mainloop()