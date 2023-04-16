# Self Service Cashier Project

## Objectives
- Membuat program untuk melakukan self service cashier bagi customer yang ingin membeli barang
- Customer perlu memasukkan nama_customer, nama_item, jumlah_item, dan harga_item untuk diproses
- Program akan memproses data yang diinput untuk menghitung total harga belanja
- Apabila ada kesalahan atau ada update data yang telah input, customer dapat melakukan update atau remove item
- Program juga dirancang dengan diskon yang berlaku saat ini:
  - Diskon 5%, jika total belanja > Rp200.000
  - Diskon 8%, jika total belanja > Rp300.000
  - Diskon 10%, jika total belanja > Rp500.000


## Flowchart
![Flowchart - Super Cashier](https://user-images.githubusercontent.com/75265653/232308776-435a5192-3060-485b-a06c-83b3cc2b17f3.jpeg)


## Kode Program
1. Membuat dictionary untuk menyimpan data customer
![Screenshot 2023-04-16 at 7 18 33 PM](https://user-images.githubusercontent.com/75265653/232309472-82e62d66-90b9-4293-8b73-459a8cc4f43f.png)

2. Customer membuat ID transaksi customer
![Screenshot 2023-04-16 at 7 13 38 PM](https://user-images.githubusercontent.com/75265653/232309125-984222bd-95d4-40e8-9a75-44fe73df65e1.png)

2. Customer memasukkan nama item, jumlah item dan harga item yang dibeli
![Screenshot 2023-04-16 at 7 14 58 PM](https://user-images.githubusercontent.com/75265653/232309180-6e67ff70-2bd0-406b-8da1-ff892d1d222f.png)

3. Customer bisa melakukan update item pada nama, jumlah, atau harga bila ada kesalahan dalam input data
![Screenshot 2023-04-16 at 7 16 05 PM](https://user-images.githubusercontent.com/75265653/232309277-97d4f367-76ee-47f5-82f1-5cc178ac9554.png)

4. Customer bisa menghapus salah satu/seluruh item bila ingin membatalkan transaksi
![Screenshot 2023-04-16 at 7 19 27 PM](https://user-images.githubusercontent.com/75265653/232309504-ac21325f-6499-4868-987b-e6e4024b78e5.png)

5. Customer dapat mengecek kembali item yang dipesan
![Screenshot 2023-04-16 at 7 20 27 PM](https://user-images.githubusercontent.com/75265653/232309547-22b074cc-d8c5-4840-8b95-9c8ef7d27f0b.png)

6. Customer dapat menampilkan total pembelian yang perlu dibayar (ada diskon sesuai objective program)
![Screenshot 2023-04-16 at 7 21 13 PM](https://user-images.githubusercontent.com/75265653/232309591-87c6f7b3-9372-4ac2-b652-5097cc0c0194.png)

## Hasil Test Case
![Screenshot 2023-04-16 at 7 26 49 PM](https://user-images.githubusercontent.com/75265653/232309889-1f6aaec5-883a-4b61-afbd-31e9f77ab471.png)



## Conclusion
Dalam pengembangan program cashier self-service ini, ada banyak hal yang perlu dipertimbangkan karena program ini masih memiliki keterbatasan yang mengakibatkan banyak masalah yang mungkin terjadi ketika digunakan oleh pengguna. Sistem self-service memiliki kelebihan dan kekurangan. Dari sisi kelebihannya, sistem ini dapat mengurangi biaya operasional. Namun, di sisi lain, jika terjadi masalah seperti bug yang fatal atau vulnerability, ini bisa menyebabkan kerugian yang besar, seperti yang terjadi pada perusahaan besar. Oleh karena itu, penting untuk terus mengembangkan program ini hingga menjadi program self-service yang lebih baik dan membantu pebisnis dalam menekan biaya operasional.
