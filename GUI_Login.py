# Gonna return: IP as "e1", PORT as "e1" and PASSWORD as "e1" (from function "get_entrys()")
# Later gonna make a login ("entry0", returned as "e0")

from tkinter import *

XVALUE = ""  # had to take it out in order to make it work


def GUI_client():
    window = Tk()
    window.configure(bg="#d1d1d1")

    color_bg = "#d1d1d1"
    color_fg = "#000000"
    font = ("Helvetica", 13, "bold")

    def get_entrys():
        global e1, e2, e3
        e1 = entry1.get()
        e2 = entry2.get()
        e3 = entry3.get()
        try:
            e2 = int(e2)
        except:
            e2 = 55555

        if XVALUE:
            window.destroy()
        else:
            LABELING(window, "Chose either 'Wait' or 'Connect'",
                     font, color_bg, color_fg, 5, "flat", 5)

    def LABELING(window, text, font, background, foreground, borderwidth, relief, highlightthickness):
        label = Label(window, text=text, font=(font[0], font[1], font[2]), bg=background, fg=foreground, bd=borderwidth,
                      relief=relief, highlightthickness=highlightthickness)
        label.pack()
        return label

    def b1():
        global XVALUE  # It will work just if "XVALUE" is global to this module (line 6)
        XVALUE = "w"

    def b2():
        global XVALUE
        XVALUE = "c"

    LABELING(window, "Do you want to wait or connect? (If you are waiting there is no need to add your IP)", font,
             color_bg, color_fg, 5, "flat", 5)

    v = IntVar()

    Radiobutton(window, text="Wait", value=1, command=b1, indicatoron=0, padx=10).pack()
    Radiobutton(window, text="Connect", value=2, command=b2, indicatoron=0, padx=10).pack()

    LABELING(window, "", font,
             color_bg, color_fg, 5, "flat", 5)

    # LABELING(window, text, font, background, foreground, borderwidth, relief, highlightthickness)
    LABELING(window, "INSTRUCTIONS: Just delete the placeholder and enter your info", font,
             color_bg, color_fg, 5, "flat", 5)

    entry1 = Entry(window, width=50, borderwidth=5, bg=color_bg, fg=color_fg)
    entry1.pack(ipady=4)  # As it cant be paded from the "Entry" Class it can be paded from the "pack" function
    entry1.insert(0, "IP TO CONNECT")  # To add a default text

    entry2 = Entry(window, width=50, borderwidth=5, bg=color_bg, fg=color_fg)
    entry2.pack(ipady=4)
    entry2.insert(0, "PORT (Default: 55555)")  # To add a default text

    entry3 = Entry(window, width=50, borderwidth=5, bg=color_bg, fg=color_fg)
    entry3.pack(ipady=4)
    entry3.insert(0, "PASSWORD")  # To add a default text

    # Button to get that value from the entry
    button = Button(window, text="DONE", borderwidth=2, bg=color_bg, fg=color_fg, command=get_entrys, font=font)
    button.pack()

    window.mainloop()

    print(e1, e2, e3, XVALUE)
    return e1, e2, e3, XVALUE
