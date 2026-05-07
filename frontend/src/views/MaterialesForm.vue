<template>
  <div class="container">
    <div class="page-header">
      <h2>{{ isEdit ? 'Editar Material' : 'Nuevo Material' }}</h2>
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
        <label for="nombre">Nombre*</label>
        <input
          type="text"
          id="nombre"
          v-model="form.nombre"
          required
        />
      </div>

      <div class="form-group">
        <label for="descripcion">Descripción</label>
        <textarea
          id="descripcion"
          v-model="form.descripcion"
          rows="3"
        ></textarea>
      </div>

      <div class="form-group">
        <label for="categoria">Categoría*</label>
        <input
          type="text"
          id="categoria"
          v-model="form.categoria"
          required
        />
      </div>

      <div class="form-group">
        <label for="estado">Estado*</label>
        <select id="estado" v-model="form.estado" required>
          <option value="disponible">Disponible</option>
          <option value="prestado">Prestado</option>
          <option value="retrasado">Retrasado</option>
        </select>
      </div>

      <div class="form-group">
        <label for="ubicacion">Ubicación</label>
        <input
          type="text"
          id="ubicacion"
          v-model="form.ubicacion"
        />
      </div>

      <div class="form-actions">
        <button type="submit" class="btn btn-primary" :disabled="loading">
          {{ loading ? 'Guardando...' : 'Guardar' }}
        </button>
        <router-link to="/materiales" class="btn btn-secondary">Cancelar</router-link>
      </div>
    </form>
  </div>
</template>

<script>
import { materialesAPI } from '../services/api'

export default {
  name: 'MaterialesForm',
  data() {
    return {
      form: {
        codigo: '',
        nombre: '',
        descripcion: '',
        categoria: '',
        estado: 'disponible',
        ubicacion: ''
      },
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
    if (this.isEdit) {
      this.fetchMaterial()
    }
  },
  methods: {
    async fetchMaterial() {
      try {
        const response = await materialesAPI.getOne(this.$route.params.id)
        this.form = { ...response.data }
      } catch (error) {
        this.error = 'Error al cargar el material: ' + error.message
      }
    },
    async handleSubmit() {
      this.loading = true
      this.error = null
      try {
        if (this.isEdit) {
          await materialesAPI.update(this.$route.params.id, this.form)
        } else {
          await materialesAPI.create(this.form)
        }
        this.$router.push('/materiales')
      } catch (error) {
        this.error = 'Error al guardar el material: ' + error.message
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

