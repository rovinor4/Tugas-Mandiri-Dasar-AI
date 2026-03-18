import numpy as np
import random

# Inisialisasi default data (3 pelanggan)
# random.randint(0, 9999) menghasilkan bilangan bulat acak dari 0 hingga 9999 secara inklusif (0 dan 9999 bisa terpilih).
# :04d adalah format string untuk memastikan angka selalu memiliki 4 digit dengan menambahkan angka 0 di depan jika perlu (misal: 7 menjadi 0007).
customer_info = [
    {"name": "Andi", "code": f"UND-{random.randint(0, 9999):04d}"},
    {"name": "Budi", "code": f"UND-{random.randint(0, 9999):04d}"},
    {"name": "Citra", "code": f"UND-{random.randint(0, 9999):04d}"}
]

# Array 2D NumPy untuk data numerik [TotalBelanja, JumlahTransaksi]
transaction_data = np.array([
    [250000.0, 4.0],
    [600000.0, 2.0],
    [800000.0, 5.0]
])


def generate_raffle_code():
    # Fungsi random.randint(a, b) membutuhkan argumen batas bawah (a) dan batas atas (b).
    # Disini kita minta program memilih satu angka acak di antara 0 sampai 9999.
    return f"UND-{random.randint(0, 9999):04d}"


def add_customer_data():
    global customer_info, transaction_data
    try:
        num_customers = int(input("Masukkan jumlah pelanggan yang ingin diinput: "))
        for i in range(num_customers):
            name = input(f"\nNama Pelanggan ke-{i + 1}: ")
            total_spent = float(input(f"Total Belanja {name}: Rp "))
            num_trans = float(input(f"Jumlah Transaksi {name}: "))

            raffle_code = generate_raffle_code()
            customer_info.append({"name": name, "code": raffle_code})

            new_data = np.array([[total_spent, num_trans]])
            transaction_data = np.vstack([transaction_data, new_data])

            print(f"Data ditambahkan dengan kode undian: {raffle_code}")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk total belanja dan jumlah transaksi.")


def display_all_customers():
    if len(transaction_data) == 0:
        print("Data pelanggan masih kosong.")
        return

    print("\n=== Seluruh Data Pelanggan ===")
    for i in range(len(customer_info)):
        name = customer_info[i]['name']
        code = customer_info[i]['code']
        total_spent = transaction_data[i, 0]
        num_trans = int(transaction_data[i, 1])
        print(f"[{code}] {name} - Total Belanja: Rp{total_spent:,.0f} | Transaksi: {num_trans}x")


def analyze_and_get_slots():
    if len(transaction_data) == 0:
        return None, []

    avg_spent = np.mean(transaction_data[:, 0])
    eligible_participants = []

    for i in range(len(customer_info)):
        total_spent = transaction_data[i, 0]
        num_trans = int(transaction_data[i, 1])

        if num_trans >= 3:
            slots = 0

            if total_spent < 300000:
                slots = 1
            elif 300000 <= total_spent <= 700000:
                slots = 2
            elif total_spent > 700000:
                slots = 3

            is_priority = total_spent > avg_spent
            if is_priority:
                slots += 2

            eligible_participants.append({
                "index": i,
                "slots": slots,
                "is_priority": is_priority
            })

    return avg_spent, eligible_participants


def show_raffle_participants():
    avg_spent, participants = analyze_and_get_slots()
    if avg_spent is None:
        print("Data pelanggan masih kosong.")
        return

    print(f"\n--- Rata-rata Total Belanja: Rp{avg_spent:,.0f} ---")
    print("\n=== Daftar Peserta Undian (Transaksi >= 3) ===")

    if not participants:
        print("Tidak ada pelanggan yang memenuhi syarat undian.")
        return

    for p in participants:
        idx = p['index']
        name = customer_info[idx]['name']
        code = customer_info[idx]['code']
        status = "Prioritas" if p['is_priority'] else "Reguler"
        print(f"[{code}] {name} - Status: {status} | Mendapat: {p['slots']} Slot")


def run_raffle():
    avg_spent, participants = analyze_and_get_slots()
    if not participants or len(participants) < 2:
        print("Minimal harus ada 2 peserta yang memenuhi syarat untuk melakukan undian.")
        return

    raffle_pool = []
    for p in participants:
        raffle_pool.extend([p['index']] * p['slots'])

    # Fungsi random.choice(sequence) digunakan untuk memilih secara acak SATU elemen dari sebuah list/array (sequence).
    # Disini, program akan mengambil satu elemen index secara acak dari dalam list 'raffle_pool'.
    # Semakin banyak index yang sama di dalam list (karena slot undian banyak), semakin besar peluang elemen tersebut terpilih.
    winner1_idx = random.choice(raffle_pool)

    raffle_pool = [idx for idx in raffle_pool if idx != winner1_idx]

    if len(raffle_pool) == 0:
        print("Tidak dapat menentukan pemenang ke-2 karena kekurangan peserta unik.")
        return

    # Pemanggilan random.choice yang kedua untuk mencari pemenang kedua dari sisa 'raffle_pool' yang ada.
    winner2_idx = random.choice(raffle_pool)

    print("\n" + "=" * 30)
    print("SELAMAT KEPADA PEMENANG UNDIAN")
    print("=" * 30)
    print(f"Pemenang 1: {customer_info[winner1_idx]['name']} ({customer_info[winner1_idx]['code']})")
    print(f"Pemenang 2: {customer_info[winner2_idx]['name']} ({customer_info[winner2_idx]['code']})")


def search_by_code():
    search_code = input("Masukkan kode undian (format: UND-XXXX): ").upper()
    found = False

    for i in range(len(customer_info)):
        if customer_info[i]['code'] == search_code:
            name = customer_info[i]['name']
            total_spent = transaction_data[i, 0]
            num_trans = int(transaction_data[i, 1])
            print(f"\nData Ditemukan:")
            print(f"Nama: {name}")
            print(f"Total Belanja: Rp{total_spent:,.0f}")
            print(f"Jumlah Transaksi: {num_trans}x")
            found = True
            break

    if not found:
        print("\nKode undian tidak ditemukan.")


def main():
    while True:
        print("\n=== Menu Sistem Promosi & Undian ===")
        print("1. Tambah Data Pelanggan")
        print("2. Tampilkan Seluruh Data")
        print("3. Cek Daftar Peserta Undian & Slot")
        print("4. Tarik Undian (Cari 2 Pemenang)")
        print("5. Cari Pelanggan via Kode Undian")
        print("6. Keluar")

        choice = input("Pilih menu (1-6): ")

        match choice:
            case '1':
                add_customer_data()
            case '2':
                display_all_customers()
            case '3':
                show_raffle_participants()
            case '4':
                run_raffle()
            case '5':
                search_by_code()
            case '6':
                print("Program dihentikan.")
                break
            case _:
                print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()