from guizero import App, Text, TextBox, PushButton, Box, Window
import math
#Tạo app
app = App(title="Giải Phương Trình", width=400, height=350)
Text(app,"Giải Phương Trình",size=18, color="blue")
#Tạo cửa sổ giải pt bậc nhất
windown = Window(app,title="Giải Phương Trình Bậc Nhất", width=400, height=350)
windown.hide()
Text(windown, text="Giải Phương Trình Bậc Nhất\nax + b = 0 (a khác 0)", size=18, color="blue")
box = Box(windown, layout="grid")
Text(box, text="Nhập a:", grid=[0,0])
a1 = TextBox(box, grid=[1,0])
Text(box, text="Nhập b:", grid=[0,1])
b1 = TextBox(box, grid=[1,1])
Text(windown, text="Kết quả:", size=17,color='red')
ketqua = Text(windown, text="---")
#Tạo cửa sổ giải pt bậc hai
windown2 = Window(app,title="Giải Phương Trình Bậc Hai", width=400, height=350)
windown2.hide()
Text(windown2, text="Giải Phương Trình Bậc Hai\nax^2 + bx + c = 0 (a khác 0)", size=18, color="blue")
box1 = Box(windown2, layout="grid")
Text(box1, text="Nhập a:", grid=[0,0])
a = TextBox(box1, grid=[1,0])
Text(box1, text="Nhập b:", grid=[0,1])
b = TextBox(box1, grid=[1,1])
Text(box1, text="Nhập c:", grid=[0,2])
c = TextBox(box1, grid=[1,2])
Text(windown2, text="Kết quả:", size=17,color='red')
ketqua2 = Text(windown2, text="---")
#Giải pt bậc nhất
def ptbac1():
    windown.show()
    def tinhtoan():
        try:          
            so_a1 = float(a1.value)
            so_b1 = float(b1.value)
            if so_a1 == 0:
                if so_b1 != 0:
                    ketqua.value = f"Vô nghiệm\n\nPhương trình {so_a1} + {so_b1} = {0}\nCó {so_a1} = 0 và {so_b1} khác 0\n===> Phương trình Vô nghiệm" 
                else:
                    ketqua.value = f"Vô số nghiệm\n\nPhương trình {so_a1} + {so_b1} = {0}\nCó {so_a1} = 0 và {so_b1} = 0\n===> Phương trình Vô số nghiệm" 
            else:
                x = -so_b1 / so_a1
                ketqua.value = f"x = {x}\n\nPhương trình {so_a1} + {so_b1} = {0}\nCó {so_a1} khác 0\n===> Phương trình có nghiệm:\n-{so_b1} : {so_a1} = {x}"
        except:
            ketqua.value = "Vui lòng chỉ nhập số!"
    PushButton(windown, command=tinhtoan, text="Tính toán")
PushButton(app, command=ptbac1, text="Phương trình bậc nhất")
#Giải pt bậc 2
def ptbac2():
    windown2.show()
    def tinhtoan1():
        try:
            so_a = float(a.value)
            so_b = float(b.value)
            so_c = float(c.value)
            if so_a == 0:
                if so_b == 0:       
                    if so_c != 0:
                        ketqua2.value = f"Vô nghiệm\n\nPhương trình {so_a}^2+{so_b}x + {so_c} = {0}\nCó {so_a} = 0 và {so_b} = 0 và {so_c} khác 0\n===>Phương trình vô nghiệm"
                    else:
                        ketqua2.value = f"Vô số nghiệm\n\nPhương trình {so_a}^2+{so_b}x + {so_c} = {0}\nCó {so_a} = 0 và {so_b} = 0 và {so_c} = 0\n===>Phương trình vô số nghiệm"
                else:
                    x = -so_c / so_b
                    ketqua2.value = f"x = {x}\n\nPhương trình {so_a}^2+{so_b}x + {so_c} = {0}\nCó {so_a} = 0 và {so_b} khác 0\n===>Phương trình có nghiệm:\n-{so_c} : {so_b} = {x}"
            else:          
                delta = so_b**2 - 4*so_a*so_c    
                if delta < 0:     
                    ketqua2.value = f"Vô nghiệm\n\nPhương trình {so_a}^2+{so_b}x + {so_c} = {0}\nCó {so_a} khác 0\n===> Delta = {so_b}^2 - 4{so_a}{so_c} = {delta}\nVì {delta} < 0\n===>Phương trình vô nghiệm"
                elif delta == 0:      
                    x = -so_b / (2 * so_a)
                    ketqua2.value = f"x1 = x2 = {x}\n\nPhương trình {so_a}^2+{so_b}x + {so_c} = {0}\nCó {so_a} khác 0\n===> Delta = {so_b}^2 - 4{so_a}{so_c} = {delta}\nVì {delta} = 0\n===>Phương trình có nghiệm kép\nx1 = x2 = -{so_b} : 2{so_a} = {x}"
                else:        
                    x1 = (-so_b + math.sqrt(delta)) / (2 * so_a)
                    x2 = (-so_b - math.sqrt(delta)) / (2 * so_a)
                    ketqua2.value = f"x1 = {x1}\nx2 = {x2}\n\nPhương trình {so_a}^2+{so_b}x + {so_c} = {0}\nCó {so_a} khác 0\n===> Delta = {so_b}^2 - 4{so_a}{so_c} = {delta}\nVì {delta} > 0\n===>Phương trình có 2 nghiệm x1 và x2\nx1 = -{so_b} + căn bậc hai {delta} : 2{so_a} = {x1}\nx2 = -{so_b} - căn bậc hai {delta} : 2{so_a} = {x2}\n===> Phương trình có 2 nghiệm:\nx1 = {x1}\nx2 = {x2}"
        except:
            ketqua2.value = "Vui lòng chỉ nhập số!"
    PushButton(windown2, command=tinhtoan1, text="Tính toán")
PushButton(app, command=ptbac2, text="Phương trình bậc hai")
app.display()