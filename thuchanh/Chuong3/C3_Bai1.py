class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None

class DaThuc:
    def __init__(self):
        self.head = None

    def Them(self, heso, somu):
        new_term = Node(heso, somu)
        if not self.head:
            self.head = new_term
        else:
            current = self.head
            while current.KeTiep:
                current = current.KeTiep
            current.KeTiep = new_term
    def Xuat(self):
        current = self.head
        while current:
            print(f"{current.HeSo}x^{current.SoMu}", end=" ")
            current = current.KeTiep
dathuc = DaThuc()
dathuc.Them(2, 3)
dathuc.Them(-1, 2)
dathuc.Them(3, 1)
dathuc.Them(4, 0)
print("Đa thức:")
dathuc.Xuat()