import customtkinter
import os
import shutil
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

def sort():
    path = pathEntry.get()
    files = os.listdir(path)
    for file in files:
        filename,extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(path+'/'+extension):
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
        else:
            os.makedirs(path+'/'+extension)
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    
    success = customtkinter.CTkLabel(master=frame, text='Your files have been sorted successfully!', font=('Roboto', 12))
    success.pack(padx=10, pady=5)

root = customtkinter.CTk()
root.geometry('600x600')
root.title('File Sorter')

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=70, padx=60, fill='both', expand=True)

label = customtkinter.CTkLabel(master=frame, text='Flacks File Sorter', font=('Roboto', 24))
label.pack(padx=10, pady=20)

info = customtkinter.CTkLabel(master=frame, text='This sorter will arrange all of your files in folders by extension type.', font=('Roboto', 12))
info.pack(padx=10, pady=5)

pathEntry = customtkinter.CTkEntry(master=frame, placeholder_text='Enter your path', width=200)
pathEntry.pack()

sortButton = customtkinter.CTkButton(master=frame, text='Sort', command=sort)
sortButton.pack(pady=12, padx=10)
root.mainloop()