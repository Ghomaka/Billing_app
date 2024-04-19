import customtkinter as ctk
from PIL import Image, ImageTk
import re
from customtkinter import CTkImage, CTkButton, CTkFrame

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def on_button_click():
    # Create a new window for the pop-up
    popup = ctk.CTkToplevel(master=root)
    popup.title("Cart")
    popup.attributes('-topmost', True)
    framepop = ctk.CTkScrollableFrame(master=popup, corner_radius=15, orientation="vertical", height=100)
    framepop.pack(pady=15, padx=65, fill="both", expand=False, side="top")

    # Increase the pop-up size (adjust width and height as desired)
    new_width = 400  # Adjust this value for desired width
    new_height = 420  # Adjust this value for desired height

    # Center the pop-up window (using the new size)
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x = int((screen_width / 2) - (new_width / 2))
    y = int((screen_height / 2) - (new_height / 2))

    # Update the pop-up geometry with new size and centered position
    popup.geometry(f"{new_width}x{new_height}+{x}+{y}")

    # Create labels
    label_combo = ctk.CTkLabel(master=framepop, text="Select a product:")
    label_combo.pack(pady=10, padx=20)
    # Create a combo box with options
    combo_options = ["Pizza", "Burger", "Chips", "Cake", "Grapes", "Watermelon", "Strawberry", "Wings", "Elvino",
                         "Jack Daniels", "Wine", "Castel", "Top", "Orange juice", "Jack Daniels", "Yogourt", "Sprite", "Shampoo", "Perfume", "Soap", "Face oil", "Moisturizer", "Tooth paste", "Liquid soap", "Shave gel"]
    combo_var = ctk.StringVar(value=combo_options[0])  # Initial selection (optional)
    combo_box = ctk.CTkComboBox(master=framepop, values=combo_options, variable=combo_var)
    combo_box.pack(pady=10, padx=20)

    label_number = ctk.CTkLabel(master=framepop, text="Enter the quantity:")
    label_number.pack(pady=10, padx=20)


    # Create an input box for numbers with validation (optional)
    number_var = ctk.StringVar()
    number_entry = ctk.CTkEntry(master=framepop, placeholder_text="Enter a number", textvariable=number_var)
    number_entry.pack(pady=10, padx=20)

    def validate_number(new_value):
        # Allow only numbers, negative signs, and decimal points
        pattern = r"^-?\d+\.?\d*$"
        return bool(re.match(pattern, new_value))

    number_var.trace_add("write", validate_number)  # Validate input on every keystroke
    label_combo = ctk.CTkLabel(master=framepop, text="")
    label_combo.pack(pady=10, padx=20)
    # Optionally add a button to handle user input
    def handle_selection():
        selected_option = combo_var.get()
        number_input = number_var.get()


        if validate_number(number_input):
            print(f"You selected: {selected_option}, Quantity entered: {float(number_input)}")
            popup.destroy()
        else:
            print("Invalid number entered. Please enter a valid number.")

    def add_product():
        label_combo = ctk.CTkLabel(master=framepop, text="Select a product:")
        label_combo.pack(pady=10, padx=20)
        # Create a combo box with options
        combo_options = ["Pizza", "Burger", "Chips", "Cake", "Grapes", "Watermelon", "Strawberry", "Wings", "Elvino",
                         "Jack Daniels", "Wine", "Castel", "Top", "Orange juice", "Jack Daniels", "Yogourt", "Sprite", "Shampoo", "Perfume", "Soap", "Face oil", "Moisturizer", "Tooth paste", "Liquid soap", "Shave gel"]
        combo_var = ctk.StringVar(value=combo_options[0])  # Initial selection (optional)
        combo_box = ctk.CTkComboBox(master=framepop, values=combo_options, variable=combo_var)
        combo_box.pack(pady=10, padx=20)

        list_of_variables=[]



        label_number = ctk.CTkLabel(master=framepop, text="Enter the quantity:")
        label_number.pack(pady=10, padx=20)

        def handle_selection():
            selected_option = combo_var.get()
            number_input = number_var.get()

            # Perform actions based on selection and number (check for valid number input)
            if validate_number(number_input):
                print(f"You selected: {selected_option}, Quantity entered: {float(number_input)}")
                popup.destroy()
            else:
                print("Invalid number entered. Please enter a valid number.")

        number_var = ctk.StringVar()
        number_entry = ctk.CTkEntry(master=framepop, placeholder_text="Enter a number", textvariable=number_var)
        number_entry.pack(pady=10, padx=20)

        def validate_number(new_value):
            # Allow only numbers, negative signs, and decimal points
            pattern = r"^-?\d+\.?\d*$"
            return bool(re.match(pattern, new_value))

        number_var.trace_add("write", validate_number)
        print("add")

    add_button = ctk.CTkButton(master=popup, text="Add Product", command=add_product, fg_color="yellow", text_color="black")
    add_button.pack(pady=10, padx=20)

    selection_button = ctk.CTkButton(master=popup, text="Generate Invoice", command=handle_selection, fg_color="yellow", text_color="black")
    selection_button.pack(pady=10, padx=20)

    # Add a close button
    close_button = ctk.CTkButton(master=popup, text="Close", command=popup.destroy, fg_color="yellow", text_color="black")
    close_button.pack(pady=10, padx=20)

