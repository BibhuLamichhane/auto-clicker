# declarations
from tkinter import *
import tkinter
import tkinter as tk
import time
from pynput.keyboard import Key, KeyCode, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from tkinter import ttk
from ctypes import windll, Structure, c_ulong, byref


keyboard = KeyboardController()
mouse = MouseController()
row_counter = 140
c = 1
commands = []
pauseTime = []
xlist = []
ylist = []
customList = []
typeorprint = []


def removedata():
    selectedop = mylist.curselection()[0]
    mylist.delete(selectedop)
    if commands[selectedop]=="lc":
         pauseTime.pop(selectedop)
         commands.pop(selectedop)
         xlist.pop(selectedop)
         ylist.pop(selectedop)
    elif commands[selectedop]=="rc":
        pauseTime.pop(selectedop)
        commands.pop(selectedop)
        xlist.pop(selectedop)
        ylist.pop(selectedop)
    elif commands[selectedop]=="custom":
        pauseTime.pop(selectedop)
        commands.pop(selectedop)
        customList.pop(selectedop)
        typeorprint.pop(selectedop)
    else:
        pauseTime.pop(selectedop)
        commands.pop(selectedop)


class ValueAssign:
    def lc(self):

        global v
        if v.get() == 1:
            return v

    def rc(self):
        global v
        if v.get() == 2:
            return v

    def lettera(self):
        global v
        if v.get() == 3:
            return v

    def letterb(self):
        global v
        if v.get() == 4:
            return v

    def letterc(self):
        global v
        if v.get() == 5:
            return v

    def letterd(self):
        global v
        if v.get() == 6:
            return v

    def lettere(self):
        global v
        if v.get() == 7:
            return v

    def letterf(self):
        global v
        if v.get() == 8:
            return v

    def letterg(self):
        global v
        if v.get() == 9:
            return v

    def letterh(self):
        global v
        if v.get() == 10:
            return v

    def letteri(self):
        global v
        if v.get() == 11:
            return v

    def letterj(self):
        global v
        if v.get() == 12:
            return v

    def letterk(self):
        global v
        if v.get() == 13:
            return v

    def letterl(self):
        global v
        if v.get() == 14:
            return v

    def letterm(self):
        global v
        if v.get() == 15:
            return v

    def lettern(self):
        global v
        if v.get() == 16:
            return v

    def lettero(self):
        global v
        if v.get() == 17:
            return v

    def letterp(self):
        global v
        if v.get() == 18:
            return v

    def letterq(self):
        global v
        if v.get() == 19:
            return v

    def letterr(self):
        global v
        if v.get() == 20:
            return v

    def letters(self):
        global v
        if v.get() == 21:
            return v

    def lettert(self):
        global v
        if v.get() == 22:
            return v

    def letteru(self):
        global v
        if v.get() == 23:
            return v

    def letterv(self):
        global v
        if v.get() == 24:
            return v

    def letterw(self):
        global v
        if v.get() == 25:
            return v

    def letterx(self):
        global v
        if v.get() == 26:
            return v

    def lettery(self):
        global v
        if v.get() == 27:
            return v

    def letterz(self):
        global v
        if v.get() == 28:
            return v

    def num0(self):
        global v
        if v.get() == 29:
            return v

    def num1(self):
        global v
        if v.get() == 30:
            return v

    def num2(self):
        global v
        if v.get() == 31:
            return v

    def num3(self):
        global v
        if v.get() == 32:
            return v

    def num4(self):
        global v
        if v.get() == 33:
            return v

    def num5(self):
        global v
        if v.get() == 34:
            return v

    def num6(self):
        global v
        if v.get() == 35:
            return v

    def num7(self):
        global v
        if v.get() == 36:
            return v

    def num8(self):
        global v
        if v.get() == 37:
            return v

    def num9(self):
        global v
        if v.get() == 38:
            return v

    def sym1(self):
        global v
        if v.get() == 39:
            return v

    def sym2(self):
        global v
        if v.get() == 40:
            return v

    def sym3(self):
        global v
        if v.get() == 41:
            return v

    def sym4(self):
        global v
        if v.get() == 42:
            return v

    def sym5(self):
        global v
        if v.get() == 43:
            return v

    def sym6(self):
        global v
        if v.get() == 44:
            return v

    def sym7(self):
        global v
        if v.get() == 45:
            return v

    def sym8(self):
        global v
        if v.get() == 46:
            return v

    def sym9(self):
        global v
        if v.get() == 47:
            return v

    def sym10(self):
        global v
        if v.get() == 48:
            return v

    def sym11(self):
        global v
        if v.get() == 49:
            return v

    def sym12(self):
        global v
        if v.get() == 50:
            return v

    def sym13(self):
        global v
        if v.get() == 51:
            return v

    def sym14(self):
        global v
        if v.get() == 52:
            return v

    def sym15(self):
        global v
        if v.get() == 53:
            return v

    def sym16(self):
        global v
        if v.get() == 54:
            return v

    def sym17(self):
        global v
        if v.get() == 55:
            return v

    def sym18(self):
        global v
        if v.get() == 56:
            return v

    def sym19(self):
        global v
        if v.get() == 57:
            return v

    def sym20(self):
        global v
        if v.get() == 58:
            return v

    def sym21(self):
        global v
        if v.get() == 59:
            return v

    def sym22(self):
        global v
        if v.get() == 60:
            return v

    def sym23(self):
        global v
        if v.get() == 61:
            return v

    def sym24(self):
        global v
        if v.get() == 62:
            return v

    def sym25(self):
        global v
        if v.get() == 63:
            return v

    def sym26(self):
        global v
        if v.get() == 64:
            return v

    def sym27(self):
        global v
        if v.get() == 65:
            return v

    def sym28(self):
        global v
        if v.get() == 66:
            return v

    def sym29(self):
        global v
        if v.get() == 67:
            return v

    def sym30(self):
        global v
        if v.get() == 68:
            return v

    def esc(self):
        global v
        if v.get() == 69:
            return v

    def tab(self):
        global v
        if v.get() == 70:
            return v

    def winkey(self):
        global v
        if v.get() == 71:
            return v

    def space(self):
        global v
        if v.get() == 72:
            return v

    def enter(self):
        global v
        if v.get() == 73:
            return v

    def backspace(self):
        global v
        if v.get() == 74:
            return v

    def up(self):
        global v
        if v.get() == 75:
            return v

    def down(self):
        global v
        if v.get() == 76:
            return v

    def left(self):
        global v
        if v.get() == 77:
            return v

    def right(self):
        global v
        if v.get() == 78:
            return v

    def delete(self):
        global v
        if v.get() == 79:
            return v

    def f1(self):
        global v
        if v.get() == 80:
            return v

    def f2(self):
        global v
        if v.get() == 81:
            return v

    def f3(self):
        global v
        if v.get() == 82:
            return v

    def f4(self):
        global v
        if v.get() == 83:
            return v

    def f5(self):
        global v
        if v.get() == 84:
            return v

    def f6(self):
        global v
        if v.get() == 85:
            return v

    def f7(self):
        global v
        if v.get() == 86:
            return v

    def f8(self):
        global v
        if v.get() == 87:
            return v

    def f9(self):
        global v
        if v.get() == 88:
            return v

    def f10(self):
        global v
        if v.get() == 89:
            return v

    def f11(self):
        global v
        if v.get() == 90:
            return v

    def f12(self):
        global v
        if v.get() == 91:
            return v

    def letterbyletter(self):
        global v
        if v.get()==92:
            return v

    def atonce(self):
        global v
        if v.get()==93:
            return v


