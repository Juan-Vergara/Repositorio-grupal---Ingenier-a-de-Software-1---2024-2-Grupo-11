import React, { useState } from 'react';
import { View, Text, TextInput, Button, Alert, StyleSheet } from 'react-native';
import axios from 'axios';
import { useNavigation } from '@react-navigation/native';
import AsyncStorage from '@react-native-async-storage/async-storage';

// Asegúrate de que este endpoint sea el correcto en tu backend.
const API_URL = 'http://172.20.10.9:8000/api/login/';

const LoginScreen = () => {
  const navigation = useNavigation();
  
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  
  const handleLogin = async () => {
    // Validación mínima
    if (!email || !password) {
      Alert.alert('Error', 'Todos los campos son obligatorios.');
      return;
    }
    
    setLoading(true);
    
    try {
      // Petición al backend con axios y headers explícitos
      const response = await axios.post(API_URL, {
        email: email,
        password: password,
      }, {
        headers: {
          'Content-Type': 'application/json',
        }
      });
      
      console.log('Respuesta del servidor:', response.data);
      
      // Si la petición fue exitosa y recibimos el token
      if (response.status === 200 && response.data.access) {
        // Guardar el token para futuras peticiones
        await AsyncStorage.setItem('authToken', response.data.access);
        
        Alert.alert(
          'Éxito', 
          'Inicio de sesión exitoso',
          [{ text: 'OK', onPress: () => navigation.navigate('home') }]
        );
      } else {
        Alert.alert('Error', 'Ocurrió un problema al iniciar sesión');
      }
    } catch (error) {
      console.error('Error de autenticación:', error);
      
      // Mostrar mensaje de error más detallado si está disponible
      const errorMsg = error.response?.data?.error || 'No se pudo conectar con el servidor';
      Alert.alert('Error', errorMsg);
    } finally {
      setLoading(false);
    }
  };
  
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Iniciar Sesión</Text>
      
      <TextInput
        style={styles.input}
        placeholder="Correo electrónico"
        keyboardType="email-address"
        value={email}
        onChangeText={setEmail}
        autoCapitalize="none"
        testID="email-input"
      />
      
      <TextInput
        style={styles.input}
        placeholder="Contraseña"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
        testID="password-input"
      />
      
      <Button 
        title={loading ? "Procesando..." : "Iniciar Sesión"} 
        onPress={handleLogin}
        disabled={loading}
      />
      
      <View style={styles.registerContainer}>
        <Text>¿No tienes cuenta? </Text>
        <Button 
          title="Regístrate" 
          onPress={() => navigation.navigate('register')}
        />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 30,
  },
  input: {
    width: '100%',
    height: 50,
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 5,
    marginBottom: 15,
    padding: 10,
  },
  registerContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 20,
  },
});

export default LoginScreen;