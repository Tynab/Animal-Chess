import math
import pygame
from pygame import Surface, Rect, draw, transform, image, font, mouse
from scripts.common import Color, ImagePath, Size, FontName, GameState, PlayerSide

import scripts.common as common

COVER_SCALED = transform.scale(image.load(ImagePath.COVER), Size.BOARD)
START_BTN_SCALED = transform.scale(image.load(ImagePath.START_BTN), Size.START_BTN)
START_BTN_RECT = Rect((Size.BOARD[0] - Size.START_BTN[0]) / 2, Size.BOARD[1] - Size.START_BTN[1] - 25, Size.START_BTN[0], Size.START_BTN[1])

FONT_TIT = font.SysFont(FontName.TIT, 45, bold=True)
FONT_BTN = font.SysFont(FontName.BTN, 23, bold=True)
FONT_RES = font.SysFont(FontName.TXT, 57, bold=True)

def draw_screen(screen, game_manager):
    screen.blit(COVER_SCALED, (0, 0))
    txt_tit = FONT_TIT.render(common.TIT, True, Color.WHITE)
    screen.blit(txt_tit, txt_tit.get_rect(center=(Size.BOARD[0] / 2, 25)))
    if game_manager.game_state == GameState.OVER:
        for i, line in enumerate(game_manager.game_result.split('\n')):
            txt_game_over = FONT_RES.render(line, True, Color.YELLOW)
            screen.blit(txt_game_over, txt_game_over.get_rect(center=(Size.BOARD[0] / 2, Size.BOARD[1] / 2 + 90 + i * (txt_game_over.get_height() + 5))))
    screen.blit(START_BTN_SCALED, START_BTN_RECT.topleft)
    txt_color = Color.WHITE
    if START_BTN_RECT.collidepoint(mouse.get_pos()):
        mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        txt_color = Color.YELLOW
    else:
        mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        txt_color = Color.WHITE
    txt_surf = FONT_BTN.render('New Game', True, txt_color)
    screen.blit(START_BTN_SCALED, START_BTN_RECT.topleft)
    screen.blit(txt_surf, txt_surf.get_rect(center=START_BTN_RECT.center))

def draw_game(screen, game_manager):
    cursor_hand = False
    for col in game_manager.board.cells:
        for cell in col:
            cell_rect = Rect(cell.position[0] * common.SPAN, cell.position[1] * common.SPAN, common.SPAN, common.SPAN)
            draw.rect(screen, Color.WHITE, [cell.position[0] * common.SPAN, cell.position[1] * common.SPAN, common.SPAN, common.SPAN], 0)
            if cell.image:
                screen.blit(cell.image, (cell.position[0] * common.SPAN, cell.position[1] * common.SPAN))
            draw.rect(screen, Color.GRAY, cell_rect, 1)
            if cell.piece:
                if cell_rect.collidepoint(mouse.get_pos()) and cell.piece.side == game_manager.current_player.side:
                    cursor_hand = True
                draw_star(screen, cell.piece.side == PlayerSide.DARK and Color.ORANGE or Color.CYAN, (cell.position[0] * common.SPAN + 50, cell.position[1] * common.SPAN + 50), 40, 20, 192, 20)
                screen.blit(cell.piece.image, (cell.position[0] * common.SPAN, cell.position[1] * common.SPAN))
    if game_manager.selected_piece:
        for cell in game_manager.selected_piece.available_moves(game_manager.board):
            cell_rect = Rect(cell.position[0] * common.SPAN, cell.position[1] * common.SPAN, common.SPAN, common.SPAN)
            if cell_rect.collidepoint(mouse.get_pos()):
                cursor_hand = True
            highlight_surface = Surface((common.SPAN, common.SPAN), pygame.SRCALPHA)
            if cell.piece:
                draw.circle(highlight_surface, (*Color.RED, 192), (common.SPAN // 2, common.SPAN // 2), common.SPAN // 4)
            elif cell.is_river() or abs(cell.position[0] - game_manager.selected_piece.position[0]) > 1 or abs(cell.position[1] - game_manager.selected_piece.position[1]) > 1:
                draw.circle(highlight_surface, (*Color.GREEN, 192), (common.SPAN // 2, common.SPAN // 2), common.SPAN // 4)
            else:
                draw.circle(highlight_surface, (*Color.YELLOW, 192), (common.SPAN // 2, common.SPAN // 2), common.SPAN // 4)
            screen.blit(highlight_surface, (cell.position[0] * common.SPAN, cell.position[1] * common.SPAN))
    if cursor_hand:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

def draw_star(surface, color, center, outer_radius, inner_radius, opacity=255, points=5):
    star_surface = Surface((2*outer_radius, 2*outer_radius), pygame.SRCALPHA)
    star_surface.fill((0, 0, 0, 0))
    outer_points = []
    inner_points = []
    angle_between_points = (2 * math.pi) / points
    start_angle = math.pi / 2
    star_center = (outer_radius, outer_radius)
    for i in range(points):
        outer_angle = start_angle - (angle_between_points * i)
        inner_angle = outer_angle - (angle_between_points / 2)
        outer_points.append((star_center[0] + math.cos(outer_angle) * outer_radius, star_center[1] - math.sin(outer_angle) * outer_radius))
        inner_points.append((star_center[0] + math.cos(inner_angle) * inner_radius, star_center[1] - math.sin(inner_angle) * inner_radius))
    star_points = []
    for i in range(points):
        star_points.append(outer_points[i])
        star_points.append(inner_points[i])
    draw.polygon(star_surface, color + (opacity,), star_points)
    surface.blit(star_surface, (center[0] - outer_radius, center[1] - outer_radius))