def main_outputinstruction():
    global c
    a = customText.get()
    selectedop = mylist.curselection()
    print(selectedop)

    if v.get() == 1:
        o = float(pause_time.get())
        x = int(X1.get())
        y = int(Y1.get())
        commands.append("lc")
        pauseTime.append(o)
        xlist.append(x)
        ylist.append(y)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press left click and pause for {o} seconds at {x} , {y}")

    if v.get() == 2:
        o = float(pause_time.get())
        x = int(X1.get())
        y = int(Y1.get())
        commands.append("rc")
        pauseTime.append(o)
        xlist.append(x)
        ylist.append(y)
        customList.append(" ")
        typeorprint.append((" "))
        for line in range(1):
            mylist.insert(END, f"Press right click and pause for {o} seconds at {x} , {y}")
    if v.get() == 3:
        o = float(pause_time.get())
        commands.append("a")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'a' and pause for {o} seconds")
    if v.get() == 4:
        o = float(pause_time.get())
        commands.append("b")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'b' and pause for {o} seconds")
    if v.get() == 5:
        o = float(pause_time.get())
        commands.append("c")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'c' and pause for {o} seconds")
    if v.get() == 6:
        o = float(pause_time.get())
        commands.append("d")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'd' and pause for {o} seconds")
    if v.get() == 7:
        o = float(pause_time.get())
        commands.append("e")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'e' and pause for {o} seconds")
    if v.get() == 8:
        o = float(pause_time.get())
        commands.append("f")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'f' and pause for {o} seconds")
    if v.get() == 9:
        o = float(pause_time.get())
        commands.append("g")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'g' and pause for {o} seconds")
    if v.get() == 10:
        o = float(pause_time.get())
        commands.append("h")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'h' and pause for {o} seconds")
    if v.get() == 11:
        o = float(pause_time.get())
        commands.append("i")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'i' and pause for {o} seconds")
    if v.get() == 12:
        o = float(pause_time.get())
        commands.append("j")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'j' and pause for {o} seconds")
    if v.get() == 13:
        o = float(pause_time.get())
        commands.append("k")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'k' and pause for {o} seconds")
    if v.get() == 14:
        o = float(pause_time.get())
        commands.append("l")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'l' and pause for {o} seconds")
    if v.get() == 15:
        o = float(pause_time.get())
        commands.append("m")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'm' and pause for {o} seconds")
    if v.get() == 16:
        o = float(pause_time.get())
        commands.append("n")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'n' and pause for {o} seconds")
    if v.get() == 17:
        o = float(pause_time.get())
        commands.append("o")
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        pauseTime.append(o)
        for line in range(1):
            mylist.insert(END, f"Press 'o' and pause for {o} seconds")
    if v.get() == 18:
        o = float(pause_time.get())
        commands.append("p")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'p' and pause for {o} seconds")
    if v.get() == 19:
        o = float(pause_time.get())
        commands.append("q")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'q' and pause for {o} seconds")
    if v.get() == 20:
        o = float(pause_time.get())
        commands.append("r")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'r' and pause for {o} seconds")
    if v.get() == 21:
        o = float(pause_time.get())
        commands.append("s")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 's' and pause for {o} seconds")
    if v.get() == 22:
        o = float(pause_time.get())
        commands.append("t")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 't' and pause for {o} seconds")
    if v.get() == 23:
        o = float(pause_time.get())
        commands.append("u")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'u' and pause for {o} seconds")
    if v.get() == 24:
        o = float(pause_time.get())
        commands.append("v")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'v' and pause for {o} seconds")
    if v.get() == 25:
        o = float(pause_time.get())
        commands.append("w")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'w' and pause for {o} seconds")
    if v.get() == 26:
        o = float(pause_time.get())
        commands.append("x")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'x' and pause for {o} seconds")
    if v.get() == 27:
        o = float(pause_time.get())
        commands.append("y")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'y' and pause for {o} seconds")
    if v.get() == 28:
        o = float(pause_time.get())
        commands.append("z")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'z' and pause for {o} seconds")
    if v.get() == 29:
        o = float(pause_time.get())
        commands.append("0")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '0' and pause for {o} seconds")
    if v.get() == 30:
        o = float(pause_time.get())
        commands.append("1")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '1' and pause for {o} seconds")
    if v.get() == 31:
        o = float(pause_time.get())
        commands.append("2")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '2' and pause for {o} seconds")
    if v.get() == 32:
        o = float(pause_time.get())
        commands.append("3")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '3' and pause for {o} seconds")
    if v.get() == 33:
        o = float(pause_time.get())
        commands.append("4")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '4' and pause for {o} seconds")
    if v.get() == 34:
        o = float(pause_time.get())
        commands.append("5")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '5' and pause for {o} seconds")
    if v.get() == 35:
        o = float(pause_time.get())
        commands.append("6")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '6' and pause for {o} seconds")
    if v.get() == 36:
        o = float(pause_time.get())
        commands.append("7")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '7' and pause for {o} seconds")
    if v.get() == 37:
        o = float(pause_time.get())
        commands.append("8")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '8' and pause for {o} seconds")
    if v.get() == 38:
        o = float(pause_time.get())
        pauseTime.append(o)
        commands.append("9")
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '9' and pause for {o} seconds")
    if v.get() == 39:
        o = float(pause_time.get())
        commands.append("(")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '(' and pause for {o} seconds")
    if v.get() == 40:
        o = float(pause_time.get())
        commands.append(")")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press ')' and pause for {o} seconds")
    if v.get() == 41:
        o = float(pause_time.get())
        commands.append("[")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '[' and pause for {o} seconds")
    if v.get() == 42:
        o = float(pause_time.get())
        commands.append("]")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press ']' and pause for {o} seconds")
    if v.get() == 43:
        o = float(pause_time.get())
        commands.append("{")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '{{' and pause for {o} seconds")
    if v.get() == 44:
        o = float(pause_time.get())
        commands.append("}")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '}}' and pause for {o} seconds")
    if v.get() == 45:
        o = float(pause_time.get())
        commands.append("<")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '<' and pause for {o} seconds")
    if v.get() == 46:
        o = float(pause_time.get())
        commands.append(">")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '>' and pause for {o} seconds")
    if v.get() == 47:
        o = float(pause_time.get())
        commands.append("!")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '!' and pause for {o} seconds")
    if v.get() == 48:
        o = float(pause_time.get())
        commands.append("@")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '@' and pause for {o} seconds")
    if v.get() == 49:
        o = float(pause_time.get())
        commands.append("#")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '#' and pause for {o} seconds")
    if v.get() == 50:
        o = float(pause_time.get())
        commands.append("$")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '$' and pause for {o} seconds")
    if v.get() == 51:
        o = float(pause_time.get())
        commands.append("%")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '%' and pause for {o} seconds")
    if v.get() == 52:
        o = float(pause_time.get())
        commands.append("^")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '^' and pause for {o} seconds")
    if v.get() == 53:
        o = float(pause_time.get())
        commands.append("&")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '&' and pause for {o} seconds")
    if v.get() == 54:
        o = float(pause_time.get())
        commands.append("*")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '*' and pause for {o} seconds")
    if v.get() == 55:
        o = float(pause_time.get())
        commands.append("-")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '-' and pause for {o} seconds")
    if v.get() == 56:
        o = float(pause_time.get())
        commands.append("_")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '_' and pause for {o} seconds")
    if v.get() == 57:
        o = float(pause_time.get())
        commands.append("=")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '=' and pause for {o} seconds")
    if v.get() == 58:
        o = float(pause_time.get())
        commands.append('+')
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '+' and pause for {o} seconds")
    if v.get() == 59:
        o = float(pause_time.get())
        commands.append(";")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press ';' and pause for {o} seconds")
    if v.get() == 60:
        o = float(pause_time.get())
        commands.append(":")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press ':' and pause for {o} seconds")
    if v.get() == 61:
        o = float(pause_time.get())
        commands.append("'")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, 'Press' + ' " ' + " ' " + ' " ' + "and pause for " + str(o) + " seconds")
    if v.get() == 62:
        o = float(pause_time.get())
        commands.append('"')
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, 'Press' + " ' " + ' " ' + " ' " + "and pause for " + str(o) + " seconds")
    if v.get() == 63:
        o = float(pause_time.get())
        commands.append("\\")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '\\' and pause for {o} seconds")
    if v.get() == 64:
        o = float(pause_time.get())
        commands.append("|")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '|' and pause for {o} seconds")
    if v.get() == 65:
        o = float(pause_time.get())
        commands.append(",")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press ',' and pause for {o} seconds")
    if v.get() == 66:
        o = float(pause_time.get())
        commands.append(".")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '.' and pause for {o} seconds")
    if v.get() == 67:
        o = float(pause_time.get())
        commands.append("/")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '/' and pause for {o} seconds")
    if v.get() == 68:
        o = float(pause_time.get())
        commands.append("?")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press '?' and pause for {o} seconds")
    if v.get() == 69:
        o = float(pause_time.get())
        commands.append("esc")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'ESC' and pause for {o} seconds")
    if v.get() == 70:
        o = float(pause_time.get())
        commands.append("Tab")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'Tab' and pause for {o} seconds")
    if v.get() == 71:
        o = float(pause_time.get())
        commands.append("Winkey")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'Windows Key' and pause for {o} seconds")
    if v.get() == 72:
        o = float(pause_time.get())
        commands.append("Space")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'Space' and pause for {o} seconds")
    if v.get() == 73:
        o = float(pause_time.get())
        commands.append("Enter")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'Enter' and pause for {o} seconds")
    if v.get() == 74:
        o = float(pause_time.get())
        commands.append("Backspace")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'Backspace' and pause for {o} seconds")
    if v.get() == 75:
        o = float(pause_time.get())
        commands.append("Up")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'Upwards Key' and pause for {o} seconds")
    if v.get() == 76:
        o = float(pause_time.get())
        commands.append("Down")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'Downwards Key' and pause for {o} seconds")
    if v.get() == 77:
        o = float(pause_time.get())
        commands.append("Left")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'Left Key' and pause for {o} seconds")
    if v.get() == 78:
        o = float(pause_time.get())
        commands.append("Right")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'Right Key' and pause for {o} seconds")
    if v.get() == 79:
        o = float(pause_time.get())
        commands.append("Delete")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'Delete' and pause for {o} seconds")
    if v.get() == 80:
        o = float(pause_time.get())
        commands.append("f1")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'F1' and pause for {o} seconds")
    if v.get() == 81:
        o = float(pause_time.get())
        commands.append("f2")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'F2' and pause for {o} seconds")
    if v.get() == 82:
        o = float(pause_time.get())
        commands.append("f3")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'F3' and pause for {o} seconds")
    if v.get() == 83:
        o = float(pause_time.get())
        commands.append("f4")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'F4' and pause for {o} seconds")
    if v.get() == 84:
        o = float(pause_time.get())
        commands.append("f5")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'F5' and pause for {o} seconds")
    if v.get() == 85:
        o = float(pause_time.get())
        commands.append("f6")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'F6' and pause for {o} seconds")
    if v.get() == 86:
        o = float(pause_time.get())
        commands.append("f7")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'F7' and pause for {o} seconds")
    if v.get() == 87:
        o = float(pause_time.get())
        commands.append("f8")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'F8' and pause for {o} seconds")
    if v.get() == 88:
        o = float(pause_time.get())
        commands.append("f9")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'F9' and pause for {o} seconds")
    if v.get() == 89:
        o = float(pause_time.get())
        commands.append("f10")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'F10' and pause for {o} seconds")
    if v.get() == 90:
        o = float(pause_time.get())
        commands.append("f11")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'F11' and pause for {o} seconds")
    if v.get() == 91:
        o = float(pause_time.get())
        commands.append("f12")
        pauseTime.append(o)
        xlist.append(0)
        ylist.append(0)
        customList.append(' ')
        typeorprint.append((' '))
        for line in range(1):
            mylist.insert(END, f"Press 'F12' and pause for {o} seconds")
    if v.get()==92:
        o = float(pause_time.get())
        for line in range(1):
            mylist.insert(END, f"Type '{a}' and pause for {o} seconds")
        pauseTime.append(o)
        commands.append("custom")
        xlist.append(0)
        ylist.append(0)
        customList.append(a)
        typeorprint.append("type")
    if v.get()==93:
        o = float(pause_time.get())
        for line in range(1):
            mylist.insert(END, f"Type '{a}' and pause for {o} seconds")
        pauseTime.append(o)
        commands.append("custom")
        customList.append(a)
        typeorprint.append("print")
        xlist.append(0)
        ylist.append(0)
    c = c + 1
    mylist.place(x=0, y=180)
    return pauseTime, commands


