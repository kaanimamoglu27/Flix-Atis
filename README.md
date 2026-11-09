# Flix Atış

FLIX'i fırlat, süzül, kovaya sok! Golf usulü 3D atış oyunu: 4 dünya (Sokak, Amerika, Avrupa, Uzay), 80 bölüm.

- Oyna: https://kaanimamoglu27.github.io/Flix-At-/
- `index.html`: tek dosyalık oyun (telefonda dik ekran).
- `kaynak/`: oyunun kaynak dosyaları ve derleme betikleri (README içinde).
- `app/`: iOS uygulaması (Capacitor 8, paket kimliği com.flixtoys.atis).

FLIX TOYS · flixtoysofficial.com

## TestFlight
Actions > **iOS TestFlight** > Run workflow. Kurulum ve gerekli secrets: [TESTFLIGHT.md](TESTFLIGHT.md)

## Yasal Bilgiler / Legal & Information (2026-11-09)

Ayarlar'da (Sen Olsaydın'da ana ekranın altında) **Yasal Bilgiler** ve **Hakkında** düğmeleri var. Panel TR/EN, dili cihaz diline göre seçer, üstteki TR/EN ile değişir.
Belgeler flixtoysofficial.com'daki resmi sayfalar; uygulamada Safari'de, web'de yeni sekmede açılır (oyun içinde WebView yok). İnternet yoksa uyarı ve adres gösterilir.
Hakkında: geliştiriciler, %50/%50 telif sahipliği, yayıncı FLIX TOYS, destek e-postası, açık kaynak bileşenler.
Kod oyunun içinde tek bir `<script>/* FLIX legal */` bloğu (FlixLegal), düğmeler `data-flixlegal="legal|about"`. Oynanış, reklam, satın alma ve kayıtlar değişmedi.
