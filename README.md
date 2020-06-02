# **Rc522 RFID Okuyucu ve** **Azure** **Cloud** ile Personel Giriş-Çıkış Takip Sistemi



[TOC]

###  Gereksinimler

1. Raspberry Pi
2. RFID-RC522 Modülü
3. Connector
4. Azure hesabı

## 1. RFID Modülü Nedir?

![Izokee RFID Kit, Mfrc RC522 RFID-RC522 RF IC kart okuyucu Sensor ...](https://images-na.ssl-images-amazon.com/images/I/41l12fnri2L._AC_SY400_.jpg)

> Açılımı **Radio Frequency Identification** yani radyo frekansı ile tanımlanır. RFID teknolojisi nesnelerin radyo dalgaları kullanılarak tanınması için kullanılan teknolojidir. 
>
> [Günlük hayatta toplu taşıma biletlerinde, işyeri ve okul girişlerindeki turnikelerde karşımıza sıklıkla çıkmaktadır. Arduino ile RFID projelerini incelediğimizde kapı kilidi, bir ortamda bulunan kişi sayısı bilgisinin alınması, bilgisayar oturum kilidi, alarm sistemi gibi projelerle sıklıkla karşılaşabilirsiniz](https://maker.robotistan.com/arduino-dersleri-18-rc522-rfid-modul-kullanimi/)

<video src="C:\Users\sevgi\Desktop\yksk\Git\RC522_RFID_AZURE_ITO_HUB\README_Files\RFID.mp4"></video>



## 2. Raspberryle Bağlantısı Nasıl Yapılır?

*Bağlantı şeması aşağıda görüldüğü üzeredir.*



<img src="https://maker.robotistan.com/wp-content/uploads/2017/03/rc522_bb-1024x801.png" style="zoom: 40%;"  >

> **Ürün Adresi**
>
> *https://urun.n11.com/arduino-urunleri-ve-setleri/arduino-rc522-rfid-kit-set-raspberry-pic-P365979220?gclid=CjwKCAjwztL2BRATEiwAvnALclHxuFlOlR0qK_DcY1D4QX7UXpknKosoMBTcumFS-IF3_OL5bPtlWhoCGQYQAvD_BwE&gclsrc=aw.ds*

### 2.1 RC522 PINOUT

RC522 pin çıkışları şematiğinden bağlantıları yaparken yararlanabilirsiniz.

<img src="https://www.algoritmauzmani.com/wp-content/uploads/2017/04/raspberry-rc522.png" alt="Raspberry Pi 3 ile RC522 RFID Kart Okuyucu Kullanımı" style="zoom:80%;" />



## 3. Azure Cloud İşlemleri

1. İlk adım olarak https://azure.microsoft.com/tr-tr/ adresinden hesap açmak gerekiyor.
2. Hesap açtıktan sonra raspberryimizi tanıtmak için IoT Hub oluşturuyoruz.

![6](C:\Users\sevgi\Desktop\yksk\Git\RC522_RFID_AZURE_ITO_HUB\README_Files\6.PNG)



#### 3.1 Iot Hub Nedir?

[IoT Hub, bulutta barındırılan ve IoT uygulamanız ve yönettiği cihazlar arasındaki iki yönlü iletişim için merkezi ileti hub’ı görevi gören, yönetilen bir hizmettir. Milyonlarca IoT cihazı ve bulutta barındırılan çözüm arka ucu arasında güvenilir ve güvenli iletişim sunan IoT çözümleri derlemek için Azure IoT Hub’ı kullanabilirsiniz. Hemen hemen her cihazı IoT Hub’a bağlayabilirsiniz. IoT Hub, hem cihazdan buluta hem de buluttan cihaza iletişimi destekler.](https://docs.microsoft.com/en-us/azure/iot-hub/about-iot-hub#:~:text=IoT%20Hub%20is%20a%20managed,and%20the%20devices%20it%20manages.&text=IoT%20Hub%20supports%20communications%20both,the%20cloud%20to%20the%20device.)

![13](C:\Users\sevgi\Desktop\yksk\Git\RC522_RFID_AZURE_ITO_HUB\README_Files\13.PNG)



## İÇERİK

**simulateddevice.py**: RFID Modülün kart idsini okumak için gerekir ve veriyi Azure clouda gönderir.



## Kullanılan Kütüphaneler

```
from pirc522 import RFID

from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse
```



## YAPILMASI GEREKENLER

**simulateddevice.py içerisindeki CONNECTION_STRING aşağıdaki gibi düzenlenmelidir.

`CONNECTION_STRING = "Connection Stringinizi yazınız."`

<u>Connection stringi raspberryi devicenızı tanımladığınız yerde bulabilirsiniz !</u>

![10](C:\Users\sevgi\Desktop\yksk\Git\RC522_RFID_AZURE_ITO_HUB\README_Files\10.PNG)



`https://azure.microsoft.com/tr-tr/ sitesinde yönergeler takip edilerek:`

1. `IoT Stream`
2. `Server Database`
3. `Sql table oluşturun`



## ÇIKTILAR

- [Mobaxterm](https://mobaxterm.mobatek.net/) Uygulamasından raspberryde bulunan python dosyamızı çalıştırabilir ve consoleu gözlemleyebiliriz.

![Resim2](C:\Users\sevgi\Desktop\yksk\Git\RC522_RFID_AZURE_ITO_HUB\README_Files\Resim2.png)IOT Stream 



- IOT STREAM sayfasından verileri gözlemleyebiliyoruz.

![Resim1](C:\Users\sevgi\Desktop\yksk\Git\RC522_RFID_AZURE_ITO_HUB\README_Files\Resim1.png)



- Setup aşağıdaki gibidir.

  

  ![IMG_6932](C:\Users\sevgi\Desktop\yksk\Git\RC522_RFID_AZURE_ITO_HUB\README_Files\IMG_6932.JPG)



<video src="C:\Users\sevgi\Desktop\yksk\Git\RC522_RFID_AZURE_ITO_HUB\README_Files\IMG_6933.MOV"></video>



## TEŞEKKÜRLER

Görüş ve öneriler için sevginurbilgin@gmail.com’ a yazabilirsiniz. 