# Laporan Proyek Machine Learning - Joko Prabowo

## Domain Proyek

## Business Understanding

### Problem Statements
Berdasarkan latar belakang yang telah dipaparkan. Berikut adalah daftar permasalahan yang perlu diselesaikan dalam proyek ini:
<ul>
  <li></li>
  <li></li>
  <li></li>
</ul>

### Goals
<ul>
  <li></li>
  <li></li>
  <li></li>
</ul>

### Solution Statements
<ul>
  <li></li>
  <li></li>
  <li></li>
</ul>

## Data Undestanding
Data yang digunakan dalam proyek ini merupakan data yang dipublikasikan oleh Dhruvil Dave, yang merupakan data mengenai permainan berbasis android yang dikumpulkan melalui Google Play dan telah diklasifikasikan kedalam setiap kategorinya dimana setiap kategori setidaknya memiliki 100 permainan. Keterangan lebih lanjut mengenai dataset ini adalah sebagai berikut:

<div align="center">
  
  Indeks|Keterangan
  ---|---
  Title|Top Games on Google Play Store
  Source|[Kaggle](https://www.kaggle.com/datasets/dhruvildave/top-play-store-games)
  Uploader|Dhruvil Dave
  Owner|Google Play
  License|Database: Open Database, Contents: © Original Authors
  Usability|10.00
  Tags|Education, Games, Video Games
  
</div>

Dalam dataset ini memiliki beberapa fitur yang tersimpan kedalam beberapa variabel sebagai berikut:

<div align="center">

  Variabel|Keterangan
  ---|---
  rank|peringkat dalam kategori tertentu
  title|judul game
  total rating|jumlah total penilaian
  installs|perkiraan tonggak instalasi
  average rating|penilaian rata-rata dari bintang 5
  growth (30 days)|pertumbuhan persen dalam 30 hari
  growth (60 days)|pertumbuhan persen dalam 60 hari
  price|harga dalam dolar
  category|kategori permainan
  5 star ratings|jumlah penilaian bintang 5
  4 star ratings|jumlah penilaian bintang 4
  3 star ratings|jumlah penilaian bintang 3
  2 star ratings|jumlah penilaian bintang 2
  1 star ratings|jumlah penilaian bintang 1
  paid|permainan berbayar atau tidak
  
</div>

Keterangan untuk setiap kolom dari dataset ini adalah sebagai berikut:

<div align="center">

  Index|Valid|Mismatched|Missing|
  ---|---|---|---
  rank|1730|0|0|0
  title|1730|0|0|0
  total rating|1730|0|0|0
  installs|1730|0|0|0
  average rating|1730|0|0|0
  growth (30 days)|1730|0|0|0
  growth (60 days)|1730|0|0|0
  price|1730|0|0|0
  category|1730|0|0|0
  5 star ratings|1730|0|0|0
  4 star ratings|1730|0|0|0
  3 star ratings|1730|0|0|0
  2 star ratings|1730|0|0|0
  1 star ratings|1730|0|0|0
  paid|1730|0|0|0
  
</div>

Berdasarkan tabel diatas dapat disimpulkan bahwa pada dataset ini terdapat `15 kolom` dengan `1730 baris` dimana setiap barisnya merupakan data yang valid tanpa ada satupun data yang hilang.

## Exploratory Data Analysis

### Deskripsi Variabel
Berdasarkan detail deskripsi dari data ditemukan bahwa:

<div align="center">

#|Column|Non-Null Count|Dtype  
---|---|---|---  
 0|rank|1730 non-null|int64  
 1|title|1730 non-null|object 
 2|total ratings|1730 non-null|int64  
 3|installs|1730 non-null|object 
 4|average rating|1730 non-null|int64  
 5|growth (30 days)|1730 non-null|float64
 6|growth (60 days)|1730 non-null|float64
 7|price|1730 non-null|float64
 8|category|1730 non-null|object 
 9|5 star ratings|1730 non-null|int64  
 10|4 star ratings|1730 non-null|int64  
 11|3 star ratings|1730 non-null|int64  
 12|2 star ratings|1730 non-null|int64  
 13|1 star ratings|1730 non-null|int64  
 14|paid|1730 non-null|bool
  
</div>

Berdasarkan data diatas dapat terlihat bahwa:
*   Terdapat 4 kolom kategorik dengan tipe data object dan bool, yaitu `title`, `installs`, `category`, dan `paid`
*   Terdapat 11 kolom numerik dengan tipe data int64, dan float64, yaitu `rank`, `total ratings`, `average rating`, `growth (30 days)`, `growth (60 days)`, `price`, `5 star ratings`, `4 star ratings`, `3 star ratings`, `2 star ratings`, dan `1 star ratings`


<p>Kemudian melalui data deskripsi juga ditemukan informasi statistik dari setiap kolom diantaranya:</p>

 |rank|total ratings|average rating|growth (30 days)|growth (60 days)|price|5 star ratings|4 star ratings|3 star ratings|2 star ratings|1 star ratings
---|---|---|---|---|---|---|---|---|---|---
count|1730.000000|1.730000e+03|1730.000000|1730.000000|1730.000000|1730.000000|1.730000e+03|1.730000e+03|1.730000e+03|1.730000e+03|1.730000e+03
mean|50.386705|1.064332e+06|3.908092|321.735896|122.554971|0.010942|7.622315e+05|1.164366e+05|5.706307e+04|2.710336e+04|1.014950e+05
std|28.936742|3.429250e+06|0.290973|6018.914507|2253.891703|0.214987|2.538658e+06|3.021631e+05|1.495314e+05|8.154542e+04|4.083745e+05
min|1.000000|3.299300e+04|2.000000|0.000000|0.000000|0.000000|1.397500e+04|2.451000e+03|7.180000e+02|2.660000e+02|5.450000e+02
25%|25.000000|1.759992e+05|4.000000|0.100000|0.200000|0.000000|1.277300e+05|2.064300e+04|9.652500e+03|4.262250e+03|1.281200e+04
50%|50.000000|4.286065e+05|4.000000|0.500000|1.000000|0.000000|2.964340e+05|5.098050e+04|2.507800e+04|1.067550e+04|3.368600e+04
75%|75.000000|8.837970e+05|4.000000|1.700000|3.300000|0.000000|6.198358e+05|1.018140e+05|5.229500e+04|2.322875e+04|8.015725e+04
max|100.000000|8.627313e+07|4.000000|227105.700000|69441.400000|7.490000|6.354677e+07|5.404966e+06|3.158756e+06|2.122183e+06|1.249592e+07

Dimana:
<ul>
  <li>count merupakan jumlah sampel,</li>
  <li>mean merupakan nilai rata-rata,</li>
  <li>std merupakan standar deviasi,</li>
  <li>min merupakan nilai minimum,</li>
  <li>25% merupakan kuartil pertama,</li>
  <li>50% merupakan kuartil kedua,</li>
  <li>75% merupakan kuartil ketiga, dan</li>
  <li>max merupakan nilai maximum.</li>
</ul>

### Univariate analysis
<div align="center">
  <img src="images/total_game_by_category.png" />
</div>
<p>Data visual diatas merupakan diagram batang yang memvisualisasikan total permainan yang ada pada setiap kategori, dan dari sekian banyaknya kategori permainan "Game Card" atau permainan kartu merupakan kategori permainan yang memiliki total jumlah permainan terbanyak.</p>

<div align="center">
  <img src="images/paid_game_percentage.png"/>
</div>
<p>Data visual diatas merupakan diagram lingkaran yang memvisualisasikan jenis permainan yang dibedakan menjadi permainan gratis, dan berbayar. Dari data visual tersebut dapat terlihat bahwa mayoritas permainan yang terdapat dalam dataset ini merupakan permainan gratis dengan persentase mencapai 99.6%.</p>

<div align="center">
  <img src="images/top10_games_based_on_total_ratings.png"/>
</div>
<p>Data visual diatas merupakan diagram batang yang memvisualisasikan 10 permainan teratas dengan total penilaian paling tinggi. Dari data  tersebut permainan Garena Free Fire - World Series menempati urutan pertama dengan lebih dari 8e7 penilaian atau lebih dari 80.000.000 total penilaian.</p>

<div align="center">
  <img src="images/top10_games_based_on_user_growth_in_30_days.png"/>
</div>
<p>Data visual diatas menampilkan 10 permainan dengan tingkat pertumbuhan pengguna paling tinggi dalam 30 hari.</p>

<div align="center">
  <img src="images/top10_games_based_on_user_growth_in_60_days.png"/>
</div>
<p>Data visual diatas menampilkan 10 permainan dengan tingkat pertumbuhan pengguna paling tinggi dalam 60 hari.</p>

### Multivariate analysis
<div align="center">
  <img src="images/heat_map_correlations.png"/>
</div>
<p>Data visual diatas merupakan heatmap atas setiap data numerik dalam dataset ini beserta nilai korelasi antar setiap fitur.</p>

<div align="center">
  <img src="images/correlation_between_user_growth_in_30_days_and_user_growth_in_60_days.png"/>
</div>
<p>Data visual diatas merupakan diagram tebar yang memvisualisasikan korelasi antara pertumbuhan pengguna dalam 30 hari dan pertumbuhan pengguna dalam 60 hari. Berdasarkan nilai korelasi yang didapatkan melalui heatmap (-0.0026) dan data visual diatas disimpulkan bahwa fitur pertumbuhan pengguna dalam 30 hari dan pertumbuhan pengguna dalam 60 hari memiliki hubungan yang lemah.</p>

<div align="center">
  <img src="images/correlation_between_total_rating_and_user_growth_in_30_days.png"/>
</div>
<p>Data visual diatas merupakan diagram tebar yang memvisualisasikan korelasi antara total penilaian dan pertumbuhan pengguna dalam 30 hari. Berdasarkan nilai korelasi yang didapatkan melalui heatmap (-0.0089) dan data visual diatas disimpulkan bahwa fitur total penilaian dan pertumbuhan pengguna dalam 30 hari memiliki hubungan yang lemah</p>

<div align="center">
  <img src="images/correlation_between_total_rating_and_user_growth_in_60_days.png"/>
</div>
<p>Data visual diatas merupakan diagram tebar yang memvisualisasikan korelasi antara total penilaian dan pertumbuhan pengguna dalam 60 hari. Berdasarkan nilai korelasi yang didapatkan melalui heatmap (-0.0045) dan data visual diatas disimpulkan bahwa fitur total penilaian dan pertumbuhan pengguna dalam 60 hari memiliki hubungan yang lemah</p>

<div align="center">
  <img src="images/correlation_between_total_rating_and_5_star_ratings.png"/>
  <img src="images/correlation_between_total_rating_and_4_star_ratings.png"/>
  <img src="images/correlation_between_total_rating_and_3_star_ratings.png"/>
  <img src="images/correlation_between_total_rating_and_2_star_ratings.png"/>
  <img src="images/correlation_between_total_rating_and_1_star_ratings.png"/>
</div>
<p>Data visual diatas merupakan diagram tebar yang memvisualisasikan korelasi antara total penilaian dengan penilaian 5 bintang, penilaian 4 bintang, penilaian 3 bintang, penilaian 2 bintang, dan penilaian 1 bintang. Berdasarkan data visual diatas total penilaian memiliki hubungan yang kuat dengan penilaian 5 bintang, penilaian 4 bintang, penilaian 3 bintang, penilaian 2 bintang, dan penilaian 1 bintang. Hal ini dibuktikan melalui skor korelasi yang diperoleh dari heatmap secara berurutan yaitu 1, 0.95, 0.98, 0.97, dan 0.94.</p>

## Data Preparation

### Menangani missing value
<p>Sebelum data diproses lebih lanjut, data terlebih dahulu akan dibersihkan dari data yang mengandung nilai kosong, dan data terduplikat. Hal ini dilakukan agar data-data tidak lengkap tersebut tidak menggangu dalam pengimplementasian model nanti.</p>

```python
df.isnull().sum()
````

<p>Menggunakan kode diatas, didapatkan bahwa tidak ada data kosong dalam dataset ini.</p>

```python
print(len(df[df.duplicated(subset='title')]))
```

<p>Lalu menggunakan kode diatas, diketahui terdapat 55 baris dengan judul permainan yang sama dalam dataset ini yang kemudian perlu dihapus. Sehingga terdapat total 1675 baris dengan 15 kolom setelah data terduplikat dihapus.</p>

### Menyederhanakan kategori
<p>Proses ini dilakukan untuk menyederhanakan kategori dalam permainan kedalam bentuk dasarnya agar lebih mudah diimplementasikan kedalam model nanti</p>
<p>Berikut adalah daftar kategori sebelum disederhanakan:</p>

`GAME ACTION`, `GAME ADVENTURE`, `GAME ARCADE`, `GAME BOARD`, `GAME CARD`, `GAME CASINO`, `GAME CASUAL`, `GAME EDUCATIONAL`, `GAME MUSIC`, `GAME PUZZEL`, `GAME RACING`, `GAME ROLE PLAYING`, `GAME SIMULATION`, `GAME SPORTS`, `GAME STRATEGY`, `GAME TRIVIA`, dan `GAME WORD`

<p>Berikut adalah kategori permainan setelah disederhanakan:</p>

`action`, `adventure`, `arcade`, `board`, `card`, `casino`, `casual`, `educational`, `music`, `puzzel`, `racing`, `role playing`, `simulation`, `sports`, `strategy`, `trivia`, dan `word`

### Menambahkan data penting
<p>Proses ini dilakukan untuk membuat dataframe baru yang diperlukan dalam proses Collaborative filtering, karena dalam proses tersebut membutuhkan data pengguna yang telah memainkan permainan agar menjadi acuan untuk memberikan rekomendasi atas permainan yang belum pernah dimainkan berdasarkan penilaian terhadap permainan yang telah dimainkan. Proses ini dilakukan karena dataset review yang dibutuhkan ini tidak terlampir dalam sumber dataset yang digunakan dalam proyek ini.</p>
<p>Berikut adalah dataframe baru yang dinamakan review untuk menampung semua data yang dibutuhkan:</p>

<div align="center">

  | |userId|gameId|rating
  ---|---|---|---
  0|52c503fd-1a1f-43f8-a710-8d3e39b065cd|15997c2d-8dd9-4fb6-bed1-748ba829c950|1
  1|cdf9fa37-8de2-4ddb-b0d7-faa2a76d5024|89698ff9-93db-4312-aa8b-4a4fa7051b54|4
  2|6af19149-b66c-4728-a49f-03ec8b8da828|bb89b8cd-b259-4bbb-a4bb-e3e8cdccdb74|4
  3|76fb4a71-3764-4508-ad85-c238d089c15d|42e7bcac-5e97-4f46-a277-17ddb6d4ede8|1
  4|b76b8bd4-7cc2-4081-ad38-f114227b1ea2|b602c45d-c173-4eb7-912f-1d6f7fc0d715|2
</div>

Yang mana `userId` merupakan identitas unik milik pengguna, `gameId` merupakan identitas unik milik permainan, dan `rating` merupakan penilaian pengguna terhaadap permainan tersebut dengan skala 1 sampai 5. Dan melalui data diatas pula terjadi perubahan terhadap dataset permainan, karena `gameId` ditambahkan untuk memberikan identitas terhadap semua permainan.

### TF-IDF vectorizer
<p>Proses ini dilakukan untuk membuat representasi numerik terhadap fitur yang akan digunakan sebagai tolak ukur atau acuan terhadap permainan yang akan direkomendasikan, fitur penting tersebut adalah fitur kategori. Fitur ini akan ditransformasikan pada bentuk dasarnya yang kemudian akan direpresentasikan ke dalam fitur numerik</p>

title|action|sports|simulation|action|adventure|arcade|racing|casino|action|music
---|---|---|---|---|---|---|---|---|---|---								
CarX Highway Racing|0.0|0.0|0.0|0.0|0.0|0.0|1.0|0.0|0.0|0.0
Travelling Millionaire|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0
Pepi House: Happy Family|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0
PPSSPP - PSP emulator|1.0|0.0|0.0|1.0|0.0|0.0|0.0|0.0|1.0|0.0
Gangstar Vegas: World of Crime|1.0|0.0|0.0|1.0|0.0|0.0|0.0|0.0|1.0|0.0

<p>Tabel diatas merupakan representasi dari hasil proses TF-IDF terhadap beberapa sampel permainan.</p>

### Encoding features
<p>Proses ini dilakukan untuk mengubah fitur kategorik yang dibutuhkan dalam proses menjadi fitur numerik, hal ini terjadi karena model yang akan digunakan nanti hanya menerima fitur numerik sehingga setiap fitur kategorik yang akan menjadi atribut perlu di encode kedalam numerik</p>

<div align="center">

| |userId|gameId|rating|user|game
---|---|---|---|---|---
0|640457f7-b759-474b-93c2-c2db26a789dd|f29cc637-d036-40f1-9c09-57fd4ada8295|3|0|0
1|6682981f-e67c-419e-8051-064016a6de99|f2401433-f461-4ebc-ab28-788933e0e4fb|2|1|1
2|78c4d317-69f6-4a91-b744-e897c92bfc47|80ba3fc1-8a72-4779-9b2b-8672db15e70e|1|2|2
3|dc63754a-ee5e-49bd-984d-2c5439299c88|316fd04e-7bd2-4122-a2fb-a18bf293a3a0|3|3|3
4|228d80b2-df94-4903-9a6d-938e8ef77aba|58486875-5d6c-4904-b511-12b61cee1432|4|4|4
</div>

Seperti yang terlihat pada tabel diatas, kolom `user`, dan `game` merupakan hasil encode dari kolom `userId`, dan `gameId` yang kemudian dapat digunakan untuk proses selanjutnya.

## Model development

### Content based filtering
Proses ini dilakukan untuk mengimplementasikan beberapa data yang sudah disiapkan sebelumnya untuk kemudian memberikan hasil berupa rekomendasi yang didasari pada data-data tersebut. Proses ini diawali dengan membuat model `Cosine Similarity`, model ini merupakan model yang digunakan untuk menghitung derajat kesamaan terhadap dua objek yang dinyatakan dalam dua vektor. Dengan mengimplementasikan hasil matriks dari model `TI-IDF` kedalam model `Cosine Similarity`, model tersebut akan menghitung derajat kesamaan berdasarkan kategori permainan dari setiap permainan dan melalui hasil dari model tersebut, proses ini dapat memberikan rekomendasi permainan berdasarkan permainan yang menjadi masukan.

Dalam kasus ini permainan `Brawl Stars` digunakan sebagai masukan, yang kemudian menghasilkan:

<div align="center">

 | |title|category
---|---|---
0|Garena Free Fire- World Series|action
1|FRAG Pro Shooter|action
2|Nebulous.io|action
3|Sea Battle 2|action
4|War Machines: Tank Battle - Army & Military Games|action
</div>

Tabel diatas merupakan 5 rekomendasi permainan yang dihasilkan berdasarkan masukan yang diberikan. `Brawl Stars` merupakan permainan dengan kategori permainan `action`, sehingga proses ini menghasilkan rekomendasi 5 permainan dengan kategori `action` sesuai dengan kategori permainan yang menjadi masukan.

### Collaborative filtering
Proses ini bekerja mulai dari mempelajari aktivitas pengguna dalam memainkan permainan, oleh karenanya proses ini membutuhkan `review` dataset yang telah dibuat sebelumnya. Melalui dataset tersebut proses ini mempelajari mulai dari permainan yang telah dimainkan pengguna, kepuasan pengguna terhadap permainan yang terlihat dari penilaian pengguna terhadap permainan tersebut, sampai ke permainan yang belum pengguna tersebut mainkan. Dengan menggunakan kolom-kolom hasil encoding sebelumnya seperti `userId`, dan `gameId` serta kolom `rating` yang diubah kedalam bentuk `float`, model dalam proses ini akan menganalisis dan mencari pola berdasarkan data-data tersebut dan kemudian model ini akan melakukan pencarian semantik sehingga dapat memberikan hasil berupa rekomendasi permainan yang relevan.

Dalam kasus ini aktivitas dari pengguna dengan id `9a664c85-c632-4ee3-81b1-5403d5e582c5` digunakan dan menghasilkan:

<div align="center">

title|category
---|---
Archero|action
Adventure Time: Heroes of Ooo|adventure
Rise Up|arcade
PianoTiles 3|music
Beat Shooter|music
ضربة معلم - لعبة الغاز مسلية|puzzle
Bubble Shooter: Panda Pop!|puzzle
Fast Racing 3D|racing
Assassin's Creed Rebellion: Adventure RPG|role playing
Fashion Empire - Dressup Boutique Sim|role playing
</div>

Tabel diatas merupakan 10 permainan yang direkomendasikan dari proses ini berdasarkan dari aktivitas pengguna dengan id `9a664c85-c632-4ee3-81b1-5403d5e582c5`, 10 permainan tersebut merupakan permainan dengan kategori yang sama dengan permainan-permainan yang biasa dimainkan pengguna yang direkomendasikan dengan rating tertinggi.

## Evaluation

