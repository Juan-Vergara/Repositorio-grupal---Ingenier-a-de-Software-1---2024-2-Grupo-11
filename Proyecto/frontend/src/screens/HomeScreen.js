import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { useNavigation } from '@react-navigation/native';

const HomeScreen = () => {
  const navigation = useNavigation();

  const handleLogout = () => {
    // Aquí podrías, por ejemplo, eliminar el token de AsyncStorage si lo usas.
    // AsyncStorage.removeItem('token');
    // Luego navegas al login:
    navigation.navigate('login');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Bienvenido a EcoScan</Text>
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
});
