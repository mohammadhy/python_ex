#this is bank project just have little change in it and use class in it 
import random

class Bank():


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
      
  
    #def __init__(self):
        #self.card = None
        #self.account = None
        
    #def _makeacoount(self):
        #self.account = self.card 
        #return self.account

    def _experinece(self):
        print(' you have an account: ')
        i = 0
        while i < 2:
            card = input(" Shomare Card ra vared konid: ")
            i+=1
            if i == 2:
                print('try latter')
                break
            else:
                
                if len(str(card)) != 16:
                    print('its not valid ')
                else :
                    print('valid account')
                    break
class new_account():
    def new_acc():
        acc_bank = []
        name = input("""enter the owner card's name:""")
        acc_bank.append(name)
        num_card = Bank.generate_random_num()
        acc_bank.append(num_card)
        print('this is your information: {} '.format(acc_bank))
class creat_account():
    def creat(self):
        input('enter your name ')
        
you = Bank()
you._experinece()

            
            