def mostimppart(event=''):
    global repeat
    repeat = int(Repeat.get())
    a = len(pauseTime)
    pauseTimecounter = len(pauseTime)
    for i in range(repeat):
        for j in range(pauseTimecounter):
            if commands[j] == "a":
                keyboard.press("a")
                keyboard.release("a")
                time.sleep(pauseTime[j])

            elif commands[j] == "b":
                keyboard.press("b")
                keyboard.release("b")
                time.sleep(pauseTime[j])

            elif commands[j] == "c":
                keyboard.press("c")
                keyboard.release("c")

                time.sleep(pauseTime[j])

            elif commands[j] == "d":
                keyboard.press("d")
                keyboard.release("d")

                time.sleep(pauseTime[j])

            elif commands[j] == "e":
                keyboard.press("e")
                keyboard.release("e")

                time.sleep(pauseTime[j])

            elif commands[j] == "f":
                keyboard.press("f")
                keyboard.release("f")

                time.sleep(pauseTime[j])

            elif commands[j] == "g":
                keyboard.press("g")
                keyboard.release("g")

                time.sleep(pauseTime[j])

            elif commands[j] == "h":
                keyboard.press("h")
                keyboard.release("h")

                time.sleep(pauseTime[j])

            elif commands[j] == "i":
                keyboard.press("i")
                keyboard.release("i")

                time.sleep(pauseTime[j])

            elif commands[j] == "j":
                keyboard.press("j")
                keyboard.release("j")

                time.sleep(pauseTime[j])

            elif commands[j] == "k":
                keyboard.press("k")
                keyboard.release("k")

                time.sleep(pauseTime[j])

            elif commands[j] == "l":
                keyboard.press("l")
                keyboard.release("l")

                time.sleep(pauseTime[j])

            elif commands[j] == "m":
                keyboard.press("m")
                keyboard.release("m")

                time.sleep(pauseTime[j])

            elif commands[j] == "n":
                keyboard.press("n")
                keyboard.release("n")

                time.sleep(pauseTime[j])

            elif commands[j] == "o":
                keyboard.press("o")
                keyboard.release("o")

                time.sleep(pauseTime[j])

            elif commands[j] == "p":
                keyboard.press("p")
                keyboard.release("p")

                time.sleep(pauseTime[j])

            elif commands[j] == "q":
                keyboard.press("q")
                keyboard.release("q")

                time.sleep(pauseTime[j])

            elif commands[j] == "r":
                keyboard.press("r")
                keyboard.release("r")

                time.sleep(pauseTime[j])

            elif commands[j] == "s":
                keyboard.press("s")
                keyboard.release("s")

                time.sleep(pauseTime[j])

            elif commands[j] == "t":
                keyboard.press("t")
                keyboard.release("t")

                time.sleep(pauseTime[j])

            elif commands[j] == "u":
                keyboard.press("u")
                keyboard.release("u")

                time.sleep(pauseTime[j])

            elif commands[j] == "v":
                keyboard.press("v")
                keyboard.release("v")
                time.sleep(pauseTime[j])

            elif commands[j] == "w":
                keyboard.press("w")
                keyboard.release("w")
                time.sleep(pauseTime[j])

            elif commands[j] == "x":
                keyboard.press("x")
                keyboard.release("x")
                time.sleep(pauseTime[j])

            elif commands[j] == "y":
                keyboard.press("y")
                keyboard.release("y")
                time.sleep(pauseTime[j])

            elif commands[j] == "z":
                keyboard.press("z")
                keyboard.release("z")
                time.sleep(pauseTime[j])

            elif commands[j] == "0":
                keyboard.press("0")
                keyboard.release("0")
                time.sleep(pauseTime[j])

            elif commands[j] == "1":
                keyboard.press("1")
                keyboard.release("1")
                time.sleep(pauseTime[j])

            elif commands[j] == "2":
                keyboard.press("2")
                keyboard.release("2")
                time.sleep(pauseTime[j])

            elif commands[j] == "3":
                keyboard.press("3")
                keyboard.release("3")
                time.sleep(pauseTime[j])

            elif commands[j] == "4":
                keyboard.press("4")
                keyboard.release("4")
                time.sleep(pauseTime[j])

            elif commands[j] == "5":
                keyboard.press("5")
                keyboard.release("5")
                time.sleep(pauseTime[j])

            elif commands[j] == "6":
                keyboard.press("6")
                keyboard.release("6")
                time.sleep(pauseTime[j])

            elif commands[j] == "7":
                keyboard.press("7")
                keyboard.release("7")
                time.sleep(pauseTime[j])

            elif commands[j] == "8":
                keyboard.press("8")
                keyboard.release("8")
                time.sleep(pauseTime[j])

            elif commands[j] == "9":
                keyboard.press("9")
                keyboard.release("9")
                time.sleep(pauseTime[j])

            elif commands[j] == "(":
                keyboard.press("(")
                keyboard.release("(")
                time.sleep(pauseTime[j])

            elif commands[j] == ")":
                keyboard.press(")")
                keyboard.release(")")
                time.sleep(pauseTime[j])

            elif commands[j] == "[":
                keyboard.press("[")
                keyboard.release("[")
                time.sleep(pauseTime[j])

            elif commands[j] == "]":
                keyboard.press("]")
                keyboard.release("]")
                time.sleep(pauseTime[j])

            elif commands[j] == "{":
                keyboard.press("{")
                keyboard.release("{")
                time.sleep(pauseTime[j])

            elif commands[j] == "}":
                keyboard.press("}")
                keyboard.release("}")
                time.sleep(pauseTime[j])

            elif commands[j] == "<":
                keyboard.press("<")
                keyboard.release("<")
                time.sleep(pauseTime[j])

            elif commands[j] == ">":
                keyboard.press(">")
                keyboard.release(">")
                time.sleep(pauseTime[j])

            elif commands[j] == "!":
                keyboard.press("!")
                keyboard.release("!")
                time.sleep(pauseTime[j])

            elif commands[j] == "@":
                keyboard.press("@")
                keyboard.release("@")
                time.sleep(pauseTime[j])

            elif commands[j] == "#":
                keyboard.press("#")
                keyboard.release("#")
                time.sleep(pauseTime[j])

            elif commands[j] == "$":
                keyboard.press("$")
                keyboard.release("$")
                time.sleep(pauseTime[j])

            elif commands[j] == "%":
                keyboard.press("%")
                keyboard.release("%")
                time.sleep(pauseTime[j])

            elif commands[j] == "^":
                keyboard.press("^")
                keyboard.release("^")
                time.sleep(pauseTime[j])

            elif commands[j] == "&":
                keyboard.press("&")
                keyboard.release("&")
                time.sleep(pauseTime[j])

            elif commands[j] == "*":
                keyboard.press("*")
                keyboard.release("*")
                time.sleep(pauseTime[j])

            elif commands[j] == "-":
                keyboard.press("-")
                keyboard.release("-")
                time.sleep(pauseTime[j])

            elif commands[j] == "_":
                keyboard.press("_")
                keyboard.release("_")
                time.sleep(pauseTime[j])

            elif commands[j] == "=":
                keyboard.press("=")
                keyboard.release("=")
                time.sleep(pauseTime[j])

            elif commands[j] == "+":
                keyboard.press("+")
                keyboard.release("+")
                time.sleep(pauseTime[j])

            elif commands[j] == ";":
                keyboard.press(";")
                keyboard.release(";")
                time.sleep(pauseTime[j])

            elif commands[j] == ":":
                keyboard.press(":")
                keyboard.release(":")
                time.sleep(pauseTime[j])

            elif commands[j] == "'":
                keyboard.press("'")
                keyboard.release("'")
                time.sleep(pauseTime[j])

            elif commands[j] == '"':
                keyboard.press('"')
                keyboard.release('"')
                time.sleep(pauseTime[j])

            elif commands[j] == "\\":
                keyboard.press("\\")
                keyboard.release("\\")
                time.sleep(pauseTime[j])

            elif commands[j] == "|":
                keyboard.press("|")
                keyboard.release("|")
                time.sleep(pauseTime[j])

            elif commands[j] == ",":
                keyboard.press(",")
                keyboard.release(",")
                time.sleep(pauseTime[j])

            elif commands[j] == ".":
                keyboard.press(".")
                keyboard.release(".")
                time.sleep(pauseTime[j])

            elif commands[j] == "/":
                keyboard.press("/")
                keyboard.release("/")
                time.sleep(pauseTime[j])

            elif commands[j] == "?":
                keyboard.press("?")
                keyboard.release("?")
                time.sleep(pauseTime[j])

            elif commands[j] == "esc":
                keyboard.press(Key.esc)
                keyboard.release(Key.esc)
                time.sleep(pauseTime[j])

            elif commands[j] == "Tab":
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
                time.sleep(pauseTime[j])

            elif commands[j] == "Winkey":
                keyboard.press(Key.cmd_l)
                keyboard.release(Key.cmd_l)
                time.sleep(pauseTime[j])

            elif commands[j] == "Space":
                keyboard.press(Key.space)
                keyboard.release(Key.space)
                time.sleep(pauseTime[j])

            elif commands[j] == "Enter":
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(pauseTime[j])

            elif commands[j] == "Backspace":
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
                time.sleep(pauseTime[j])

            elif commands[j] == "Up":
                keyboard.press(Key.up)
                keyboard.release(Key.up)
                time.sleep(pauseTime[j])

            elif commands[j] == "Down":
                keyboard.press(Key.down)
                keyboard.release(Key.down)
                time.sleep(pauseTime[j])

            elif commands[j] == "Left":
                keyboard.press(Key.left)
                keyboard.release(Key.left)
                time.sleep(pauseTime[j])

            elif commands[j] == "Right":
                keyboard.press(Key.right)
                keyboard.release(Key.right)
                time.sleep(pauseTime[j])

            elif commands[j] == "Delete":
                keyboard.press(Key.delete)
                keyboard.release(Key.delete)
                time.sleep(pauseTime[j])

            elif commands[j] == "f1":
                keyboard.press(Key.f1)
                keyboard.release(Key.f1)
                time.sleep(pauseTime[j])

            elif commands[j] == "f2":
                keyboard.press(Key.f2)
                keyboard.release(Key.f2)
                time.sleep(pauseTime[j])

            elif commands[j] == "f3":
                keyboard.press(Key.f3)
                keyboard.release(Key.f3)
                time.sleep(pauseTime[j])

            elif commands[j] == "f4":
                keyboard.press(Key.f4)
                keyboard.release(Key.f4)
                time.sleep(pauseTime[j])

            elif commands[j] == "f5":
                keyboard.press(Key.f5)
                keyboard.release(Key.f5)
                time.sleep(pauseTime[j])
            elif commands[j] == "f6":
                keyboard.press(Key.f6)
                keyboard.release(Key.f6)
                time.sleep(pauseTime[j])

            elif commands[j] == "f7":
                keyboard.press(Key.f7)
                keyboard.release(Key.f7)
                time.sleep(pauseTime[j])

            elif commands[j] == "f8":
                keyboard.press(Key.f8)
                keyboard.release(Key.f8)
                time.sleep(pauseTime[j])

            elif commands[j] == "f9":
                keyboard.press(Key.f9)
                keyboard.release(Key.f9)
                time.sleep(pauseTime[j])

            elif commands[j] == "f10":
                keyboard.press(Key.f10)
                keyboard.release(Key.f10)
                time.sleep(pauseTime[j])

            elif commands[j] == "f11":
                keyboard.press(Key.f11)
                keyboard.release(Key.f11)
                time.sleep(pauseTime[j])

            elif commands[j] == "f12":
                keyboard.press(Key.f12)
                keyboard.release(Key.f12)
                time.sleep(pauseTime[j])
            elif commands[j] == "lc":
                mouse.position = (xlist[j], ylist[j])
                mouse.press(Button.left)
                mouse.release(Button.left)
                time.sleep(pauseTime[j])

                time.sleep(pauseTime[j])
            elif commands[j] == "rc":
                mouse.position = (xlist[j], ylist[j])
                mouse.press(Button.right)
                mouse.release(Button.right)
                time.sleep(pauseTime[j])
            elif commands[j] == "custom" and typeorprint[j] == "print":
                keyboard.type(customList[j])
                time.sleep(pauseTime[j])

            elif commands[j] == "custom" and typeorprint[j] == "type":
                for char in customList[j]:
                    keyboard.press(char)
                    time.sleep(pauseTime[j])


