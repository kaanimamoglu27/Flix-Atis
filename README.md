# Flix Atış

FLIX'i fırlat, süzül, kovaya sok! Golf usulü 3D atış oyunu: 9 dünya (Sokak, Türkiye, Amerika, Avrupa, Asya, Avustralya, Afrika, Antarktika, Uzay), 180 bölüm.

- `index.html`: tek dosyalık oyun (telefonda dik ekran).
- `kaynak/`: oyunun kaynak dosyaları ve derleme betikleri (README içinde).
- `app/`: iOS uygulaması (Capacitor 8, paket kimliği com.flixtoys.atis).

App Store: Flix Atış (tr) / Flix Shot (en), App ID 6832637118, SKU FLIXSHOT001.

FLIX TOYS · flixtoysofficial.com

## 6 dil ve ayrıntılı Nasıl oynanır (2026-11-18)

- **Diller:** Türkçe (varsayılan), English, Français, Deutsch, Español, العربية. Ayarlar'daki 🌐 Dil kartından seçilir, cihazda saklanır (`localStorage.flixLang`).
- Çeviri katmanı `i18n/`: oyunun Türkçe metni kaynak; `flix-i18n.js` ekrandaki yazıları (HTML, düğmeler, canvas yazıları, dükkân ve bölüm adları, yoldakilerin konuşma balonları) `i18n/ceviri_*.tsv` tablosundan seçili dilde gösterir. Satır: `tr<TAB>en<TAB>fr<TAB>de<TAB>es<TAB>ar`. Yeni metin eklenince tabloya satır ekle, `python3 i18n/apply_i18n.py` (index.html'deki `FLIX-I18N` bloğunu yeniler), sonra `cd app && python3 tools/build_www.py`. Dükkân tabelaları (LOKUMCU LÜTFÜ gibi isimler) bilerek çevrilmedi.
- **Nasıl oynanır** ayrıntılandı ve kaydırılabilir: nişan alma, süzülme ve tüy enerjisi, 8 atış hakkı, yıldız kuralları, ceza atışı, insanlar/hayvanlar/çamaşır ipleri, rüzgâr, harita düğmesi, 9 dünya ve açılma kuralı, tüy ve dükkân, isteğe bağlı reklamlar.
- Reklamlar kontrol edildi, değişiklik gerekmedi (ödüllü reklamlar isteğe bağlı, geçiş reklamı 3 bölümde bir, Reklamsız pakette yok).

## TestFlight
Actions > **iOS TestFlight** > Run workflow. Kurulum ve gerekli secrets: [TESTFLIGHT.md](TESTFLIGHT.md)

## Yasal Bilgiler / Legal & Information (2026-11-09)

Ayarlar'da **Yasal Bilgiler** ve **Hakkında** düğmeleri var. Panel TR/EN, dili cihaz diline göre seçer, üstteki TR/EN ile değişir.
Belgeler flixtoysofficial.com'daki resmi sayfalar; uygulamada Safari'de, web'de yeni sekmede açılır (oyun içinde WebView yok). İnternet yoksa uyarı ve adres gösterilir.
Hakkında: geliştiriciler, %50/%50 telif sahipliği, yayıncı FLIX TOYS, destek e-postası, açık kaynak bileşenler.
Kod oyunun içinde tek bir `<script>/* FLIX legal */` bloğu (FlixLegal), düğmeler `data-flixlegal="legal|about"`. Oynanış, reklam, satın alma ve kayıtlar değişmedi.
