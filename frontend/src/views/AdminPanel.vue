<template>
  <div class="admin-panel">
    <div class="admin-header">
      <h1>🔧 Panel de Administración</h1>
      <p>Gestión completa del sistema</p>
    </div>

    <div class="admin-nav">
      <button
        v-for="section in sections"
        :key="section.id"
        @click="currentSection = section.id"
        :class="['nav-btn', { active: currentSection === section.id }]"
      >
        {{ section.icon }} {{ section.name }}
        <span class="badge">{{ getCounts[section.id] || 0 }}</span>
      </button>
    </div>

    <div class="admin-content">
      <!-- MATERIALES -->
      <div v-if="currentSection === 'materiales'" class="section">
        <div class="section-header">
          <h2>📦 Gestión de Materiales</h2>
          <router-link to="/materiales/crear" class="btn btn-primary">+ Añadir Material</router-link>
        </div>

        <div v-if="loading" class="loading">Cargando...</div>
        <div v-else-if="error" class="error">{{ error }}</div>

        <table v-else class="admin-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Código</th>
              <th>Nombre</th>
              <th>Categoría</th>
              <th>Estado</th>
              <th>Ubicación</th>
              <th>Fecha Alta</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in materiales" :key="item.id">
              <td>{{ item.id }}</td>
              <td><strong>{{ item.codigo }}</strong></td>
              <td>{{ item.nombre }}</td>
              <td>{{ item.categoria }}</td>
              <td>
                <span class="badge" :class="'badge-' + item.estado">{{ item.estado }}</span>
              </td>
              <td>{{ item.ubicacion }}</td>
              <td>{{ formatDate(item.fecha_alta) }}</td>
              <td class="actions">
                <router-link :to="`/materiales/${item.id}/editar`" class="btn-icon" title="Editar">✏️</router-link>
                <button @click="deleteItem('materiales', item.id)" class="btn-icon" title="Eliminar">🗑️</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- USUARIOS -->
      <div v-if="currentSection === 'usuarios'" class="section">
        <div class="section-header">
          <h2>👥 Gestión de Usuarios</h2>
          <router-link to="/usuarios/crear" class="btn btn-primary">+ Añadir Usuario</router-link>
        </div>

        <div v-if="loading" class="loading">Cargando...</div>
        <div v-else-if="error" class="error">{{ error }}</div>

        <table v-else class="admin-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>DNI</th>
              <th>Nombre Completo</th>
              <th>Email</th>
              <th>Teléfono</th>
              <th>Tipo</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in usuarios" :key="item.id">
              <td>{{ item.id }}</td>
              <td><strong>{{ item.dni }}</strong></td>
              <td>{{ item.nombre }} {{ item.apellidos }}</td>
              <td>{{ item.email }}</td>
              <td>{{ item.telefono }}</td>
              <td><span class="badge badge-info">{{ item.tipo_usuario }}</span></td>
              <td class="actions">
                <router-link :to="`/usuarios/${item.id}/editar`" class="btn-icon" title="Editar">✏️</router-link>
                <button @click="deleteItem('usuarios', item.id)" class="btn-icon" title="Eliminar">🗑️</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- PRÉSTAMOS -->
      <div v-if="currentSection === 'prestamos'" class="section">
        <div class="section-header">
          <h2>📋 Gestión de Préstamos</h2>
          <router-link to="/prestamos/crear" class="btn btn-primary">+ Añadir Préstamo</router-link>
        </div>

        <div v-if="loading" class="loading">Cargando...</div>
        <div v-else-if="error" class="error">{{ error }}</div>

        <table v-else class="admin-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Código</th>
              <th>Material</th>
              <th>Usuario</th>
              <th>Fecha Préstamo</th>
              <th>Fecha Devolución</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in prestamos" :key="item.id">
              <td>{{ item.id }}</td>
              <td><strong>{{ item.codigo }}</strong></td>
              <td>{{ getMaterialNombre(item.material) }}</td>
              <td>{{ getUsuarioNombre(item.usuario) }}</td>
              <td>{{ formatDate(item.fecha_prestamo) }}</td>
              <td>{{ item.fecha_real_devolucion ? formatDate(item.fecha_real_devolucion) : 'Pendiente' }}</td>
              <td>
                <span class="badge" :class="'badge-' + item.estado">{{ item.estado }}</span>
              </td>
              <td class="actions">
                <router-link :to="`/prestamos/${item.id}/editar`" class="btn-icon" title="Editar">✏️</router-link>
                <button v-if="item.estado !== 'devuelto'" @click="cerrarPrestamo(item.id)" class="btn-icon" title="Cerrar">✅</button>
                <button @click="deleteItem('prestamos', item.id)" class="btn-icon" title="Eliminar">🗑️</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- INCIDENCIAS -->
      <div v-if="currentSection === 'incidencias'" class="section">
        <div class="section-header">
          <h2>⚠️ Gestión de Incidencias</h2>
          <router-link to="/incidencias/crear" class="btn btn-primary">+ Añadir Incidencia</router-link>
        </div>

        <div v-if="loading" class="loading">Cargando...</div>
        <div v-else-if="error" class="error">{{ error }}</div>

        <table v-else class="admin-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Código</th>
              <th>Fecha</th>
              <th>Tipo</th>
              <th>Préstamo</th>
              <th>Descripción</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in incidencias" :key="item.id">
              <td>{{ item.id }}</td>
              <td><strong>{{ item.codigo }}</strong></td>
              <td>{{ formatDate(item.fecha) }}</td>
              <td><span class="badge badge-warning">{{ item.tipo_incidencia }}</span></td>
              <td>{{ getPrestamoCodigo(item.prestamo) }}</td>
              <td>{{ item.descripcion.substring(0, 50) }}...</td>
              <td class="actions">
                <router-link :to="`/incidencias/${item.id}/editar`" class="btn-icon" title="Editar">✏️</router-link>
                <button @click="deleteItem('incidencias', item.id)" class="btn-icon" title="Eliminar">🗑️</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { materialesAPI, usuariosAPI, prestamosAPI, incidenciasAPI } from '../services/api'

