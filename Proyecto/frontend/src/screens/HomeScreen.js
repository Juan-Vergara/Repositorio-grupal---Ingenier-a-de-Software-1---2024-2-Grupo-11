import React from 'react';
import { View, Text, Button, StyleSheet, TouchableOpacity } from 'react-native';
import { useNavigation } from '@react-navigation/native';

const HomeScreen = () => {
  const navigation = useNavigation();

  const handleLogout = () => {
    // Aquí podrías, por ejemplo, eliminar el token de AsyncStorage si lo usas.
    // AsyncStorage.removeItem('token');
    navigation.navigate('login');
  };

  const handleScan = () => {
    navigation.navigate('ScanScreen'); // Asegúrate de que 'ScanScreen' esté registrado en tu navigator
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Bienvenido a EcoScan</Text>

      <TouchableOpacity style={styles.scanButton} onPress={handleScan}>
        <Text style={styles.buttonText}>Escanear objeto</Text>
      </TouchableOpacity>

      <Button title="Cerrar sesión" onPress={handleLogout} />
    </View>
  );
};

export default HomeScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1, 
    justifyContent: 'center', 
    alignItems: 'center',
    padding: 16,
  },
  title: {
    fontSize: 24, 
    fontWeight: 'bold',
    marginBottom: 20,
  },
  scanButton: {
    backgroundColor: 'green',
    padding: 15,
    borderRadius: 8,
    marginBottom: 20,
  },
  buttonText: {
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
  },
});