def mouposi():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return f'x: {pt.x}, y: {pt.y}'


def rfneokfge():
    counter = 1
    Label(Mouse_Clicks, text="                                                                              ").place(
        x=150, y=20)
    for i in range(counter):
        time.sleep(2)
        tabs.add(Mouse_Clicks, text='Mouse Clicker')
        h = mouposi()
        Label(Mouse_Clicks, text=h).place(x=150, y=20)
        counter = counter + 1


# main screen
main_screen = Tk()
main_screen.title("Auto Typer/Clicker")
main_screen.geometry("500x645")
tk.Button(main_screen, text="Start", width=20, height=3, bg="grey", font="19", command=mostimppart).place(x=125, y=559)
Label(main_screen, text="Cycles:").place(x=30, y=559)
Repeat = Entry(main_screen, width=10)
Repeat.place(x=30, y=579)
main_screen.resizable(False, False)
tk.Button(main_screen, text="Add command", command=main_outputinstruction).place(x=0, y=153)
sb = Scrollbar(main_screen)
sb.pack(side=RIGHT, fill=Y)
mylist = Listbox(main_screen, yscrollcommand=sb.set, width=80, height=23)
sb.config(command=mylist.yview)
main_screen.bind('<Control-s>', mostimppart)
# main tab
tabs = ttk.Notebook(main_screen)

