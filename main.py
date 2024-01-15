import customtkinter as ctk
import tkinter as tk
from tkinter import StringVar, filedialog

# window 
window = ctk.CTk()
window.title('Signature generetor for thunderbird')
window.geometry('400x450')

# Button function
def generate():

    # Get details
    name_info=name.get()
    designation_info=designation.get()
    mobile_info=mobile.get()

    # Mobile number formated 12 345 6789 
    formated_mobile_info=f"{mobile_info[:2]} {mobile_info[2:5]} {mobile_info[5:]}"

    email_info=email.get()
    land_info=land.get()

    # Mobile number formated 12 345 6789 
    formated_land_info=f"{land_info[:2]} {land_info[2:5]} {land_info[5:]}"
    address_info=address.get()
    city_info=city.get()

    cpc_check_info=cpc_check_var.get()
    life_check_info=life_check_var.get()
    ho_check_info=ho_check_var.get()
    mobile_check_info=mobile_check_var.get()

    # Creating HTML File
    file=filedialog.asksaveasfile(defaultextension='.html',
                                  filetypes=[
                                      ("HTML file",".html")
                                  ])
    file.write("<html><Font size=2> With Best Regards, </Font><BR><Font size=2><B>")
    file.write("\n")
    file.write(name_info + " | " + designation_info + "</B></Font>") 
    file.write("\n")
    file.write('<DIV class="NonPrintable"> <B><FONT size=2 color="red">ABC (PVT) ltd</FONT></B><FONT size=2><BR>')
    file.write("\n")

    if cpc_check_info == "on":
        file.write ("# 123, Main Road | Colombo | Sri Lanka.<BR>")
        file.write("\n")
    elif life_check_info == "on":
        file.write ("# 123, Main Road | Colombo | Sri Lanka.<BR>")
        file.write("\n")
    elif ho_check_info == "on":
        file.write ("# 123, Main Road | Colombo | Sri Lanka.<BR>")
        file.write("\n")
    else:
     file.write("#" + address_info + "|" + city_info + "| Sri Lanka.<BR>")
     file.write("\n")

    file.write("Tel:  +94 " + formated_land_info + " | Fax: +94 12 345 6789 " )
    if mobile_check_info == "on":
        file.write ("| GSM: +94 " + formated_mobile_info)
    else:
        file.write (" ")
    file.write("\n")
    file.write("<BR>Email: " + email_info )
    file.write("\n")
    file.write(' | <A href="http://www.abc.com">http://www.abc.com</A></Font>')

    file.close

#GUI
#lable and text box
name_lable = ctk.CTkLabel(master = window, text="Name", anchor="e")
name_lable.grid(row = 0, column = 0, pady=8)

name=StringVar()
name_entry = ctk.CTkEntry(master = window, textvariable=name)
name_entry.grid(row = 0, column = 1)

Designation_lable = ctk.CTkLabel(master = window, text="Designation")
Designation_lable.grid(row = 1, column = 0, pady=8 )

designation=StringVar()
Designation_entry = ctk.CTkEntry(master = window, textvariable=designation)
Designation_entry.grid(row = 1, column = 1)

Mobile_lable = ctk.CTkLabel(master = window, text="Mobile")
Mobile_lable.grid(row = 2, column = 0, pady=8 )

mobile=StringVar()
Mobile_entry = ctk.CTkEntry(master = window, textvariable=mobile)
Mobile_entry.grid(row = 2, column = 1)

mobile_check_var = ctk.StringVar(value="on")
mobile_check = ctk.CTkCheckBox(master = window, text="", variable=mobile_check_var, onvalue="on", offvalue="off")
mobile_check.grid(row = 2, column = 2, padx=20, pady=20)

email_lable = ctk.CTkLabel(master = window, text="E-mail")
email_lable.grid(row = 3, column = 0, pady=8 )

email=StringVar()
email_entry = ctk.CTkEntry(master = window, textvariable=email)
email_entry.grid(row = 3, column = 1)

#check buttons
cpc_check_var = ctk.StringVar(value="on")
cpc_check = ctk.CTkCheckBox(master = window, text="CPC", variable=cpc_check_var, onvalue="on", offvalue="off")
cpc_check.grid(row = 4, column = 0, padx=20, pady=20)

life_check_var = ctk.StringVar(value="off")
life_check = ctk.CTkCheckBox(master = window, text="Life", variable=life_check_var, onvalue="on", offvalue="off")
life_check.grid(row = 4, column = 1, padx=20, pady=20)

ho_check_var = ctk.StringVar(value="off")
ho_check = ctk.CTkCheckBox(master = window, text="HO", variable=ho_check_var, onvalue="on", offvalue="off")
ho_check.grid(row = 4, column = 2, padx=20, pady=20)

#lable and text box
Land_lable = ctk.CTkLabel(master = window, text="Land Phone")
Land_lable.grid(row = 5, column = 0, pady=2,)

land=StringVar()
Land_entry = ctk.CTkEntry(master = window, textvariable=land)
Land_entry.grid(row = 5, column = 1)

Address_lable = ctk.CTkLabel(master = window, text="Address")
Address_lable.grid(row = 6, column = 0, pady=8 )

address=StringVar()
Address_entry = ctk.CTkEntry(master = window, textvariable=address)
Address_entry.grid(row = 6, column = 1)

city_lable = ctk.CTkLabel(master = window, text="City")
city_lable.grid(row = 7, column = 0, pady=8 )

city=StringVar()
city_entry = ctk.CTkEntry(master = window, textvariable=city)
city_entry.grid(row = 7, column = 1)

#button
button = ctk.CTkButton(master = window, text="Generate", command=generate)
button.grid(row = 8, column = 1)

# run
window.mainloop()