<template>
  <div class="container">
    <div class="page-header">
      <h2>{{ isEdit ? 'Editar Incidencia' : 'Nueva Incidencia' }}</h2>
    </div>

    <div v-if="error" class="error">{{ error }}</div>

    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="codigo">Código*</label>
        <input
          type="text"
          id="codigo"
          v-model="form.codigo"
          required
        />
      </div>

      <div class="form-group">
        <label for="prestamo">Préstamo*</label>
        <select id="prestamo" v-model="form.prestamo" required>
          <option value="">Selecciona un préstamo</option>
          <option v-for="prestamo in prestamos" :key="prestamo.id" :value="prestamo.id">
            {{ prestamo.codigo }} - {{ prestamo.material_detalle ? prestamo.material_detalle.nombre : 'N/A' }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="fecha">Fecha*</label>
        <input
          type="date"
          id="fecha"
          v-model="form.fecha"
          required
        />
      </div>

      <div class="form-group">
        <label for="tipo_incidencia">Tipo de Incidencia*</label>
        <select id="tipo_incidencia" v-model="form.tipo_incidencia" required>
          <option value="daño">Daño</option>
          <option value="pérdida">Pérdida</option>
          <option value="otro">Otro</option>
        </select>
      </div>

      <div class="form-group">
        <label for="descripcion">Descripción*</label>
        <textarea
          id="descripcion"
          v-model="form.descripcion"
          rows="4"
          required
        ></textarea>
      </div>

      <div class="form-actions">
        <button type="submit" class="btn btn-primary" :disabled="loading">
          {{ loading ? 'Guardando...' : 'Guardar' }}
        </button>
        <router-link to="/incidencias" class="btn btn-secondary">Cancelar</router-link>
      </div>
    </form>
  </div>
</template>

<script>
import { incidenciasAPI, prestamosAPI } from '../services/api'

export default {
  name: 'IncidenciasForm',
  data() {
    return {
      form: {
        codigo: '',
        prestamo: '',
        fecha: '',
        tipo_incidencia: 'daño',
        descripcion: ''
      },
      prestamos: [],
      loading: false,
      error: null
    }
  },
  computed: {
    isEdit() {
      return !!this.$route.params.id
    }
  },
  mounted() {
    this.fetchPrestamos()
    if (this.isEdit) {
      this.fetchIncidencia()
    }
  },
  methods: {
    async fetchPrestamos() {
      try {
        const response = await prestamosAPI.getAll()
        this.prestamos = response.data
      } catch (error) {
        console.error('Error al cargar préstamos:', error)
      }
    },
    async fetchIncidencia() {
      try {
        const response = await incidenciasAPI.getOne(this.$route.params.id)
        this.form = {
          codigo: response.data.codigo,
          prestamo: response.data.prestamo,
          fecha: response.data.fecha,
          tipo_incidencia: response.data.tipo_incidencia,
          descripcion: response.data.descripcion
        }
      } catch (error) {
        this.error = 'Error al cargar la incidencia: ' + error.message
      }
    },
    async handleSubmit() {
      this.loading = true
      this.error = null
      try {
        if (this.isEdit) {
          await incidenciasAPI.update(this.$route.params.id, this.form)
        } else {
          await incidenciasAPI.create(this.form)
        }
        this.$router.push('/incidencias')
      } catch (error) {
        this.error = 'Error al guardar la incidencia: ' + error.message
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.form-actions {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}

.page-header h2 {
  margin-bottom: 2rem;
}
</style>