# mouse

Mouse_Clicks = ttk.Frame(tabs)
newlist = tk.Button(Mouse_Clicks, text="Locate X & Y", command=rfneokfge)
newlist.place(x=150, y=40)


class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]


tabs.add(Mouse_Clicks, text='Mouse Clicker')
h = mouposi()
Label(Mouse_Clicks, text=h).place(x=150, y=20)

v = tkinter.IntVar()
btn = Radiobutton(Mouse_Clicks, text="Left Click", font=1, variable=v, value=1, command=ValueAssign.lc)
btn.pack(anchor=W)
btn2 = Radiobutton(Mouse_Clicks, text="Right Click", font="1", variable=v, value=2, command=ValueAssign.rc)
btn2.pack(anchor="w")
lb1 = Label(main_screen, text="Input the pause between the commands (1 = 1 sec)")
lb1.place(x=0, y=95)
Label(Mouse_Clicks, text="Position of mouse", fg="blue").place(x=150, y=0)
Label(Mouse_Clicks, text="Enter the displayed X and Y", fg="blue").place(x=320, y=0)
X1 = Entry(Mouse_Clicks, width=5)
Y1 = Entry(Mouse_Clicks, width=5)
X1.place(x=430, y=20)
Y1.place(x=430, y=40)
Label(Mouse_Clicks, text="X").place(x=413, y=20)
Label(Mouse_Clicks, text="Y").place(x=413, y=40)
pause_time = Entry(main_screen, width=5)
pause_time.place(x=0, y=114)
tk.Button(main_screen, text="Delete Command", command=removedata, bg="red2", height=3, width=17).place(x=287, y=114)
lb2 = Label(main_screen, text="Enter a numeric value", fg="red")
lb2.place(x=0, y=133)

