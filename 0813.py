import sys
from itertools import count
from random import randint

def checkfn(left, right, guess):
       if left < right and guess == 'h':
              return True
       if left == right and (guess == 'h' or guess == 'l'):
              return True
       if left > right and guess == 'l':
              return False


def create_title(title):
       separator = '*' * 14
       return '\n'.join([
              separator,
              f'* {title} *',
              separator
              ])


message = 'High or Low ?(h/l)'


print(create_title('High & Low'))

for i in count():
       left = randint(1,13)
       right = randint(1,13)       
       print('  [問題表示]')
       print('*****   *****')
       print('*   *   *   *')
       print('* {0} *   *   *'.format(left))
       print('*   *   *   *')
       print('*****   *****')
       guess = input(message)
       if checkfn(left, right, guess) == True and guess == 'h':
             print('→Highを選択しました。')
             print('  [結果発表]') 
             print('*****    *****')
             print('*   *    *   *')
             print('* {0} *    * {1} *'.format(left, right))
             print('*   *    *   *')
             print('*****    *****')
             print('You Win!')
       if checkfn(left, right, guess) == True and guess == 'l':
             print('→Lowを選択しました。')
             print('  [結果発表]') 
             print('*****    *****')
             print('*   *    *   *')
             print('* {0} *    * {1} *'.format(left, right))
             print('*   *    *   *')
             print('*****    *****')
             print('You Win!')
       if checkfn(left, right, guess) == False and guess == 'h':
              print('→Highを選択しました。')
              print('  [結果発表]') 
              print('*****    *****')
              print('*   *    *   *')
              print('* {0} *    * {1} *'.format(left, right))
              print('*   *    *   *')
              print('*****    *****')
              print('You Lose...')
              print('---ゲーム終了---')
              sys.exit()
       if checkfn(left, right, guess) == False and guess == 'l':
              print('→lowを選択しました。')
              print('  [結果発表]') 
              print('*****    *****')
              print('*   *    *   *')
              print('* {0} *    * {1} *'.format(left, right))
              print('*   *    *   *')
              print('*****    *****')
              print('You Lose...')
              print('---ゲーム終了---')
              sys.exit()
   

