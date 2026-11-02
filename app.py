import pandas as pd
import streamlit as st

st.set_page_config(page_title="FitLife: ketishni aniqlash", layout="wide")
st.title("FitLife: a'zolar ketishini oldindan aniqlash")
st.caption("O'quv keysi. Dataset: Kaggle gym churn, 800 a'zolik test namunasi. Foyda hisobi tahminiy.")

df = pd.read_csv('test_predictions.csv')
df = df.rename(columns={'kredit': 'ketdi', "Churn": 'ketdi'})

st.sidebar.header("Sozlamalar")
K = st.sidebar.slider("Ro'yxat uzunligi (kishi)", 40, 300, 160, 10)
retention = st.sidebar.slider("Ushlab qolish ehtimoli (%)", 5, 50, 20) / 100
ltv = st.sidebar.number_input("Ketgan a'zodan yo'qotish (so'm)", value=3_200_000, step=100_000)
cost = st.sidebar.number_input("Bir kontakt xarajati (so'm)", value=230_000, step=10_000)

top = df.sort_values("risk", ascending=False).head(K)
hits = int(top["ketdi"].sum())
precision = hits / K
recall = hits / df["ketdi"].sum()
saved = hits * retention * ltv
spent = K * cost
net = saved - spent

c1, c2, c3, c4 = st.columns(4)
c1.metric("Precision", f"{precision:.0%}")
c2.metric("Recall", f"{recall:.0%}")
c3.metric("Xarajat", f"{spent / 1e6:.1f} mln so'm")
c4.metric("Taxminiy sof foyda", f"{net / 1e6:.1f} mln so'm")

st.subheader("3 darajali ro'yxat")
tier = df.groupby("daraja")["ketdi"].agg(["count", "sum", "mean"]).reindex(["yuqori", "o'rta", "past"])
tier.columns = ["A'zolar", "Ketgan", "Ketish ulushi (%)"]
tier["Ketish ulushi (%)"] = (tier["Ketish ulushi (%)"] * 100).round(0)
left, right = st.columns(2)
left.dataframe(tier)
right.bar_chart(tier["Ketish ulushi (%)"])

st.subheader("Usullar solishtirmasi (precision, 160 kishilik ro'yxat)")
methods = pd.Series({"Tasodifiy": 0.269, "Faqat Lifetime": 0.719,
                     "Model, Lifetime siz": 0.756, "Model": 0.900})
st.bar_chart(methods)

st.subheader("Ketish xavfiga ta'sir qiluvchi omillar (logreg koeffitsiyentlari)")
coef = pd.Series({"Lifetime": -3.75, "Age": -1.16, "Contract_period": -0.73,
                  "Avg_class_frequency_total": -0.69, "Month_to_end_contract": -0.65,
                  "Avg_additional_charges_total": -0.55, "Group_visits": -0.35,
                  "Promo_friends": -0.19, "Near_Location": -0.08, "Partner": -0.02})
st.bar_chart(coef)
st.caption("Manfiy: qiymat oshsa ketish xavfi kamayadi.")

st.subheader("Cheklovlar")
st.warning("""
1. Ma'lumot bir oylik surat, vaqt bo'yicha tekshirilmagan.
2. Model a'zolik muddatiga kuchli tayanadi. Shu ustunsiz precision ~76%.
3. Joriy oy tashrifi ro'yxat sanasida ma'lum bo'lmagani uchun chiqarildi.
4. Foyda hisobi taxminiy (ushlab qolish farazi).
5. Ketuvchilarning ~32% i past guruhda qoladi.
""")
