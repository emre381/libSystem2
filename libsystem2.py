
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 20:34:46 2024

@author: cigo_
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog  

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kütüphane Yönetim Sistemi")

      
        self.admin_password = "admin123"
        

        self.available_books = [
            {"title": "Küçük Prens", "author": "Antoine de Saint-Exupéry", "stock": 10},
            {"title": "Harry Potter", "author": "J.K. Rowling", "stock": 15},
            {"title": "Yüzüklerin Efendisi", "author": "J.R.R. Tolkien", "stock": 8},
            {"title": "Da Vinci Şifresi", "author": "Dan Brown", "stock": 20},
            {"title": "1984", "author": "George Orwell", "stock": 30},
            {"title": "To Kill a Mockingbird", "author": "Harper Lee", "stock": 4},
            {"title": "Bülbülü Öldürmek", "author": "Harper Lee", "stock": 6},
            {"title": "Don Quijote", "author": "Miguel de Cervantes", "stock": 6},
            {"title": "Suç ve Ceza", "author": "Fyodor Dostoyevski", "stock": 13},
            {"title": "Sefiller", "author": "Victor Hugo", "stock": 17},
            {"title": "Dorian Gray'in Portresi", "author": "Oscar Wilde", "stock": 18},
            {"title": "Oniki Levha", "author": "Anton Çehov", "stock": 3},
            {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "stock": 44},
            {"title": "Savaş ve Barış", "author": "Lev Tolstoy", "stock": 30},
            {"title": "Jane Eyre", "author": "Charlotte Brontë", "stock": 8},
            {"title": "Ulysses", "author": "James Joyce", "stock": 19},
            {"title": "Romeo ve Juliet", "author": "William Shakespeare", "stock": 22},
            {"title": "Martı", "author": "Anton Çehov", "stock": 5},
            {"title": "Moby Dick", "author": "Herman Melville", "stock": 11},
            {"title": "Prens", "author": "Niccolò Machiavelli", "stock": 19},
            {"title": "İnce Mehmed", "author": "Halit Ziya Uşaklıgil", "stock": 10},
            {"title": "Kuyucaklı Yusuf", "author": "Sabahattin Ali", "stock": 15},
            {"title": "Sineklerin Tanrısı", "author": "Ahmet Ümit", "stock": 8},
            {"title": "İstanbul Hatırası", "author": "Ahmet Ümit", "stock": 20},
            {"title": "Beyaz Gemi", "author": "Cengiz Aytmatov", "stock": 12},
            {"title": "Aşk-ı Memnu", "author": "Halit Ziya Uşaklıgil", "stock": 7},
            {"title": "Fatih-Harbiye", "author": "Peyami Safa", "stock": 5},
            {"title": "Kürk Mantolu Madonna", "author": "Sabahattin Ali", "stock": 9},
            {"title": "İnci", "author": "John Steinbeck", "stock": 14},
            {"title": "Bir İdam Mahkûmunun Son Günü", "author": "Victor Hugo", "stock": 11},
            {"title": "Çalıkuşu", "author": "Reşat Nuri Güntekin", "stock": 8},
            {"title": "Kardeşimin Hikayesi", "author": "Zülfü Livaneli", "stock": 6},
            {"title": "Baba ve Piç", "author": "Zülfü Livaneli", "stock": 10},
            {"title": "Bir Gün", "author": "David Nicholls", "stock": 15},
            {"title": "Sırça Köşk", "author": "Sabahattin Ali", "stock": 20},
            {"title": "Dönüşüm", "author": "Franz Kafka", "stock": 25},
            {"title": "Uçurtma Avcısı", "author": "Khaled Hosseini", "stock": 30},
            {"title": "Beyhude", "author": "Halit Ziya Uşaklıgil", "stock": 8},
            {"title": "Fareler ve İnsanlar", "author": "John Steinbeck", "stock": 18},
            {"title": "Sefiller", "author": "Victor Hugo", "stock": 22},
            {"title": "Kumarbaz", "author": "Fyodor Dostoyevski", "stock": 12},
            {"title": "Bir Delinin Hatıra Defteri", "author": "Nikolai Gogol", "stock": 15},
            {"title": "Dracula", "author": "Bram Stoker", "stock": 20},
            {"title": "Küçük Kara Balık", "author": "Samed Behrengi", "stock": 10},
            {"title": "Simru", "author": "Halit Ziya Uşaklıgil", "stock": 5},
            {"title": "İstanbul'un Altınları", "author": "Sait Faik Abasıyanık", "stock": 13},
            {"title": "Cevdet Bey ve Oğulları", "author": "Orhan Pamuk", "stock": 17},
            {"title": "Köle", "author": "Isaac Bashevis Singer", "stock": 9},
            {"title": "Ölü Canlar", "author": "Nikolai Gogol", "stock": 14},
            {"title": "Eylül", "author": "Mehmet Rauf", "stock": 11}
            
        ]

        self.borrowed_books = {}

        self.label_footer = tk.Label(self.root, text="Cihat Emre Çınar Projesidir", font=("Helvetica", 12, "bold"))
        self.label_footer.grid(row=6, column=0, padx=5, pady=5, sticky="sw")

        self.listbox_books = tk.Listbox(self.root, selectmode=tk.SINGLE, height=10, width=100)
        self.listbox_books.grid(row=0, column=0, padx=5, pady=5, rowspan=2)

        # Kitaplar Listesini doldur
        self.populate_books_listbox()

        # Scrollbar
        self.scrollbar_books = tk.Scrollbar(self.root, command=self.listbox_books.yview)
        self.scrollbar_books.grid(row=0, column=1, pady=5, sticky='ns')
        self.listbox_books.config(yscrollcommand=self.scrollbar_books.set)

        # Öğrenci bilgileri için giriş widget'ları
        self.label_student_name = tk.Label(self.root, text="Öğrenci Adı:")
        self.label_student_name.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_student_name = tk.Entry(self.root)
        self.entry_student_name.grid(row=2, column=1, padx=5, pady=5)

        self.label_student_id = tk.Label(self.root, text="Öğrenci Telefon:")
        self.label_student_id.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_student_id = tk.Entry(self.root)
        self.entry_student_id.grid(row=3, column=1, padx=5, pady=5)

        # Ödünç Al, Geri Getir, Kitap Ekle ve Kitap Çıkart butonları
        self.borrow_button = tk.Button(self.root, text="Ödünç Al", command=lambda: self.borrow_return_book(True))
        self.borrow_button.grid(row=4, column=0, padx=5, pady=5, sticky="e")

        self.return_button = tk.Button(self.root, text="Geri Getir", command=lambda: self.borrow_return_book(False))
        self.return_button.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        # Kitap ekle ve çıkart butonlarına yönetici şifresi istenmesi
        self.add_book_button = tk.Button(self.root, text="Kitap Ekle", command=self.open_add_book_window)
        self.add_book_button.grid(row=5, column=0, pady=10, sticky="e")

        self.remove_book_button = tk.Button(self.root, text="Kitap Çıkart", command=self.open_remove_book_window)
        self.remove_book_button.grid(row=5, column=1, pady=10, sticky="w")

        # Öğrenci bilgileri için Treeview
        self.treeview_students = ttk.Treeview(self.root, columns=("Student Name", "Student ID", "Book Name", "Author"))
        self.treeview_students.grid(row=0, column=2, rowspan=5, padx=5, pady=5, sticky='nsew')

        # Scrollbar
        self.scrollbar_students = ttk.Scrollbar(self.root, command=self.treeview_students.yview)
        self.scrollbar_students.grid(row=0, column=3, rowspan=5, pady=5, sticky='ns')
        self.treeview_students.configure(yscrollcommand=self.scrollbar_students.set)

        self.scrollbar_horizontal = ttk.Scrollbar(self.root, orient="horizontal", command=self.treeview_students.xview)
        self.scrollbar_horizontal.grid(row=5, column=2, sticky="ew")
        self.treeview_students.configure(xscrollcommand=self.scrollbar_horizontal.set)

        # Treeview Başlıkları
        self.treeview_students["show"] = "headings"
        self.treeview_students.heading("Student Name", text="Öğrenci Adı")
        self.treeview_students.heading("Student ID", text="Öğrenci Telefon")
        self.treeview_students.heading("Book Name", text="Kitap Adı")
        self.treeview_students.heading("Author", text="Yazar")

        # Ödünç Alınan Kitaplar
        self.display_borrowed_books()

    def populate_books_listbox(self):
        for book in self.available_books:
            self.listbox_books.insert(tk.END, f"{book['title']} - {book['author']} - Stok: {book['stock']}")

    def borrow_return_book(self, is_borrow):
        student_name = self.entry_student_name.get()
        student_id = self.entry_student_id.get()
        selected_book_index = self.listbox_books.curselection()

        if not selected_book_index:
            messagebox.showwarning("Uyarı", "Lütfen bir kitap seçin.")
            return

        selected_book_index = selected_book_index[0]
        selected_book = self.available_books[selected_book_index]

        if is_borrow:
            if selected_book["stock"] > 0 and student_name not in self.borrowed_books:
                selected_book["stock"] -= 1
                self.borrowed_books[student_name] = {"book": selected_book, "student_id": student_id}
                self.display_borrowed_books()
                messagebox.showinfo("Bilgi", f"{student_name}, {selected_book['title']} kitabını ödünç aldı.")
            elif student_name in self.borrowed_books:
                messagebox.showwarning("Uyarı", f"{student_name}, zaten bir kitap ödünç almış durumda.")
            else:
                messagebox.showwarning("Uyarı", f"{selected_book['title']} stokta bulunmuyor.")
        else:
            if student_name in self.borrowed_books and selected_book["title"] == self.borrowed_books[student_name]["book"]["title"]:
                selected_book["stock"] += 1
                del self.borrowed_books[student_name]
                self.display_borrowed_books()
                messagebox.showinfo("Bilgi", f"{student_name}, {selected_book['title']} kitabını geri getirdi.")
            elif student_name not in self.borrowed_books:
                messagebox.showwarning("Uyarı", f"{student_name}, henüz bir kitap ödünç almamış.")
            else:
                messagebox.showwarning("Uyarı", f"{student_name}, aldığı kitabı geri getiremez.")

    def display_borrowed_books(self):
        for i in self.treeview_students.get_children():
            self.treeview_students.delete(i)

        for student_name, data in self.borrowed_books.items():
            book = data["book"]
            self.treeview_students.insert("", tk.END, values=(student_name, data["student_id"],
                                                             book['title'], book['author']))

    def open_add_book_window(self):
        # Yönetici şifresi doğrulaması
        admin_password = simpledialog.askstring("Yönetici Şifresi", "Yönetici şifresini girin:", show="*")
        if admin_password != self.admin_password:
            messagebox.showerror("Hata", "Yanlış yönetici şifresi. Kitap eklemek için yetkiniz yok.")
            return

        add_book_window = tk.Toplevel(self.root)
        add_book_window.title("Kitap Ekle")

        add_book_window = tk.Toplevel(self.root)
        add_book_window.title("Kitap Ekle")

        label_title = tk.Label(add_book_window, text="Kitap Adı:")
        label_title.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        entry_title = tk.Entry(add_book_window)
        entry_title.grid(row=0, column=1, padx=10, pady=5)

        label_author = tk.Label(add_book_window, text="Yazar:")
        label_author.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entry_author = tk.Entry(add_book_window)
        entry_author.grid(row=1, column=1, padx=10, pady=5)

        label_stock = tk.Label(add_book_window, text="Stok Adedi:")
        label_stock.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        entry_stock = tk.Entry(add_book_window)
        entry_stock.grid(row=2, column=1, padx=10, pady=5)

        add_button = tk.Button(add_book_window, text="Ekle",
                               command=lambda: self.add_book(add_book_window, entry_title.get(), entry_author.get(),
                                                            entry_stock.get()))
        add_button.grid(row=3, column=1, pady=10)

    def open_remove_book_window(self):
        # Yönetici şifresi doğrulaması
        admin_password = simpledialog.askstring("Yönetici Şifresi", "Yönetici şifresini girin:", show="*")
        if admin_password != self.admin_password:
            messagebox.showerror("Hata", "Yanlış yönetici şifresi. Kitap çıkartmak için yetkiniz yok.")
            return

        self.remove_book()

        self.remove_book()

    def add_book(self, add_book_window, title, author, stock):
        try:
            stock = int(stock)
            if stock < 0:
                raise ValueError("Stok adedi negatif olamaz.")
        except ValueError as ve:
            messagebox.showerror("Hata", f"Hatalı stok adedi: {ve}")
            return

        new_book = {"title": title, "author": author, "stock": stock}
        self.available_books.append(new_book)
        self.listbox_books.insert(tk.END, f"{new_book['title']} - {new_book['author']} - Stok: {new_book['stock']}")
        messagebox.showinfo("Bilgi", f"{new_book['title']} kitabı başarıyla eklendi.")

        add_book_window.destroy()

    def remove_book(self):
        selected_book_index = self.listbox_books.curselection()

        if not selected_book_index:
            messagebox.showwarning("Uyarı", "Lütfen bir kitap seçin.")
            return

        selected_book_index = selected_book_index[0]
        selected_book = self.available_books[selected_book_index]

        remove_book_window = tk.Toplevel(self.root)
        remove_book_window.title("Kitap Çıkart")

        label_title = tk.Label(remove_book_window, text="Kitap Adı:")
        label_title.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        entry_title = tk.Entry(remove_book_window)
        entry_title.insert(0, selected_book["title"])
        entry_title.config(state="readonly")
        entry_title.grid(row=0, column=1, padx=10, pady=5)

        label_author = tk.Label(remove_book_window, text="Yazar:")
        label_author.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entry_author = tk.Entry(remove_book_window)
        entry_author.insert(0, selected_book["author"])
        entry_author.config(state="readonly")
        entry_author.grid(row=1, column=1, padx=10, pady=5)

        label_stock = tk.Label(remove_book_window, text="Çıkartılacak Stok Adedi:")
        label_stock.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        entry_stock = tk.Entry(remove_book_window)
        entry_stock.grid(row=2, column=1, padx=10, pady=5)

        remove_button = tk.Button(remove_book_window, text="Çıkart",
                                  command=lambda: self.subtract_stock(remove_book_window, selected_book,
                                                                      entry_stock.get(), selected_book_index))
        remove_button.grid(row=3, column=1, pady=10)

    def subtract_stock(self, remove_book_window, selected_book, stock_to_subtract, selected_book_index):
        try:
            stock_to_subtract = int(stock_to_subtract)
            if stock_to_subtract < 0 or stock_to_subtract > selected_book["stock"]:
                raise ValueError("Geçersiz stok adedi.")
        except ValueError as ve:
            messagebox.showerror("Hata", f"Hatalı stok adedi: {ve}")
            return

        selected_book["stock"] -= stock_to_subtract
        self.listbox_books.delete(selected_book_index)
        self.listbox_books.insert(tk.END,
                                  f"{selected_book['title']} - {selected_book['author']} - Stok: {selected_book['stock']}")
        messagebox.showinfo("Bilgi", f"{stock_to_subtract} adet {selected_book['title']} kitabı başarıyla çıkartıldı.")

        remove_book_window.destroy()
        
        

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.geometry("1600x600")
    root.mainloop()
