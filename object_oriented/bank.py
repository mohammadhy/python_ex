##shopping 
##first customer want check the account have account on that bank or no 
import datetime
import re
import random


day = datetime.datetime.now()



acc_bank = []


def generate_random_num(secure=False):
  random.seed()

  credit_card_num = []

  for i in range(4):
    # Generate a 4-digit random number
    four_digit_rand_num = [random.randint(1,9) for i in range(4)]
    #print four_digit_rand_num
    number = four_digit_rand_num
    
    if secure:      
      # Generate a random upper case letter
      upper_case_letters = map(chr, range(65, 91))
      letter = random.choice(upper_case_letters)
      #print letter
            
      # Generate a random position
      position = random.randint(0,3)
      #print position
            
      # Replace position
      number = four_digit_rand_num[:position]
      number.append(letter)
      number = number + four_digit_rand_num[position+1:]
      #print number
    
    number_str = ''.join(str(e) for e in number)
    #print number_str
    credit_card_num.append(number_str)
          
  return credit_card_num

def new_acc():
    name = input('Enter Your Name :')
    acc_bank.append(name)
    num_cart = generate_random_num()
    acc_bank.append(num_cart)
    print('this is your new account;{}'.format(acc_bank))

    return new_acc


    #for key, value in dicto.items():
    #    print('Name : {}, number_cart: {}'. format(key, value))




last_mojodi = '1357754000'


print('today is {} and i have {} $money'.format(day, last_mojodi))

## if you enter invalid cart number the program stop working 
print(""" ATTENTION :
                        Enter 16 Digit For Cart Number: THANK YOU  """)


cart_number = int(input('enter your card bank :'))
if len(str(cart_number)) != 16:
    print('you need to creat account :')
    new_acc()
else: 
    print('Valid Cart_number')

    #raise Exception('sorry no valid cart number enterd')

new_mojodi = []
cost = (input('enter the prise of thing that you want to buy :$'))

if last_mojodi < cost:
    print('mojodi kafi nist ')
else:       
    baghi =[ int(last_mojodi) - int(cost) ]
    new_mojodi.append(baghi)
    print(new_mojodi,'$mande hesabe shoma' )



