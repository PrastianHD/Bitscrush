 <h1 align="center">Bitscrush Incentive Testnet</h1>

### Query
1. Buatlah akun baru di menu Customer misal "bitscrush"
2. Kemudian klik Add Fund. Depositkan USDC 
3. Download file access-key.json

### Visual Code Studio
1. Create a folder Bitscrush
2. Open in Visual Code Studio
3. Open Terminal
  
```
pip install --upgrade pip
```

```
pip install pycryptodome
```

```
git clone https://github.com/PrastianHD/Bitscrush.git
```

4. Coba Run terlebih daulu untuk memastikan apakah kode nya work
5. Ganti file access-json sesuai dengan file kalian
6. Ganti mau sampai berapa untuk menjalankan query. Disini saja men-setting 10 Query. Anda bisa mengeditnya di kode baris 24 num_requests = 10 pada file query.py
7. Kemdudian run
```
python query.py
```
