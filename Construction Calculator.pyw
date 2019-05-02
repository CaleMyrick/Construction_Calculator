import tkinter as tk 


window = tk.Tk() 

window.title("Flooring Calculator")




f = open('NewBid.txt', 'w')

#window.geometry("250x250")

my_menu = tk.Menu(window)
window.config(menu=my_menu)


#Standard File Menu
# file_menu = tk.Menu(my_menu)
# my_menu.add_cascade(label='File', menu = file_menu)
# file_menu.add_command(label='New Project', command=window.clear)
# file_menu.add_command(label='Exit', command=window.quit)

#Menu To Choose A Trade
# trades_menu = tk.Menu(my_menu) 
# my_menu.add_cascade(label='Switch Trades', menu = trades_menu)
# trades_menu.add_command(label = 'Flooring')
# trades_menu.add_command(label = 'Paint')




# for col_num in range(1, 10):
    # spacer=tk.Label(window, text=str(col_num))
    # spacer.grid(row = 0, column = col_num)
# for row_num in range(10):
    # spacer=tk.Label(window, text=str(row_num))
    # spacer.grid(row = row_num, column = 0)
    # window.rowconfigure(row_num, minsize=40)



#Entry Fields / Labels


#Information About All Entry Fields Being In Square Feet

sf_label = tk.Label(window, text='Calculations Automatically \n Add Waste')
sf_label.grid(row=1 , column= 3, sticky=tk.E)


#Label For Tile Type @ Tops Of Columns

vct_type_label = tk.Label(window, text='Square Footages')
vct_type_label.grid(row=1, column=1)

vct_type_label = tk.Label(window, text='Square Footages')
vct_type_label.grid(row=1, column=5)

vest_ceramic_label = tk.Label(window, text='Vestibule Ceramic')
vest_ceramic_label.grid(row=6, column=5)

#Estimator Name / Entry Label & Field
name_label = tk.Label(window, text='Estimator: ')
name_label.grid(row=0, column=0,)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

#Job Name / Entry Label & Field

job_label=tk.Label(window, text='Job: ')
job_label.grid(row=0, column=2,sticky=tk.E)
job_entry=tk.Entry(window)
job_entry.grid(row=0, column=3)

#Job Location / Entry Label & Field

job_location=tk.Label(window, text='Location: ')
job_location.grid(row=0, column=4, sticky=tk.E)
job_location=tk.Entry(window)
job_location.grid(row=0, column=5, padx=10)

#VCT Pattern / Entry Label & Fields

vct_1_label=tk.Label(window, text='VCT-1: ')
vct_1_label.grid(row=2, column=0,sticky=tk.E)
vct_1_location=tk.Entry(window)
vct_1_location.grid(row=2, column=1)

vct_2_label=tk.Label(window, text='VCT-2: ')
vct_2_label.grid(row=3, column=0,sticky=tk.E)
vct_2_location=tk.Entry(window)
vct_2_location.grid(row=3, column=1)

vct_3_label=tk.Label(window, text='VCT-3: ')
vct_3_label.grid(row=4, column=0,sticky=tk.E)
vct_3_location=tk.Entry(window)
vct_3_location.grid(row=4, column=1)

vct_4_label=tk.Label(window, text='VCT-4: ')
vct_4_label.grid(row=5, column=0,sticky=tk.E)
vct_4_location=tk.Entry(window)
vct_4_location.grid(row=5, column=1)

vct_5_label=tk.Label(window, text='VCT-5: ')
vct_5_label.grid(row=6, column=0,sticky=tk.E)
vct_5_location=tk.Entry(window)
vct_5_location.grid(row=6, column=1)

vct_6_label=tk.Label(window, text='VCT-6: ')
vct_6_label.grid(row=7, column=0,sticky=tk.E)
vct_6_location=tk.Entry(window)
vct_6_location.grid(row=7, column=1)

vct_7_label=tk.Label(window, text='VCT-7: ')
vct_7_label.grid(row=8, column=0,sticky=tk.E)
vct_7_location=tk.Entry(window)
vct_7_location.grid(row=8, column=1)

vct_8_label=tk.Label(window, text='VCT-8: ')
vct_8_label.grid(row=9, column=0,sticky=tk.E)
vct_8_location=tk.Entry(window)
vct_8_location.grid(row=9, column=1)

