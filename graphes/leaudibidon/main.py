class leaudibidon(object):

    def __init__(self,capacity):
        self.capacity = capacity
        self.quantity = 0

    def fullfill_b5(b5,b3):
        b5.quantity = b5.capacity
        print("Fullfill b5")

    def fullfill_b3(b5,b3):
        b3.quantity = b3.capacity
        print("Fullfill b3")

    def void_b5(b5,b3):
        b5.quantity = 0
        print("void b5")


    def void_b3(b5,b3):
        b3.quantity = 0
        print("void b3")

    def transfer_b5_b3(b5,b3):
        transfer_amount = min(b5.quantity, b3.capacity - b3.quantity)
        b5.quantity, b3.quantity = b5.quantity - transfer_amount, b3.quantity + transfer_amount
    
    
    def transfer_b5_b3(b5,b3):
        transfer_amount = min(b3.quantity, b5.capacity - b5.quantity)
        b5.quantity, b3.quantity = b5.quantity + transfer_amount, b3.quantity - transfer_amount