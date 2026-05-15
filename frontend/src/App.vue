<template>
  <div id="app">
    <nav>
      <div class="nav-container">
        <h1>🏢 SGE - Préstamos de Material</h1>
        <ul>
          <li><router-link to="/">🏠 Inicio</router-link></li>
          <li><router-link to="/materiales">📦 Materiales</router-link></li>
          <li><router-link to="/usuarios">👥 Usuarios</router-link></li>
          <li><router-link to="/prestamos">📋 Préstamos</router-link></li>
          <li><router-link to="/incidencias">⚠️ Incidencias</router-link></li>
          <li><router-link to="/admin" class="admin-link">🔧 Admin</router-link></li>
        </ul>
      </div>
    </nav>

    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

