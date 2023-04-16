import numpy as np

# Membuat dictionary all_transaction untuk menampung data item yang dibeli
all_transaction = {}

class Transaction:  

  def __init__(self):
    print("Selamat datang di PacStore")
    self.customer_name = input('masukan nama Anda: ')
    self.id_generator = self.customer_name + "-" + str(np.random.randint(0, 10000, 1)[0])
    return( print(f'Id-transaksi anda adalah {self.id_generator}'))
    print("\n")
  def add_item(self):
    """
    Menambahkan detail nama item, jumlah item,
    dan harga per item yang akan dibeli
    """
    self.additional = "ya"
    while self.additional == "ya":
      self.item_name = str(input("Item apa yang ingin anda beli: ").lower())
      self.item_count = int(input("Berapa jumlah item yang dibeli: "))
      self.item_price = int(input("Berapa harga tiap item yang dibeli: "))
      self.additional = input("Apakah ada yang ingin anda beli lagi (ya/tidak): ").lower()
      self.total_per_item = self.item_count * self.item_price
      all_transaction[self.item_name] = [self.item_count, self.item_price, self.total_per_item]
      print("\n")
    
  def update_item_name(self, item_name, new_item_name):
    """
    fungsi untuk mengupdate nama item yang sebelumnya sudah di input
    """
    self.new_item_name = new_item_name
    all_transaction[self.new_item_name] = all_transaction.pop(self.item_name)
    return all_transaction

  def update_item_count(self, item_name, new_item_count):
    """
    fungsi untuk mengupdate jumlah item yang sebelumnya sudah di input
    """
    self.new_item_count = new_item_count
    all_transaction[self.item_name][0] = self.new_item_count 
    return all_transaction

  def update_item_price(self, item_name, new_item_price):
    """
    fungsi untuk mengupdate harga item yang sebelumnya sudah di input
    """
    self.new_item_price = new_item_price
    all_transaction[self.item_name][1] = self.new_item_price
    return all_transaction

  def delete_item(self, item_name):
    """
    fungsi untuk mendelete salah satu item berdasarkan nama item
    """
    all_transaction.pop(self.item_name)
    return all_transaction

  def reset_transaction(self):
    """
    fungsi untuk me-reset semua transaksi yang sudah di input
    """
    all_transaction.clear()
    return ("transaksi berhasil di reset")

  def check_order(self):
    """
    fungsi untuk mengecek kelengkapan data order
    """
    if type(self.item_name) == str and type(self.item_count == int) and type(self.item_price) == int:
      print("Pemesanan sudah sesuai")
    else:
      print("Terdapat kesalahan input data")
      print("\n")
    
    print("{:<15} {:<15} {:<15} {:<15}".format("Nama Item", "Jumlah Item", "Harga Per Item", "Total per Item"))
    for self.item_name, v in all_transaction.items():
      self.item_count, self.item_price, self.total_per_item = v
      print("{:<15} {:<15} {:<15} {:<15}".format(self.item_name, self.item_count, self.item_price, self.total_per_item))
  
  def total_price(self):
    """
    Menghitung total pembayaran berdasarkan jumlah item, harga item, 
    dan diskon yang diterima
    """
    # default discount 
    discount = 1
    overall_price = 0
    for key in all_transaction:
      quantity = all_transaction[key][0]
      price = all_transaction[key][1]
      overall_price += quantity * price
    if overall_price > 500_000:
      discount = 0.90
    elif overall_price > 300_000:
      discount = 0.98
    elif overall_price > 200_000:
      discount = 0.95
    final_price = overall_price * discount
    print(f"Total harga belanja Anda sebesar Rp{round(final_price)}")

    # menambahkan jumlah yang dibayar dan kembalian (jika ada)
    payment = int(input("Berapa total pecahan yang akan Anda bayar?: "))
    calculate = int(payment - final_price)
    if calculate < 0:
      print(f"Uang anda kurang sebesar Rp{-calculate}")
    elif calculate == 0:
      print("Uang pas. Terima kasih telah berbelanja disini")
    else:
      print(f"Anda mendapatkan kembalian sebesar Rp{calculate}. Terima kasih telah berbelanja disini")