from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
import os
import gcd_lcm
import webbrowser
def resource_path(relative_path):
	try:
		base_path = os.path.join(sys._MEIPASS, 'data')
	except Exception:
		base_path = '...' # folder path of code
	return os.path.join(base_path, relative_path)

def main():
	root = Tk()
	root.title("GCD & LCM Calculator")
	root.resizable(width=False, height=False)
	root.geometry('550x440')
	root.iconbitmap(resource_path("icon.ico"))
	tab_control = Notebook(root)
	tab1 = Frame(tab_control)
	tab2 = Frame(tab_control)
	tab3 = Frame(tab_control)
	tab_control.add(tab1, text='GCD')
	tab_control.add(tab2, text='LCM')
	tab_control.add(tab3, text='Factor')
	tab_control.pack(expand=1, fill='both')

	str_var1 = StringVar()
	str_var2 = StringVar()
	str_var3 = StringVar()

	def web():
		webbrowser.open("https://www.facebook.com/white.nattapat")

	def loop_cal_gcd(alist, count=1):
		try: return show_gcd.insert(INSERT, "{}. GCD of {} and {} is {}.\n".format(count, alist[0], alist[1], gcd_lcm.gcd(alist[0], alist[1]))) + loop_cal_gcd([gcd_lcm.gcd(alist[0], alist[1])] + alist[2:], count=count+1)
		except: pass

	def loop_cal_gcd_2(alist):
		for i in range(len(alist)):
			show_gcd.insert(INSERT, "{}. Factors of {} are: {}.\n".format(i+1, alist[i], " ".join(list(map(str, gcd_lcm.factors(alist[i]))))))

	def gcd_calculate(*args):
		if str_var1.get() == "":
			show_gcd.configure(state="normal")
			show_gcd.delete("0.0", END)
			show_gcd.configure(state="disable")
		try:
			list_int = list(map(int, str_var1.get().split(" ")))
			loop_int = list(map(int, str_var1.get().split(" ")))
		except: return

		show_gcd.configure(state="normal")
		show_gcd.delete("0.0", END)
		show_gcd.insert(INSERT, "Result: \n")
		show_gcd.insert(INSERT, "Greatest Common Divisor (GCD) for {} is {}.\n\n".format(str_var1.get(), gcd_lcm.cal_gcd(list_int)))
		
		show_gcd.insert(INSERT, "Step by Step: \n")
		loop_cal_gcd(loop_int)
		if len(loop_int) == 1:
			show_gcd.insert(INSERT, "1. GCD of {} is 1 {}.\n".format(loop_int[0], loop_int[0]))
		show_gcd.insert(INSERT, "\n")
		show_gcd.insert(INSERT, "Step Factor: \n")
		loop_cal_gcd_2(loop_int)
		show_gcd.insert(INSERT, "\n")
		show_gcd.insert(INSERT, "We see that the Greatest Common Factor (Divisor) is {}.\n".format(gcd_lcm.factor_sum(loop_int)))

		show_gcd.configure(state="disable")

	str_var1.trace("w", gcd_calculate)
	Label(tab1, text="GCD Calculator", font=("Tohama", 20)).pack()
	Label(tab1, text="Greatest Common Divisor (GCD):", font=("Tohama", 10)).place(x=10, y=40)
	entry = Entry(tab1, width=87, textvariable=str_var1)
	entry.place(x=10, y=65)
	Label(tab1, text="This calculator will find Greatest Common Divisor (GCD) of two or more numbers with Step-by-step.").place(x=10, y=95)
	show_gcd = scrolledtext.ScrolledText(tab1,width=71,height=15,bd=4, font=("Tahoma", 10))
	show_gcd.configure(state="disable")
	show_gcd.place(x=10, y=125)
	Button(tab1, text="About me", command=web, width=20).place(x=200, y=385)

	def loop_cal_lcm(alist, count=1):
		try: return show_lcm.insert(INSERT, "{}. LCM of {} and {} is {}.\n".format(count, alist[0], alist[1], gcd_lcm.lcmfactor(alist[0], alist[1]))) + loop_cal_lcm([gcd_lcm.lcmfactor(alist[0], alist[1])] + alist[2:], count=count+1)
		except: pass

	def loop_cal_lcm_2(alist):
		for i in range(len(alist)):
			show_lcm.insert(INSERT, "{}. Factors of {} are: {}.\n".format(i+1, alist[i], " ".join(list(map(str, gcd_lcm.prime_factors(alist[i]))))))

	def lcm_calculate(*args):
		if str_var2.get() == "":
			show_lcm.configure(state="normal")
			show_lcm.delete("0.0", END)
			show_lcm.configure(state="disable")
		try:
			list_int = list(map(int, str_var2.get().split(" ")))
			loop_int = list(map(int, str_var2.get().split(" ")))
		except: return

		show_lcm.configure(state="normal")
		show_lcm.delete("0.0", END)
		show_lcm.insert(INSERT, "Result: \n")
		show_lcm.insert(INSERT, "Least Common Multiple (LCM) for {} is {}.\n\n".format(str_var2.get(), gcd_lcm.cal_lcm(list_int)))
		
		show_lcm.insert(INSERT, "Step by Step: \n")
		if len(loop_int) != 1:
			loop_cal_lcm(loop_int)
		else:
			show_lcm.insert(INSERT, "1. LCM of {} is 1 {}.\n".format(loop_int[0], loop_int[0]))
		show_lcm.insert(INSERT, "\n")
		show_lcm.insert(INSERT, "Step Prime Factor: \n")
		loop_cal_lcm_2(loop_int)
		show_lcm.insert(INSERT, "\n")
		show_lcm.insert(INSERT, "We see that the Least Common Multiple (LCM) is {} = {}.\n".format(" x ".join(list(map(str, gcd_lcm.prime_factors(gcd_lcm.cal_lcm(list_int))))), gcd_lcm.cal_lcm(list_int)))

		show_lcm.configure(state="disable")

	str_var2.trace("w", lcm_calculate)
	Label(tab2, text="LCM Calculator", font=("Tohama", 20)).pack()
	Label(tab2, text="Least Common Multiple (LCM):", font=("Tohama", 10)).place(x=10, y=40)
	entry2 = Entry(tab2, width=87, textvariable=str_var2)
	entry2.place(x=10, y=65)
	Label(tab2, text="This calculator will find Least Common Multiple (LCM) of two or more numbers with Step-by-step.").place(x=10, y=95)
	show_lcm = scrolledtext.ScrolledText(tab2,width=71,height=15,bd=4, font=("Tahoma", 10))
	show_lcm.configure(state="disable")
	show_lcm.place(x=10, y=125)
	Button(tab2, text="About me", command=web, width=20).place(x=200, y=385)

	def loop_cal_fac(alist):
		for i in range(len(alist)):
			show_fac.insert(INSERT, "{}. Factors of {} are: {}.\n".format(i+1, alist[i], " ".join(list(map(str, gcd_lcm.factors(alist[i]))))))

	def loop_prime(alist):
		for i in range(len(alist)):
			show_fac.insert(INSERT, "{}. Prime Factors of {} are: {}.\n".format(i+1, alist[i], " ".join(list(map(str, gcd_lcm.prime_factors(alist[i]))))))

	def fac_calculate(*args):
		if str_var3.get() == "":
			show_fac.configure(state="normal")
			show_fac.delete("0.0", END)
			show_fac.configure(state="disable")

		try:
			loop_int = list(map(int, str_var3.get().split(" ")))
		except: return

		show_fac.configure(state="normal")
		show_fac.delete("0.0", END)
		
		show_fac.insert(INSERT, "Factor: \n")
		loop_cal_fac(loop_int)
		show_fac.insert(INSERT, "\n")

		show_fac.insert(INSERT, "Prime Factor: \n")
		loop_prime(loop_int)

		show_fac.configure(state="disable")

	str_var3.trace("w", fac_calculate)
	Label(tab3, text="Factor Calculator", font=("Tohama", 20)).pack()
	Label(tab3, text="Factor and prime factor of number:", font=("Tohama", 10)).place(x=10, y=40)
	entry3 = Entry(tab3, width=87, textvariable=str_var3)
	entry3.place(x=10, y=65)
	show_fac = scrolledtext.ScrolledText(tab3,width=71,height=15,bd=4, font=("Tahoma", 10))
	show_fac.configure(state="disable")
	show_fac.place(x=10, y=125)
	Label(tab3, text="This calculator will find factor and prime factor of number.").place(x=10, y=95)
	Button(tab3, text="About me", command=web, width=20).place(x=200, y=385)

	root.mainloop()

if __name__ == '__main__':
	main()
