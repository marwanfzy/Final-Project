import smtplib #memanggil smtplib
from email.mime.multipart import MIMEMultipart #memanggil MIMEMultipart dari email.mime.multipart
from email.mime.text import MIMEText #memanggil MIMEText dari email.mime.text
mail_content = 'Hallo, email berhasil dikirimkan menggunakan bahasa pemrograman python' #Isi dari email
#Script pengiriman pengirim dan penerima
listEmail = open('email.txt','r') #memanggil file txt
sender_address = 'marwannfzy@gmail.com' #pengirim
sender_pass = 'xxxxxx' #password email
receiver_address = listEmail.read() #penerima email
#setting MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Coba kirim pesan menggunakan python'   #Isi Subject dari pengirim
#Setting isi dari email
message.attach(MIMEText(mail_content, 'plain')) #
#Membuat SMTP session untuk kirim mail
session = smtplib.SMTP('smtp.gmail.com', 587) #Gunakan port GMAIL
session.starttls() #aktifkan pengamanan email
session.login(sender_address, sender_pass) #proses login di email
text = message.as_string() #isi text berbentuk string
session.sendmail(sender_address, receiver_address, text) #sesi kirim email dari pengirim ke penerima email
session.quit() #sesi selesai dan email sudah terkirim
print('Selamat, email sudah terkirim!')