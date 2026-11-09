# Flix Atış: GitHub'dan TestFlight'a yükleme

Yükleme artık tek tuşla yapılıyor. GitHub'da bu repoda sırayla şuralara gir: **Actions** > **iOS TestFlight** > **Run workflow**. Sürümü yaz (örneğin `1.5.1`) ve **Run workflow**'a bas.

Yaklaşık 20-30 dakika sürer. Bittiğinde özet sayfasında "TestFlight'a yüklendi" yazar. Apple'ın build'i işlemesi 10-30 dakika daha sürer, sonra App Store Connect > TestFlight'ta görünür.

- **Build numarası:** Her çalıştırmada otomatik ve benzersiz verilir (tarih + saat). Elle bir şey yapman gerekmez. **Sürüm** (1.5.1 gibi) App Store'a gönderilene kadar aynı kalabilir. App Store'a gönderdiğin bir sürümden sonra yeni build için sürümü artır.
- **Reklamlar:** TestFlight build'i gerçek AdMob reklamlarını kullanır. Sadece denemek için "test_ads" kutusunu işaretlersen Google test reklamları çıkar. Kendi reklamına tıklama.
- **Satın almalar:** TestFlight'ta Apple'ın sandbox ortamında çalışır, para çekilmez.

## Neden "Cloud signing permission error" bir daha çıkmaz?

İş akışı Xcode'un otomatik (bulut) imzalamasını hiç kullanmıyor. Uygulamayı senin **Apple Distribution sertifikan** ve **App Store provisioning profile**'ınla elle imzalıyor. API anahtarı sadece yüklemek için kullanılıyor.

Başlamadan önce şunları da kontrol ediyor ve sorun varsa Türkçe hata yazıyor:
- Profil gerçekten `com.flixtoys.atis` için mi?
- Profil App Store türünde mi?
- Profil doğru takıma mı ait?
- Profil bu sertifikayla mı oluşturulmuş?

## Gerekli GitHub Secrets (7 tane)

Secret'ları şuraya gir: GitHub > **Flix-At-** reposu > **Settings** > **Secrets and variables** > **Actions** > **New repository secret**. İsimler birebir aynı olmalı.

| Secret adı | Ne |
|---|---|
| `APPLE_TEAM_ID` | 10 karakterlik Team ID |
| `APP_STORE_CONNECT_KEY_ID` | API anahtarının Key ID'si |
| `APP_STORE_CONNECT_ISSUER_ID` | Issuer ID |
| `APP_STORE_CONNECT_PRIVATE_KEY` | İndirilen `AuthKey_XXXX.p8` dosyasının tüm metni |
| `IOS_DIST_CERT_P12_BASE64` | Apple Distribution sertifikasının `.p12` dosyası, base64 metin olarak |
| `IOS_DIST_CERT_PASSWORD` | O `.p12` dosyasının şifresi |
| `IOS_PROVISION_PROFILE_BASE64` | App Store provisioning profile (`.mobileprovision`), base64 metin olarak |

Bu değerler hiçbir zaman repoya yazılmaz. Sadece GitHub Secrets'ta durur, loglarda da gösterilmez.

### 1. Team ID
developer.apple.com > **Account** > **Membership details** > **Team ID** (örnek: `ABCDE12345`). Bunu `APPLE_TEAM_ID` olarak gir.

### 2. App Store Connect API anahtarı (3 secret)
1. appstoreconnect.apple.com > **Users and Access** > **Integrations** > **App Store Connect API** > **Team Keys** > **+**.
2. Bir ad ver (örnek: `GitHub TestFlight`), Access olarak **App Manager** seç (Admin de olur). **Generate**'e bas.
3. Sayfadaki **Issuer ID**'yi `APP_STORE_CONNECT_ISSUER_ID`, anahtarın **Key ID**'sini `APP_STORE_CONNECT_KEY_ID` olarak gir.
4. **Download API Key** ile `.p8` dosyasını indir (sadece bir kez indirilebilir). Dosyayı metin düzenleyiciyle aç. `-----BEGIN PRIVATE KEY-----` dahil tüm metni `APP_STORE_CONNECT_PRIVATE_KEY` olarak yapıştır.