vct_11_label=tk.Label(window, text='VCT-11: ')
vct_11_label.grid(row=10, column=0,sticky=tk.E)
vct_11_location=tk.Entry(window)
vct_11_location.grid(row=10, column=1)

vct_12_label=tk.Label(window, text='VCT-12: ')
vct_12_label.grid(row=11, column=0,sticky=tk.E)
vct_12_location=tk.Entry(window)
vct_12_location.grid(row=11, column=1)

#LVT Labels & Entry Fields

lvt_13_label=tk.Label(window, text='LVT-13: ')
lvt_13_label.grid(row=2, column=4,sticky=tk.E)
lvt_13_location=tk.Entry(window)
lvt_13_location.grid(row=2, column=5)

lvt_14_label=tk.Label(window, text='LVT-14: ')
lvt_14_label.grid(row=3, column=4,sticky=tk.E)
lvt_14_location=tk.Entry(window)
lvt_14_location.grid(row=3, column=5)

lvt_15_label=tk.Label(window, text='LVT-15: ')
lvt_15_label.grid(row=4, column=4,sticky=tk.E)
lvt_15_location=tk.Entry(window)
lvt_15_location.grid(row=4, column=5)

#Vestibule Ceramic Labels & Entry Fields

vest_9_label=tk.Label(window, text='9x9 Tiles (Ea): ')
vest_9_label.grid(row=7, column=4,sticky=tk.E)
vest_9_location=tk.Entry(window)
vest_9_location.grid(row=7, column=5)

vest_18_label=tk.Label(window, text='18x18 Tiles (Ea): ')
vest_18_label.grid(row=8, column=4,sticky=tk.E)
vest_18_location=tk.Entry(window)
vest_18_location.grid(row=8, column=5)


#Functions



