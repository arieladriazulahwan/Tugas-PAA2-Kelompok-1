def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:  # Jika elemen sekarang lebih besar, tukar
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Jika tidak ada pertukaran, keluar dari loop lebih awal

# Dataset suhu ruangan (20 nilai berbeda)
suhu = [22.5, 25.1, 19.8, 21.3, 24.7, 26.9, 23.4, 20.2, 27.6, 18.9, 
        22.8, 25.6, 19.5, 28.3, 21.9, 23.1, 26.2, 24.0, 20.7, 27.1]

# Menampilkan data sebelum pengurutan
print("Suhu sebelum diurutkan:", suhu)

# Mengurutkan menggunakan Bubble Sort
bubble_sort(suhu)

# Menampilkan hasil setelah diurutkan
print("Suhu setelah diurutkan:", suhu)