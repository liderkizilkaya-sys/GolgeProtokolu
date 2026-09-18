# Gölge Protokolü Android

Gölge Protokolü, çevrimdışı çalışan seçim tabanlı bir aksiyon/macera oyunudur.

## Sürüm

- Application ID: `com.golgeprotokolu.game`
- Version: `1.0.1` / versionCode 2
- minSdk: 23
- compileSdk / targetSdk: 36
- Android Gradle Plugin: 8.13.2
- Gradle: 8.13
- Çevrimdışı WebView tabanlı
- Ağ izni istemez

## Oyun içeriği

- 9 kritik karar
- Her bölümde 3 seçim, toplam 19.683 karar yolu
- 5 erişilebilir final
- Sağlık, gizlilik ve istihbarat değerleri
- 8 başarım
- Günlük meydan okuma
- Cihazda yerel otomatik kayıt
- Gizlilik politikası ekranı

## Doğrulama

`scripts/validate_game.py` tüm 19.683 karar yolunu simüle eder ve beş finalin de erişilebilir olduğunu doğrular.

GitHub Actions her `main` push'unda:
1. oyun yol doğrulamasını çalıştırır,
2. Android lint kontrolünü çalıştırır,
3. release AAB üretir,
4. AAB dosyasını workflow artifact'i olarak yükler.

> İmzalama anahtarları depoya eklenmez. Google Play'e gönderilecek AAB, güvenli upload key ile imzalanmalıdır.
