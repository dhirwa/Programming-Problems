class Discount:
    @staticmethod
    def calc_discount(total,percent):
        if percent > 100 or percent < 0 :
            return "Sorry"
        else:
            the_discount=total *(percent* .01)
            return round(the_discount, 2)
