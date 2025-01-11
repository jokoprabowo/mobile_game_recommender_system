# -*- coding: utf-8 -*-
"""Recommender_system_game.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/153iw1CltGBbTyrMjkXH6n2K6B0ClofpB

# **Sistem rekomendasi**
Nama: Joko Prabowo <br>
Username: jprabowo <br>
email: jokoprabowwo4550@gmail.com
"""

import textwrap
import uuid
import random
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""## **Data Loading**
---
Proses dalam menyimpan dan memuat data untuk diproses lebih lanjut
"""

url = 'https://github.com/jokoprabowo/mobile_game_recommender_system/releases/download/dataset/android-games.csv'
df = pd.read_csv(url)
df.head()

row, col = df.shape
print(f'Jumlah baris: {row}')
print(f'Jumlah kolom: {col}')

"""Dengan begitu dalam dataset ini terdapat total 1730 baris dengan 15 kolom

## **Exploratory Data Analysis**
---
 Proses untuk menganalisis karakteristik, menemukan pola, anomali, dan memeriksa asumsi pada data.

### Deskripsi Variabel
---
Proses untuk mendeskripsikan setiap variabel agar variabel tersebut dapat dimengerti secara umum

Berdasarkan informasi dari kaggle, variable-variable diatas dapat diartikan:

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
"""

df.info()

"""Berdasarkan data diatas dapat terlihat bahwa:
*   Terdapat 8 kolom dengan tipe data int64,
*   Terdapat 3 kolom dengan tipe data float64,
*   Terdapat 3 kolom dengan tipe data object, dan
*   Terdapat 1 kolom dengan tipe data boolean.


"""

df.describe()

"""Tabel diatas memperlihatkan informasi statistik pada setiap kolom yaitu:

Variabel|Keterangan
---|---
count|jumlah sampel
mean|nilai rata-rata
std|standar deviasi
min|nilai minimum
25%|kuartil pertama
50%|kuartil kedua
75%|kuartil ketiga
max|nilai maximum

### Unvariate Analysis
---
Proses untuk menganalisis data terhadap satu variabel secara mandiri
"""

plt.figure(figsize=(10, 5))
color = sns.color_palette('crest')
plt.barh(df['category'].value_counts().index, df['category'].value_counts(), color=color)
plt.title('Jumlah Game Berdasarkan Kategori')
plt.xlabel('Jumlah Game')
plt.ylabel('Kategori')
plt.show()

"""Berdasarkan data visual diatas, dari sekian banyaknya kategori game "Game Card" atau permainan kartu merupakan kategori yang memiliki total jumlah game terbanyak"""

status = df['paid'].value_counts()
status.index = ['Gratis', 'Berbayar']

plt.figure(figsize=(10, 5))
colors = sns.color_palette('crest')
plt.pie(status, labels=status.index, autopct='%1.1f%%', colors=colors)
plt.title('Persentase game berbayar')
plt.show()

"""Berdasarkan pie chart diatas terlihat bahwa mayoritas game yang terdapat dalam dataset ini merupakan game gratis dengan persentase mencapai 99.6%"""

top10_game = df.sort_values(by='total ratings', ascending=False).head(10)
top10_game = top10_game[['title', 'total ratings']]
top10_game

plt.figure(figsize=(10, 5))
color = sns.color_palette('crest')
plt.barh(top10_game['title'], top10_game['total ratings'], color=color)
plt.title('Top 10 Game Berdasarkan Jumlah Rating')
plt.xlabel('Jumlah Rating')
plt.ylabel('Judul Game')
plt.show()

"""Data visualisasi diatas menunjukan 10 game dengan total rating terbanyak, dimana game Garena Free Fire - World Series menempati urutan pertama dengan lebih dari 8e7 rating atau lebih dari 80.000.000 total rating"""

top10_30days = df.sort_values(by='growth (30 days)', ascending=False).head(10)
top10_30days = top10_30days[['title', 'growth (30 days)']]

plt.figure(figsize=(10, 5))
color = sns.color_palette('crest')
plt.barh(top10_30days['title'], top10_30days['growth (30 days)'], color=color)
plt.title('Top 10 Game Berdasarkan Pertumbuhan dalam 30 Hari')
plt.xlabel('Pertumbuhan (%)')
plt.ylabel('Judul Game')
plt.show()

"""Data visualisasi diatas menunjukan top 10 game dengan tingkat pertumbuhan tertinggi dalam 30 hari."""

top10_60days = df.sort_values(by='growth (60 days)', ascending=False).head(10)
top10_60days = top10_60days[['title', 'growth (60 days)']]

plt.figure(figsize=(10, 5))
color = sns.color_palette('crest')
plt.barh(top10_60days['title'], top10_60days['growth (60 days)'], color=color)
plt.title('Top 10 Game Berdasarkan Pertumbuhan dalam 60 Hari')
plt.xlabel('Pertumbuhan (%)')
plt.ylabel('Judul Game')
plt.show()

"""Data visualisasi diatas menunjukan top 10 game dengan tingkat pertumbuhan tertinggi dalam 60 hari.

