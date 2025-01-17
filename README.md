# -lk-Projem
GitHuba'a ilk proje yükleme denemesidir.

Ürün Fiyat Takip Sistemi 
Bu proje, bir e-ticaret sitesinde (Amazon) belirli bir ürünün fiyatını her gün kontrol 
eden ve fiyatı düştüğünde kullanıcıya Telegram botu aracılığıyla bildirim gönderen bir 
sistemdir. 
Özellikler 
 Web kazıma (Web Scraping) ile Amazon'dan ürün fiyatı çekilir. 
 Fiyat her gün belirli bir saatte kontrol edilir. 
 Fiyat düştüğünde Telegram botu aracılığıyla kullanıcıya bildirim gönderilir. 
 Basit bir hata yönetimi ile, fiyat bilgisi bulunamadığında kullanıcıya bildirim 
yapılır. 

Kullanım 
Gereksinimler 
Projenin çalışabilmesi için aşağıdaki Python kütüphanelerine ihtiyacınız var: 
 requests: Web sayfasına HTTP istekleri göndermek için. 
 beautifulsoup4: Sayfa içeriğini parse etmek için. 
 python-telegram-bot: Telegram botu aracılığıyla mesaj göndermek için. 
 schedule: Belirli bir saatte fiyat kontrolü yapmak için. 
 time: Döngüyü çalıştırmak için. 
Telegram Botu Oluşturma 
Bu projeyi kullanabilmek için bir Telegram botu oluşturmanız gerekmektedir. Telegram 
botu oluşturmak için şu adımları izleyin: 
1. Telegram'da @BotFather'a gidin. 
2. /newbot komutunu kullanarak yeni bir bot oluşturun. 
3. Botunuz için bir isim ve kullanıcı adı belirleyin. 
4. BotFather, size bir token verecek. Bu token'ı kaydedin. 
Ayrıca, botunuzu kullanmak için chat_id'ye ihtiyacınız var. @userinfobot gibi botlar 
ile kendi chat ID'nizi öğrenebilirsiniz.

Çalıştırmak İçin:
python urun_fiyat_takip.py
Bu komutla, program her gün belirlediğiniz saatte çalışarak ürün fiyatını kontrol eder. 
Eğer fiyat düşerse, Telegram botu üzerinden bir bildirim alırsınız.
