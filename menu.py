import pygame
import os
upgrade_menu_IMAGE = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
upgrade_IMAGE=pygame.image.load(os.path.join("images", "upgrade.png"))
sell_IMAGE=pygame.image.load(os.path.join("images", "sell.png"))
    
class UpgradeMenu:
    def __init__(self, x, y):
        self.__buttons = []  # (Q2) Add buttons here
        self.upgrade_menu_IMAGE = pygame.transform.scale(upgrade_menu_IMAGE, (200, 200))
        self.upgrade_IMAGE = pygame.transform.scale(upgrade_IMAGE, (80, 50))
        self.sell_IMAGE = pygame.transform.scale(sell_IMAGE, (50, 50))  
        self.rect = self.upgrade_menu_IMAGE.get_rect()
        self.rect.center=(x,y)   # center of the tower
        pass

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu 
        x,y=self.rect.center
        win.blit(self.upgrade_menu_IMAGE,(x-100,y-100))        
        # draw button
        # (Q2) Draw buttons here
        win.blit(self.upgrade_IMAGE, (x-40,y+50))
        win.blit(self.sell_IMAGE,(x-30,y-100))       
        pass

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons           
        pass


class Button:
    def __init__(self, image, name, x, y):
        self.image = image
        self.name = name
        x,y=self.rect.center                            
        
    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        if rect.collidepoint(x, y):
            return True
        else:
            return False

        pass

    def response(self):
        """
        (Q2) Return the button name.
        retur
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name 
       #return upgrade sell
        
        pass






