import streamlit as st
import cv2

st.title('カメラテスト')
if st.button('カメラ起動'):
	cap = cv2.VideoCapture(0)
	while True:
		ret,frame = cap.read()
		if ret == True:
			cv2.imshow('frame',frame)
		else:
			st.text('カメラが設定されていません')

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cap.release()
	cv2.destroyAllWindows()