import tkinter as tk
from tkinter import Image, Label, Menu, PhotoImage, Text, ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
from tkinter.constants import END, FALSE, INSERT, LEFT, NONE, RIGHT

main_application=tk.Tk()
main_application.geometry("1200x800")
main_application.title(" vpad text editor")
main_application.wm_iconbitmap("icon.ico")
################################# main menu ############################################

main_menu=tk.Menu()
#file
new_icon=tk.PhotoImage(file="icons2/new.png")
open_icon=tk.PhotoImage(file="icons2/open.png")
save_icon=tk.PhotoImage(file="icons2/save.png")
save_as_icon=tk.PhotoImage(file="icons2/save_as.png")
Exit_icon=tk.PhotoImage(file="icons2/Exit.png")

file=tk.Menu(main_menu,tearoff=False)


#edit
copy_icon=tk.PhotoImage(file="icons2/Copy.png")
paste_icon=tk.PhotoImage(file="icons2/paste.png")
cut_icon=tk.PhotoImage(file="icons2/Cut.png")
clear_all_icon=tk.PhotoImage(file="icons2/Clear_all.png")
find_icon=tk.PhotoImage(file="icons2/find.png")

edit=tk.Menu(main_menu,tearoff=False)


#view
tool_bar_icon=tk.PhotoImage(file="icons2/tool_bar.png")
status_bar_icon=tk.PhotoImage(file="icons2/status_bar.png")

view=tk.Menu(main_menu,tearoff=False)


#color_theme
light_default_icon=tk.PhotoImage(file="icons2/light_default.png")
light_plus_icon=tk.PhotoImage(file="icons2/light_plus.png")
dark_icon=tk.PhotoImage(file="icons2/dark.png")
red_icon=tk.PhotoImage(file="icons2/red.png")
monokai_icon=tk.PhotoImage(file="icons2/monokai.png")
night_blue_icon=tk.PhotoImage(file="icons2/night_blue.png")

color_theme_icon=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
theme_choice=tk.StringVar()
color_dict={
    "light_default":("#000000","#ffffff"),
    "light_plus":("#474747","#e0e0e0"),
    "Dark":("#c4c4c4","#2d2d2d"),
    "Red":("#2d2d2d","#ffe8e8"),
    "Monokai":("#d3b774","#474747"),
    "Night Blue":("#ededed","#6b9dc2")
}
color_theme=tk.Menu(main_menu,tearoff=False)

#cascade
main_menu.add_cascade(label="File",menu=file)
main_menu.add_cascade(label="edit",menu=edit)
main_menu.add_cascade(label="view",menu=view)
main_menu.add_cascade(label="color theme",menu=color_theme)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> end main menu >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

################################# toolbar ############################################
tool_bar=tk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)
#font
font_tuple=tk.font.families()
font_familiy=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_familiy,state="readonly")
font_box["values"]=font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0,column=0,padx=5)

#Size box
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state="readonly")
font_size["values"]=tuple(range(1,81))
font_size.current(8)
font_size.grid(row=0,column=1,padx=5)

#bold button
bold_icon=tk.PhotoImage(file="icons2/bold.png")
bold_button=ttk.Button(tool_bar,image=bold_icon)
bold_button.grid(row=0,column=2,padx=5)

#italic button
italic_icon=tk.PhotoImage(file="icons2/italic.png")
italic_button=tk.Button(tool_bar,image=italic_icon)
italic_button.grid(row=0,column=3,padx=5)

#underline button
underline_icon=tk.PhotoImage(file="icons2/underline.png")
underline_button=ttk.Button(tool_bar,image=underline_icon)
underline_button.grid(row=0,column=4,padx=5)

#font color button
font_color_icon=tk.PhotoImage(file="icons2/font_color.png")
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

#align_left button
align_left_icon=tk.PhotoImage(file="icons2/align_left.png")
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

#align_center button
align_center_icon=tk.PhotoImage(file="icons2/align_center.png")
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)

#align_right button
align_right_icon=tk.PhotoImage(file="icons2/align_right.png")
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> end toolbar >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


