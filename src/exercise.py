from payment_card import PaymentCard
from payment_terminal import PaymentTerminal
def main():
    exact_amount = PaymentTerminal()
    print(exact_amount)

    annes_card = PaymentCard(2)

    print("amount of money on the card is " + str(annes_card.balance) + " pounds")

    was_successful = exact_amount.eat_heartily(annes_card)
    print("there was enough money: " + str(was_successful))

    exact_amount.add_money_to_card(annes_card, 100)

    was_successful = exact_amount.eat_heartily(annes_card)
    print("there was enough money: " + str(was_successful))

    print("amount of money on the card is " + str(annes_card.balance) + " pounds")

    print(exact_amount)
if __name__ == '__main__':
  main()
  from payment_card import PaymentCard
  from payment_terminal import PaymentTerminal

else:
  from src.payment_card import PaymentCard
  from src.payment_terminal import PaymentTerminal



