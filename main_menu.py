import pygame, sys
from battleship import main
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    # Estados iniciales de los checkboxes
    selected_option = None  # Ninguna opción seleccionada al inicio

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        # Título de la pantalla de opciones
        OPTIONS_TEXT = get_font(45).render("Selecciona tu método de entrada:", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 200))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # Posiciones y textos para las opciones
        mouse_checkbox_rect = pygame.Rect(400, 300, 30, 30)  # Checkbox para "Mouse"
        gamepad_checkbox_rect = pygame.Rect(400, 350, 30, 30)  # Checkbox para "Gamepad"

        # Dibujar los checkboxes
        pygame.draw.rect(SCREEN, "Black", mouse_checkbox_rect, 2)
        pygame.draw.rect(SCREEN, "Black", gamepad_checkbox_rect, 2)

        # Dibujar texto de las opciones
        mouse_text = get_font(35).render("Mouse", True, "Black")
        gamepad_text = get_font(35).render("Gamepad", True, "Black")
        SCREEN.blit(mouse_text, (450, 295))
        SCREEN.blit(gamepad_text, (450, 345))

        # Marcar el checkbox seleccionado
        if selected_option == "Mouse":
            pygame.draw.rect(SCREEN, "Green", mouse_checkbox_rect.inflate(-6, -6))
        elif selected_option == "Gamepad":
            pygame.draw.rect(SCREEN, "Green", gamepad_checkbox_rect.inflate(-6, -6))

        # Botón para regresar al menú principal
        OPTIONS_BACK = Button(
            image=None,
            pos=(640, 460),
            text_input="Regresar a inicio.",
            font=get_font(75),
            base_color="Black",
            hovering_color="Green"
        )
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Detectar selección de opciones
                if mouse_checkbox_rect.collidepoint(OPTIONS_MOUSE_POS):
                    selected_option = "Mouse"
                elif gamepad_checkbox_rect.collidepoint(OPTIONS_MOUSE_POS):
                    selected_option = "Gamepad"

                # Detectar clic en el botón "BACK"
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        # Actualizar la pantalla
        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("BATTLESHIP", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 70))
        MENU_TEXT1 = get_font(60).render("STELIOS", True, "#7aa3d5")
        MENU_RECT1 = MENU_TEXT1.get_rect(center=(640, 150))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="JUGAR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPCIONES", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="SALIR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(MENU_TEXT1, MENU_RECT1)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
