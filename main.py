from tkinter import * 
 
Aplikasi = Tk()
Aplikasi.title("Prediksi Prodi")

label = Label(Aplikasi, text="Aplikasi prediksi Prodi Pilihan")
label.pack()

nilai1 = Label(Aplikasi, text="Nilai 1:")
nilai1.pack()
nilai1 = Entry(Aplikasi)
nilai1.pack()

nilai2 = Label(Aplikasi, text="Nilai 2:")
nilai2.pack()
nilai2 = Entry(Aplikasi)
nilai2.pack()

nilai3 = Label(Aplikasi, text="Nilai 3:")
nilai3.pack()
nilai3 = Entry(Aplikasi)
nilai3.pack()

nilai4 = Label(Aplikasi, text="Nilai 4:")
nilai4.pack()
nilai4 = Entry(Aplikasi)
nilai4.pack()

nilai5 = Label(Aplikasi, text="Nilai 5:")
nilai5.pack()
nilai5 = Entry(Aplikasi)
nilai5.pack()

nilai6 = Label(Aplikasi, text="Nilai 6:")
nilai6.pack()
nilai6 = Entry(Aplikasi)
nilai6.pack()

nilai7 = Label(Aplikasi, text="Nilai 7:")
nilai7.pack()
nilai7 = Entry(Aplikasi)
nilai7.pack()

nilai8 = Label(Aplikasi, text="Nilai 8:")
nilai8.pack()
nilai8 = Entry(Aplikasi)
nilai8.pack()

nilai9 = Label(Aplikasi, text="Nilai 9:")
nilai9.pack()
nilai9 = Entry(Aplikasi)
nilai9.pack()

nilai10 = Label(Aplikasi, text="Nilai Mata 10:")
nilai10.pack()
nilai10 = Entry(Aplikasi)
nilai10.pack()

def tampilkan_hasil():
    hasil.config(text="Hasil Prediksi: Teknologi Informasi")


prediksi = Button(Aplikasi, text="Hasil Prediksi", command=tampilkan_hasil)
prediksi.pack()

hasil = Label(Aplikasi, text="Hasil Prediksi:")
hasil.pack()

Aplikasi.mainloop()