def show_food_frame():
    framec2.pack_forget()
    framec3.pack_forget()
    framec5.pack_forget()
    framec.pack(pady=20, padx=70, fill="both", expand=False, side="left")
    print("food")

def show_drink_frame():
    framec.pack_forget()
    framec3.pack_forget()
    framec5.pack_forget()

    framec2.pack(pady=20, padx=70, fill="both", expand=False, side="left")
    print("drink")

def show_hygene_frame():
        framec.pack_forget()
        framec2.pack_forget()
        framec5.pack_forget()
        framec3.pack(pady=20, padx=70, fill="both", expand=False, side="left")
        print("hygene")

def show_AU_frame():
    framec.pack_forget()
    framec2.pack_forget()
    framec3.pack_forget()
    framec5.pack(pady=20, padx=70, fill="both", expand=False, side="left")
    print("Au")

root = ctk.CTk()
root.title("BillBlitzz")
root.geometry("1280x720")
frameu = ctk.CTkFrame(master=root,width=300, height=200)
frameu.pack( fill="x")

image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\logo.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=frameu, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack(side="left", padx=10)

#icons on button
Fimg = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\food.png")
Fimga = CTkImage(Fimg)
Dimg = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\drink.png")
Dimga = CTkImage(Dimg)
Himg = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\hygene.png")
Himga = CTkImage(Himg)
Eimg = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\electronic.png")
Eimga = CTkImage(Eimg)
Aimg = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\aboutus.png")
Aimga = CTkImage(Aimg)

#Upper frame
label = ctk.CTkLabel(master=frameu, text="Welcome to BillBlitz!", font=("Arial", 35))
label.pack(side="bottom", pady=10)

frame = ctk.CTkFrame(master=root, height=5500)
frame.pack( fill="y", side="left")

#Center Frames
framec = ctk.CTkFrame(master=root, corner_radius=15)
framec.pack(pady=15, padx=65, fill="both", expand=False, side="left")

label = ctk.CTkLabel(master=framec, text="FOOD CATALOG", font=("Franklin Gothic Heavy", 30), text_color="yellow")
label.pack(pady=5)

framec2 = ctk.CTkFrame(master=root, corner_radius=15)
framec2.pack(pady=20, padx=70, fill="both", expand=False, side="left")

label = ctk.CTkLabel(master=framec2, text="DRINK CATALOG", font=("Franklin Gothic Heavy", 30), text_color="yellow")
label.pack(pady=5)

