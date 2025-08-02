from tkinter import*
from tkinter import messagebox
from scipy.io.wavfile import write, read
import sounddevice as sd
import os
def record_play(duration,fs=44100,filename="repeat.wav"):

    try:
        sd.default.device=(1,None)
        audio=sd.rec(int(duration*fs),samplerate=fs, channels=2)
        label.config(text="We’re recording... don’t worry, it won’t be improved in any way.")
        window.update()
        sd.wait() 
        write(filename, fs, audio)  
        label.config(text="Replaying your masterpiece... exactly how you left it.")
        window.update()

        fs_read, data = read(filename)
        sd.play(data, samplerate=fs_read)
        sd.wait()

    except Exception as e:
        messagebox.showerror("error ",str(e))
        label.config(text="Error occured, maybe you weren't loud enough?")
window=Tk()
window.title("singasong")
label = Label(window, bg="white", font=('Arial,50,bold'), width=90, height=5)
label.pack()
button = Button(window, text="Begin the Useless Recording", command=lambda:record_play(duration=10), height=2, width=30, font=('Arial,15,bold'),bg="#4a90e2")
button.pack()
window.geometry("600x400")
window.mainloop()