#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog
from NLP_text_similarity import text_similarity


# In[3]:


window= Tk()
window.title("NLP_text_similarity")
window.geometry("700x400")



# TAB LAYOUT
tab_control = ttk.Notebook(window,style='lefttab.TNotebook')
 
tab2 = ttk.Frame(tab_control)


# ADD TABS TO NOTEBOOK
tab_control.add(tab2, text=f'{"Home":^20s}')

label1 = Label(tab2, text= 'Text Similarity',padx=5, pady=5)
label1.grid(column=0, row=0)
                
                
                
tab_control.pack(expand=1, fill='both')
 
def openfiles1():
	file1 = tkinter.filedialog.askopenfilename(filetypes=(("Text Files",".txt"),("All files","*")))
	read_text = open(file1,encoding="utf8").read()
	displayed_file1.insert(tk.END,read_text)
                
def openfiles2():
	file1 = tkinter.filedialog.askopenfilename(filetypes=(("Text Files",".txt"),("All files","*")))
	read_text = open(file1,encoding="utf8").read()
	displayed_file2.insert(tk.END,read_text)   
                
                
result=""
def get_text_similarity():
	raw_text1 = displayed_file1.get('1.0',tk.END)
	raw_text2 = displayed_file2.get('1.0',tk.END)

	final_text = text_similarity(raw_text1,raw_text2)
	result = '\nSimilarity is:{}%'.format(final_text)
	tab2_display_text.insert(tk.END,result)

                
                
def clear():
    displayed_file1.delete('1.0',END)
    displayed_file2.delete('1.0',END)
    tab2_display_text.delete('1.0',END)

                
                
#FILE TAB                
l1=Label(tab2,text="Open File1")
l1.grid(row=1,column=0)

displayed_file1 = ScrolledText(tab2,height=10)# Initial was Text(tab2)
displayed_file1.grid(row=2,column=0, columnspan=3,padx=5,pady=3)

l2=Label(tab2,text="Open File2")
l2.grid(row=4,column=0)

displayed_file2 = ScrolledText(tab2,height=10)# Initial was Text(tab2)
displayed_file2.grid(row=5,column=0, columnspan=3,padx=5,pady=3)

# BUTTONS FOR SECOND TAB/FILE READING TAB
b0=Button(tab2,text="Open File 1", width=12,command=openfiles1,bg='#c5cae9')
b0.grid(row=3,column=0,padx=10,pady=10)
                
b1=Button(tab2,text="Open File 2", width=12,command=openfiles2,bg='#c5cae9')
b1.grid(row=6,column=0,padx=10,pady=10)
                
b2=Button(tab2,text="Compare", width=12,command=get_text_similarity,bg='#c5cae9')
b2.grid(row=7,column=0,padx=10,pady=10)

b3=Button(tab2,text="Reset", width=12,command=clear,bg='#c5cae9')
b3.grid(row=7,column=1,padx=10,pady=10)                





                

# Display Screen
tab2_display_text = Text(tab2,height=2)
tab2_display_text.grid(row=8,column=0, columnspan=3,padx=5,pady=5)


window.mainloop()


# In[ ]:




