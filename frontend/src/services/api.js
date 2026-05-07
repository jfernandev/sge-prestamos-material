import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000/api'

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
})

// Materiales
export const materialesAPI = {
  getAll: () => apiClient.get('/materiales/'),
  getOne: (id) => apiClient.get(`/materiales/${id}/`),
  create: (data) => apiClient.post('/materiales/', data),
  update: (id, data) => apiClient.put(`/materiales/${id}/`, data),
  delete: (id) => apiClient.delete(`/materiales/${id}/`)
}

// Usuarios
export const usuariosAPI = {
  getAll: () => apiClient.get('/usuarios/'),
  getOne: (id) => apiClient.get(`/usuarios/${id}/`),
  create: (data) => apiClient.post('/usuarios/', data),
  update: (id, data) => apiClient.put(`/usuarios/${id}/`, data),
  delete: (id) => apiClient.delete(`/usuarios/${id}/`)
}

// Préstamos
export const prestamosAPI = {
  getAll: () => apiClient.get('/prestamos/'),
  getOne: (id) => apiClient.get(`/prestamos/${id}/`),
  create: (data) => apiClient.post('/prestamos/', data),
  update: (id, data) => apiClient.put(`/prestamos/${id}/`, data),
  delete: (id) => apiClient.delete(`/prestamos/${id}/`),
  cerrar: (id) => apiClient.post(`/prestamos/${id}/cerrar/`)
}

// Incidencias
export const incidenciasAPI = {
  getAll: () => apiClient.get('/incidencias/'),
  getOne: (id) => apiClient.get(`/incidencias/${id}/`),
  create: (data) => apiClient.post('/incidencias/', data),
  update: (id, data) => apiClient.put(`/incidencias/${id}/`, data),
  delete: (id) => apiClient.delete(`/incidencias/${id}/`)
}

