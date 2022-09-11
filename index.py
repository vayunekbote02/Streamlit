def main():
    import cv2 as opencv
    import streamlit as st

    st.title("Face Detection")
    st.write("Web application for realtime face detection using only Haar Cascades, streamlit and Python!")
    FRAME_WINDOW = st.image([])
    face_detector = opencv.CascadeClassifier(
        opencv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cam = opencv.VideoCapture(0)

    while cam.isOpened():
        _, frame = cam.read()
        gray = opencv.cvtColor(frame, opencv.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            opencv.rectangle(frame, pt1=(x, y), pt2=(
                x+w, y+h), color=(0, 0, 0), thickness=2)
        frame = opencv.cvtColor(frame, opencv.COLOR_BGR2RGB)
        frame = opencv.flip(frame, 1)
        FRAME_WINDOW.image(frame)


if __name__ == "__main__":
    main()
