import time
hello = print('Сейчас вылезет змеяяя!!!')
body = '*'
time.sleep(1)
try:
  while True:
      time.sleep(0.1)
      print('{:>6}'.format(body))
      time.sleep(0.1)
      print('{:>5}'.format(body))
      time.sleep(0.1)
      print('{:>5}'.format(body))
      time.sleep(0.1)
      print('{:>6}'.format(body))
except KeyboardInterrupt:
      print('0_0')
      exit(0)
