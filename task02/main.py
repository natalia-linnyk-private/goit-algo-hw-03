import consts
from draw_snowflake import draw_snowflake

def main():
    try:
        depth = input("Enter recursion level (0-7) or press enter to set it to 3 by default >>>> ")
        depth = int(depth)
        if depth < consts.MIN_RECURSION_LEVEL or depth > consts.MAX_RECURSION_LEVEL:
            print("Level of recursion can be set from 0 to 7. By default it's set as 3")
            depth = consts.DEFAULT_RECURSION_LEVEL
    except:
        print("Value of recursion level is incorrect. By default it's set as 3")
        depth = consts.DEFAULT_RECURSION_LEVEL
    draw_snowflake(depth)

if __name__ == "__main__":
    main()