import face_recognition
import numpy as np
import pickle
import os

def check():
    known_face_encodings = []
    known_face_names = []
    for file_name in os.listdir("./known"):
        with open(f"./known/{file_name}") as file:
            f_enc = pickle.loads(bytes.fromhex(file.read()))
            known_face_encodings.append(f_enc)
            known_face_names.append(file_name)


    unknown_image = face_recognition.load_image_file("./cam.png")

    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)


        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            return known_face_names[best_match_index]
    else:
        return None


if __name__ == "__main__":
    name = check()
    if name is not None:
        print(name)
    else:
        print("Unknown")
