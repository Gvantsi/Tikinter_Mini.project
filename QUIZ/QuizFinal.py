# import tkinter
# from tkinter import *
# import random
# from tkinter import messagebox
#
# # import tk
# # from PIL import Image, ImageTk
#
# root = tkinter.Tk()
# root.geometry("350x400")
# root.title("ანაკონდა")
# root.configure(background="Lightpink2")
#
#
# def motion(event):
#     print("Mouse position: (%s %s)" % (event.x, event.y))
#     return
#
#
# master = Tk()
# master.title("თამაშის აღწერა")
# rules = "გამოდის სიტყვები შებრუნებული, აუცილებელია შენ ჩაწერო ის სწორად. წარმატებები :) "
# msg = Message(master, text=rules)
# msg.config(bg='red', font=('times', 23, 'italic'))
# msg.bind('<Motion>', motion)
# msg.pack()
#
# # myimage=PhotoImage(file='C:\\Users\\Gvantsa\\PycharmProjects\\untitled1\\img.gif')
# # root.create_image(0,0,anchor=NW, image=myimage)
# # ////მცდელობები მქონდა რომ სურათი ჩამესვა მაგრამ ვერცერთი ხერხით ვერ მოვახერხე////////
#
#
# Answers = ["Each",
#            "love",
#            "something nice",
#            "share",
#            "friends",
#            "canada",
#            "tweet",
#            "programming",
#            "zolanski",
#            "Intellect",
#            "lecturer",
#            "reset",
#            "weird",
#            "social",
#            "beautiful",
#            "electronic",
#            "coding",
#            "structure",
#            "hello",
#            ]
#
# words = ["hcaE",
#          "evol",
#          "ecin gnihtemos",
#          "erahs",
#          "sdneirf",
#          "adanac",
#          "teewt",
#          "gnimmargorp",
#          "iksnaloz",
#          "tcelletnI",
#          "rerutcel",
#          "teser",
#          "driew",
#          "laicos",
#          "lufituaeb",
#          "cinortcele",
#          "gnidoc",
#          "erutcurts",
#          "olleh",
#          ]
#
# num = random.randrange(0, 20, 1)
#
#
# def res():
#     global words, Answers, num
#     num = random.randrange(0, 20, 1)
#     lbl.config(text=words[num])
#     e1.delete(0, END)
#
#
# def default():
#     global words, Answers, num
#     lbl.config(text=words[num])
#
#
# def CheckAns():
#     global words, Answers, num
#     var = e1.get()
#     if var == Answers[num]:
#         messagebox.showinfo("სწორი პასუხია")
#         res()
#     else:
#         messagebox.showerror("ERROR", "ეს არასწორი პასუხია")
#         e1.delete(0, END)
#
#
# root.iconbitmap('C:\\Users\\Gvantsa\\PycharmProjects\\untitled1\\img')
#
# lbl = Label(root, text="გამოიცანი", font=("Verdana", 18), background="black", foreground="white")
# lbl.pack()
#
# ans1 = StringVar()
# e1 = Entry(root, font=("Verdana", 16), textvariable=ans1)
# e1.pack()
#
# btncheck = Button(root, text="შემოწმება", background="Grey", foreground="White", relief=GROOVE, command=CheckAns)
# btncheck.pack()
# btncheck.place(x=50, y=100)
#
# btnreset = Button(root, text="სხვა", background="red", foreground="White", relief=GROOVE, command=res)
# btnreset.pack()
# # btnreset.place(x=300, y=100)
#
#
# button_quit = Button(root, text="გამოსვლა", command=root.quit)
# button_quit.pack()
# btnreset.place(x=200, y=100)
#
# default()
#
# root.mainloop()




