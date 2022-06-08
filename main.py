# Игра в конфеты. Правила: В блюде имеется некоторое количество конфет, игроки по очереди берут по однойб по две или по три конфеты. Побеждает игрок, забравший последнюю конфету.

from random import randint

rest_of_candies = 20
counter = 1  # Будем использовать счетчик {counter} для определения игрока, чья очередь брать конфеты

def choicer(counter, rest_of_candies): # Функция определяет игрока, чья очередь брать конфеты и возвращает номер игрока и количество конфет, которые он взял
  global num_of_candies
  global player
  if counter%2:
    player = 'Игрок'
    num_of_candies = int(input(f'{player} введите количество конфет, которое вы хотите взять: '))
    if num_of_candies in range(1,4):
      if num_of_candies <= rest_of_candies:
        return counter, num_of_candies, player
      else: 
        print(f'Вы не можете взять больше {rest_of_candies} конфет')
        return choicer(counter, rest_of_candies)
  else:
    num_of_candies = randint(1,3)
    player = 'Искин'
    print(f'{player} берет {num_of_candies} конфеты')
  
def game(counter, rest_of_candies):
  while rest_of_candies > 0:
    choicer(counter, rest_of_candies)
    rest_of_candies -= num_of_candies
    print(f'Осталось {rest_of_candies} конфет')
    counter += 1
    return game(counter, rest_of_candies)
  else:
    exit(f'{player} выиграл!')

print(f'Сейчас в блюде {rest_of_candies} конфет')
game(counter, rest_of_candies)
  
    
    
    
    



