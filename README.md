Film Önerisi Web Uygulaması
Genel Bakış
Bu proje, tür ve özet metnine göre benzer filmler öneren, Streamlit tabanlı bir film öneri web uygulamasıdır.

Proje Hedefi
Bu projenin amacı, bir öneri algoritmasını kullanıcıların doğrudan etkileşimde bulunabileceği etkileşimli bir web uygulamasına dönüştürmektir.

Kullanılan Teknolojiler
Python
Streamlit
Pandalar
Scikit-learn
Özellikler
Etkileşimli film seçimi
İçerik tabanlı öneri sistemi
Temiz ve sade kullanıcı arayüzü
Veri kümesi
Bu proje, aşağıdaki bileşenleri içeren küçük bir film veri kümesi kullanmaktadır:

Başlık
Tür
Genel Bakış
Nasıl Çalışır
Tür ve genel bakışı tek bir metin özelliğinde birleştirir.
CountVectorizer kullanarak metni vektörlere dönüştürür.
Kosinüs benzerliği ile benzerliği hesaplar.
En benzer 5 filmi döndürür.
Proje Yapısı
movie-recommendation-webapp/
├── data/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
