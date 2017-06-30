#include <LiquidCrystal.h>// lcd kütühanesi 
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);// lcd giriş portları
void setup() {

  lcd.begin(16, 2);// ekran tanımlaması
  Serial.begin(9600);// port belirlenmesi
  lcd.setCursor(0, 0);// imlecin ekrandaki güncel konumunu ayarlama
  lcd.print("Tahmin Sayi=");//ekrana ayarlanan imleçten itibaren yazı yazdırma
  lcd.setCursor(13, 0);// imlec konumunu güncelleme
}
void loop() {

  if (Serial.available() > 0)// veri geldimi
  {
    int x = Serial.read();// veriyi oku
    if (x == 48) {//geri kalan kısım okuduktan sonra veriyi kontrol işlemleri
      lcd.print("0");
      lcd.setCursor(0, 1);
      delay(2000);
      lcd.write("Buldum=");
      lcd.setCursor(8, 1);
      lcd.write(x);
      lcd.setCursor(10, 1);
      lcd.write(":)");
      exit(0);

    }
    else if (x == 49) {
      lcd.print("1");
      lcd.setCursor(0, 1);
      delay(2000);
      lcd.write("Buldum=");
      lcd.setCursor(8, 1);
      lcd.write(x);
      lcd.setCursor(10, 1);
      lcd.write(":)");
      exit(0);
    }
    else if (x == 50) {
      lcd.print("2");
      lcd.setCursor(0, 1);
      delay(2000);
      lcd.write("Buldum=");
      lcd.setCursor(8, 1);
      lcd.write(x);
      lcd.setCursor(10, 1);
      lcd.write(":)");
      exit(0);
    }
    else if (x == 51) {
      lcd.print("3");
      lcd.setCursor(0, 1);
      delay(2000);
      lcd.write("Buldum=");
      lcd.setCursor(8, 1);
      lcd.write(x);
      lcd.setCursor(10, 1);
      lcd.write(":)");
      exit(0);
    }
    else if (x == 52) {
      lcd.print("4");
      lcd.setCursor(0, 1);
      delay(2000);
      lcd.write("Buldum=");
      lcd.setCursor(8, 1);
      lcd.write(x);
      lcd.setCursor(10, 1);
      lcd.write(":)");
      exit(0);
    }
    else if (x == 53) {
      lcd.print("5");
      lcd.setCursor(0, 1);
      delay(2000);
      lcd.write("Buldum=");
      lcd.setCursor(8, 1);
      lcd.write(x);
      lcd.setCursor(10, 1);
      lcd.write(":)");
      exit(0);
    }
    else if (x == 54) {
      lcd.print("6");
      lcd.setCursor(0, 1);
      delay(2000);
      lcd.write("Buldum=");
      lcd.setCursor(8, 1);
      lcd.write(x);
      lcd.setCursor(10, 1);
      lcd.write(":)");
      exit(0);
    }
    else if (x == 55) {
      lcd.print("7");
      lcd.setCursor(0, 1);
      delay(2000);
      lcd.write("Buldum=");
      lcd.setCursor(8, 1);
      lcd.write(x);
      lcd.setCursor(10, 1);
      lcd.write(":)");
      exit(0);
    }
    else if (x == 56) {
      lcd.print("8");
      lcd.setCursor(0, 1);
      delay(2000);
      lcd.write("Buldum=");
      lcd.setCursor(8, 1);
      lcd.write(x);
      lcd.setCursor(10, 1);
      lcd.write(":)");
      exit(0);
    }
    else if (x == 57) {
      lcd.print("9");
      lcd.setCursor(0, 1);
      delay(2000);
      lcd.write("Buldum=");
      lcd.setCursor(8, 1);
      lcd.write(x);
      lcd.setCursor(10, 1);
      lcd.write(":)");
      exit(0);
    }
  }
}
