# FitLife_Churn

# FitLife: a'zolar ketishini oldindan aniqlash

O'quv keysi: fitnes klub uchun ketish xavfi yuqori a'zolarni oldindan topish.
FitLife va Dilnoza obrazlari to'qima (Mohirdev uslubidagi simulyatsiya).

Dashboard: [havola]

## Ma'lumot
Kaggle: [Gym customers features and churn](https://www.kaggle.com/datasets/adrianvinueza/gym-customers-features-and-churn)
(4000 a'zo). test_predictions.csv shu datasetning 800 a'zolik test qismi.

## Natija
- Tasodifiy ro'yxat: precision 27%
- Faqat a'zolik muddati bo'yicha: 72%
- Logistic regression (Lifetime siz): 76%
- Logistic regression: 90%

## Cheklovlar
1. Bir oylik surat, vaqt bo'yicha tekshirilmagan.
2. Model a'zolik muddatiga kuchli tayanadi.
3. Joriy oy tashrifi ro'yxat sanasida ma'lum bo'lmagani uchun chiqarildi.
4. Foyda hisobi taxminiy (ushlab qolish farazi).
5. Ketuvchilarning ~32% i past guruhda qoladi.
