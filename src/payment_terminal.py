class PaymentTerminal:

    def __init__(self):
        self.money = 1000 # amount of cash
        self.affordable_meals = 0 # number of sold affordable meals
        self.hearty_meals = 0 # number of sold hearty meals

    def eat_affordably(self,payment):
        # an affordable meal costs 2.50 pounds
        # increase the amount of cash by the price of an affordable mean and return the change
        # if the payment parameter is not large enough, no meal is sold and the method should return the whole payment
        if type(payment) is int or type(payment) is float: 
          if(payment>=2.5):
            self.money+=2.5
            change = payment - 2.5
            self.affordable_meals +=1
          else:
            return payment
          return change

        if type(payment) is PaymentCard:
          if payment.take_money(2.5):
            self.affordable_meals +=1
            return True
          else:
            return False


    def eat_heartily(self,payment):
        # a hearty meal costs 4.30 pounds
        # increase the amount of cash by the price of a hearty mean and return the change
        # if the payment parameter is not large enough, no meal is sold and the method should return the whole payment
        if type(payment) is int or type(payment) is float:
          if(payment>=4.3):
            self.money+=4.3
            change = payment - 4.3
            self.hearty_meals +=1
          else:
            return payment
          return change

        if type(payment) is PaymentCard:
          if payment.take_money(4.3):
            self.hearty_meals+=1
            return True
          else:
            return False

    def add_money_to_card(self, card, sum):
      self.money += sum
      card.add_money(sum)


    def __str__(self):
        return "money: " + str(self.money) + ", number of sold afforable meals: " + str(self.affordable_meals) + ", number of sold hearty meals: " + str(self.hearty_meals)

if __name__=='main':
  from payment_card import PaymentCard
else:
  from src.payment_card import PaymentCard