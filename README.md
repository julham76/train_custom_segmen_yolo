LANGKAH AWAL
1. Siapkan gambar yang akan di segmen, lalu masukan ke folder di langkah 2
2. Buatkan folder untuk menyimpan gambar yang akan di segmen (misalkan: image)
3. Buatkan folder untuk menyimpan informasi JSON hasil segmen (misalkan: output)
4. Download aplikasi AnyLabelling (AnyLabeling-Windows-CPU-x64.exe)
5. Buka aplikasi AnyLabelling, lalu setting seperti pada gambar dibawah (open_dir untuk folder gambar yg akan di segmen, change_output_dir untuk folder simpan file JSON hasil segmen, save_automatically untuk simpan otomatis setiap pindah gambar) 
<img src="/asset/1.png" alt="prototype" width="300">
6. Bila garis segmen-nya dipakai untuk gambar berikutnya, maka gunakan setingan seperti pada gambar di bawah ini:
<img src="/asset/2.png" alt="prototype" width="300">
7. Untuk melakukan gambar segmentasi ke objek maka lakukan dengan memilih gambar polygon (gambar pada nomor 6 yang berbentuk segi 5), lalu dengan menggunakan mouse dan klik kiri ditandailah tepi-tepi dari objek yang diinginkan, seperti gambar di bawah ini:
<img src="/asset/3.png" alt="prototype" width="300">
8. Perlu diketahui bahwa AnyLabelling hanya cocok untuk labelling jenis COCO, sehingga untuk labelling ke YOLO perlu dikonversi
9. Bila sudah selesai melakukan segmentasi objek, maka lakukan EXPORT labelling ke COCO (Jgn lupa siapkan folder untuk menampung hasil EXPORT), caranya seperti urutan gambar di bawah ini
<img src="/asset/4.png" alt="prototype" width="300">
<img src="/asset/5.png" alt="prototype" width="300">

KONVERSI LABELLING COCO KE YOLO
1. Buka file "annotations.json" yang terletak di folder hasil EXPORT pada poin 9 di langkah awal.
2. PERLU DIKETAHUI BAHWA LABELLING Class COCO DIMULAI DARI ANGKA 1, SEDANGKAN LABELLING Class YOLO DIMULAI DARI ANGKA 0 (sesuaikan jika untuk banyak class). Untuk itu perlu dilakukan perubahan pada file annotation.json milik COCO dengan cara seperti pada gambar berikut:
<img src="/asset/6.png" alt="prototype" width="300">
<img src="/asset/7.png" alt="prototype" width="300">
3. Setelah dilakukan perubahan, maka gunakan google colab
