bilangan = int(input("Masukan sebuah bilangan : "))


def check_ganjilgenap(bilangan):
    if(bilangan % 2 == 0):
        print(bilangan, "merupakan bilangan GENAP")
    else:
        print(bilangan, "merupakan bilangan GANJIL")


check_ganjilgenap(bilangan)
