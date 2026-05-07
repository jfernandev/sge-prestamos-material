<template>
  <div class="container">
    <div class="page-header">
      <h2>📦 Materiales</h2>
      <router-link to="/materiales/crear" class="btn btn-primary">+ Nuevo Material</router-link>
    </div>

    <div v-if="loading" class="loading">Cargando materiales...</div>

    <div v-else-if="error" class="error">{{ error }}</div>

    <table v-else>
      <thead>
        <tr>
          <th>Código</th>
          <th>Nombre</th>
          <th>Categoría</th>
          <th>Estado</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="material in materiales" :key="material.id">
          <td>{{ material.codigo }}</td>
          <td>{{ material.nombre }}</td>
          <td>{{ material.categoria }}</td>
          <td>
            <span class="badge" :class="'badge-' + material.estado">
              {{ material.estado }}
            </span>
          </td>
          <td class="actions">
            <router-link :to="`/materiales/${material.id}/editar`" class="btn btn-sm btn-secondary">
              Editar
            </router-link>
            <button @click="deleteMaterial(material.id)" class="btn btn-sm btn-danger">
              Borrar
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { materialesAPI } from '../services/api'

export default {
  name: 'MaterialesList',
  data() {
    return {
      materiales: [],
      loading: false,
      error: null
    }
  },
  mounted() {
    this.fetchMateriales()
  },
  methods: {
    async fetchMateriales() {
      this.loading = true
      this.error = null
      try {
        const response = await materialesAPI.getAll()
        this.materiales = response.data
      } catch (error) {
        this.error = 'Error al cargar los materiales: ' + error.message
      } finally {
        this.loading = false
      }
    },
    async deleteMaterial(id) {
      if (confirm('¿Estás seguro de que quieres eliminar este material?')) {
        try {
          await materialesAPI.delete(id)
          this.materiales = this.materiales.filter(m => m.id !== id)
        } catch (error) {
          alert('Error al eliminar el material: ' + error.message)
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

.badge {
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 500;
}

.badge-disponible {
  background: #e8f5e9;
  color: #2e7d32;
}

.badge-prestado {
  background: #fff3e0;
  color: #e65100;
}

.badge-retrasado {
  background: #ffebee;
  color: #c62828;
}
</style>

