data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
1. menggunakan single quote '...'
2.menggunakan doubel quote "..."
'''
data = 'menggunakan single quote'
print(data)

data = "menggunakan doubel quote"
print(data)

print('"halo, apa kabar"')
print("'halo,  apa kabar'")
print("ini adalah hari jum'at")

# 2. menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day,isn\'t it')

# backslash
print('c:\\user\\asep')

# tab 
print('asep\tkumarudin,lagi sedih')

# backspase
print('asep \bkumar,lagi sad')

# newline
print('baris pertama. \nbaris kedua.') #LF ->line feed->dipakai unix,macos,linux
print('baris pertama. \rbaris kedua.')#CR ->carriage return -> dipakai commodore,acorn,lips
print('baris pertama. \nbaris kedua.')#CRLF -> line feed  carriage return -> dipakai windows

# 3.String literal atau raw

# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Asep
Kelas : 12 SMA
""")

# multiline literal string dan RAW
print(r"""
Nama : Asep
Kelas : 12 SMA \new normal
Website : www.asep.com/newID
""")