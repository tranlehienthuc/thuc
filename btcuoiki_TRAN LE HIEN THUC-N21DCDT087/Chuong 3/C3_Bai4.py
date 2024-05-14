class Node:
    def __init__(self, he_so, so_mu):
        self.he_so = he_so
        self.so_mu = so_mu
        self.ke_tiep = None

class DaThuc:
    def __init__(self):
        self.head = None

    def them_so_hang(self, he_so, so_mu):
        new_node = Node(he_so, so_mu)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.ke_tiep:
                current = current.ke_tiep
            current.ke_tiep = new_node

    def rut_gon(self):
        current = self.head
        while current:
            temp = current.ke_tiep
            while temp:
                if temp.so_mu == current.so_mu:
                    current.he_so += temp.he_so
                    current.ke_tiep = temp.ke_tiep
                temp = temp.ke_tiep
            if current.he_so == 0:
                current = current.ke_tiep
            else:
                current = current.ke_tiep

    def doi_dau(self):
        current = self.head
        while current:
            current.he_so = -current.he_so
            current = current.ke_tiep

    def in_da_thuc(self):
        current = self.head
        while current:
            print(f"{current.he_so}x^{current.so_mu}", end=" ")
            current = current.ke_tiep
        print()

dathuc = DaThuc()
dathuc.them_so_hang(3, 2)
dathuc.them_so_hang(-2, 3)
dathuc.them_so_hang(5, 2)

print("Đa thức ban đầu:")
dathuc.in_da_thuc()

dathuc.doi_dau()

print("Đa thức sau khi đổi dấu:")
dathuc.in_da_thuc()
