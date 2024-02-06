import tkinter
import base64
from tkinter import messagebox

FONT = ("Verdena", 15, "normal")
COLOR = "#CC8D1A"

#Creating and editing the window
window = tkinter.Tk()
window.title("Şifrele ve Şifreyi Çöz!")
window.minsize(width=800, height=600)
window.maxsize(width=800, height=600)
window.config(bg="#16232E", pady=30, padx=30)

#Add Image
img = tkinter.PhotoImage(file="lockImage.png")
imgLabel = tkinter.Label(image=img, bg="#16232E")
imgLabel.pack()

#Encrypt UI
titleLabel = tkinter.Label(text="Başlık gir", font=FONT, bg=COLOR)
titleLabel.place(x=90, y=150)

titleEntry = tkinter.Entry(width=30)
titleEntry.place(x=42, y=183)

messageLabel = tkinter.Label(text="Şifrelemek istediğin mesajı gir", font=FONT, bg=COLOR)
messageLabel.place(x=10, y=215)

messageText = tkinter.Text(width=30, height=10)
messageText.place(x=20, y=250)

keyLabel = tkinter.Label(text="Şifreyi gir", font=FONT, bg=COLOR)
keyLabel.place(x=90, y=430)

keyEntry = tkinter.Entry(width=30)
keyEntry.place(x=45, y=465)

#Encrypt Functions
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def encryptMessage():
    title = titleEntry.get()
    message = messageText.get("1.0", tkinter.END)
    key = keyEntry.get()

    if len(title) == 0 or len(message) == 0 or len(key) == 0:
        messagebox.showerror(title="Hata!", message="Boş değer girmeyin!")
    else:
        encryptedMessage = encode(key, message)
        try:
            with open("passwords.txt", mode="a") as f:
                f.write(f"{title}\n{encryptedMessage}\n")
        except:
            with open("passwords.txt", mode="w") as f:
                f.write(f"{title}\n{encryptedMessage}\n")
        messagebox.showinfo(title="İşlem başarılı", message="Şifreniz oluşturuldu")

    titleEntry.delete(0, tkinter.END)
    messageText.delete("1.0", tkinter.END)
    keyEntry.delete(0, tkinter.END)

#Decrypt UI
encryptedMessageLabel = tkinter.Label(text="Şifresini çözmek istediğiniz mesajı girin")
encryptedMessageLabel.config(font=FONT, bg=COLOR)
encryptedMessageLabel.place(x=370, y=150)

encryptedMessageText = tkinter.Text(width=30, height=10)
encryptedMessageText.place(x=420, y=185)

encryptKeyLabel = tkinter.Label(text="Şifreyi gir", font=FONT, bg=COLOR)
encryptKeyLabel.place(x=490, y=370)

encryptKey = tkinter.Entry(width=30)
encryptKey.place(x=440, y=405)

#Decrypt Functions
def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

decryptMessageLabel = tkinter.Label(text="")
def decryptMessage():
    encryptedMessage = encryptedMessageText.get("1.0", tkinter.END)
    key = encryptKey.get()

    if len(encryptedMessage) == 0 or len(key) == 0:
        messagebox.showerror(title="Hata", message="Boş değer girmeyiniz")
    else:
        try:
            decryptedMessage = decode(key, encryptedMessage)
            decryptMessageLabel.config(text=f"Şifre: {decryptedMessage}", font=FONT, bg="#4BE2E5")
            decryptMessageLabel.place(x=465, y=490)
        except:
            messagebox.showerror(title="Hata!", message="Şifreli Bir Mesaj Gir!")

    encryptedMessageText.delete("1.0", tkinter.END)
    encryptKey.delete(0, tkinter.END)

#Encrypt button
encryptButton = tkinter.Button(text="Şifrele", font=FONT, bg="#46E766", command=encryptMessage)
encryptButton.place(x=100, y=500)

#Decrypt Button
decryptButton = tkinter.Button(text="Şifreyi Çöz", font=FONT, bg="#46E766", command=decryptMessage)
decryptButton.place(x=480, y=440)

window.mainloop()