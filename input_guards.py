def get_int_input(msg):
    while True:
        try:
            val=input(msg).strip()
            return int(val)
        except ValueError:
            print("please enter a whole number")
def get_float_input(msg):
    while True:
        try:
            val=input(msg).strip()
            num=float(val)
            if num>=0.0 and num<=100.0:
                return num
            print("score has to be between 0 and 100")
        except ValueError:
            print("invalid decimal number try again")