################################# text editor ########################################
text_editor=tk.Text(main_application)
scroll_bar=tk.Scrollbar(main_application)
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
scroll_bar.config(command=text_editor.yview)
text_editor.focus_set()
text_editor.config(wrap="word",relief=tk.FLAT)
text_editor.pack(expand=True,fill=tk.BOTH)
text_editor.config(yscrollcommand=scroll_bar.set)

#font style and font size functionality
current_font_family="Arial"
current_font_size=12
def change_font(event=None):
    global current_font_family
    current_font_family=font_familiy.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_fontsize(main_application):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))
font_size.bind("<<ComboboxSelected>>",change_fontsize)        
font_box.bind("<<ComboboxSelected>>",change_font) 
text_editor.configure(font=("Arial",12))   

#bold button functuionality
def change_bold(event=None):
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=="normal":
        text_editor.configure(font=(current_font_family,current_font_size,"bold"))
    if text_property.actual()['weight']=="bold":
        text_editor.configure(font=(current_font_family,current_font_size,"normal"))
bold_button.configure(command=change_bold)             
 #italic button functionality
def change_italic(event=None):
    text_property=tk.font.Font(font=text_editor["font"])
    if text_property.actual()["slant"]=="roman":
        text_editor.configure(font=(current_font_family,current_font_size,"italic"))
    if text_property.actual()["slant"]=="italic":
        text_editor.configure(font=(current_font_family,current_font_size,"normal"))
italic_button.configure(command=change_italic)
#underline button functionality
def change_underline(event=None):
    text_proprerty=tk.font.Font(font=text_editor['font'])
    if text_proprerty.actual()["underline"]==0:
        text_editor.configure(font=(current_font_family,current_font_size,"underline"))
    if text_proprerty.actual()["underline"]==1:
        text_editor.configure(font=(current_font_family,current_font_size,"normal"))
underline_button.configure(command=change_underline) 

#font color functionality
def change_font_color(event=None):
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
font_color_btn.configure(command=change_font_color)    

# align left functionality
def align_left(event=None):
    text_content=text_editor.get(1.0,"end")
    text_editor.tag_config("left",justify=tk.LEFT)
    text_editor.delete(1.0,"end")
    text_editor.insert(tk.INSERT,text_content,"left")
align_left_btn.configure(command=align_left) 

#align right functionality
def align_right(event=None):
    text_content=text_editor.get(1.0,"end")
    text_editor.tag_config("right",justify=tk.RIGHT)
    text_editor.delete(1.0,"end")
    text_editor.insert(tk.INSERT,text_content,"right")
align_right_btn.configure(command=align_right)

#align center functionality
def align_center(event=None):
    text_content=text_editor.get(1.0,"end")
    text_editor.tag_config("center",justify=tk.CENTER)
    text_editor.delete(1.0,"end")
    text_editor.insert(tk.INSERT,text_content,"center")
align_center_btn.configure(command=align_center)    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> end text editor >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


################################# main status bar #####################################
status_bar=ttk.Label(main_application,text='Status bar')
status_bar.pack(side=tk.BOTTOM)

text_changed=False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0,"end-1c").split())
        characters=len(text_editor.get(1.0,"end-1c"))
        status_bar.config(text=f"characters:{characters} words:{words}")
    text_editor.edit_modified(False)    
text_editor.bind("<<Modified>>",changed)    

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> end status bar >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


################################# main menu functionality ##############################
#add file comond
#variable
url=""
#new file
def new_file(event=None):
    global url
    url=""
    text_editor.delete(1.0,tk.END)
file.add_command(label="new",image=new_icon,compound=LEFT,accelerator="ctrl+n",command=new_file)

#open file
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select file",filetypes=(('Text files','*.txt'),('All files','*.*')))
    try:
        with open(url,"r") as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return 
    main_application.title(os.path.basename(url))               
file.add_command(label="open",image=open_icon,compound=LEFT,accelerator="ctrl+o",command=open_file)