Kick Up ya da Arkana için zaten bir API anahtarın varsa aynısını kullanabilirsin.

### 3. Apple Distribution sertifikası (.p12)

Mac'te yapmak istersen:
1. **Anahtar Zinciri Erişimi** > menüden **Sertifika Asistanı** > **Bir Sertifika Yetkilisinden Sertifika İste** > e-postanı yaz > **Diske kaydedildi**. Bir `.certSigningRequest` dosyası oluşur.
2. developer.apple.com > **Certificates, Identifiers & Profiles** > **Certificates** > **+** > **Apple Distribution** > bu dosyayı yükle > `.cer` dosyasını indir.
3. İndirdiğin `.cer` dosyasına çift tıkla. Anahtar Zinciri'nde **Apple Distribution: FLIX TOYS...** satırına sağ tıkla > **Dışa Aktar** > `.p12` olarak kaydet ve bir şifre koy. Bu şifreyi `IOS_DIST_CERT_PASSWORD` olarak gir.
4. Terminalde `base64 -i sertifika.p12 | pbcopy` çalıştır. Panoya kopyalanan metni `IOS_DIST_CERT_P12_BASE64` olarak yapıştır.

Mac yoksa (Windows'ta Git Bash ya da herhangi bir terminal, `openssl` ile):
```bash
openssl genrsa -out dist.key 2048
openssl req -new -key dist.key -out dist.csr -subj "/emailAddress=kaanimam1998@gmail.com/CN=FLIX TOYS/C=TR"
# dist.csr dosyasını developer.apple.com > Certificates > + > Apple Distribution'a yükle, distribution.cer'i indir
openssl x509 -inform der -in distribution.cer -out dist.pem
openssl pkcs12 -export -legacy -inkey dist.key -in dist.pem -out dist.p12 -passout pass:BURAYA_SIFRE
base64 -w0 dist.p12 > dist.p12.txt      # bu dosyanın içi = IOS_DIST_CERT_P12_BASE64
```
`dist.key` dosyasını sakla, kimseyle paylaşma.

Not: Apple bir takımda en fazla 3 Distribution sertifikasına izin veriyor. Daha önce bulut imzalamanın oluşturduğu sertifikalar varsa ve sınır doluysa, kullanmadığını **Revoke** edebilirsin. App Store'daki uygulamalar bundan etkilenmez.

### 4. App Store provisioning profile
1. developer.apple.com > **Identifiers**: `com.flixtoys.atis` kayıtlı olmalı. Yoksa **+** > **App IDs** > **App** ile ekle. Capabilities'de **In-App Purchase** zaten açık gelir.
2. **Profiles** > **+** > **Distribution** altında **App Store Connect** seç > App ID olarak `com.flixtoys.atis` > 3. adımdaki **Apple Distribution** sertifikasını seç > ad ver (örnek: `Flix Atis AppStore`) > **Generate** > indir.
3. Profili base64 metne çevir. Mac'te: `base64 -i Flix_Atis_AppStore.mobileprovision | pbcopy`. Windows'ta: `base64 -w0 Flix_Atis_AppStore.mobileprovision > profil.txt`. Çıkan metni `IOS_PROVISION_PROFILE_BASE64` olarak gir.

Profil 1 yıl geçerlidir. Süresi dolunca ya da sertifikayı yenilersen profili yeniden oluşturup bu secret'ı güncelle.

## Bir şey ters giderse
- **Kırmızı adım:** Actions'ta kırmızı adıma tıkla. Hata mesajı Türkçe, neyin eksik ya da yanlış olduğunu söyler.
- **Ayrıntılı loglar:** Çalıştırma sayfasının altındaki **build-logs** dosyasında archive, export ve upload logları var.
- **App Store Connect'te uygulama kaydı yoksa:** Yükleme "app not found" der. App Store Connect > **Uygulamalar** > **+** > Yeni Uygulama ile ekle. Ad **Flix Atış**, paket kimliği `com.flixtoys.atis`, SKU `atis1`.
