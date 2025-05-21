from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxID = 1
        if self.soLuongSinhVien() > 0:
            maxID = max(sv._id for sv in self.listSinhVien) + 1
        return maxID

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        try:
            svId = self.generateID()
            print(f"ID sinh vien duoc tao: {svId}")
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh cua sinh vien: ")
            diemTB = float(input("Nhap diem cua sinh vien: "))
            if not (0 <= diemTB <= 10):
                raise ValueError("Diem trung binh phai tu 0 den 10.")
            sv = SinhVien(svId, name, sex, major, diemTB)
            self.xepLoaiHocLuc(sv)
            self.listSinhVien.append(sv)
        except ValueError as e:
            print(f"Loi nhap lieu: {e}")

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv:
            try:
                name = input("Nhap ten sinh vien: ")
                sex = input("Nhap gioi tinh sinh vien: ")
                major = input("Nhap chuyen nganh cua sinh vien: ")
                diemTB = float(input("Nhap diem cua sinh vien: "))
                if not (0 <= diemTB <= 10):
                    raise ValueError("Diem trung binh phai tu 0 den 10.")
                sv._name = name
                sv._sex = sex
                sv._major = major
                sv._diemTB = diemTB
                self.xepLoaiHocLuc(sv)
                print(f"Cap nhat sinh vien ID {ID} thanh cong.")
            except ValueError as e:
                print(f"Loi nhap lieu: {e}")
        else:
            print(f"Sinh vien co ID = {ID} khong ton tai.")

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB)

    def findByID(self, ID):
        return next((sv for sv in self.listSinhVien if sv._id == ID), None)

    def findByName(self, keyword):
        return [sv for sv in self.listSinhVien if keyword.upper() in sv._name.upper()]

    def deleteById(self, ID):
        sv = self.findByID(ID)
        if sv:
            self.listSinhVien.remove(sv)
            return True
        return False

    def xepLoaiHocLuc(self, sv: SinhVien):
        if sv._diemTB >= 8:
            sv._hocluc = "Gioi"
        elif sv._diemTB >= 5:
            sv._hocluc = "Trung binh"
        else:
            sv._hocluc = "Yeu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<15} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        for sv in listSV:
            print("{:<8} {:<18} {:<8} {:<15} {:<8.2f} {:<8}".format(sv._id, sv._name[:18], sv._sex, sv._major[:15], sv._diemTB, sv._hocluc))
        print()

    def getListSinhVien(self):
        return self.listSinhVien