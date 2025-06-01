import pygame

class ShopItem:
    def __init__(self, price: int, image_path: str, prefab: object):
        self.price = price
        self.prefab = prefab
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (48, 48))
        self.selected = False 

    def draw(self, screen, pos):
        slot_width, slot_height = 60, 80
        slot_x, slot_y = pos

        if self.selected:
            border_color = (0, 255, 0)
        else:
            border_color = (200, 200, 200)

        # draw slot
        slot_rect = pygame.Rect(slot_x, slot_y, slot_width, slot_height)
        pygame.draw.rect(screen, (40, 40, 40), slot_rect)
        pygame.draw.rect(screen, border_color, slot_rect, 2)

        # draw image
        image_rect = self.image.get_rect(midtop=(slot_x + slot_width // 2, slot_y + 5))
        screen.blit(self.image, image_rect)

        # Price
        font = pygame.font.SysFont("Arial-Bold", 14)
        price_text = font.render(f"${self.price}", True, (255, 255, 255))
        price_rect = price_text.get_rect(midtop=(slot_x + slot_width // 2, image_rect.bottom + 5))
        screen.blit(price_text, price_rect)

        # for colision detection
        return slot_rect
