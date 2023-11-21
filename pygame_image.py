import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))#練習1
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")#練習1
    kk_img = pg.image.load("ex01/fig/3.png")#練習2
    kk_img = pg.transform.flip(kk_img, True, False)##練習2左右反転
    


    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img,[300, 200])

        pg.display.update()

        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()