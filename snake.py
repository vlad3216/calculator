import random
import time
hello = print('Сейчас вылезет змеяяя!!!')
body = '*'
head = '0_0'
try:
  while True:
      time.sleep(0.3)
      body_pos = '{:>4}'.format(body) , '{:>5}'.format(body), '{:>6}'.format(body)
      head_pos = '{:>6}'.format(head) , '{:>5}'.format(head), '{:>5}'.format(head)
      print(random.choice(body_pos))
except KeyboardInterrupt:
      print(random.choice(head_pos))
      exit(0)
