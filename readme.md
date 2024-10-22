Subscriptions in GraphQL

Obunalar - bu GraphQL serverdan obuna bo'lgan mijozlarga real vaqtda yangilanishlarni etkazib berish uchun foydalanadigan narsa.

Bu serverdan frontendga real vaqtda aloqa o'rnatish uchun Socket.io dan foydalanishga o'xshaydi. Bu erda GraphQL o'zining funksionalligiga o'rnatilgan.

GraphQL obunalari asosan serverda ma'lumotlar yaratilganda, yangilanganda, o'chirilganda va so'rov orqali o'qilganda tinglash uchun amalga oshiriladi. Emissiya hodisasi ishlab chiqaruvchi nima istayotganiga bog'liq. Voqealar serverdan obuna bo'lgan mijozlarga uzatiladi.

Mijozlar obuna so'rovi yordamida server tomonidagi hodisaga obuna bo'lishadi:
```

subscription NewsFeed {

  newsCreated {

    title

    body

  }

}
```
Bu obuna yangiliklar yaratildi maydoni uchun bo'ladi.

Bu obuna so'rovini yuborish orqali server bilan uzoq muddatli ulanishni ochadi, u qaysi voqeani qiziqtiradi.

Yuqoridagi obuna soʻrovi WebSocket orqali GraphQL serveriga soʻrov yuboradi, soʻrov rezolyutsiyani qayta qoʻngʻiroq qilish funksiyasi bilan serverda hodisani oʻrnatadi. Har safar GraphQL serverida hodisa chiqarilganda, rezolyutsiya funktsiyasi chaqiriladi, chaqirilgandan qaytariladigan qiymat obuna so'roviga yuboriladi.

Obunalar aloqa uchun WebSocket-dan foydalanadi, oddiy POST usuli so'rovlari va mutatsiyalar ishlatilmaydi. Obunalar serverga faol ulanishni tinglaydi va server yangilanishlarni yuborishini kutadi.
