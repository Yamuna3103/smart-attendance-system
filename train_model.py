import pickle
import os
from sklearn.neighbors import KNeighborsClassifier

os.makedirs("models", exist_ok=True)

names = pickle.load(open("data/names.pkl", "rb"))
faces = pickle.load(open("data/faces.pkl", "rb"))

print("Training KNN model...")

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(faces, names)

pickle.dump(knn, open("models/knn_model.pkl", "wb"))

print("✅ Model trained and saved successfully!")