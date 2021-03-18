# Tugas 3 Soal 2

# Nama, Hobi, Sosmed, Lagufav, Makananfav
dict = {'Nama' : 'Tazkiya Mutia Yogasani',
        'hobi' : ['nonton','rebahan', 'jalan-jalan', 'makan-makan'],
        'sosmed' : {'IG' : 'tazkiyamy', 'line' : 'tazkiyamy', 'twitter' : 'tazkiyamy'},
        'lagufav' : ['vida', 'fools', 'Rasool Allah'],
        'makananfav' : ['cah kangkung', 'seafood', 'dengkul goreng']}
#print (*dict['hobi'], sep= ",")

# Mengubah salah satu hobi dan sosmed
dict['hobi'][0] = 'renang'
dict['sosmed']['IG'] = 'kiyaaraya'

#print(dict['hobi'][0])
#print(dict['sosmed'].get('IG'))

# Menghapus 2 makanan favorit
dict['makananfav'].pop(1)
dict['makananfav'].pop(0)

#print(*dict['makananfav'])

# Menambahkan 1 hobi
dict['hobi'].append('nyanyi')

#print (*dict['hobi'], sep= ", ")
