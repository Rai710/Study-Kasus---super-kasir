import os
os.system('cls')


user = [    
    {"username" : "ardi123", "password": "12345678", "nama" : "Ardi"},
    {"username" : "arda123", "password": "12345678", "nama" : "Arda"},
    ]
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    attemp = 0
    max_A = 3

    while attemp < max_A:
        clear()
        print("========= LOGIN =========\n")
        username = str(input("Username\t: "))
        password = str(input("Password\t: "))
        
        for akun in user:
            if akun['username'] == username and akun['password'] == password:
                print(f"\nSelamat datang {akun['nama'].upper()}")
                return
        print("\nlogin gagal username atau password salah\n")
        input("Tekan Enter untuk melanjutkan...")
        attemp += 1
    
    print("\nTerlalu banyak percobaan login gagal...\nExit")
    exit()

def regis():
    clear()
    print("======== REGISTRASION =========")
    nama = str(input("Your name\t\t: "))
    
    check = True

    while True:
        username = str(input("username\t\t: "))

        for akun in user :
            if akun["username"] == username :
                print("\nUsername sudah digunakan. Coba lagi.")
                input("Tekan Enter untuk kembali...\n")
                break

        else :
            passW = str(input(f'Input your Password\t: '))
            # tambahin ke list user
            user.append({
                "username": username,
                "password": passW,
                "nama": nama
            })
            print(f"\nRegistrasi berhasil! \nHalo, {nama.upper()}!")
            input("Tekan Enter untuk login...\n")
            login()  # langsung login setelah daftar
            break

print("Hallooo!! selamat datang DI" \
      "\n\tSUPERMARKET   ")
print("\nSilahkan login terlebih dahulu" \
      "\n0.Login \n" \
      "1.Registrasi.")
menu = int(input("Masukan pilihan anda : "))

while menu > 1 :
    menu = int(input("Masukan angka 0 - 1 saja : "))
    
# MENU

clear()


if menu == 0:
    login()

elif menu == 1:
    regis()
