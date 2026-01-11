# -------------------------------
# Onluk -> Ikilik Donusum
# -------------------------------
def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary = ""
    while n > 0:
        kalan = n % 2
        binary = str(kalan) + binary
        n = n // 2

    return binary


# -------------------------------
# Onluk -> Onaltilik Donusum
# -------------------------------
def decimal_to_hexadecimal(n):
    if n == 0:
        return "0"

    hex_chars = "0123456789ABCDEF"
    hex_number = ""

    while n > 0:
        kalan = n % 16
        hex_number = hex_chars[kalan] + hex_number
        n = n // 16

    return hex_number


# -------------------------------
# 8-bit Bellek Gosterimi
# -------------------------------
def show_8bit_memory(binary):
    binary = binary.zfill(8)

    print("\n8-bit Bellek Gosterimi:")
    for bit in binary:
        print("[", bit, "]", end=" ")
    print()


# -------------------------------
# ANA PROGRAM
# -------------------------------

sayi = int(input("Onluk tabanda bir sayi giriniz: "))

print("\nDonusturme seciniz:")
print("1 - Ikilik (Binary)")
print("2 - Onaltilik (Hexadecimal)")

secim = int(input("Seciminiz: "))

if secim == 1:
    binary = decimal_to_binary(sayi)
    print("\nIkilik Gosterim:", binary)
    show_8bit_memory(binary)

elif secim == 2:
    hex_value = decimal_to_hexadecimal(sayi)
    print("\nOnaltilik Gosterim:", hex_value)

    binary = decimal_to_binary(sayi)
    show_8bit_memory(binary)

else:
    print("Hatali secim yaptiniz!")
