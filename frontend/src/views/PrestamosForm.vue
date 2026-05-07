<template>
  <div class="container">
    <div class="page-header">
      <h2>{{ isEdit ? 'Editar Préstamo' : 'Nuevo Préstamo' }}</h2>
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
        <label for="usuario">Usuario*</label>
        <select id="usuario" v-model="form.usuario" required>
          <option value="">Selecciona un usuario</option>
          <option v-for="usuario in usuarios" :key="usuario.id" :value="usuario.id">
            {{ usuario.nombre }} {{ usuario.apellidos }} ({{ usuario.dni }})
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="material">Material*</label>
        <select id="material" v-model="form.material" required>
          <option value="">Selecciona un material</option>
          <option v-for="material in materiales" :key="material.id" :value="material.id">
            {{ material.nombre }} ({{ material.codigo }})
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="fecha_prestamo">Fecha de Préstamo*</label>
        <input
          type="date"
          id="fecha_prestamo"
          v-model="form.fecha_prestamo"
          required
        />
      </div>

      <div class="form-group">
        <label for="fecha_prevista_devolucion">Fecha Prevista de Devolución*</label>
        <input
          type="date"
          id="fecha_prevista_devolucion"
          v-model="form.fecha_prevista_devolucion"
          required
        />
      </div>

      <div class="form-group" v-if="isEdit">
        <label for="fecha_real_devolucion">Fecha Real de Devolución</label>
        <input
          type="date"
          id="fecha_real_devolucion"
          v-model="form.fecha_real_devolucion"
        />
      </div>

      <div class="form-group" v-if="isEdit">
        <label for="estado">Estado*</label>
        <select id="estado" v-model="form.estado" required>
          <option value="activo">Activo</option>
          <option value="devuelto">Devuelto</option>
          <option value="retrasado">Retrasado</option>
        </select>
      </div>

      <div class="form-group">
        <label for="observaciones">Observaciones</label>
        <textarea
          id="observaciones"
          v-model="form.observaciones"
          rows="3"
        ></textarea>
      </div>

      <div class="form-actions">
        <button type="submit" class="btn btn-primary" :disabled="loading">
          {{ loading ? 'Guardando...' : 'Guardar' }}
        </button>
        <router-link to="/prestamos" class="btn btn-secondary">Cancelar</router-link>
      </div>
    </form>
  </div>
</template>

<script>
import { prestamosAPI, materialesAPI, usuariosAPI } from '../services/api'

export default {
  name: 'PrestamosForm',
  data() {
    return {
      form: {
        codigo: '',
        usuario: '',
        material: '',
        fecha_prestamo: '',
        fecha_prevista_devolucion: '',
        fecha_real_devolucion: '',
        estado: 'activo',
        observaciones: ''
      },
      usuarios: [],
      materiales: [],
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
    this.fetchUsuarios()
    this.fetchMateriales()
    if (this.isEdit) {
      this.fetchPrestamo()
    }
  },
  methods: {
    async fetchUsuarios() {
      try {
        const response = await usuariosAPI.getAll()
        this.usuarios = response.data
      } catch (error) {
        console.error('Error al cargar usuarios:', error)
      }
    },
    async fetchMateriales() {
      try {
        const response = await materialesAPI.getAll()
        this.materiales = response.data
      } catch (error) {
        console.error('Error al cargar materiales:', error)
      }
    },
    async fetchPrestamo() {
      try {
        const response = await prestamosAPI.getOne(this.$route.params.id)
        this.form = {
          codigo: response.data.codigo,
          usuario: response.data.usuario,
          material: response.data.material,
          fecha_prestamo: response.data.fecha_prestamo,
          fecha_prevista_devolucion: response.data.fecha_prevista_devolucion,
          fecha_real_devolucion: response.data.fecha_real_devolucion || '',
          estado: response.data.estado,
          observaciones: response.data.observaciones || ''
        }
      } catch (error) {
        this.error = 'Error al cargar el préstamo: ' + error.message
      }
    },
    async handleSubmit() {
      this.loading = true
      this.error = null
      try {
        const data = { ...this.form }
        if (!data.fecha_real_devolucion) {
          delete data.fecha_real_devolucion
        }

        if (this.isEdit) {
          await prestamosAPI.update(this.$route.params.id, data)
        } else {
          await prestamosAPI.create(data)
        }
        this.$router.push('/prestamos')
      } catch (error) {
        this.error = 'Error al guardar el préstamo: ' + error.message
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

