<template>
  <div class="container">
    <div class="page-header">
      <h2>📋 Préstamos</h2>
      <router-link to="/prestamos/crear" class="btn btn-primary">+ Nuevo Préstamo</router-link>
    </div>

    <div v-if="loading" class="loading">Cargando préstamos...</div>

    <div v-else-if="error" class="error">{{ error }}</div>

    <table v-else>
      <thead>
        <tr>
          <th>Código</th>
          <th>Material</th>
          <th>Usuario</th>
          <th>Fecha Préstamo</th>
          <th>Estado</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="prestamo in prestamos" :key="prestamo.id">
          <td>{{ prestamo.codigo }}</td>
          <td>{{ prestamo.material_detalle ? prestamo.material_detalle.nombre : '-' }}</td>
          <td>{{ prestamo.usuario_detalle ? `${prestamo.usuario_detalle.nombre} ${prestamo.usuario_detalle.apellidos}` : '-' }}</td>
          <td>{{ formatDate(prestamo.fecha_prestamo) }}</td>
          <td>
            <span class="badge" :class="'badge-' + prestamo.estado">
              {{ prestamo.estado }}
            </span>
          </td>
          <td class="actions">
            <button v-if="prestamo.estado !== 'devuelto'" @click="cerrarPrestamo(prestamo.id)" class="btn btn-sm btn-success">
              Cerrar
            </button>
            <router-link :to="`/prestamos/${prestamo.id}/editar`" class="btn btn-sm btn-secondary">
              Editar
            </router-link>
            <button @click="deletePrestamo(prestamo.id)" class="btn btn-sm btn-danger">
              Borrar
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { prestamosAPI } from '../services/api'

export default {
  name: 'PrestamosList',
  data() {
    return {
      prestamos: [],
      loading: false,
      error: null
    }
  },
  mounted() {
    this.fetchPrestamos()
  },
  methods: {
    async fetchPrestamos() {
      this.loading = true
      this.error = null
      try {
        const response = await prestamosAPI.getAll()
        this.prestamos = response.data
      } catch (error) {
        this.error = 'Error al cargar los préstamos: ' + error.message
      } finally {
        this.loading = false
      }
    },
    async cerrarPrestamo(id) {
      if (confirm('¿Cerrar este préstamo?')) {
        try {
          await prestamosAPI.cerrar(id)
          this.fetchPrestamos() // Recargar la lista
        } catch (error) {
          alert('Error al cerrar el préstamo: ' + error.message)
        }
      }
    },
    async deletePrestamo(id) {
      if (confirm('¿Estás seguro de que quieres eliminar este préstamo?')) {
        try {
          await prestamosAPI.delete(id)
          this.prestamos = this.prestamos.filter(p => p.id !== id)
        } catch (error) {
          alert('Error al eliminar el préstamo: ' + error.message)
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
  flex-wrap: wrap;
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

/* Compatibilidad con estado antiguo "activo" */
.badge-activo {
  background: #fff3e0;
  color: #e65100;
}

/* Estado actual "prestado" (naranja, como Materiales) */
.badge-prestado {
  background: #fff3e0;
  color: #e65100;
}

.badge-devuelto {
  background: #e8f5e9;
  color: #2e7d32;
}

.badge-retrasado {
  background: #ffebee;
  color: #c62828;
}
</style>

