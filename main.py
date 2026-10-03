print("=== CEK CUACA ===")

kota = input("Masukkan nama kota: ")
suhu = float(input("Masukkan suhu saat ini (°C): "))

print("\nKota:", kota)
print("Suhu:", suhu, "°C")

if suhu >= 30:
    print("Cuaca: Panas ☀️")
elif suhu >= 20:
    print("Cuaca: Sejuk 🌤️")
else:
    print("Cuaca: Dingin 🌧️")