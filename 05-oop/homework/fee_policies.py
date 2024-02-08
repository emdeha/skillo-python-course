from fee import Fee


class RegularFee(Fee):
    def withdrawal_fee(self):
        return 0.10

    def monthly_fee(self, overdraft):
        return 0.02 * overdraft * -1


class ExtremeFee(Fee):
    def withdrawal_fee(self):
        return 1.10

    def monthly_fee(self, overdraft):
        return 0.12 * overdraft * -1
