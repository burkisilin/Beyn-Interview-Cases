# PROJENİN AYAĞA KALDIRILMASI

Projenin ayağa kaldırılması için öncelikle Python ve gerekli paketlerin kurulması gerekmektedir. Aşağıda bulunan kodu çalıştırarak gerekli paketlerin kurulumunu otomatik olarak gerçekleştirebilirsiniz.

```
pip install -r /path/to/requirements.txt
```



Projenin bulunduğu dizinde CMD üzerinden aşağıda bulunan kodu çalıştırarak testleri koşmaya başlayabilirsiniz.\
```
py.test --capture=tee-sys
```



# TEST EDİLEN SENARYOLAR #
Proje içerisinde tüm kodumu detaylı bir biçimde yorum satırları ile açıklamaya çalıştım. Koşulan test senaryolarında izlenen adımlardan kısaca bahsedecek olursak;

- https://www.mizu.com/flowers ‘da aşağı scroll yaptıkça ilk 10 sayfa için her sayfada 60 ürün geldiğinin kontrolü.\
https://www.mizu.com/flowers adresine gidilir ve her sayfanın sonunda bulunan elemana scroll edilerek responsive load triggerlanır. 10 sayfanın tamamı yüklenene kadar bu işlem tekrarlanır. 10 sayfanın yüklenmesinin ardından sayfada görüntülenebiliyor olması beklenen 600. ürünün sayfada mevcut olup olmadığı assert edilir.

- https://www.mizu.com/flowers sayfasında filtre alanından sort: price high to low seçilip listeleme sayfasındaki ürünlerin doğru fiyat sırasıyla listelendiğinin kontrolü.\
https://www.mizu.com/flowers adresine gidilir ve istenilen filtreleme seçeneği seçilir. Her sayfanın sonunda bulunan elemana scroll edilerek responsive load triggerlanır. Bu işlem tüm sayfalar yüklenene kadar tekrarlanır. Tüm sayfaların yüklenmesinin ardından tüm ürünlerin fiyatları sıra ile bir liste içerisine çekilir. Liste içerisinde iterasyon yaparak tüm ürünlerin fiyatları sırası ile birbiri ile ">=" operatörü kullanılarak kıyaslanır. Sıralamada bir sorun bulunması durumunda iterasyon "Break" komutu ile bölünür ve False assertion gerçekleştirilir.

- https://www.mizu.com menü altında bulunan tüm alt kategorilerin linklerinin kırık olup olmadığının kontrolü.\
Anasayfada beliren popup'un kapatılmasının ardından tüm menü butonlarının üzerinde hover işlemi gerçekleştirilir. Böylece dinamik menü yüklenmesi tetiklenerek menü altındaki bütün linkler Selenium tarafından çekilebilir duruma getirilir. Çekilen linkler üzerinde iterasyon yapılarak link kırıklığını kontrol etmek üzere iki seçenekten birisi tercih edilebilir.

```Python
helpers.checkPageValidation(by ="By.BrowserTitle", operand ="!=", validate ="Page Not Found", link =link)
```
- Linklerin hepsine Driver.get atılarak tarayıcı başlığı kontrol edilir. Bu işlem response kodunu sorgulamaya göre daha uzun sürmektedir.

```Python
helpers.checkPageValidation(by="By.ResponseCode", validate=200, link=link)
```
- Linklerin hepsine request atılarak status kodunun 200 olup olmadığı kontrol edilir.

Yapılan testlerde https://www.mizu.com/new-products-gourmet linkinin kırık olduğu tespit edilmiştir. Bu durum raporlama üzerinde ve Utils/helpers.py dosyası içerisinde bulunan "save_screenshot" fonksiyonu çağırılarak ./screenshots/"tarih"/ klasörüne kaydedilir.

![image](https://user-images.githubusercontent.com/13181041/149820940-17b77b55-e0ca-459e-812f-fc58b135c364.png)



# ALLURE RAPORLAMA
<p align="center">
  <img src="https://user-images.githubusercontent.com/13181041/149825670-a88dbeb4-d4fc-4e75-9965-6a2221302967.gif" alt="animated" />
</p>

- https://github.com/allure-framework/allure2/releases allure indirilir ve sistem değişkenlerine tanımlanır. Ayrıca Python için gerekli paketler pip üzerinden aşağıdaki komut ile indirilir 

```
pip install allure-pytest
```

- Aşağıda belirtilen komut, komut istemcisi üzerinde çalıştırılarak test koşulur.
```
py.test --alluredir="pathToAllureReportsFolder"
```

- Son olarak raporları görüntülemek için aşağıdaki komut, komut istemcisi üzerinden çalıştırılır.
```
allure serve pathToAllureReportsFolder
```

# HTML RAPORLAMA
Test koşum raporlarımızı görüntülememizin bir diğer yolu PyTest HTML raporlama. Aşağıdaki komutu, komut istemcisi üzerinden çalıştırarak kolayca testlerimize ait bir HTML rapor sayfası oluşturabiliriz.

```
py.test --html=reportFileName.html --capture=tee-sys
```
![image](https://user-images.githubusercontent.com/13181041/149817712-a4eea80b-cd97-46fa-a7a6-11f3ee10dab7.png)

