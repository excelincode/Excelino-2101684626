#Version Alpha 0.1 Created by WR
#Version Beta 0.2 Updated by EF
import sys
class Laundromat():
    def __init__(self, wash):
        self.wash = wash

class ClothesType(Laundromat):
    def __init__(self):
        super(ClothesType, self).__init__(1 or "clothes")
        self.wash = "clothes"

class BedcoverType(Laundromat):
    def __init__(self):
        super(BedcoverType, self).__init__(2 or "bedcover")
        self.wash = "bedcover"

class WashingFee():
    def __init__(self, clothesF, bedcoverF):
        self.washF = {"clothesfee":clothesF,"bedcoverfee":bedcoverF}
        self.weightCFinal = 0
        self.weightBCFinal = 0
        self.revenueTemp = 0
        self.revenueTotal = 0

    def in_caculation(self, in_category, we):
        if isinstance(in_category, ClothesType):
            self.weightCFinal += we
            self.revenueTemp = (self.washF["clothesfee"] * we)
            self.revenueTotal += self.washF["clothesfee"]
            return self.revenueTemp
        elif isinstance(in_category, BedcoverType):
            self.weightBCFinal += we
            self.revenueTemp = (self.washF["bedcoverfee"] * we)
            self.revenueTotal += self.washF["bedcoverfee"]
            return self.revenueTemp

    def moneymoney(self):
        return self.revenueTotal

    def totalweight(self):
        return self.weightCFinal, self.weightBCFinal

def repeat():
    question = input("Is there anything else we can do for you?  <Yes or No>").lower()
    if question == "yes":
        input("Please, 'ENTER' to Continue!")
        a()
    elif question == "no":
        finalrevenue = washy1.moneymoney()
        finalweight = washy1.totalweight()
        print("----------------------------------------\n"
              "The report for Gottlieb Laundry\n"
              "Type(s)\t\t\tCount\n"
              "Clothes\t\t\t%d KG(s)\n"
              "Bedcover\t\t\t%d Piece(s)\n"
              "\nTotal of Revenue: IDR %d\n"
              "------------------------------------------\n"
              "Thank you for using Laundromat!"
              % (finalweight[0], finalweight[1], finalrevenue))
        input("Please, 'ENTER' to Exit!")
        sys.exit()
    elif question != "no" and question != "yes":
        print("Please, only type YES or NO as your input!")
        input("Please, 'ENTER' to Continue!")
        repeat()
washy1 = WashingFee(8000,12000) #8k == Clothes, 12k == Bedcover
print("Welcome to Gottlieb Laundromat! How can I help you today?")
def a():
    while True:
        print("===============================================================")
        inp = input("Available Services:\t\t\tPrice\n"
                          "(1) Clothes\t\t\tIDR %d\n"
                          "(2) Bedcover\t\t\tIDR %d\n"
                          "____________________________________________________\n"
                    "Please, input the name or the number: "
                    %(washy1.washF["clothesfee"],washy1.washF["bedcoverfee"])).lower()
        if inp == "1" or inp == "clothes":
            in_category = ClothesType()
            out_types = "Clothes"
        elif inp == "2" or inp == "bedcover":
            in_category = BedcoverType()
            out_types = "Bed Cover"
        else:
            input("Press, 'ENTER' to Continue!")
        print("How many KG(s) or Piece(s) are there?")
        weight = int(input("Answer: "))
        fee = washy1.in_caculation(in_category, weight)
        print("----------------------------------------")
        print("\t\t\tLaundry Receipt"
              "\nLaundry Type\t\t", out_types,
              "\nTotal Weight(Piece)\t\t", weight,
              "\nTotal fee\t\tIDR %d" % fee)
        print("----------------------------------------")
        repeat()
a()
