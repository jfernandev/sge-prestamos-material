<template>
  <div class="container">
    <div class="hero">
      <h1>Sistema de Gestión de Préstamos de Material</h1>
      <p>Gestiona materiales, usuarios, préstamos e incidencias de forma eficiente</p>
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
export default {
  name: 'Home'
}
</script>

<style scoped>
.hero {
  text-align: center;
  padding: 3rem 0;
  margin-bottom: 3rem;
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
  margin: 0 auto;
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

