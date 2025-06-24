import numpy as np

def menu():
    print("\nKOMPUTASI NUMERIK")
    print("==== TUGAS UAS ====")

    print("\nPilihlah salah satu Persamaan di bawah!!!")
    print("1.) Persamaan Linear")
    print("2.) Persamaan Non-Linear")

# -------------------------------------------
# FUNGSI METODE PERSAMAAN LINEAR
# -------------------------------------------

def input_linear_system():
    n = int(input("Masukkan jumlah variabel: "))
    A = []
    B = []
    for i in range(n):
        row = list(map(float, input(f"Masukkan koefisien baris ke-{i+1} (pisahkan spasi): ").split()))
        A.append(row)
        b = float(input(f"Masukkan konstanta ke-{i+1}: "))
        B.append(b)
    return np.array(A), np.array(B)

def metode_gauss(A, B):
    try:
        X = np.linalg.solve(A, B)
        print("\nHasil solusi (Eliminasi Gauss):")
        for i, x in enumerate(X):
            print(f"x{i+1} = {x}")
    except np.linalg.LinAlgError:
        print("Matriks singular, tidak dapat diselesaikan.")

def metode_gauss_jordan(A, B):
    try:
        n = len(B)
        M = np.hstack([A.astype(float), B.reshape(-1, 1)])
        for i in range(n):
            M[i] = M[i] / M[i][i]
            for j in range(n):
                if i != j:
                    M[j] = M[j] - M[j][i] * M[i]
        print("\nHasil solusi (Gauss-Jordan):")
        for i in range(n):
            print(f"x{i+1} = {M[i][-1]}")
    except:
        print("Terjadi kesalahan dalam perhitungan.")

def metode_invers(A, B):
    try:
        A_inv = np.linalg.inv(A)
        X = A_inv.dot(B)
        print("\nHasil solusi (Invers Matriks):")
        for i, x in enumerate(X):
            print(f"x{i+1} = {x}")
    except np.linalg.LinAlgError:
        print("Matriks tidak memiliki invers (singular).")

def metode_gauss_seidel(A, B, iterasi=100, tol=1e-6):
    n = len(B)
    x = np.zeros(n)
    for k in range(iterasi):
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j]*x_new[j] for j in range(i))
            s2 = sum(A[i][j]*x[j] for j in range(i+1, n))
            x_new[i] = (B[i] - s1 - s2) / A[i][i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print(f"\nHasil solusi (Gauss-Seidel, iterasi ke-{k+1}):")
            for i, xi in enumerate(x_new):
                print(f"x{i+1} = {xi}")
            return
        x = x_new
    print("Iterasi maksimal tercapai, solusi mendekati:")
    for i, xi in enumerate(x):
        print(f"x{i+1} = {xi}")

def menu_linear():
    print("\nMetode Penyelesaian Persamaan Linear:")
    print("1. Eliminasi Gauss")
    print("2. Gauss-Jordan")
    print("3. Invers Matriks")
    print("4. Gauss-Seidel (iteratif)")
    
    metode = input("Pilih metode (1-4): ")
    A, B = input_linear_system()
    
    if metode == '1':
        metode_gauss(A, B)
    elif metode == '2':
        metode_gauss_jordan(A, B)
    elif metode == '3':
        metode_invers(A, B)
    elif metode == '4':
        metode_gauss_seidel(A, B)
    else:
        print("Pilihan tidak valid.")

# -------------------------------------------
# FUNGSI NON-LINEAR
# -------------------------------------------

def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

def g(x):
    return (x + 2)**(1/3)  # contoh transformasi untuk fixed point

def bisection(a, b, tol=1e-6, max_iter=100):
    print("\n--- Metode Bisection ---")
    if f(a) * f(b) > 0:
        print("Tidak ada akar di interval tersebut.")
        return
    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol or abs(b - a) < tol:
            print(f"Akar ditemukan: x = {c:.6f} setelah {i+1} iterasi")
            return
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print(f"Akar mendekati: x = {c:.6f} (maksimal iterasi tercapai)")

def newton_raphson(x0, tol=1e-6, max_iter=100):
    print("\n--- Metode Newton-Raphson ---")
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            print("Turunan nol, metode gagal.")
            return
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < tol:
            print(f"Akar ditemukan: x = {x1:.6f} setelah {i+1} iterasi")
            return
        x0 = x1
    print(f"Akar mendekati: x = {x1:.6f} (maksimal iterasi tercapai)")

def secant(x0, x1, tol=1e-6, max_iter=100):
    print("\n--- Metode Secant ---")
    for i in range(max_iter):
        if f(x1) - f(x0) == 0:
            print("Pembagi nol, metode gagal.")
            return
        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            print(f"Akar ditemukan: x = {x2:.6f} setelah {i+1} iterasi")
            return
        x0, x1 = x1, x2
    print(f"Akar mendekati: x = {x2:.6f} (maksimal iterasi tercapai)")

def fixed_point(x0, tol=1e-6, max_iter=100):
    print("\n--- Metode Fixed Point Iteration ---")
    for i in range(max_iter):
        x1 = g(x0)
        if abs(x1 - x0) < tol:
            print(f"Akar ditemukan: x = {x1:.6f} setelah {i+1} iterasi")
            return
        x0 = x1
    print(f"Akar mendekati: x = {x1:.6f} (maksimal iterasi tercapai)")

def menu_nonlinear():
    print("\nMetode Penyelesaian Persamaan Non-Linear:")
    print("1. Bisection")
    print("2. Newton-Raphson")
    print("3. Secant")
    print("4. Fixed Point Iteration")

    metode = input("Pilih metode (1-4): ")
    if metode == '1':
        a = float(input("Masukkan batas bawah a: "))
        b = float(input("Masukkan batas atas b: "))
        bisection(a, b)
    elif metode == '2':
        x0 = float(input("Masukkan tebakan awal x0: "))
        newton_raphson(x0)
    elif metode == '3':
        x0 = float(input("Masukkan tebakan awal x0: "))
        x1 = float(input("Masukkan tebakan awal x1: "))
        secant(x0, x1)
    elif metode == '4':
        x0 = float(input("Masukkan tebakan awal x0: "))
        fixed_point(x0)
    else:
        print("Pilihan tidak valid.")

# -------------------------------------------
# PROGRAM UTAMA
# -------------------------------------------

if __name__ == "__main__":
    while True:
        menu()
        pilihan = input("Pilih menu (1/2 atau q untuk keluar): ").strip()
        
        if pilihan == '1':
            menu_linear()
        elif pilihan == '2':
            print("\nGunakan fungsi f(x) = x^3 - x - 2")
            menu_nonlinear()
        elif pilihan.lower() == 'q':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")