export default {
  name: 'AdminPanel',
  data() {
    return {
      currentSection: 'materiales',
      sections: [
        { id: 'materiales', name: 'Materiales', icon: '📦' },
        { id: 'usuarios', name: 'Usuarios', icon: '👥' },
        { id: 'prestamos', name: 'Préstamos', icon: '📋' },
        { id: 'incidencias', name: 'Incidencias', icon: '⚠️' }
      ],
      materiales: [],
      usuarios: [],
      prestamos: [],
      incidencias: [],
      loading: false,
      error: null
    }
  },
  computed: {
    getCounts() {
      return {
        materiales: this.materiales.length,
        usuarios: this.usuarios.length,
        prestamos: this.prestamos.length,
        incidencias: this.incidencias.length
      }
    }
  },
  watch: {
    currentSection(newSection) {
      this.loadData(newSection)
    }
  },
  mounted() {
    this.loadAllData()
  },
  methods: {
    async loadAllData() {
      try {
        const [mat, usr, prs, inc] = await Promise.all([
          materialesAPI.getAll(),
          usuariosAPI.getAll(),
          prestamosAPI.getAll(),
          incidenciasAPI.getAll()
        ])
        this.materiales = mat.data
        this.usuarios = usr.data
        this.prestamos = prs.data
        this.incidencias = inc.data
      } catch (error) {
        console.error('Error cargando datos:', error)
      }
    },
    async loadData(section) {
      this.loading = true
      this.error = null
      try {
        let response
        switch(section) {
          case 'materiales':
            response = await materialesAPI.getAll()
            this.materiales = response.data
            break
          case 'usuarios':
            response = await usuariosAPI.getAll()
            this.usuarios = response.data
            break
          case 'prestamos':
            response = await prestamosAPI.getAll()
            this.prestamos = response.data
            break
          case 'incidencias':
            response = await incidenciasAPI.getAll()
            this.incidencias = response.data
            break
        }
      } catch (error) {
        this.error = 'Error al cargar los datos: ' + error.message
      } finally {
        this.loading = false
      }
    },
    async deleteItem(type, id) {
      if (!confirm('¿Estás seguro de que quieres eliminar este registro?')) return

      try {
        switch(type) {
          case 'materiales':
            await materialesAPI.delete(id)
            this.materiales = this.materiales.filter(m => m.id !== id)
            break
          case 'usuarios':
            await usuariosAPI.delete(id)
            this.usuarios = this.usuarios.filter(u => u.id !== id)
            break
          case 'prestamos':
            await prestamosAPI.delete(id)
            this.prestamos = this.prestamos.filter(p => p.id !== id)
            break
          case 'incidencias':
            await incidenciasAPI.delete(id)
            this.incidencias = this.incidencias.filter(i => i.id !== id)
            break
        }
        alert('Registro eliminado correctamente')
      } catch (error) {
        alert('Error al eliminar: ' + error.message)
      }
    },
    async cerrarPrestamo(id) {
      try {
        await prestamosAPI.cerrar(id)
        await this.loadData('prestamos')
        alert('Préstamo cerrado correctamente')
      } catch (error) {
        alert('Error al cerrar préstamo: ' + error.message)
      }
    },
    formatDate(date) {
      if (!date) return '-'
      return new Date(date).toLocaleDateString('es-ES')
    },
    getMaterialNombre(id) {
      const material = this.materiales.find(m => m.id === id)
      return material ? material.nombre : `Material #${id}`
    },
    getUsuarioNombre(id) {
      const usuario = this.usuarios.find(u => u.id === id)
      return usuario ? `${usuario.nombre} ${usuario.apellidos}` : `Usuario #${id}`
    },
    getPrestamoCodigo(id) {
      const prestamo = this.prestamos.find(p => p.id === id)
      return prestamo ? prestamo.codigo : `Préstamo #${id}`
    }
  }
}
</script>

