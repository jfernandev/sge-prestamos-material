<template>
  <div class="container">
    <div class="page-header">
      <h2>⚠️ Incidencias</h2>
      <router-link to="/incidencias/crear" class="btn btn-primary">+ Nueva Incidencia</router-link>
    </div>

    <div v-if="loading" class="loading">Cargando incidencias...</div>

    <div v-else-if="error" class="error">{{ error }}</div>

    <table v-else>
      <thead>
        <tr>
          <th>Código</th>
          <th>Fecha</th>
          <th>Tipo</th>
          <th>Préstamo</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="incidencia in incidencias" :key="incidencia.id">
          <td>{{ incidencia.codigo }}</td>
          <td>{{ formatDate(incidencia.fecha) }}</td>
          <td>
            <span class="badge" :class="'badge-' + incidencia.tipo_incidencia">
              {{ incidencia.tipo_incidencia }}
            </span>
          </td>
          <td>{{ incidencia.prestamo_detalle ? incidencia.prestamo_detalle.codigo : '-' }}</td>
          <td class="actions">
            <router-link :to="`/incidencias/${incidencia.id}/editar`" class="btn btn-sm btn-secondary">
              Editar
            </router-link>
            <button @click="deleteIncidencia(incidencia.id)" class="btn btn-sm btn-danger">
              Borrar
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { incidenciasAPI } from '../services/api'

export default {
  name: 'IncidenciasList',
  data() {
    return {
      incidencias: [],
      loading: false,
      error: null
    }
  },
  mounted() {
    this.fetchIncidencias()
  },
  methods: {
    async fetchIncidencias() {
      this.loading = true
      this.error = null
      try {
        const response = await incidenciasAPI.getAll()
        this.incidencias = response.data
      } catch (error) {
        this.error = 'Error al cargar las incidencias: ' + error.message
      } finally {
        this.loading = false
      }
    },
    async deleteIncidencia(id) {
      if (confirm('¿Estás seguro de que quieres eliminar esta incidencia?')) {
        try {
          await incidenciasAPI.delete(id)
          this.incidencias = this.incidencias.filter(i => i.id !== id)
        } catch (error) {
          alert('Error al eliminar la incidencia: ' + error.message)
        }
      }
    },
    formatDate(dateString) {
      if (!dateString) return '-'
      const date = new Date(dateString)
      return date.toLocaleDateString('es-ES')
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

.badge-daño {
  background: #fff3e0;
  color: #e65100;
}

.badge-pérdida {
  background: #ffebee;
  color: #c62828;
}

.badge-otro {
  background: #f1f1f1;
  color: #666;
}
</style>

