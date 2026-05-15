<template>
  <div class="container">
    <div class="hero">
      <h1>Sistema de Gestión de Préstamos de Material</h1>
      <p>Gestiona materiales, usuarios, préstamos e incidencias de forma eficiente</p>
    </div>

    <!-- DASHBOARD ESTADÍSTICAS -->
    <div class="dashboard" v-if="!loading">
      <h2>📊 Dashboard</h2>
      <div class="stats-grid">
        <div class="stat-card stat-materiales">
          <div class="stat-icon">📦</div>
          <div class="stat-info">
            <span class="stat-number">{{ stats.materiales.total }}</span>
            <span class="stat-label">Materiales</span>
          </div>
          <div class="stat-detail">
            <span class="available">{{ stats.materiales.disponibles }} disponibles</span>
            <span class="loaned">{{ stats.materiales.prestados }} prestados</span>
          </div>
        </div>

        <div class="stat-card stat-usuarios">
          <div class="stat-icon">👥</div>
          <div class="stat-info">
            <span class="stat-number">{{ stats.usuarios.total }}</span>
            <span class="stat-label">Usuarios</span>
          </div>
          <div class="stat-detail">
            <span>{{ stats.usuarios.estudiantes }} estudiantes</span>
            <span>{{ stats.usuarios.profesores }} profesores</span>
          </div>
        </div>

        <div class="stat-card stat-prestamos">
          <div class="stat-icon">📋</div>
          <div class="stat-info">
            <span class="stat-number">{{ stats.prestamos.activos }}</span>
            <span class="stat-label">Préstamos Activos</span>
          </div>
          <div class="stat-detail">
            <span class="warning" v-if="stats.prestamos.retrasados > 0">
              ⚠️ {{ stats.prestamos.retrasados }} retrasados
            </span>
            <span v-else class="success">✅ Sin retrasos</span>
          </div>
        </div>

        <div class="stat-card stat-incidencias">
          <div class="stat-icon">⚠️</div>
          <div class="stat-info">
            <span class="stat-number">{{ stats.incidencias.total }}</span>
            <span class="stat-label">Incidencias</span>
          </div>
          <div class="stat-detail">
            <span>{{ stats.incidencias.danos }} daños</span>
            <span>{{ stats.incidencias.perdidas }} pérdidas</span>
          </div>
        </div>
      </div>
    </div>

    <div class="cards-grid">
      <router-link to="/materiales" class="home-card">
        <div class="card-icon">📦</div>
        <h3>Materiales</h3>
        <p>Gestiona el inventario de materiales disponibles</p>
      </router-link>

      <router-link to="/usuarios" class="home-card">
        <div class="card-icon">👥</div>
        <h3>Usuarios</h3>
        <p>Administra estudiantes, empleados y departamentos</p>
      </router-link>

      <router-link to="/prestamos" class="home-card">
        <div class="card-icon">📋</div>
        <h3>Préstamos</h3>
        <p>Controla préstamos activos y devoluciones</p>
      </router-link>

      <router-link to="/incidencias" class="home-card">
        <div class="card-icon">⚠️</div>
        <h3>Incidencias</h3>
        <p>Reporta y gestiona daños o pérdidas</p>
      </router-link>
    </div>

    <div class="admin-section">
      <div class="card">
        <h3>🔧 Panel de Administración</h3>
        <p>Accede al panel completo de gestión del sistema</p>
        <router-link to="/admin" class="btn btn-primary">Ir al Panel Admin</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { materialesAPI, usuariosAPI, prestamosAPI, incidenciasAPI } from '../services/api'

export default {
  name: 'Home',
  data() {
    return {
      loading: true,
      stats: {
        materiales: { total: 0, disponibles: 0, prestados: 0 },
        usuarios: { total: 0, estudiantes: 0, profesores: 0 },
        prestamos: { total: 0, activos: 0, retrasados: 0 },
        incidencias: { total: 0, danos: 0, perdidas: 0 }
      }
    }
  },
  async mounted() {
    await this.loadStats()
  },
  methods: {
    async loadStats() {
      try {
        const [mat, usr, prs, inc] = await Promise.all([
          materialesAPI.getAll(),
          usuariosAPI.getAll(),
          prestamosAPI.getAll(),
          incidenciasAPI.getAll()
        ])

        const materiales = mat.data
        const usuarios = usr.data
        const prestamos = prs.data
        const incidencias = inc.data

        this.stats = {
          materiales: {
            total: materiales.length,
            disponibles: materiales.filter(m => m.estado === 'disponible').length,
            prestados: materiales.filter(m => m.estado === 'prestado' || m.estado === 'retrasado').length
          },
          usuarios: {
            total: usuarios.length,
            estudiantes: usuarios.filter(u => u.tipo_usuario === 'estudiante').length,
            profesores: usuarios.filter(u => u.tipo_usuario === 'profesor').length
          },
          prestamos: {
            total: prestamos.length,
            activos: prestamos.filter(p => p.estado === 'prestado').length,
            retrasados: prestamos.filter(p => p.estado === 'retrasado').length
          },
          incidencias: {
            total: incidencias.length,
            danos: incidencias.filter(i => i.tipo_incidencia === 'daño').length,
            perdidas: incidencias.filter(i => i.tipo_incidencia === 'pérdida').length
          }
        }
      } catch (error) {
        console.error('Error cargando estadísticas:', error)
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.hero {
  text-align: center;
  padding: 2rem 0;
  margin-bottom: 2rem;
}

.hero h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero p {
  font-size: 1.2rem;
  color: #666;
}

/* DASHBOARD */
.dashboard {
  margin-bottom: 3rem;
}

.dashboard h2 {
  text-align: center;
  margin-bottom: 1.5rem;
  color: #333;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.5rem;
}

.stat-card {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.stat-card .stat-icon {
  font-size: 2rem;
}

.stat-card .stat-info {
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
}

.stat-number {
  font-size: 2rem;
  font-weight: bold;
  color: #333;
}

.stat-label {
  font-size: 0.9rem;
  color: #666;
}

.stat-detail {
  display: flex;
  gap: 1rem;
  font-size: 0.85rem;
  color: #888;
  flex-wrap: wrap;
}

.stat-detail .available { color: #27ae60; }
.stat-detail .loaned { color: #e67e22; }
.stat-detail .warning { color: #e74c3c; font-weight: bold; }
.stat-detail .success { color: #27ae60; }

.stat-materiales { border-left: 4px solid #667eea; }
.stat-usuarios { border-left: 4px solid #f093fb; }
.stat-prestamos { border-left: 4px solid #4facfe; }
.stat-incidencias { border-left: 4px solid #fa709a; }

/* CARDS */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.home-card {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  text-align: center;
  text-decoration: none;
  color: inherit;
  transition: all 0.3s;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.home-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
}

.card-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.home-card h3 {
  margin-bottom: 0.5rem;
  color: #333;
}

.home-card p {
  color: #666;
  font-size: 0.9rem;
}

.admin-section {
  max-width: 600px;
  margin: 0 auto 3rem auto;
}

.admin-section .card {
  text-align: center;
}

.admin-section h3 {
  margin-bottom: 0.5rem;
}

.admin-section p {
  margin-bottom: 1.5rem;
  color: #666;
}
</style>

