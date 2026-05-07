<template>
  <div class="container">
    <div class="page-header">
      <h2>👥 Usuarios</h2>
      <router-link to="/usuarios/crear" class="btn btn-primary">+ Nuevo Usuario</router-link>
    </div>

    <div v-if="loading" class="loading">Cargando usuarios...</div>

    <div v-else-if="error" class="error">{{ error }}</div>

    <table v-else>
      <thead>
        <tr>
          <th>DNI</th>
          <th>Nombre</th>
          <th>Email</th>
          <th>Tipo</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="usuario in usuarios" :key="usuario.id">
          <td>{{ usuario.dni }}</td>
          <td>{{ usuario.nombre }} {{ usuario.apellidos }}</td>
          <td>{{ usuario.email }}</td>
          <td>
            <span class="badge badge-info">{{ usuario.tipo_usuario }}</span>
          </td>
          <td class="actions">
            <router-link :to="`/usuarios/${usuario.id}/editar`" class="btn btn-sm btn-secondary">
              Editar
            </router-link>
            <button @click="deleteUsuario(usuario.id)" class="btn btn-sm btn-danger">
              Borrar
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { usuariosAPI } from '../services/api'

export default {
  name: 'UsuariosList',
  data() {
    return {
      usuarios: [],
      loading: false,
      error: null
    }
  },
  mounted() {
    this.fetchUsuarios()
  },
  methods: {
    async fetchUsuarios() {
      this.loading = true
      this.error = null
      try {
        const response = await usuariosAPI.getAll()
        this.usuarios = response.data
      } catch (error) {
        this.error = 'Error al cargar los usuarios: ' + error.message
      } finally {
        this.loading = false
      }
    },
    async deleteUsuario(id) {
      if (confirm('¿Estás seguro de que quieres eliminar este usuario?')) {
        try {
          await usuariosAPI.delete(id)
          this.usuarios = this.usuarios.filter(u => u.id !== id)
        } catch (error) {
          alert('Error al eliminar el usuario: ' + error.message)
        }
      }
    }
  }
}
</script>

<style scoped>
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.page-header h2 {
  margin: 0;
}

.actions {
  display: flex;
  gap: 0.5rem;
}

.btn-sm {
  padding: 0.5rem 1rem;
  font-size: 0.9rem;
}

.badge-info {
  background: #e3f2fd;
  color: #1565c0;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 500;
}
</style>

