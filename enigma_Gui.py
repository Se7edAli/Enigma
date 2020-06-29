#5e7ed
import tkinter as tk
import pickle

root = tk.Tk()
root.title("Enigma")
root.geometry("300x100")
lb1 = tk.Label(root,text = 'Input Text')
lb1.pack()
en_entry = tk.Entry(root,width=35)
en_entry.pack()

def clicked():
    global r1,r2,r3
    alphabet = 'abcdefghijklmnopqrstuvwxyz '

    f = open('./rotor_state.enigma','rb')
    r1 , r2 , r3 = pickle.load(f)
    f.close()


    def reflector(c):
        return alphabet[len(alphabet)-alphabet.find(c)-1]


    def enigma_one_char(c):
        c1 = r1[alphabet.find(c)]
        c2 = r2[alphabet.find(c1)]
        c3 = r3[alphabet.find(c2)]
        reflected = reflector(c3)
        c3 = alphabet[r3.find(reflected)]
        c2 = alphabet[r2.find(c3)]
        c1 = alphabet[r1.find(c2)]
        return c1



    def rotate_rotors():
        global r1,r2,r3
        r1 = r1[1:] + r1[0]
        if state % 27 :
            r2 = r2[1:] + r2[0]
        if state % (27 * 27) :
            r3 = r3[1:] + r3[0]

    state = 0
    cipher = ""
    plain = en_entry.get()
   
    for c in plain:
        state += 1
        cipher += enigma_one_char(c)
        rotate_rotors()
    
    newwin = tk.Toplevel(root)
    newwin.title('Resualt')
    newwin.geometry('300x100')
    txts = tk.Label(newwin,text='Encrypted text is : \n' + cipher)
    txts.pack()

bt1 = tk.Button(root,text='start',command=clicked)
bt1.pack()

root.mainloop()