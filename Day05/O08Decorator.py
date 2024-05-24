




def BankFlow(fnc):

    def helper(cash):
        print("Logging into the server......")
        fnc(cash)
        print("Logging out of the server......")
        print("-" * 60)

    return helper


@BankFlow               # deposit = BankFlow(deposit)
def deposit(amt):
    print(f"Succefully credited {amt} into account ending xxxx")

@BankFlow
def withdraw(amt):
    print(f"Debited {amt} from the account end xxxx")


deposit(50000)
withdraw(12500)
