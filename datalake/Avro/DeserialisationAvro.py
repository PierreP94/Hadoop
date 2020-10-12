import fastavro

# Ouverture du fichier binaire en mode lecture
with open("characters.avro", 'rb') as avro_file:

    # Création d'un reader pour lire les données
    reader = fastavro.reader(avro_file)

    # Affichage du schéma des données
    print(reader.schema)

    # Itération sur tous les personnages
    for character in reader:
        print(character)
