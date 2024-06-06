from uniref import WinUniRef

def Main():
    unity3d_pcbs2 = WinUniRef("PCBS2.exe")
    klass = unity3d_pcbs2.find_class_in_image("Assembly-CSharp.dll", "CareerConstants")
    money_cash = klass.find_field("s_startingCash")
    print("Old Value: " + str(money_cash.value))
    money_cash.set_value(int(9999999))
    print("New Value: " + str(money_cash.value))

if __name__ == "__{}__".format("main"):
    Main()
