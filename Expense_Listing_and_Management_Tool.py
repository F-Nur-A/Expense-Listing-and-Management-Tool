from tkinter import *
import json
from tkinter import filedialog as fd

class SiparişListeleme(Frame):
    """ Kullanıcı harcama listesini raporladıktan sonra seçtiği harcamaları ya da bütün harcamalarını silebilir
    """
    
    def __init__(self, root):
        Frame.__init__(self , root)
        self.root = root
        self.harcamalar=[]
        self.initUI()
        
    def initUI(self):
        self.pack()
        self.lb = Listbox(self,height=20, width=110, selectmode="single")
        self.lb.pack()
        
  
        self.aktar = Button(self, text="Aktar", relief=RAISED, command = self.aktar)
        self.seciliSil = Button(self, text="Seçili Sil", relief=RAISED, command = self.seciliSil)
        self.hepsiniSil = Button(self, text="Hepsini Sil",relief=RAISED, command = self.hepsiniSil)
        self.aktar.pack(side=LEFT)
        self.seciliSil.pack(side=LEFT)
        self.hepsiniSil.pack(side=LEFT)
        
    def aktar(self):
        self.pack()
        name= fd.askopenfilename() 
        file= open(name,"r",encoding="utf-8")
        urunler = json.load(file)
        for satir in urunler:
            urunlerTemiz=("Kategori: {} | Ürün İsmi: {} | Marka: {} | Fiyat: {} | Stok: {} |"
            .format(satir["kategori"],satir["isim"],satir["marka"],satir["fiyat"],satir["stok"]))
            self.harcamalar.append(urunlerTemiz)

        for indeks, harcama in enumerate(self.harcamalar):
            self.lb.insert(indeks, harcama)

        file.close()
        self.initUI
        return self.harcamalar

    def seciliSil(self):
        indexNo=self.lb.curselection()
        self.lb.delete(indexNo)
        self.harcamalar.pop(indexNo[0])

    def hepsiniSil(self):
        self.lb.delete(0,END)
        del self.harcamalar


        
def main():
    root = Tk()
    root.geometry("700x500+200+200")
    root.title("Harcama Raporu")
    app = SiparişListeleme(root)
    root.mainloop()
    app.mainloop()

main()