#save file
def save_file(event=None):
    global url
    content=text_editor.get(1.0,tk.END)
    try:
        if url:
            with open(url,"w",encoding="utf-8") as wf:
                wf.write(content)
        else:
            url=filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=(("Text file","*.txt"),("All files","*.*")))
            url.write(content)
            url.close() 
    except:
        return               
file.add_command(label="save",image=save_icon,compound=LEFT,accelerator="ctrl+s",command=save_file)

#save_as file
def save_as_file(evet=None):
    global url
    content=text_editor.get(1.0,tk.END)
    url=filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetype=(("Text file","*.txt"),("All file","*.*")))
    url.write(content)
    url.close()
file.add_command(label="save as",image=save_as_icon,compound=LEFT,accelerator="ctrl+a",command=save_as_file)

#exit functionality
def exit_func(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel("Warning","Do you want to save the file")
            content=text_editor.get(1.0,tk.END)
            if mbox is True:
                if url:
                    with open(url,"w", encoding="utf-8") as wf:
                        wf.write(content)
                        main_application.destroy()
                else:
                    url=filedialog.asksaveasfile(mode="w",defaultextension="*.txt",filetype=(("Text file","*.txt"),("All file","*.*"))) 
                    url.write(content)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return                               

file.add_command(label="Exit",image=Exit_icon,compound=LEFT,accelerator="ctrl+e",command=exit_func)

#add edit commond
edit.add_command(label="Copy",image=copy_icon,compound=LEFT,accelerator="ctrl+c",command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste",image=paste_icon,compound=LEFT,accelerator="ctrl+v",command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut",image=cut_icon,compound=LEFT,accelerator="ctrl+x",command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="Clear all",image=clear_all_icon,compound=LEFT,accelerator="ctrl+l",command=lambda:text_editor.delete(1.0,tk.END))

def find_func(event=None):
    def find_():
        word=find_input.get()
        text_editor.tag_remove("matches",1.0,tk.END)
        if word:
            start_pos="1.0"
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                text_editor.tag_add("matches",start_pos,end_pos)
                start_pos=end_pos
                text_editor.tag_config("matches",foreground="red",background="yellow")
    def replace():
        word=find_input.get()
        replace_txt=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_txt)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)
    find_dialog=tk.Toplevel()
    find_dialog.title("find")
    find_dialog.geometry("450x250+500+200")
    find_dialog.resizable(0,0)
   #frame 
    find_frame=tk.LabelFrame(find_dialog)
    find_frame.pack(pady=20)
    #label
    text_find_label=tk.Label(find_frame,text="Find")
    text_replace_label=tk.Label(find_frame,text="replace")
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)
    #entry
    find_input=tk.Entry(find_frame,width=30)
    replace_input=tk.Entry(find_frame,width=30)
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)

    #button
    find_btn=tk.Button(find_frame,text="Find",command=find_)
    replace_btn=tk.Button(find_frame,text="Replace",command=replace)
    find_btn.grid(row=2,column=0,padx=8,pady=4)
    replace_btn.grid(row=2,column=1,pady=4,padx=8)
    
    find_dialog.mainloop()

edit.add_command(label="Find",image=find_icon,compound=LEFT,accelerator="ctrl+f",command=find_func)

#add view check button
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)
show_statusbar=tk.BooleanVar()
show_toolbar.set(True)
def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True                
view.add_checkbutton(label="toolbar",image=tool_bar_icon,variable=show_toolbar,compound=LEFT,command=hide_toolbar)
view.add_checkbutton(label="statusbar",image=status_bar_icon,variable=show_statusbar,compound=LEFT,command=hide_statusbar)

#add colortheme radiobutton
def change_theme():
    chossen_theme=theme_choice.get()
    color_tuple=color_dict.get(chossen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.configure(background=bg_color,foreground=fg_color)
count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_theme_icon[count],variable=theme_choice,compound=LEFT,command=change_theme)
    count=count+1
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> end main menu functionality>>>>>>>>>>>>>>>>>>>>>>>>>>>
main_application.config(menu=main_menu)
main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Control-a>",save_as_file)
main_application.bind("<Control-e>",exit)
main_application.bind("<Control-f>",find_func)
main_application.mainloop()