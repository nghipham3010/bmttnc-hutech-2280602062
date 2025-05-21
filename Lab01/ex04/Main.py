from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*************************MENU**************************")
    print("**  1. Them sinh vien.                               **")
    print("**  2. Cap nhat thong tin sinh vien boi ID.          **")
    print("**  3. Xoa sinh vien boi ID.                         **")
    print("**  4. Tim kiem sinh vien theo ten.                  **")
    print("**  5. Sap xep sinh vien theo diem trung binh.       **")
    print("**  6. Sap xep sinh vien theo ten.                   **")
    print("**  7. Hien thi danh sach sinh vien.                 **")
    print("**  0. Thoat                                         **")
    print("*******************************************************")

    try:
        key = int(input("Nhap tuy chon: "))
        if key == 1:
            print("\n1. Them sinh vien.")
            qlsv.nhapSinhVien()
            print("\nThem sinh vien thanh cong!")
        elif key == 2:
            print("\n2. Cap nhat thong tin sinh vien.")
            ID = int(input("Nhap ID: "))
            qlsv.updateSinhVien(ID)
        elif key == 3:
            print("\n3. Xoa sinh vien.")
            ID = int(input("Nhap ID: "))
            if qlsv.deleteById(ID):
                print(f"\nSinh vien co id = {ID} da bi xoa.")
            else:
                print(f"\nSinh vien co id = {ID} khong ton tai.")
        elif key == 4:
            print("\n4. Tim kiem sinh vien theo ten.")
            name = input("Nhap ten de tim kiem: ")
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        elif key == 5:
            print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        elif key == 6:
            print("\n6. Sap xep sinh vien theo ten.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        elif key == 7:
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        elif key == 0:
            print("\nBan da chon thoat chuong trinh!")
            break
        else:
            print("\nKhong co chuc nang nay!")
            print("\nHay chon chuc nang trong hop menu.")
    except ValueError:
        print("\nVui long nhap so nguyen hop le!")