class PaymentManager:
    def pay(self):
        self.create_payment_account()
        self.check_funds()
        self.create_tranaction()
        self.release_funds()

    def create_payment_account(self):
        pass

    def create_tranaction(self):
        pass


    def check_funds(self):
        pass

    def release_funds(self):
        pass


pm = PaymentManager()
print(pm.pay())