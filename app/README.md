# Flix Atış iOS uygulaması

Capacitor 8 paketi. Oyunun kendisi `../index.html` .

- Paket kimliği: `com.flixtoys.atis`, ad "Flix Atış", sadece iPhone, dikey.
- App Store adı: Flix Atış (tr) / Flix Shot (en), App ID 6832637118, SKU FLIXSHOT001.
- Reklam: AdMob (rewarded + interstitial, banner yok; kimlikler `www/ads-config.js`). AB/UK/İsviçre için Google rıza mesajı; Ayarlar > Gizlilik Seçenekleri ile rıza değiştirilebilir.
- Uygulama içi satın almalar: `atis_feathers_500/1200/3500/8000/20000` (consumable), `atis_starter`, `atis_noads` (non-consumable). `www/native-bridge.js`.
- Gizlilik politikası: https://www.flixtoysofficial.com/sayfa/flix-toys-privacy-policy
- `npm run build`: `../index.html`'den `www/index.html` üretir (yazı tipleri ve three.js uygulamanın içinde, internet gerekmez).
- `ios/` klasörü depoya konmaz; `npx cap add ios --packagemanager CocoaPods` + `python3 tools/ios_setup.py` ile üretilir.

TestFlight'a yükleme (Mac gerekmez): GitHub > Actions > "iOS TestFlight" > Run workflow (sürümü yaz).
Ayrıntılı adımlar: depo kökündeki `TESTFLIGHT.md`.
Mac'ten: `./ios.sh hazirla`, `./ios.sh simulator`, `./ios.sh yukle 1.0`.
