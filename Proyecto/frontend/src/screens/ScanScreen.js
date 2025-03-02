import React, { useState } from 'react';
import { View, Text, Button, Image, ActivityIndicator, StyleSheet, Alert } from 'react-native';
import * as ImagePicker from 'expo-image-picker';

const ScanScreen = () => {
  const [imageUri, setImageUri] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  // Función para solicitar permisos y capturar imagen
  const pickImage = async () => {
    // Solicitar permisos de cámara
    const { status } = await ImagePicker.requestCameraPermissionsAsync();
    if (status !== 'granted') {
      Alert.alert('Permiso denegado', 'Se necesitan permisos para acceder a la cámara.');
      return;
    }
    
    // Abrir la cámara para tomar una foto
    let result = await ImagePicker.launchCameraAsync({
      allowsEditing: true,
      aspect: [4, 3],
      quality: 1,
    });
    
    // En la versión reciente, el resultado contiene "canceled" y "assets"
    if (!result.canceled) {
      // La imagen se encuentra en result.assets[0].uri
      setImageUri(result.assets[0].uri);
      setResult(null);
    }
  };

  // Función para enviar la imagen al backend
  const uploadImage = async () => {
    if (!imageUri) {
      Alert.alert('Error', 'Debes tomar una foto primero.');
      return;
    }
    
    setLoading(true);
    let localUri = imageUri;
    let filename = localUri.split('/').pop();

    // Inferir el tipo MIME
    let match = /\.(\w+)$/.exec(filename);
    let type = match ? `image/${match[1].toLowerCase()}` : `image`;

    // Construir FormData
    let formData = new FormData();
    formData.append('image', { uri: localUri, name: filename, type });

    try {
      // Cambia la URL según tu entorno. Si usas un emulador de Expo, 127.0.0.1 se resuelve al dispositivo; en ese caso, usa la IP de tu máquina.
      const response = await fetch('http://192.168.80.62:8000/api/scan/', {
        method: 'POST',
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        body: formData,
      });
      const json = await response.json();
      setResult(json);
    } catch (error) {
      Alert.alert('Error al subir la imagen', error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <Button title="Tomar Foto" onPress={pickImage} />
      {imageUri && (
        <Image source={{ uri: imageUri }} style={styles.image} />
      )}
      <Button title="Enviar a escanear" onPress={uploadImage} />
      {loading && <ActivityIndicator size="large" color="#0000ff" />}
      {result && (
        <View style={styles.resultContainer}>
          <Text style={styles.resultText}>
            Material identificado: {result.predicted_class}
          </Text>
          <Text style={styles.resultText}>
            Contenedor recomendado: {result.recommended_container}
          </Text>
        </View>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    alignItems: 'center',
    justifyContent: 'center',
  },
  image: {
    width: 300,
    height: 300,
    marginVertical: 16,
    borderRadius: 8,
  },
  resultContainer: {
    marginTop: 16,
    alignItems: 'center',
  },
  resultText: {
    fontSize: 16,
    marginVertical: 4,
  },
});

export default ScanScreen;
