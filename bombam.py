dictionary = {}
def menu():
	print("-"*50)
	print("พจนานุกรม\n 1.เพิ่มคำศัพท์\n 2.แสดงคำศัพท์\n 3.ลบคำศัพท์\n 4.ออกจากโปรแกรม\n")
def add():
	w = input("เพิ่มคำศัพท์ : " )
	t = input("ชนิดคำศัพท์ (n,v,adj,adv) : ")
	m = input("ความหมาย : ")
	dictionary.update({w:{t,m}})
def view():
	print("-"*50)
	print(" "*20 +"คำศัพท์ของคุณมีดังนี้"+"	"*20)
	print("-"*50)
	print("{0:-<15}{1:-<15}{2:-<10}".format("คำศัพท์" , "ประเภท", "ความหมาย"))
	for a,b in dictionary.items():
		print(a+"   ",b)
def remove():
	x = input("พิมพ์คำศัพท์ที่ต้องการลบ :")
	z = input("คุณแน่ใจใช่ไหมว่าต้องการลบ (y/n) :")
	if z == "y":
		dictionary.pop(x)
	else:
		print(" ")

while True:
	menu()
	me = int(input("เลือกรายการที่ต้องการ : "))
	if me == 1:
		add()
	elif me == 2:
		view()
	elif me == 3:
		remove()
	else:
		z = input("คุณแน่ใจใช่มั้ยว่าต้องการออกจากโปรแกรม : ")
		if z == "y":
			break
		else:
			print(" ")