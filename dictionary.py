user = {  
    "nama": ["arsene lupin", "sherlock holmes" , "irene adler"], 
    "nik" : [1234, 4321, 6789], 
    "jenis_kelamin": ["male","male","female"],
    "tanggal_lahir": ["1902-03-23", "1876-08-16","1884-10-07"],
}

nama = [input("masukkan nama anda: ")]
nik = [input("Masukkan NIK Anda: ")]
jenis_kelamin = [input("Masukkan jenis kelamin Anda: ")]
tanggal_lahir = [input("Masukkan tanggal lahir Anda (format: yyyy-mm-dd): ")]

user["nama"] += nama
user["nik"] += nik
user["jenis_kelamin"] += jenis_kelamin
user["tanggal_lahir"] += tanggal_lahir

print(user['nama'])