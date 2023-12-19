from random import random

def move_cars(car_positions):
   return list(map(lambda x: x + 1 if random() > 0.3 else x,
               car_positions))

def run_step_of_race(state):
    return {'time': state['time'] - 1,
            'car_positions': move_cars(state['car_positions'])}

def draw_car(car_position):
    print('-' * car_position)

def draw(state):
    print(state['time'])
    for car_position in state['car_positions']:
        draw_car(car_position)

def race(state):
    draw(state)
    if state['time']:
        race(run_step_of_race(state))   
    


state = {'time':5, 'car_positions':[1,1,1]}

race(state)