framec3 = ctk.CTkFrame(master=root, corner_radius=15)
framec3.pack(pady=20, padx=70, fill="both", expand=False, side="left")

label = ctk.CTkLabel(master=framec3, text="HYGENE CATALOG", font=("Franklin Gothic Heavy", 30), text_color="yellow")
label.pack(pady=5)

framec5 = ctk.CTkFrame(master=root, corner_radius=15)
framec5.pack(pady=20, padx=70, fill="both", expand=False, side="left")

label = ctk.CTkLabel(master=framec5, text="ABOUT US", font=("Franklin Gothic Heavy", 30), text_color="yellow")
label.pack(pady=1)

label = ctk.CTkLabel(master=frame, text="CATEGORIES", font=("Franklin Gothic Heavy", 20))
label.pack(side="top", pady=10)

#Button on nav bar
Fbutton = ctk.CTkButton(master=frame, command=show_food_frame, text="Food", font=("Arial", 20), text_color="yellow", fg_color="transparent", height=40, width=150, image=Fimga)
Fbutton.pack(side="top", pady=25)
Dbutton = ctk.CTkButton(master=frame, command=show_drink_frame, text="Drinks", font=("Arial", 20), text_color="yellow", fg_color="transparent", height=40, width=150, image=Dimga)
Dbutton.pack(side="top", pady=25)
Hbutton = ctk.CTkButton(master=frame, command=show_hygene_frame, text="Hygene", font=("Arial", 20), text_color="yellow", fg_color="transparent", height=40, width=150, image=Himga)
Hbutton.pack(side="top", pady=25)
Abutton = ctk.CTkButton(master=frame, command=show_AU_frame, text="About us", font=("Arial", 20), text_color="yellow", fg_color="transparent", height=40, width=150, image=Aimga)
Abutton.pack(side="top", pady=25)

#Create cart button
button = ctk.CTkButton(master=frame, text="Buy", command=on_button_click, height=50, fg_color="yellow", text_color="black")
button.pack(side="bottom", pady=25)

