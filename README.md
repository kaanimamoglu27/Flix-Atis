# Flix Atış

FLIX'i fırlat, süzül, kovaya sok! Golf usulü 3D atış oyunu: 9 dünya (Sokak, Türkiye, Amerika, Avrupa, Asya, Avustralya, Afrika, Antarktika, Uzay), 180 bölüm.

- `index.html`: tek dosyalık oyun (telefonda dik ekran).
- `kaynak/`: oyunun kaynak dosyaları ve derleme betikleri (README içinde).
- `app/`: iOS uygulaması (Capacitor 8, paket kimliği com.flixtoys.atis).

App Store: Flix Atış (tr) / Flix Shot (en), App ID 6832637118, SKU FLIXSHOT001.

FLIX TOYS · flixtoysofficial.com

## TestFlight
Actions > **iOS TestFlight** > Run workflow. Kurulum ve gerekli secrets: [TESTFLIGHT.md](TESTFLIGHT.md)

## Yasal Bilgiler / Legal & Information (2026-11-09)

Ayarlar'da **Yasal Bilgiler** ve **Hakkında** düğmeleri var. Panel TR/EN, dili cihaz diline göre seçer, üstteki TR/EN ile değişir.
Belgeler flixtoysofficial.com'daki resmi sayfalar; uygulamada Safari'de, web'de yeni sekmede açılır (oyun içinde WebView yok). İnternet yoksa uyarı ve adres gösterilir.
Hakkında: geliştiriciler, %50/%50 telif sahipliği, yayıncı FLIX TOYS, destek e-postası, açık kaynak bileşenler.
Kod oyunun içinde tek bir `<script>/* FLIX legal */` bloğu (FlixLegal), düğmeler `data-flixlegal="legal|about"`. Oynanış, reklam, satın alma ve kayıtlar değişmedi.