### Multivariate analysis
---
Proses yang digunakan untuk menganalisis hubungan antara dua variabel atau lebih
"""

numerical = df[['total ratings', '5 star ratings', '4 star ratings', '3 star ratings', '2 star ratings', '1 star ratings', 'average rating', 'price', 'growth (30 days)', 'growth (60 days)']]
plt.figure(figsize=(10, 5))
sns.heatmap(numerical.corr(), annot=True, cmap='crest')
plt.show()

plt.figure(figsize=(10, 5))
sns.scatterplot(data=df, x='growth (30 days)', y='growth (60 days)', palette='crest')
plt.title('Korelasi antara pertumbuhan pengguna dalam 30 hari dan pertumbuhan pengguna dalam 60 hari')
plt.show()

"""Berdasarkan nilai korelasi yang didapatkan melalui heatmap (-0.0026) dan data visual diatas disimpulkan bahwa fitur growth (30 days) dan growth (60 days) memiliki hubungan yang lemah"""

plt.figure(figsize=(10, 5))
sns.scatterplot(data=df, x='total ratings', y='growth (30 days)', palette='crest')
plt.title('Korelasi antara total rating dan pertumbuhan pengguna dalam 30 hari')
plt.show()

"""Berdasarkan nilai korelasi yang didapatkan melalui heatmap (-0.0089) dan data visual diatas disimpulkan bahwa fitur total rating dan growth (30 days) memiliki hubungan yang lemah"""

plt.figure(figsize=(10, 5))
sns.scatterplot(data=df, x='total ratings', y='growth (60 days)', palette='crest')
plt.title('Korelasi antara total rating dan pertumbuhan pengguna dalam 60 hari')
plt.show()

"""Berdasarkan nilai korelasi yang didapatkan melalui heatmap (-0.0045) dan data visual diatas disimpulkan bahwa fitur total rating dan growth (60 days) memiliki hubungan yang lemah"""

ratings = df[['5 star ratings', '4 star ratings', '3 star ratings', '2 star ratings', '1 star ratings']]
for col in ratings.columns:
  plt.figure(figsize=(10, 5))
  sns.scatterplot(data=df, x=col, y='total ratings', palette='crest')
  plt.title(f'Korelasi antara total rating dan {col}')
  plt.show()

"""Namun berdasarkan data visual diatas total rating memiliki hubungan yang kuat dengan 5 star ratings, 4 star ratings, 3 star ratings, 2 star ratings, dan 1 star ratings. Hal ini dibuktikan melalui skor korelasi yang diperoleh dari heatmap secara berurutan yaitu 1, 0.95, 0.98, 0.97, dan 0.94.

## **Data preparation**
---
Proses untuk menyiapkan data mentah agar dapat diproses dan dianalisis lebih lanjut.

### Menangani missing value
---
Proses untuk menghapus kolom yang bernilai kosong (NaN) serta terduplikat, untuk mengatasi data ganda dan data yang tidak lengkap
"""

# menampilkan data kosong
df.isnull().sum()

"""Berdasarkan data diatas, tidak ditemukan data kosong dalam dataset ini.

Kemudian mari melakukan cek terhadap data terduplikasi dalam kasus data ini cek judul game yang terduplikasi
"""

# menampilkan data terduplikasi
print(len(df[df.duplicated(subset='title')]))

"""Berdasarkan data diatas terdapat 55 data dengan judul game yang sama yang harus dihapus"""

# menghapus data terduplikasi
df.drop_duplicates(subset='title', inplace=True)
df.shape

"""Sesudah menghapus data duplikat dataset game memiliki total 1675 baris dari yang sebelumnya 1730 baris

