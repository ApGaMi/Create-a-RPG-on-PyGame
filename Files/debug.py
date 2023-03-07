from pygame import *
init()
font = font.Font(None, 30)

def debug(info, y = 10, x = 10):
    display_surface = display.get_surface()
    debug_surf = font.render(str(info), True, (255, 255, 255))
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    draw.rect(display_surface, (0, 0, 0), debug_rect)
    display_surface.blit(debug_surf, debug_rect)