# alphabets
Alphabets = ttk.Frame(tabs)
tabs.add(Alphabets, text='Alphabets')

btn = Radiobutton(Alphabets, text="a", variable=v, value=3, command=ValueAssign.lettera)
btn.place(x=0, y=0)
btn = Radiobutton(Alphabets, text="b", variable=v, value=4, command=ValueAssign.letterb)
btn.place(x=28, y=0)
btn = Radiobutton(Alphabets, text="c", variable=v, value=5, command=ValueAssign.letterc)
btn.place(x=58, y=0)
btn = Radiobutton(Alphabets, text="d", variable=v, value=6, command=ValueAssign.letterd)
btn.place(x=88, y=0)
btn = Radiobutton(Alphabets, text="e", variable=v, value=7, command=ValueAssign.lettere)
btn.place(x=118, y=0)
btn = Radiobutton(Alphabets, text="f", variable=v, value=8, command=ValueAssign.letterf)
btn.place(x=148, y=0)
btn = Radiobutton(Alphabets, text="g", variable=v, value=9, command=ValueAssign.letterg)
btn.place(x=178, y=0)
btn = Radiobutton(Alphabets, text="h", variable=v, value=10, command=ValueAssign.letterh)
btn.place(x=208, y=0)
btn = Radiobutton(Alphabets, text="i", variable=v, value=11, command=ValueAssign.letteri)
btn.place(x=238, y=0)
btn = Radiobutton(Alphabets, text="j", variable=v, value=12, command=ValueAssign.letterj)
btn.place(x=268, y=0)
btn = Radiobutton(Alphabets, text="k", variable=v, value=13, command=ValueAssign.letterk)
btn.place(x=298, y=0)
btn = Radiobutton(Alphabets, text="l", variable=v, value=14, command=ValueAssign.letterl)
btn.place(x=328, y=0)
btn = Radiobutton(Alphabets, text="m", variable=v, value=15, command=ValueAssign.letterm)
btn.place(x=358, y=0)
btn = Radiobutton(Alphabets, text="n", variable=v, value=16, command=ValueAssign.lettern)
btn.place(x=393, y=0)
btn = Radiobutton(Alphabets, text="o", variable=v, value=17, command=ValueAssign.lettero)
btn.place(x=423, y=0)
btn = Radiobutton(Alphabets, text="p", variable=v, value=18, command=ValueAssign.letterp)
btn.place(x=0, y=25)
btn = Radiobutton(Alphabets, text="q", variable=v, value=19, command=ValueAssign.letterq)
btn.place(x=30, y=25)
btn = Radiobutton(Alphabets, text="r", variable=v, value=20, command=ValueAssign.letterr)
btn.place(x=60, y=25)
btn = Radiobutton(Alphabets, text="s", variable=v, value=21, command=ValueAssign.letters)
btn.place(x=90, y=25)
btn = Radiobutton(Alphabets, text="t", variable=v, value=22, command=ValueAssign.lettert)
btn.place(x=120, y=25)
btn = Radiobutton(Alphabets, text="u", variable=v, value=23, command=ValueAssign.letteru)
btn.place(x=150, y=25)
btn = Radiobutton(Alphabets, text="v", variable=v, value=24, command=ValueAssign.letterv)
btn.place(x=180, y=25)
btn = Radiobutton(Alphabets, text="w", variable=v, value=25, command=ValueAssign.letterw)
btn.place(x=210, y=25)
btn = Radiobutton(Alphabets, text="x", variable=v, value=26, command=ValueAssign.letterx)
btn.place(x=243, y=25)
btn = Radiobutton(Alphabets, text="y", variable=v, value=27, command=ValueAssign.lettery)
btn.place(x=273, y=25)
btn = Radiobutton(Alphabets, text="z", variable=v, value=28, command=ValueAssign.letterz)
btn.place(x=303, y=25)

