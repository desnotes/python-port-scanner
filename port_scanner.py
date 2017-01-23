
# A port scanner developed by Srce Cde

import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
import socket
import threading
from queue import Queue
from tkinter import messagebox


LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
thread_lock = threading.Lock()

target = str()
res = str()
w_res = []
s_port = 1024


f = open("out.txt", "w").close


class PortScanner(tk.Tk):
    global w_res

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, bitmap="@/home/Desktop/Python/Git Clone/python-port-scanner/icon2.png")

        tk.Tk.wm_title(self, "Mini Port Scanner")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand="True")
        container.grid_rowconfigure(0, weight=0)
        container.grid_columnconfigure(0, weight=0)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=1)
        filemenu.add_command(label="Important Ports", command=lambda: popupmessageInfo("Yet to come!"))
        filemenu.add_command(label="Exit", command=quit, accelerator="Ctrl+Q")



        menubar.add_cascade(label="File", menu=filemenu)

        container.bind_all('<Control-Key-q>', quit)
        container.bind_all('<Control-Key-Q>', quit)

        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (PortScannerUI, ImpPort):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PortScannerUI)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class PortScannerUI(tk.Frame, PortScanner):
    global target
    global res
    # global all_port_chk

    def __init__(self, parent, controller):


        tk.Frame.__init__(self, parent)
        all_port_chk = IntVar()

        self.enter_host = tk.Label(parent, text="Enter Host", font=LARGE_FONT)
        self.enter_host.grid(row=1, column=0, columnspan=1, sticky="w", padx=35, pady=20)
        self.enter_host.bind("<Control-KeyRelease-a>", lambda: ttk.enter_host.select_range(0, END))


        host_entry = tk.Entry(parent, text="get", width=40)
        host_entry.grid(row=1, column=1, sticky="w", padx=0)

        lst_bx = tk.Checkbutton(parent, text="Scan All ports", variable=all_port_chk, offvalue=0, onvalue=1)
        lst_bx.grid(row=2, column=0, sticky="ew", padx=10)

        host_scan = tk.Button(parent, text="Scan", command=lambda: self.scn_me(host_entry.get(), all_port_chk.get()))
        host_scan.grid(row=1, column=3, columnspan=3, sticky="w", padx=0)

        load_data = tk.Button(parent, text="Load Result", command=lambda: l_text())
        load_data.grid(row=3, column=8, sticky="w", padx=0)

        scroll= tk.Scrollbar(parent)
        result_text = tk.Text(parent, width=75, height=15)

        scroll.grid(row=3, rowspan=7, column=2, columnspan=3, sticky="nse", pady=20, padx=1)
        result_text.grid(row=3, column=0, columnspan=6, sticky="e", padx=35, pady=20)

        scroll.config(command=result_text.yview)
        result_text["yscrollcommand"] = scroll.set

        info_label = tk.Label(parent, text="A fast and multi-threaded port scanner\nBy default it scan ports from 1 - 1024", font=NORMAL_FONT)
        info_label.grid(row=2, rowspan=2, column=1, columnspan=2, sticky="ws", padx=10)

        host_entry.focus_set()

        def l_text():
            result_text.delete('1.0', END)
            xL = []

            with open('out.txt') as f:
                f.seek(0)
                fc = f.read(1)
                if not fc:
                    pass
                else:
                    f2 = open('out.txt', 'r').read()
                    fr = f2.replace("[","").replace("]", "")

                    xL = fr.split(", ")
                    ins = []
                    for line in xL:
                        op = "Port {} is open for {}".format(line, target) + "\n"
                        result_text.insert(END, op)
            fc = open('out.txt', 'w').truncate()

    def scn_me(self, parms, all_port_chk):
        global s_port
        global target
        ckc = chkcon()
        target = parms
        pc = all_port_chk

        if pc == 0:
            s_port = 1024
        else:
            s_port = 65535

        if target == "" or not ckc:
            if target == "":
                popupmessageErr("Host name cannot be empty")
            else:
                popupmessageErr("No Internet connection")
        else:
            open("out.txt", "w").close
            rst = run_scn_thread()
            t2 = threading.Thread(target=(rst.run_scan))
            t2.start()


def popupmessageErr(msg):

    tk.messagebox.showerror("Error", msg)


def popupmessageInfo(msg):

    tk.messagebox.showinfo("Error", msg)


def chkcon():
    hostname = "google.com"
    con = os.system("ping -c 1 " + hostname)
    if con == 0:
        return True
    else:
        return False


class run_scn_thread:

    global res

    def run_scan(self):
        global w_res
        global s_port
        print(s_port)
        try:

            ip = socket.gethostbyname(target)
            print(ip)
        except socket.gaierror:
            popupmessageErr("Invalid Host Name")

        def scn(port):

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            try:
                s.connect((ip, port))
                s.settimeout(3)
                with thread_lock:

                    print("Port open", port)
                    w_res.append(port)
                    s.close()
            except:
                pass

            f = open('out.txt', 'w')
            f.write(str(w_res))
            f.close
        del w_res[:]

        q = Queue()

        def threader():
            worker = q.get()
            scn(worker)
            q.task_done()

        for x in range(200):
            t = threading.Thread(target=threader)
            t.daemon = True
            t.start()

        for worker in range(1, s_port):
            q.put(worker)
            pass

        q.join()


class ImpPort(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            pass


ps = PortScanner()
ps.geometry("720x400")
# ps.wm_iconbitmap(bitmap="@/home/Desktop/Python/Git Clone/python-port-scanner/icon2.png")
ps.resizable(0, 0)
ps.mainloop()