<style scoped>
.admin-panel {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
}

.admin-header {
  text-align: center;
  margin-bottom: 3rem;
  padding: 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 15px;
}

.admin-header h1 {
  margin: 0 0 0.5rem 0;
  font-size: 2.5rem;
}

.admin-header p {
  margin: 0;
  opacity: 0.9;
}

.admin-nav {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  justify-content: center;
}

.nav-btn {
  padding: 1rem 2rem;
  border: 2px solid #e0e0e0;
  background: white;
  border-radius: 10px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 500;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.nav-btn:hover {
  background: #f5f5f5;
  transform: translateY(-2px);
}

.nav-btn.active {
  background: #667eea;
  color: white;
  border-color: #667eea;
}

.nav-btn .badge {
  background: rgba(0,0,0,0.2);
  padding: 0.25rem 0.5rem;
  border-radius: 12px;
  font-size: 0.85rem;
  min-width: 24px;
  text-align: center;
}

.nav-btn.active .badge {
  background: rgba(255,255,255,0.3);
}

.admin-content {
  background: white;
  border-radius: 15px;
  padding: 2rem;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid #e0e0e0;
}

.section-header h2 {
  margin: 0;
  color: #333;
}

.admin-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.95rem;
}

.admin-table thead {
  background: #f8f9fa;
}

.admin-table th {
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  color: #666;
  border-bottom: 2px solid #dee2e6;
}

.admin-table td {
  padding: 1rem;
  border-bottom: 1px solid #dee2e6;
  vertical-align: middle;
}

.admin-table tbody tr:hover {
  background: #f8f9fa;
}

.actions {
  display: flex;
  gap: 0.5rem;
  white-space: nowrap;
}

.btn-icon {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.3rem;
  padding: 0.25rem;
  transition: transform 0.2s;
}

.btn-icon:hover {
  transform: scale(1.2);
}

.badge {
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 500;
  display: inline-block;
}

.badge-disponible {
  background: #d4edda;
  color: #155724;
}

.badge-prestado {
  background: #fff3cd;
  color: #856404;
}

.badge-retrasado {
  background: #f8d7da;
  color: #721c24;
}

.badge-devuelto {
  background: #d1ecf1;
  color: #0c5460;
}

.badge-info {
  background: #e7f3ff;
  color: #004085;
}

.badge-warning {
  background: #fff3cd;
  color: #856404;
}

.loading, .error {
  text-align: center;
  padding: 3rem;
  font-size: 1.1rem;
}

.error {
  color: #721c24;
  background: #f8d7da;
  border-radius: 8px;
}
</style>
