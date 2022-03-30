# Test Automation Bootcamp API Entegrasyon Testleri
![image](https://user-images.githubusercontent.com/13181041/160855652-81f1782d-480b-43d6-96b5-1ea9ca5ff768.png)



Projede kullanılan endpointlere bu linkten ulaşabilirsiniz : https://bootcampapi.techcs.io/api/fe/v1/#/

# PROJE GEREKSİNİMLERİ

Projenin ayağa kalması için Postman ve aşağıdaki görselde paylaşılan Environmente ihtiyaç duyulmaktadır. İndirdiğiniz Collection'u Postman'ın içerisine import ettikten sonra belirtilen Environment'ı içe aktararak aktif olarak seçmeniz gerekmektedir.

![image](https://user-images.githubusercontent.com/13181041/160854971-41181701-f83a-4b65-aedf-a5c83e8a2085.png)



Environmentin ayarlanmasının ardından koleksiyonu koşmak için requestBody.json dosyasını veri olarak Postman'e göstermemiz gerekiyor. Koleksiyonu koştuğumuz kısımdan "Data Select File" diyerek dosyamızı gösteriyoruz ve "Data File Type" seçeneğini "application/json" olarak ayarlıyoruz.


![image](https://user-images.githubusercontent.com/13181041/160855313-6aa56bc9-f9ee-4413-9052-c6a87b8ead97.png)

# Newman Kullanarak Koşma

Testi Newman kullanarak koşmak için aşağıdaki kod bloğunda bulunan kodu koleksiyon dosyalarının bulunduğu klasörde terminalden çalıştırmanız yeterli olacaktır.
```
newman run "Beyn Interview.postman_collection.json" -e "Beyn Interview Collection Environment.postman_environment.json" -d requestBody.json
```

# Newman HTML Raporlama

Bu işlemi gerçekleştirmek için Node Package Manager'e ihtiyaç duymaktasınız!

```
npm install -g newman-reporter-htmlextra
```

Terminal üzerinden yukarıdaki kod bloğunu çalıştırarak gerekli pakedin kurulumunu gerçekleştirebilirsiniz.

HTML raporu oluşturmak için gerekli kod:

```
newman run "Beyn Interview.postman_collection.json" -e "Beyn Interview Collection Environment.postman_environment.json" -d requestBody.json -r htmlextra
```