# numbers
Numbers = ttk.Frame(tabs)
tabs.add(Numbers, text='Numbers')

btn = Radiobutton(Numbers, text="0", font=1, variable=v, value=29, command=ValueAssign.num0)
btn.place(x=0, y=0)
btn = Radiobutton(Numbers, text="1", font=1, variable=v, value=30, command=ValueAssign.num1)
btn.place(x=0, y=25)
btn = Radiobutton(Numbers, text="2", font=1, variable=v, value=31, command=ValueAssign.num2)
btn.place(x=50, y=0)
btn = Radiobutton(Numbers, text="3", font=1, variable=v, value=32, command=ValueAssign.num3)
btn.place(x=50, y=25)
btn = Radiobutton(Numbers, text="4", font=1, variable=v, value=33, command=ValueAssign.num4)
btn.place(x=98, y=0)
btn = Radiobutton(Numbers, text="5", font=1, variable=v, value=34, command=ValueAssign.num5)
btn.place(x=98, y=25)
btn = Radiobutton(Numbers, text="6", font=1, variable=v, value=35, command=ValueAssign.num6)
btn.place(x=148, y=0)
btn = Radiobutton(Numbers, text="7", font=1, variable=v, value=36, command=ValueAssign.num7)
btn.place(x=148, y=25)
btn = Radiobutton(Numbers, text="8", font=1, variable=v, value=37, command=ValueAssign.num8)
btn.place(x=198, y=0)
btn = Radiobutton(Numbers, text="9", font=1, variable=v, value=38, command=ValueAssign.num9)
btn.place(x=198, y=25)

