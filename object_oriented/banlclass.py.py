import random
class bank:
    def experience(self):
        print(' check card is valid or not  ')
        i = 0
        while i < 2:
            card = input(" Shomare Card ra vared konid: ")
            i+=1
            if i == 2:
                if len(str(card)) != 16:
                    print('not match')
                else:
                    print('matched')
               # print('try latter')
                break
            else:
                
                if len(str(card)) != 16:
                    print('its not valid ')
                else :
                    print('valid account')
                
                    break
class creat_acc:
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

    def new_acc(self):
        acc_bank = []
        name = input("""enter the owner card's name:""")
        acc_bank.append(name)
        num_card = creat_acc.generate_random_num()
        acc_bank.append(num_card)
        print('this is your information: {} '.format(acc_bank))
        
class nothing:
    def not_account(self):
        print('you need an account')
        creat_acc.new_acc(self)
        


class check_acc:
    def creat(self):
        x = input('do you have account or not ? {yes;no}:')
        y = 'yes'
        z = 'no'
        if x == y :
            print('you have account')
            bank.experience(self)
        elif x == z :
            nothing.not_account(self)
        else:
            print('put just yes or no ')
class buy:
    def buy_thing(self):
        last_mojodi = '135789745000'
        cost = input('enter price that you want to pay for thing$:')
        if last_mojodi > cost:
            print('need more money ')
        else:
            baghi = int(last_mojodi) - int(cost)
            print(baghi,'$ mande hesab shoma')


you = buy()
you.buy_thing()
