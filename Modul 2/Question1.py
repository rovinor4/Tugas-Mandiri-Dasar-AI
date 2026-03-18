import numpy as np

# 1. Inisialisasi default data (3 mahasiswa)
student_names = ["Budi", "Siti", "Andi"]
# Array 2D NumPy: Setiap baris merepresentasikan 1 mahasiswa,
# Kolom merepresentasikan komponen nilai: [Tugas, UTS, UAS]
student_grades = np.array([
    [80.0, 85.0, 90.0],
    [75.0, 70.0, 80.0],
    [90.0, 95.0, 85.0]
])


def calculate_final_grades():
    # Menggunakan "Vectorization" dari NumPy untuk menghitung nilai akhir semua mahasiswa sekaligus tanpa looping.
    # [:, 0] artinya ambil semua baris pada kolom indeks 0 (Tugas), dst.
    if len(student_grades) == 0:
        return np.array([])
    return (student_grades[:, 0] * 0.3) + (student_grades[:, 1] * 0.3) + (student_grades[:, 2] * 0.4)


def input_student_data():
    global student_names, student_grades
    try:
        num_students = int(input("Masukkan jumlah mahasiswa: "))
        for i in range(num_students):
            name = input(f"\nMasukkan nama mahasiswa ke-{i + 1}: ")
            task_grade = float(input(f"Nilai Tugas {name}: "))
            mid_grade = float(input(f"Nilai UTS {name}: "))
            final_grade = float(input(f"Nilai UAS {name}: "))

            student_names.append(name)

            # Membuat array 2D baru untuk 1 mahasiswa
            new_grades = np.array([[task_grade, mid_grade, final_grade]])
            # np.vstack (vertical stack) menggabungkan baris baru tersebut ke bagian bawah array utama
            student_grades = np.vstack([student_grades, new_grades])

        print("Data berhasil ditambahkan.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")


def display_grades_array():
    if len(student_grades) == 0:
        print("Data mahasiswa masih kosong.")
    else:
        print("\nArray Nilai Mahasiswa (Kolom: Tugas, UTS, UAS):")
        print(student_grades)


def display_final_grades():
    final_scores = calculate_final_grades()
    if len(final_scores) == 0:
        print("Data mahasiswa masih kosong.")
        return

    print("\nNilai Akhir Mahasiswa:")
    for i in range(len(student_names)):
        print(f"{student_names[i]}: {final_scores[i]:.2f}")


def analyze_class_grades():
    final_scores = calculate_final_grades()
    if len(final_scores) == 0:
        print("Data mahasiswa masih kosong.")
        return

    # np.mean dan np.median langsung memproses seluruh elemen di dalam array final_scores
    avg_class = np.mean(final_scores)
    median_class = np.median(final_scores)

    print(f"\nRata-rata nilai akhir kelas: {avg_class:.2f}")
    print(f"Median nilai akhir kelas: {median_class:.2f}")

    print("\nMahasiswa dengan nilai UAS lebih besar dari median nilai akhir kelas:")
    for i in range(len(student_names)):
        # Mengecek elemen pada baris ke-i dan kolom ke-2 (Nilai UAS)
        if student_grades[i, 2] > median_class:
            print(f"- {student_names[i]} (UAS: {student_grades[i, 2]})")


def display_top_3_students():
    final_scores = calculate_final_grades()
    if len(final_scores) == 0:
        print("Data mahasiswa masih kosong.")
        return

    # np.argsort mengembalikan *indeks* dari nilai array yang sudah diurutkan dari kecil ke besar.
    # [::-1] dipakai untuk membalik urutannya menjadi besar ke kecil (descending).
    sorted_indices = np.argsort(final_scores)[::-1]

    print("\n3 Mahasiswa dengan Nilai Tertinggi:")
    # Memastikan tidak error kalau jumlah mahasiswa kurang dari 3
    for i in range(min(3, len(sorted_indices))):
        idx = sorted_indices[i]
        print(f"{i + 1}. {student_names[idx]} - {final_scores[idx]:.2f}")


def search_student_data():
    search_name = input("Masukkan nama mahasiswa yang dicari: ")
    if search_name in student_names:
        idx = student_names.index(search_name)
        # Mengakses nilai spesifik pakai koordinat [baris, kolom]
        print(
            f"\nData {search_name} -> Tugas: {student_grades[idx, 0]}, UTS: {student_grades[idx, 1]}, UAS: {student_grades[idx, 2]}")
    else:
        print("Mahasiswa tidak ditemukan.")


def update_student_grades():
    global student_grades
    search_name = input("Masukkan nama mahasiswa yang nilainya ingin diupdate: ")
    if search_name in student_names:
        idx = student_names.index(search_name)
        try:
            # Langsung me-replace (menimpa) data di array berdasarkan baris index mahasiswanya
            student_grades[idx, 0] = float(input("Masukkan nilai Tugas baru: "))
            student_grades[idx, 1] = float(input("Masukkan nilai UTS baru: "))
            student_grades[idx, 2] = float(input("Masukkan nilai UAS baru: "))
            print("Data nilai berhasil diperbarui.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
    else:
        print("Mahasiswa tidak ditemukan.")


def delete_student():
    global student_names, student_grades
    search_name = input("Masukkan nama mahasiswa yang ingin dihapus: ")
    if search_name in student_names:
        idx = student_names.index(search_name)
        student_names.pop(idx)

        # np.delete menghapus data dari array.
        # 'idx' adalah target yang dihapus, 'axis=0' berarti targetnya adalah baris secara utuh.
        student_grades = np.delete(student_grades, idx, axis=0)
        print(f"Data {search_name} berhasil dihapus.")
    else:
        print("Mahasiswa tidak ditemukan.")


def main():
    while True:
        print("\n=== Menu Manajemen Nilai ===")
        print("1. Input Data Mahasiswa")
        print("2. Tampilkan Array Nilai")
        print("3. Tampilkan Nilai Akhir Mahasiswa")
        print("4. Analisis Nilai Kelas")
        print("5. Tampilkan 3 Nilai Tertinggi")
        print("6. Cari Data Mahasiswa")
        print("7. Update Nilai Mahasiswa")
        print("8. Hapus Mahasiswa")
        print("9. Keluar")

        choice = input("Pilih menu (1-9): ")

        match choice:
            case '1':
                input_student_data()
            case '2':
                display_grades_array()
            case '3':
                display_final_grades()
            case '4':
                analyze_class_grades()
            case '5':
                display_top_3_students()
            case '6':
                search_student_data()
            case '7':
                update_student_grades()
            case '8':
                delete_student()
            case '9':
                print("Program selesai dijalankan.")
                break
            case _:
                print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()