import streamlit as st
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

st.title('QRコード生成＆読み込みアプリ')
url = st.text_input('URL入力')
fm = 'qrcode.png'

if st.button('QRコード生成'):
    _img = qrcode.make(url)
    _img.save(fm)
    img = Image.open(fm)
    st.image(img)
if st.button('QRコード読み込み'):
    img = Image.open(fm)
    st.text(decode(img[0].data.decode('utf-8')))