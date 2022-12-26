#cari 4

#mengimport file negara
from negara import negara_asia                                                            
print('JAWAB PERTANYAAN BERIKUT INI')                                                  
print('--'*20) 
#pertanyaan dan menginput negara                                                                           
print('1.negara dibenua asia yang kamu ketahui...')  
x = input()
b = x
print(' ')                                                                        
print('negara yang anda jawab',b)   
#memproses inputan
def match(b):
    if b in negara_asia.asia:                      
        return f'yapp {b} adalah negara dibenua asia'   
    else:                                               
        return f'{b} bukan negara dibenua asia'         

print('')
#11.mendeklarasikan fungsi match
print(match(b))

print('--'*20)
#12.megecek tipe data dari variabel b
print(type(b))