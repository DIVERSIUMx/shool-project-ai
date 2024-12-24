import face_recognition
import sys


f_img = face_recognition.load_image_file(sys.argv[-2])
f_enc = face_recognition.face_encodings(f_img)[0]
f_enc_hex = f_enc.dumps().hex()

with open(f"./known/{sys.argv[-1]}", "w") as file:
    file.write(f_enc_hex)
