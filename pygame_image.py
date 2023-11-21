import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))#練習1
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")#練習1
    
    kk_img = pg.image.load("ex01/fig/3.png")#練習2
    kk_img = pg.transform.flip(kk_img, True, False)##練習2左右反転
    kk_imgs = [kk_img,pg.transform.rotozoom(kk_img, 5, 1.0)]##練習3、10°回転


    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        x = tmr%1600 
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img, [1600-x, 0])
        screen.blit(kk_imgs[tmr%1.5],[300, 200])
        
        pg.display.update()

        tmr += 1       
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()