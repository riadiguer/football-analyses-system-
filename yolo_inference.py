from ultralytics import YOLO

# Charger le modèle YOLOv8x
model = YOLO("models/best.pt")  # Assurez-vous d'ajouter '.pt' pour spécifier le modèle correctement

# Effectuer la prédiction sur la vidéo et enregistrer les résultats dans le dossier 'runs/detect'
result = model.predict('input_video/video.mp4', save=True, project='runs', name='detect')

# Afficher les résultats de la première frame (index 0)
print(result[0])
print('***************************************************************')

# Parcourir et afficher les boîtes détectées
for box in result[0].boxes:
    print(box)
