 <h1 align="center">Bitscrush Incentive Testnet</h1>

## Query
1. Buatlah akun baru di menu Customer misal "bitscrush"
2. Kemudian klik Add Fund. Depositkan USDC 
3. Download file access-key.json

## Visual Code Studio
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

```
cd Bitscrush
```

4. Ganti file access-json sesuai dengan file kalian
5. Ganti mau sampai berapa untuk menjalankan query. Disini saja men-setting 10 Query. Anda bisa mengeditnya di kode baris 24 num_requests = 10 pada file query.py
6. Kemudian run
   
```
python query.py
```

## Termux
```
pkg upgrade
pkg install python
pip install --upgrade pip
```

```
pip install pycryptodome
```

```
pip install git
```

```
git clone https://github.com/PrastianHD/Bitscrush.git
```

```
cd Bitscrush
```

```
python query.py
```

### Edit dulu access-key.json yang sudah di download tadi
### Edit juga mau berapa kali run query
