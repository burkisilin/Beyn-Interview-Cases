# PROJENİN AYAĞA KALDIRILMASI

Projenin ayağa kaldırılması için öncelikle Python ve gerekli paketlerin kurulması gerekmektedir. Aşağıda bulunan kodu çalıştırarak gerekli paketlerin kurulumunu otomatik olarak gerçekleştirebilirsiniz.

```
pip install -r /path/to/requirements.txt
```



Projenin bulunduğu dizinde CMD üzerinden aşağıda bulunan kodu çalıştırarak testleri koşmaya başlayabilirsiniz.\
```
py.test --capture=tee-sys
```

# ALLURE RAPORLAMA

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