#Food Proucts line 1
iuframe= ctk.CTkFrame(master=framec, corner_radius=20)
iuframe.pack(side="top", padx=10, pady=30)
innerframe1= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe1.pack(side="left", padx=20, pady=5)
label = ctk.CTkLabel(master=innerframe1, text="Pizza", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
label = ctk.CTkLabel(master=innerframe1, text="1500", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe1, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()
innerframe2= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe2.pack(side="left", padx=20)
label = ctk.CTkLabel(master=innerframe2, text="Burger", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe2, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()
innerframe3= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe3.pack(side="left", padx=20)
label = ctk.CTkLabel(master=innerframe3, text="Chips", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\chips.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe3, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()
innerframe4= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe4.pack(side="left", padx=20)
label = ctk.CTkLabel(master=innerframe4, text="Cake", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\cake.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe4, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()

#Food Proucts line 2
iuframe= ctk.CTkFrame(master=framec, corner_radius=20)
iuframe.pack(side="bottom", padx=15, pady=10)
innerframe1= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe1.pack(side="left", padx=20, pady=5)
label = ctk.CTkLabel(master=innerframe1, text="Grapes", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\raisin.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe1, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()
innerframe2= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe2.pack(side="left", padx=20)
label = ctk.CTkLabel(master=innerframe2, text="Watermelon", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\watermelon.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe2, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()
innerframe3= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe3.pack(side="left", padx=20)
label = ctk.CTkLabel(master=innerframe3, text="Strawberry", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\fraise.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe3, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()
innerframe4= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe4.pack(side="left", padx=20)
label = ctk.CTkLabel(master=innerframe4, text="Wings", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\wings.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe4, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()



#Drink Proucts line 1
iuframe= ctk.CTkFrame(master=framec2, corner_radius=20)
iuframe.pack(side="top", padx=10, pady=30)
innerframe1= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe1.pack(side="left", padx=20, pady=5)
label = ctk.CTkLabel(master=innerframe1, text="El Vino", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\elvino.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe1, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()
innerframe2= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe2.pack(side="left", padx=20)
label = ctk.CTkLabel(master=innerframe2, text="Jack Daniels", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\jack.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe2, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()
innerframe3= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe3.pack(side="left", padx=20)
label = ctk.CTkLabel(master=innerframe3, text="Wine", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\wine.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe3, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()
innerframe4= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe4.pack(side="left", padx=20)
label = ctk.CTkLabel(master=innerframe4, text="Castel", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\castel.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe4, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()

#Drink Proucts line 2
iuframe= ctk.CTkFrame(master=framec2, corner_radius=20)
iuframe.pack(side="bottom", padx=15, pady=10)
innerframe1= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe1.pack(side="left", padx=20, pady=5)
label = ctk.CTkLabel(master=innerframe1, text="Top", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\top.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe1, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()
innerframe2= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe2.pack(side="left", padx=20)
label = ctk.CTkLabel(master=innerframe2, text="Orange juice", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\orangej.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe2, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()
innerframe3= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe3.pack(side="left", padx=20)
label = ctk.CTkLabel(master=innerframe3, text="Yogourt", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\yogourt.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe3, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()
innerframe4= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe4.pack(side="left", padx=20)
label = ctk.CTkLabel(master=innerframe4, text="Sprite", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\sprite.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe4, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()


#hygene Proucts line 1
iuframe= ctk.CTkFrame(master=framec3, corner_radius=20)
iuframe.pack(side="top", padx=10, pady=30)
innerframe1= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe1.pack(side="left", padx=20, pady=5)
label = ctk.CTkLabel(master=innerframe1, text="Shampoo", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\Shampo.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe1, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()
innerframe2= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe2.pack(side="left", padx=20)
label = ctk.CTkLabel(master=innerframe2, text="Perfume", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\Perfume.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe2, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()
innerframe3= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe3.pack(side="left", padx=20)
label = ctk.CTkLabel(master=innerframe3, text="Soap", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\savon.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe3, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()
innerframe4= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe4.pack(side="left", padx=20)
label = ctk.CTkLabel(master=innerframe4, text="Face oil", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\huile.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe4, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()

#hygene Proucts line 2
iuframe= ctk.CTkFrame(master=framec3, corner_radius=20)
iuframe.pack(side="top", padx=15, pady=10)
innerframe1= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe1.pack(side="left", padx=20, pady=5)
label = ctk.CTkLabel(master=innerframe1, text="Moisturizer", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\moisturizer.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe1, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()
innerframe2= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe2.pack(side="left", padx=20)
label = ctk.CTkLabel(master=innerframe2, text="Tooth Paste", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\tpaste.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe2, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()
innerframe3= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe3.pack(side="left", padx=20)
label = ctk.CTkLabel(master=innerframe3, text="Liquid Soap", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\lSoap.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe3, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()
innerframe4= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe4.pack(side="left", padx=20)
label = ctk.CTkLabel(master=innerframe4, text="Shave gel", font=("Arial", 25), text_color="Yellow")
label.pack(side="bottom")
image = Image.open(r"C:\Users\Ange AK\Desktop\mymarket1\sgel.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe4, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()

#About us Proucts line 1
iuframe= ctk.CTkFrame(master=framec5, corner_radius=20)
iuframe.pack(side="top", padx=20, pady=30)
innerframe1= ctk.CTkFrame(master=iuframe, corner_radius=20,height=220, width=220)
innerframe1.pack(side="bottom", padx=20, pady=15)
image = Image.open(r"C:\Users\DELL\Desktop\about us.png")
img_tk = ImageTk.PhotoImage(image)
label = ctk.CTkLabel(master=innerframe1, image=img_tk, text="")
label.place(relx=0.5, rely=0.5)
label.pack()


root.mainloop()
