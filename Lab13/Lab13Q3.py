from abc import ABC, abstractmethod

#Target interface
class PayPalPaymentGateway(ABC):
    @abstractmethod
    def process_paypal_payment(self, email: str, amount: float) -> bool:
        pass

#Adaptee
class LegacyPaymentGateway:
    def process_credit_card_payment(self, credit_card_number: str, expiration_date: str, cvv: str, amount: float) -> bool:
        print("Simulates processoing a credit card payment")
        return True
    
class PayPalPaymentAdapter(PayPalPaymentGateway):
    def __init__(self, obj: LegacyPaymentGateway) -> None:
        self.__obj = obj
        
    def process_paypal_payment(self, email_address: str, amount: float) -> bool:
        # Simulate converting PayPal payment to credit card payment
        credit_card_number = self.get_credit_card_number(email_address)
        expiration_date = self.get_expiration_date(email_address)
        cvv = self.get_cvv()
        return self.__obj.process_credit_card_payment(credit_card_number, expiration_date, cvv, amount)
    
    def get_credit_card_number(self, email_address: str) -> str:
        # Simulate retrieving credit card number based on email
        return "4111111111111111"
    
    def get_expiration_date(self, email_address: str) -> str:
        # Simulate retrieving expiration date based on email
        return "12/25"
    
    def get_cvv(self) -> str:
        # Simulate retrieving CVV
        return "123"
    
class PaymentGatewayFactory:
    @staticmethod
    def get_payment_gateway() -> PayPalPaymentGateway:
        #return LegacyPaymentGateway()  # Using factory to return legacy gateway
        return PayPalPaymentAdapter(LegacyPaymentGateway())  # Using adapter to return adapted gateway
    
def main():
    payment_gateway = PaymentGatewayFactory.get_payment_gateway()
    success = payment_gateway.process_paypal_payment("demo@gmail.com", 100.0)
    print("Payment successful:", success)

if __name__ == "__main__":
    main()