### Menyederhanakan kategori
---
Proses untuk melakukan penyederhanaan kategori agar kategori yang ada dalam dataset ini hanya terdiri dari 1 kata
"""

df['category'] = df['category'].str.lower()
df['category'] = df['category'].str.split(' ', n=1).str.get(-1)
df['category'].unique()

"""### Menambahkan data penting
---
Proses untuk menambahkan dataa yang kurang untuk melakukan proses selanjutnya

Dalam data yang diperoleh dari kaggle ini belum ada dataset untuk review  yang sebenarnya diperlukan dalam proses collaborative filtering oleh karenanya data tersebut akan dibuat terlebih dahulu

Namun sebelum itu ada hal yang perlu ditambahkan dalam dataset game agar dapat membuat contoh dataset review yaitu game id
"""

df.insert(0, 'gameId', '')
df['gameId'] = df.apply(lambda x: uuid.uuid4(), axis=1)
df.head()

"""Membuat dataframe review"""

reviews = pd.DataFrame(columns=['userId', 'gameId', 'rating'])
reviews.head()

# mengisi dataframe

# membuat user id
userId = [uuid.uuid4() for x in range(200)]
# menyimpan game id ke dalam list
gameId = df['gameId'].unique().tolist()

for x in range(len(gameId)):
  reviews.loc[len(reviews.index)] = [random.choice(userId), gameId[x], random.randint(1, 5)]

reviews.head()

"""Tabel diatas menandakan bahwa dataset review telah berhasil dibuat

Selanjutnya siapkan dataset untuk review dengan kolom `userId`, 'gameId', dan `rating`

## **Model development**
---
Proses sistematis dalam membuat model untuk menyelesaikan masalah.

### Content based filtering
---
Metode yang digunakan data untuk memberikan rekomendasi berdasarkan karakteristik atau konten dari item yang ingin dianalisis atau direkomendasikan

**TF-IDF Vectorizer** <br>
tahap ini dilakukan untuk menemukan representasi fitur penting untuk setiap kategori game
"""

tf = TfidfVectorizer()
tf.fit(df['category'])
tf.get_feature_names_out()

"""Kemudian transformasikan kedalam bentuk matrix"""

tfidf_matrix = tf.fit_transform(df['category'])

tfidf_matrix.shape

tfidf_matrix.todense()

tfidf_matrix = tf.fit_transform(df['category'])

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=df.title
).sample(10, axis=1, replace=True).sample(5, axis=0)

"""Data diatas merupakan contoh dari matriks tf-idf terhadap 5 contoh game yang ada

**Cosine similarity** <br>
Tahap ini dilakukan untuk mengukur derajat kesamaan antar game
"""

cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

cosine_sim_df = pd.DataFrame(cosine_sim, index=df['title'], columns=df['title'])
print('Shape:', cosine_sim_df.shape)

cosine_sim_df.sample(10, axis=1).sample(5, axis=0)

"""Tabel diatas merupakan matriks kesamaan terhadap beberapa game yang ada

Kemudian saatnya untuk membuat fungsi rekomendasi berdasarkan persiapan dari tahapan sebelumnya
"""

def game_recommendations(title, similarity_data=cosine_sim_df, items=df[['title', 'category']], k=5):
    index = similarity_data.loc[:,title].to_numpy().argpartition(
        range(-1, -k, -1))
    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    closest = closest.drop(title, errors='ignore')
    return pd.DataFrame(closest).merge(items).head(k)

df[df.title.eq('Brawl Stars')]

game_recommendations('Brawl Stars')

"""Tabel diatas merupakan daftar game yang direkomendasikan berdasarkan game `Brawl Stars` yang merupakan game dengan kategori `Action`

### Collaborative filtering
---
Metode dalam merekomendasikan suatu hal berdasarkkan preferensi pengguna

