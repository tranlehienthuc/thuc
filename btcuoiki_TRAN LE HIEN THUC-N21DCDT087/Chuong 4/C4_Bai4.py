class Solution:
    def HauTo(self, bt):
        def la_toan_tu(char):
            return char in '+-*/'
        def do_uu_tien(toan):
            if toan == '+' or toan == '-':
                return 1
            elif toan == '*' or toan == '/':
                return 2
            return 0  
        hau_to = []  
        toan_tu_stack = []  

        i = 0
        while i < len(bt):
            if bt[i] == ' ':
                i += 1
                continue
            elif bt[i].isdigit():
                operand = ''
                while i < len(bt) and bt[i].isdigit():
                    operand += bt[i]
                    i += 1
                hau_to.append(operand)
            elif bt[i] == '(':
                toan_tu_stack.append(bt[i])
            elif bt[i] == ')':
                while toan_tu_stack and toan_tu_stack[-1] != '(':
                    hau_to.append(toan_tu_stack.pop())
                toan_tu_stack.pop()  
            elif la_toan_tu(bt[i]):
                while toan_tu_stack and do_uu_tien(bt[i]) <= do_uu_tien(toan_tu_stack[-1]):
                    hau_to.append(toan_tu_stack.pop())
                toan_tu_stack.append(bt[i])
            i += 1
        while toan_tu_stack:
            hau_to.append(toan_tu_stack.pop())
        return ' '.join(hau_to)

bt = "2 + 3 * 5"
solution = Solution()
print("Biểu thức hậu tố tương ứng là:", solution.HauTo(bt))

