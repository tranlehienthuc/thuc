class Solution:
    def GiaTri(self, bt):
        def tinh(toan, operand1, operand2):
            if toan == '+':
                return operand1 + operand2
            elif toan == '-':
                return operand1 - operand2
            elif toan == '*':
                return operand1 * operand2
            elif toan == '/':
                return operand1 / operand2
        def la_toan_tu(char):
            return char in '+-*/'

        toan_hang_stack = []  
        toan_tu_stack = []  
        i = 0
        while i < len(bt):
            if bt[i] == ' ':
                i += 1
                continue
            elif bt[i] == '(':
                toan_tu_stack.append(bt[i])
            elif la_toan_tu(bt[i]):
                while toan_tu_stack and toan_tu_stack[-1] != '(' and (
                        (bt[i] == '*' or bt[i] == '/') and (toan_tu_stack[-1] == '+' or toan_tu_stack[-1] == '-')):
                    toan_hang2 = toan_hang_stack.pop()
                    toan_hang1 = toan_hang_stack.pop()
                    toan_tu = toan_tu_stack.pop()
                    toan_hang_stack.append(tinh(toan_tu, toan_hang1, toan_hang2))
                toan_tu_stack.append(bt[i])
            elif bt[i] == ')':
                while toan_tu_stack and toan_tu_stack[-1] != '(':
                    toan_hang2 = toan_hang_stack.pop()
                    toan_hang1 = toan_hang_stack.pop()
                    toan_tu = toan_tu_stack.pop()
                    toan_hang_stack.append(tinh(toan_tu, toan_hang1, toan_hang2))
                toan_tu_stack.pop() 
            else:
                toan_hang = ''
                while i < len(bt) and bt[i].isdigit():
                    toan_hang += bt[i]
                    i += 1
                toan_hang_stack.append(int(toan_hang))
                continue
            i += 1
        while toan_tu_stack:
            toan_hang2 = toan_hang_stack.pop()
            toan_hang1 = toan_hang_stack.pop()
            toan_tu = toan_tu_stack.pop()
            toan_hang_stack.append(tinh(toan_tu, toan_hang1, toan_hang2))
        return toan_hang_stack[-1]

bt = "(3 + 4) * 2 / ( 3 - 1 )"
solution = Solution()
print("Giá trị của biểu thức là:", solution.GiaTri(bt))
