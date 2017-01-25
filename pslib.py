
# Created by Srce Cde

"""
You can also use this file as import whie creating Port Scanner application
I have created this file by keeping in mind that other can also import this
file and use it.
"""

import os
import socket
from queue import Queue
import threading
from tkinter import messagebox
import tkinter as tk

thread_lock = threading.Lock()
START_PORT = 1
END_PORT = 1024
write_result = []
TARGET = str()


def scn_me(parms, all_port_chk):
        global END_PORT
        global TARGET
        ckc = check_con()
        TARGET = parms
        pc = all_port_chk

        if pc == 0:
            END_PORT = 1024
        else:
            END_PORT = 65535

        if TARGET == "" or not ckc:
            if TARGET == "":
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


def check_con():
    hostname = "google.com"
    con = os.system("ping -c 1 " + hostname)
    if con == 0:
        return True
    else:
        return False


class run_scn_thread:

    def run_scan(self):
        global write_result
        global END_PORT
        try:

            ip = socket.gethostbyname(TARGET)

        except socket.gaierror:

            popupmessageErr("Invalid Host Name")

        def scn(port):

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            try:
                s.connect((ip, port))
                s.settimeout(3)
                with thread_lock:

                    print("Port open", port)
                    write_result.append(port)
                    s.close()
            except:
                pass

            f = open('out.txt', 'w')
            f.write(str(write_result))
            f.close
        del write_result[:]

        q = Queue()

        def threader():
            worker = q.get()
            scn(worker)
            q.task_done()

        for x in range(200):
            t = threading.Thread(target=threader)
            t.daemon = True
            t.start()

        for worker in range(START_PORT, END_PORT):
            q.put(worker)
            pass

        q.join()
