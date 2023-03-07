from pygame import *
from player import Player
from debug import debug
from tile import Tile
from settings import *
from support import *
from random import choice
class Level:
    def __init__(self):
        
        self.display_surface = display.get_surface()

        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = sprite.Group()


        self.create_map()
    def create_map(self):
        layouts = {
            'boundary' : import_csv_layout('../csv_file/map_FloorBlocks.csv') ,
            'detail' : import_csv_layout('../csv_file/map_Details.csv'),
            'object' : import_csv_layout('../csv_file/map_Objects.csv')

        }
        graphics = {
            'details' : import_folder('../map/Details'),
            'objects' : import_folder('../map/Objects')
        }


        for style,layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                        if style == 'detail':
                            surf = graphics['details'][int(col)-1]
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'detail', surf)
                        if style == 'object':
                            surf = graphics['objects'][int(col)-1]
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)

                self.player = Player((2000, 1550), [self.visible_sprites], self.obstacle_sprites) 
            
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.status)


class YSortCameraGroup(sprite.Group):
    def __init__(self):

        super().__init__()
        self.display_surface = display.get_surface()    
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = math.Vector2() 

        self.floor_surface = image.load('../map/My Map.png').convert()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))


    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_pos)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)   
        