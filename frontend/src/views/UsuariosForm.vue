<template>
  <div class="container">
    <div class="page-header">
      <h2>{{ isEdit ? 'Editar Usuario' : 'Nuevo Usuario' }}</h2>
    </div>

    <div v-if="error" class="error">{{ error }}</div>

    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="dni">DNI*</label>
        <input
          type="text"
          id="dni"
          v-model="form.dni"
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
        <label for="apellidos">Apellidos*</label>
        <input
          type="text"
          id="apellidos"
          v-model="form.apellidos"
          required
        />
      </div>

      <div class="form-group">
        <label for="email">Email*</label>
        <input
          type="email"
          id="email"
          v-model="form.email"
          required
        />
      </div>

      <div class="form-group">
        <label for="telefono">Teléfono</label>
        <input
          type="tel"
          id="telefono"
          v-model="form.telefono"
        />
      </div>

      <div class="form-group">
        <label for="tipo_usuario">Tipo de Usuario*</label>
        <select id="tipo_usuario" v-model="form.tipo_usuario" required>
          <option value="estudiante">Estudiante</option>
          <option value="empleado">Empleado</option>
          <option value="departamento">Departamento</option>
        </select>
      </div>

      <div class="form-actions">
        <button type="submit" class="btn btn-primary" :disabled="loading">
          {{ loading ? 'Guardando...' : 'Guardar' }}
        </button>
        <router-link to="/usuarios" class="btn btn-secondary">Cancelar</router-link>
      </div>
    </form>
  </div>
</template>

<script>
import { usuariosAPI } from '../services/api'

export default {
  name: 'UsuariosForm',
  data() {
    return {
      form: {
        dni: '',
        nombre: '',
        apellidos: '',
        email: '',
        telefono: '',
        tipo_usuario: 'estudiante'
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
      this.fetchUsuario()
    }
  },
  methods: {
    async fetchUsuario() {
      try {
        const response = await usuariosAPI.getOne(this.$route.params.id)
        this.form = { ...response.data }
      } catch (error) {
        this.error = 'Error al cargar el usuario: ' + error.message
      }
    },
    async handleSubmit() {
      this.loading = true
      this.error = null
      try {
        if (this.isEdit) {
          await usuariosAPI.update(this.$route.params.id, this.form)
        } else {
          await usuariosAPI.create(this.form)
        }
        this.$router.push('/usuarios')
      } catch (error) {
        this.error = 'Error al guardar el usuario: ' + error.message
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