Pada tahap ini, data yang akan digunakan perlu disiapkan sebelum dilakukannya proses encoding
"""

user = reviews['userId'].unique().tolist()
print('List user', user[:10])

user_encoded = {x: i for i, x in enumerate(user)}
print('encoded user id : ', user_encoded)

user_decoded = {i: x for i, x in enumerate(user)}
print('decoded user id : ', user_decoded)

game = reviews['gameId'].unique().tolist()
print('List game', game[:10])

game_encoded = {x: i for i, x in enumerate(game)}
print('encoded game id : ', game_encoded)

game_decoded = {i: x for i, x in enumerate(game)}
print('decoded game id : ', game_decoded)

"""Kemudian petakan setiap data tersebut kedalam dataframe"""

reviews['user'] = reviews['userId'].map(user_encoded)
reviews['game'] = reviews['gameId'].map(game_encoded)
reviews.head()

"""Kemudian cek total dana dan ubah tipe data rating ke dalam float"""

num_user = len(user_encoded)
print('Total user', num_user)

num_game = len(game_encoded)
print('Total game', num_game)

# Mengubah tipe data raating menjadi float
reviews['rating'] = reviews['rating'].values.astype(np.float32)

# Nilai minimum rating
min_rating = min(reviews['rating'])

# Nilai maksimal rating
max_rating = max(reviews['rating'])

print('Number of Game: {}, Min Rating: {}, Max Rating: {}'.format(
    num_game, min_rating, max_rating
))

"""**Train-Test_Split**
Proses untuk membagi data menjadi data latih dan data uji
"""

collaborative = reviews.sample(frac=1, random_state=42)

x = reviews[['user', 'game']].values
y = collaborative['rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

train_indices = int(0.7 * df.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

"""### Proses training

Membuat class menggunakan RecommenderNet untuk mempersiapkan proses
"""

class RecommenderNet(tf.keras.Model):

  def __init__(self, num_user, num_game, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_user = num_user
    self.num_game = num_game
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding(
        num_user,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_user, 1)
    self.game_embedding = layers.Embedding(
        num_game,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.game_bias = layers.Embedding(num_game, 1)

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0])
    user_bias = self.user_bias(inputs[:, 0])
    game_vector = self.game_embedding(inputs[:, 1])
    game_bias = self.game_bias(inputs[:, 1])

    dot_user_game = tf.tensordot(user_vector, game_vector, 2)

    x = dot_user_game + user_bias + game_bias

    return tf.nn.sigmoid(x)

"""Lakukan proses compile terhadap model"""

model = RecommenderNet(num_user, num_game, 50) # inisialisasi model

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

"""Kemudian mulai proses training"""

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 8,
    epochs = 100,
    validation_data = (x_val, y_val)
)

"""### Hasil rekomendasi
---
Proses untuk menampilkan hasil rekomendasi berdasarkan model yang telah dibuat

Sebelum menampilkan rekomendasi, perlu untuk membuat beberapa variabel untuk diterapkan dalam `model.predict`, seperti sampel user id sebagai acuan untuk game yang sudah dimainkan serta game-game belum dimainkannya
"""

games = df
rated = reviews

# mengambil sampel user
user_id = rated.userId.sample(1).iloc[0]
game_played_by_user = rated[rated.userId == user_id]

games_not_played = games[~games['gameId'].isin(game_played_by_user.gameId.values)]['gameId']
games_not_played = list(
    set(games_not_played).intersection(set(game_encoded.keys()))
)

games_not_played = [[game_encoded.get(x)] for x in games_not_played]
user_encoder = user_encoded.get(user_id)
user_game_array = np.hstack(
    ([[user_encoder]] * len(games_not_played), games_not_played)
)

"""Kemudian gunakan model predict untuk mendapatkan rekomendasi"""

ratings = model.predict(user_game_array).flatten()

top_ratings_indices = ratings.argsort()[-10:][::-1]
recommended_game_ids = [
    game_decoded.get(games_not_played[x][0]) for x in top_ratings_indices
]

print('Showing recommendations for users: {}'.format(user_id))
print('===' * 9)
print('Game with high ratings from user')
print('----' * 8)

top_game_user = (
    game_played_by_user.sort_values(
        ['rating'], ascending=False
    )
    .head(5)
    .gameId.values
)

recommended_game = df[df['gameId'].isin(recommended_game_ids)]
for row in recommended_game.itertuples():
    print(row.title, ':', row.category)

"""Data diatas merupakan hasil rekomendasi game berdasarkan data rating dari user dengan user id `15a56a38-d249-48b6-b3b2-910c8d67e533`, game-game tersebut merupakan 10 game dengan rating tertinggi yang direkomendasikan oleh model

## **Model evaluation**
---
Proses ini dilakukan untuk mengevaluasi model yang telah dibuat

Visualisasikan performa dari model yang telah dibuat kedalam plot
"""

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

"""Berdasarkan data visual diatas, model yang telah dibuat sebelumnya menghasilkan `root mean squared error` sekitar 0.15 pada data latih dan 0.40 pada data uji."""