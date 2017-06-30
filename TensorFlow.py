from tensorflow.examples.tutorials.mnist import input_data#Resimlerin nasıl eğitileceğini bildirir. Görülen resmin ne olduğunu anlamak için kullanılır.
import tensorflow as tf#Gerekli olan kütüphane
import os
import serial
import time
import random
import time


mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
import scipy.ndimage
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # CPU icin makine hizliligi hatasi giderme


x = tf.placeholder(tf.float32, [None, 784])#burada x tensorflow işlemi yapılır. 784 kullanılmasının amacı 28*28 piksellik bir boyut olan matriste çalışmak içindir.placeholder fonksiyonu ile de yerleştirilir.x yer tutucu görevini görür


W = tf.Variable(tf.zeros([784, 10])) #optimum yani gerçek değere yaklaşabilmek için kullanılır. Ağırlık olarak nitelendirelebilir.

b = tf.Variable(tf.zeros([10]))#b değişkenine varsayılan sıfır değeri atamak için kullanıldı.

y = tf.nn.softmax(tf.matmul(x, W) + b)#Dışardan çarpma işlemi yapar yani x ile b çarpılır. matmul tensorflow'un çarpma için kullanıldığı fonksiyondur.Matris çarpmı yapar

y_ = tf.placeholder(tf.float32, [None, 10])#hatayı türev alarak düüşürülmeye çalışılır.cross_entropy düzensizlik demektir. Düzensizliği sıfıra getirene kadar kademeli düşürmesi sağlanır


cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)#adım adım verileri eğitir. Kademeli düşürme optimizasyonuna göre en uygu değeri bulmaya çalış

sess = tf.InteractiveSession()#modele ulaşmak için kullanıldı. kodun sürekli çalışması istendiği için kullanılır.

tf.global_variables_initializer().run()

for _ in range(1000):#verileri oluşturuldu.
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))#doğru tahmnini almak için kullanıldı. 1-0 gibi değerler üretir

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))#correct_prediction ortalaması doğruluk hesabını verir


print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))#basari oranini ekrana yazdirdik

cizim = np.vectorize(lambda x: 255 - x)(np.ndarray.flatten(scipy.ndimage.imread("sayi3.png", flatten=True)))#cizimi aliyoruz

sonuc = sess.run(tf.argmax(y, 1), feed_dict={x: [cizim]})#cizim degerini degiskenlerimize donduruyoruz


print(sonuc)
data=np.str(sonuc)#veriyi yollarken string olarak yollayip ascii degerine gore almak icin kullanildi
ser = serial.Serial('COM3', 9600,timeout=0)#haberleşme 9600 portu uzerinden saglandi
time.sleep(2)#arduino ile haberleştikten sonra biraz bekletildi(veri duzgun aktarilmasi icin)
ser.write(bytes(data,encoding='ascii',errors='replace'))#veri arduino ile haberlesti
ser.flush()#arduino ile baglanti kapatildi

for i in data:#data verisinde deger [] geldiginden veriyi 'x' halinde almak icin kullanilan dongu
    tahmin=data[1]#gelen veriyi bir degiskene atadik

while True:
    tahminSayi=random.randint(0,9)#random sayi tahmin ettik

    tahminSayi=np.str(tahminSayi)#tahmin sayisini karsilastirma icin str ye donusturdum

    if(tahminSayi==tahmin):#tahmin sayimizi bulduk
        time.sleep(2)
        ser.write(bytes(data, encoding='ascii', errors='replace'))#tekrar arduino ile haberlestik ve sonucu o kisimda yazdirdik

        break
