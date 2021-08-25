#!/usr/bin/env python

import pygame as pg
import time     ## to control speed
import random
import sys

score = 0

def get_score():
	'''
	Retrieve Score function
	'''
	font = pg.font.SysFont('sans serif', 20)
	score_display = font.render(f'Score: {score}!', True, green)

	window.blit(score_display, score_display.get_rect())

def play_again():
	for event in pg.event.get():
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_ESCAPE:
				pg.quit()
				sys.exit()
			else:
				fruit_cords = [random.randrange(1, 600//10) *10, 
					random.randrange(1, 600//10) *10]
				fruit_spawn = True

				snake_pos = [300,300]
				snake_body = [[200,200]]

				start_game = True


def game_over():
	'''
	Display game over and what to do after that
	'''
	start_game = False
	font = pg.font.SysFont('sans serif', 40)

	score_display = font.render(f'Game Over! You Scored {score}!', True, red)
	prgramming_credits = font.render('This Game Was Programmed by BYY2100!', True, green)
	# again = font.render('Press any Key to play again', True, (255,255,255))
	# esc = font.render('Press Escape button to close', True, (255,255,255))

	score_rect = score_display.get_rect()
	prog_rect = prgramming_credits.get_rect()
	# again_rect = again.get_rect()
	# esc_rect = esc.get_rect()

	score_rect.midtop = (300,200)
	prog_rect.midtop = (300, 250)
	# again_rect.midtop = (300, 300)
	# esc_rect.midtop = (300,100)

	# window.blit(esc, esc_rect)
	window.blit(score_display, score_rect)
	window.blit(prgramming_credits, prog_rect)
	# window.blit(again, again_rect)

	pg.display.flip()

	time.sleep(3)
	pg.quit()
	exit()



base_speed = 15

## Colors for the bodies
red = pg.Color(255,0,0)
green = pg.Color(0,255,0)

## Snake default position
snake_pos = [300,300]

## Snake Body
snake_body = [[200,200]]

## Directions
direction = ''
change_dir = direction

pg.init()

pg.display.set_caption('Snaky Snake')
window = pg.display.set_mode((600,600))

fps = pg.time.Clock()

fruit_cords = [random.randrange(1, 600//10) *10, 
				random.randrange(1, 600//10) *10]
fruit_spawn = True

start_game = True



## Starting the game

while start_game:
	for event in pg.event.get():
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_UP:
				change_dir = 'UP'
			elif event.key == pg.K_DOWN:
				change_dir = 'DOWN'
			elif event.key == pg.K_LEFT:
				change_dir = 'LEFT'
			elif event.key == pg.K_RIGHT:
				change_dir = 'RIGHT'

	## Enhance Movement
	if change_dir == 'UP' and direction != 'DOWN':
		direction = 'UP'
	elif change_dir == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	elif change_dir == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'
	elif change_dir == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'

	## Control Directions
	if direction == 'UP':
		snake_pos[1] -= 10
	elif direction == 'DOWN':
		snake_pos[1] += 10
	elif direction  == 'RIGHT':
		snake_pos[0] +=10
	elif direction == 'LEFT':
		snake_pos[0] -=10

	## Feed snake
	snake_body.insert(0, list(snake_pos))

	if snake_pos[0] == fruit_cords[0] and snake_pos[1] == fruit_cords[1]:
		score += 10
		fruit_spawn = False  ## Remove the fruit
	else:
		snake_body.pop()

	if not fruit_spawn:    ## Add a new fruit
		fruit_cords = [random.randrange(1, 600//10) *10, 
				random.randrange(1, 600//10) *10]
	fruit_spawn = True

	window.fill((0,0,0))

	## Draw snake and fruits
	for position in snake_body:
		pg.draw.rect(window, green, pg.Rect(position[0], position[1], 10, 10))
	pg.draw.rect(window, red, pg.Rect(fruit_cords[0], fruit_cords[1],10,10))

	## Check if game over
	if snake_pos[0] < 0 or snake_pos[0] > 590:
		game_over()
       
	if snake_pos[1] < 0 or snake_pos[1] > 590:
		game_over()
        
	for block in snake_body[1:]:
		if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
			game_over()

	get_score()
	pg.display.update()
	fps.tick(base_speed)