# Symbols
Symbols = ttk.Frame(tabs)
tabs.add(Symbols, text='Symbols')
btn = Radiobutton(Symbols, text="(", variable=v, value=39, command=ValueAssign.sym1)
btn.place(x=0, y=0)
btn = Radiobutton(Symbols, text=")", variable=v, value=40, command=ValueAssign.sym2)
btn.place(x=30, y=0)
btn = Radiobutton(Symbols, text="[", variable=v, value=41, command=ValueAssign.sym3)
btn.place(x=63, y=0)
btn = Radiobutton(Symbols, text="]", variable=v, value=42, command=ValueAssign.sym4)
btn.place(x=93, y=0)
btn = Radiobutton(Symbols, text="{", variable=v, value=43, command=ValueAssign.sym5)
btn.place(x=123, y=0)
btn = Radiobutton(Symbols, text="}", variable=v, value=44, command=ValueAssign.sym6)
btn.place(x=153, y=0)
btn = Radiobutton(Symbols, text="<", variable=v, value=45, command=ValueAssign.sym7)
btn.place(x=183, y=0)
btn = Radiobutton(Symbols, text=">", variable=v, value=46, command=ValueAssign.sym8)
btn.place(x=213, y=0)
btn = Radiobutton(Symbols, text="!", variable=v, value=47, command=ValueAssign.sym9)
btn.place(x=243, y=0)
btn = Radiobutton(Symbols, text="@", variable=v, value=48, command=ValueAssign.sym10)
btn.place(x=273, y=0)
btn = Radiobutton(Symbols, text="#", variable=v, value=49, command=ValueAssign.sym11)
btn.place(x=310, y=0)
btn = Radiobutton(Symbols, text="$", variable=v, value=50, command=ValueAssign.sym12)
btn.place(x=340, y=0)
btn = Radiobutton(Symbols, text="%", variable=v, value=51, command=ValueAssign.sym13)
btn.place(x=370, y=0)
btn = Radiobutton(Symbols, text="^", variable=v, value=52, command=ValueAssign.sym14)
btn.place(x=405, y=0)
btn = Radiobutton(Symbols, text="&", variable=v, value=53, command=ValueAssign.sym15)
btn.place(x=0, y=25)
btn = Radiobutton(Symbols, text="*", variable=v, value=54, command=ValueAssign.sym16)
btn.place(x=33, y=25)
btn = Radiobutton(Symbols, text="-", variable=v, value=55, command=ValueAssign.sym17)
btn.place(x=63, y=25)
btn = Radiobutton(Symbols, text="_", variable=v, value=56, command=ValueAssign.sym18)
btn.place(x=93, y=25)
btn = Radiobutton(Symbols, text="=", variable=v, value=57, command=ValueAssign.sym19)
btn.place(x=123, y=25)
btn = Radiobutton(Symbols, text="+", variable=v, value=58, command=ValueAssign.sym20)
btn.place(x=153, y=25)
btn = Radiobutton(Symbols, text=";", variable=v, value=59, command=ValueAssign.sym21)
btn.place(x=183, y=25)
btn = Radiobutton(Symbols, text=":", variable=v, value=60, command=ValueAssign.sym22)
btn.place(x=213, y=25)
btn = Radiobutton(Symbols, text="'", variable=v, value=61, command=ValueAssign.sym23)
btn.place(x=243, y=25)
btn = Radiobutton(Symbols, text='"', variable=v, value=62, command=ValueAssign.sym24)
btn.place(x=273, y=25)
btn = Radiobutton(Symbols, text="\\", variable=v, value=63, command=ValueAssign.sym25)
btn.place(x=310, y=25)
btn = Radiobutton(Symbols, text="|", variable=v, value=64, command=ValueAssign.sym26)
btn.place(x=340, y=25)
btn = Radiobutton(Symbols, text=",", variable=v, value=65, command=ValueAssign.sym27)
btn.place(x=375, y=25)
btn = Radiobutton(Symbols, text=".", variable=v, value=66, command=ValueAssign.sym28)
btn.place(x=405, y=25)
btn = Radiobutton(Symbols, text="/", variable=v, value=67, command=ValueAssign.sym29)
btn.place(x=0, y=49)
btn = Radiobutton(Symbols, text="?", variable=v, value=68, command=ValueAssign.sym30)
btn.place(x=30, y=49)

custom = ttk.Frame(tabs)
tabs.add(custom, text="Custom Text")
Label(custom, text="Enter Your Custom Text", font=2, fg="Green").place(x=0, y=0)
btn4 = Radiobutton(custom, text="Type Letter By Letter", variable=v, value=92, command=ValueAssign.letterbyletter)
btn4.place(x=0, y=50)
btn4 = Radiobutton(custom, text="Type at once", variable=v, value=93, command=ValueAssign.atonce)
btn4.place(x=250, y=50)
customText = Entry(custom, width=42, font=25)
customText.place(x=0, y=28)

other_keys = ttk.Frame(tabs)
tabs.add(other_keys, text="Other Keys")

btn = Radiobutton(other_keys, text="ESC", variable=v, value=69, command=ValueAssign.esc)
btn.place(x=0, y=0)
btn = Radiobutton(other_keys, text="Tab", variable=v, value=70, command=ValueAssign.tab)
btn.place(x=41, y=0)
btn = Radiobutton(other_keys, text="Windows Key", variable=v, value=71, command=ValueAssign.winkey)
btn.place(x=83, y=0)
btn = Radiobutton(other_keys, text="Space", variable=v, value=72, command=ValueAssign.space)
btn.place(x=177, y=0)
btn = Radiobutton(other_keys, text="Enter", variable=v, value=73, command=ValueAssign.enter)
btn.place(x=231, y=0)
btn = Radiobutton(other_keys, text="Backspace", variable=v, value=74, command=ValueAssign.backspace)
btn.place(x=283, y=0)
btn = Radiobutton(other_keys, text="Upwards arrow", variable=v, value=75, command=ValueAssign.up)
btn.place(x=361, y=0)
btn = Radiobutton(other_keys, text="Downwards arrow", variable=v, value=76, command=ValueAssign.down)
btn.place(x=0, y=25)
btn = Radiobutton(other_keys, text="Left arrow", variable=v, value=77, command=ValueAssign.left)
btn.place(x=121, y=25)
btn = Radiobutton(other_keys, text="Right arrow", variable=v, value=78, command=ValueAssign.right)
btn.place(x=198, y=25)
btn = Radiobutton(other_keys, text="Delete", variable=v, value=79, command=ValueAssign.delete)
btn.place(x=285, y=25)
btn = Radiobutton(other_keys, text="F1", variable=v, value=80, command=ValueAssign.f1)
btn.place(x=341, y=25)
btn = Radiobutton(other_keys, text="F2", variable=v, value=81, command=ValueAssign.f2)
btn.place(x=378, y=25)
btn = Radiobutton(other_keys, text="F3", variable=v, value=82, command=ValueAssign.f3)
btn.place(x=415, y=25)
btn = Radiobutton(other_keys, text="F4", variable=v, value=83, command=ValueAssign.f4)
btn.place(x=0, y=50)
btn = Radiobutton(other_keys, text="F5", variable=v, value=84, command=ValueAssign.f5)
btn.place(x=38, y=50)
btn = Radiobutton(other_keys, text='F6', variable=v, value=85, command=ValueAssign.f6)
btn.place(x=75, y=50)
btn = Radiobutton(other_keys, text="F7", variable=v, value=86, command=ValueAssign.f7)
btn.place(x=113, y=50)
btn = Radiobutton(other_keys, text="F8", variable=v, value=87, command=ValueAssign.f8)
btn.place(x=148, y=50)
btn = Radiobutton(other_keys, text="F9", variable=v, value=88, command=ValueAssign.f9)
btn.place(x=184, y=50)
btn = Radiobutton(other_keys, text="F10", variable=v, value=89, command=ValueAssign.f10)
btn.place(x=219, y=50)
btn = Radiobutton(other_keys, text="F11", variable=v, value=90, command=ValueAssign.f11)
btn.place(x=262, y=50)
btn = Radiobutton(other_keys, text="F12", variable=v, value=91, command=ValueAssign.f12)
btn.place(x=306, y=50)

tabs.pack(fill=X)
main_screen.mainloop()