def submit_button_clicked(self):
	
	
	
	name_entry.get()
	f.write("Name: ")
	f.write(str(name_entry.get()))
	f.write("\n")
	
	job_entry.get()
	f.write("Job: ")
	f.write(str(job_entry.get()))
	f.write("\n")
	
	job_location.get()
	f.write("Location: ")
	f.write(str(job_location.get()))
	f.write("\n")
	
	
	vct_1_location.get()
	f.write("VCT-1 Boxes Needed: ")
	vct_1_convert = int(vct_1_location.get())
	if vct_1_convert > 0:
		f.write(str(vct_1_convert // 45 + 1))
		f.write("\n")
	else:
		f.write("0")
		f.write("\n")
		
	
	vct_2_location.get()
	f.write("VCT-2 Boxes Needed: ")
	vct_2_convert = int(vct_2_location.get())
	if vct_2_convert > 0:
		f.write(str(vct_2_convert // 45 + 1))
		f.write("\n")
	else:
		f.write("0")
		f.write("\n")
	
	
	vct_3_location.get()
	f.write("VCT-3 Boxes Needed: ")
	vct_3_convert = int(vct_3_location.get())
	if vct_3_convert > 0:
		f.write(str(vct_3_convert // 45 + 1))
		f.write("\n")
	else:
		f.write("0")
		f.write("\n")
	
	vct_4_location.get()
	f.write("VCT-4 Boxes Needed: ")
	vct_4_convert = int(vct_4_location.get())
	if vct_4_convert > 0:
		f.write(str(vct_4_convert // 45 + 1))
		f.write("\n")
	else:
		f.write("0")
		f.write("\n")
	
	vct_5_location.get()
	f.write("VCT-5 Boxes Needed: ")
	vct_5_convert = int(vct_5_location.get())
	if vct_5_convert > 0:
		f.write(str(vct_5_convert // 45 + 1))
		f.write("\n")
	else:
		f.write("0")
		f.write("\n")
	
	vct_6_location.get()
	f.write("VCT-6 Boxes Needed: ")
	vct_6_convert = int(vct_6_location.get())
	if vct_6_convert > 0:
		f.write(str(vct_6_convert // 45 + 1))
		f.write("\n")
	else:
		f.write("0")
		f.write("\n")
	
	vct_7_location.get()
	f.write("VCT-7 Boxes Needed: ")
	vct_7_convert = int(vct_7_location.get())
	if vct_7_convert > 0:
		f.write(str(vct_7_convert // 45 + 1))
		f.write("\n")
	else:
		f.write("0")
		f.write("\n")
	
	vct_8_location.get()
	f.write("VCT-8 Boxes Needed: ")
	vct_8_convert = int(vct_8_location.get())
	if vct_8_convert > 0:
		f.write(str(vct_8_convert // 45 + 1))
		f.write("\n")
	else:
		f.write("0")
		f.write("\n")
	
	vct_11_location.get()
	f.write("VCT-11 Boxes Needed: ")
	vct_11_convert = int(vct_11_location.get())
	if vct_11_convert > 0:
		f.write(str(vct_11_convert // 45 + 1))
		f.write("\n")
	else:
		f.write("0")
		f.write("\n")
	
	vct_12_location.get()
	f.write("VCT-12 Boxes Needed: ")
	vct_12_convert = int(vct_12_location.get())
	if vct_12_convert > 0:
		f.write(str(vct_12_convert // 45 + 1))
		f.write("\n")
	else:
		f.write("0")
		f.write("\n")
	
	lvt_13_location.get()
	f.write("LVT-13 Boxes Needed: ")
	lvt_13_convert = int(lvt_13_location.get())
	if lvt_13_convert > 0:
		f.write(str(lvt_13_convert // 45 + 1))
		f.write("\n")
	else:
		f.write("0")
		f.write("\n")
	
	lvt_14_location.get()
	f.write("LVT-14 Boxes Needed: ")
	lvt_14_convert = int(lvt_14_location.get())
	if lvt_14_convert > 0:
		f.write(str(lvt_14_convert // 45 + 1))
		f.write("\n")
	else:
		f.write("0")
		f.write("\n")
	
	lvt_15_location.get()
	f.write("LVT-15 Boxes Needed: ")
	lvt_15_convert = int(lvt_15_location.get())
	if lvt_15_convert > 0:
		f.write(str(lvt_15_convert // 45 + 1))
		f.write("\n")
	else:
		f.write("0")
		f.write("\n")
	
	vest_9_location.get()
	f.write("9x9 Tiles Needed: ")
	vest_9_convert = int(vest_9_location.get())
	if vest_9_convert > 0:
		f.write(str(vest_9_convert // 0.5625 + 1))
		f.write("\n")
	else:
		f.write("0")
		f.write("\n")
	
	
	vest_18_location.get()
	f.write("18x18 Tiles Needed: ")
	vest_18_convert = int(vest_18_location.get())
	if vest_18_convert > 0:
		f.write(str(vest_18_convert // 0.5625 + 1))
		f.write("\n")
	else:
		f.write("0")
		f.write("\n")
	
	total_vct_boxes_needed = (vct_1_convert + vct_2_convert + vct_3_convert + vct_4_convert + 
	vct_5_convert + vct_6_convert + vct_7_convert + vct_8_convert + vct_11_convert + vct_12_convert)
	f.write("Total VCT Boxes Needed: ")
	f.write(str(total_vct_boxes_needed * 1.10 // 45 + 1))
	f.write("\n")
	
	total_lvt_boxes_needed = lvt_13_convert + lvt_14_convert + lvt_15_convert
	f.write("Total LVT Boxes Needed: ")
	f.write (str(total_lvt_boxes_needed * 1.12 // 45 + 1))
	f.write("\n")
	
	
# Clear Button Function

def clear_button_clicked(self):
	
	name_entry.delete(0,20)
	job_entry.delete(0,20)
	job_location.delete(0,20)
	vct_1_location.delete(0,20)
	vct_2_location.delete(0,20)
	vct_3_location.delete(0,20)
	vct_4_location.delete(0,20)
	vct_5_location.delete(0,20)
	vct_6_location.delete(0,20)
	vct_7_location.delete(0,20)
	vct_8_location.delete(0,20)
	vct_11_location.delete(0,20)
	vct_12_location.delete(0,20)
	lvt_13_location.delete(0,20)
	lvt_14_location.delete(0,20)
	lvt_15_location.delete(0,20)
	vest_9_location.delete(0,20)
	vest_18_location.delete(0,20)
	
	
	



#Buttons

clear_button = tk.Button(window, text='Clear')
clear_button.bind("<Button-1>", clear_button_clicked)
clear_button.grid(row=12, column=4, sticky=tk.E)


submit_button = tk.Button(window, text='Submit')
submit_button.bind("<Button-1>", submit_button_clicked)
submit_button.grid(row=12, column=5, sticky=tk.W)




window.mainloop()
