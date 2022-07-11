import streamlit as st
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
import cv2

st.title('QRコード生成＆読み込みアプリ')
url = st.text_input('URL入力')
fm = 'qrcode.png'

if st.button('QRコード生成'):
    _img = qrcode.make(url)
    _img.save(fm)
    img = Image.open(fm)
    st.image(img)
if st.button('QRコード読み込み'):
	cap = cv2.VideoCapture(0)
	font = cv2.FONT_HERSHEY_SIMPLEX
	while cap.isOpened():
		ret,frame = cap.read()
		if ret == True:
			d = decode(frame)
			if d:
				frame = cv2.putText(frame,d[0].data.decode('utf-8'),(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
			cv2.imshow('frame',frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cap.release()