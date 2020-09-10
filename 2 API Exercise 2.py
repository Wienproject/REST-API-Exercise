# ######## Konversi mata uang ke dan atau dari rupiah ########

# Input:
#     - Masukan nama bank
#     - Menu Opsi:
#         1. IDR to 'mata uang asing'
#         2. 'mata uang asing' to IDR

# pilih 1:
#     - Masukan 'mata uang asing'
#     - Masukan nilai rupiah 
#             Output:
#                 - Nilai uang anda xxxx Rupiah dalam 'mata uang asing' adalah xxxxx

# pilih 2:
#     - Masukan 'mata uang asing'
#     - Masukan nilai rupiah
#             Output:
#                 - Nilai uang anda xxxx dalam 'mata uang asing' adalah xxxxx rupiah



import requests

def currency_exchange():

    Token =  'ql2fpT1uujZFiBao1zuGPdZe4j7OB94rqawf1kLl' #token API

    choice = input('Selamat datang di Moneychanger Mike\nPilih sesuka hati: \n Tekan 1 untuk menkonversi rupiah ke mata uang asing\n Tekan 2 untuk menkonversi mata uang asing ke rupiah\n')

    Bank = str(input('Masukan nama Bank: ')).lower() #variabel untuk memilih bank
    Currency=str(input('Masukan nama mata uang: ')).lower() #variabel untuk memilih mata uang asing

    url = f"https://api.kurs.web.id/api/v1?token={Token}&bank={Bank}&matauang={Currency}" #Link API
    datacurrency = (requests.get(url)).json() #Bentuk data format JSON dari url

    nilai_beli= datacurrency['beli'] #kurs nilai beli
    nilai_jual= datacurrency['jual'] #kurs nilai jual

    '''Buat 2 kondisi untuk memilih pilihan dari choice tersebut'''
    
    if choice == '1': #Jika pilih 1, maka rupiah akan diconvert ke mata uang yang dipilih
        uang = int(input('Berapa rupiah? ')) #Jumlah uang yang akan diconvert
        print(f"Nilai uang anda dalam {uang} rupiah adalah {uang/nilai_jual:,} {Currency.upper()}")
    else: #Jika pilih yang lain, makan mata uang lain aka diconvert ke rupiah
        uang = int(input(f'Berapa {Currency.upper()}? ')) #Jumlah uang yang akan diconvert
        print(f"Nilai uang anda {uang} {Currency.upper()} dalam rupiah adalah {uang*nilai_beli:,} rupiah")

currency_exchange()