import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import MaterialesList from '../views/MaterialesList.vue'
import MaterialesForm from '../views/MaterialesForm.vue'
import UsuariosList from '../views/UsuariosList.vue'
import UsuariosForm from '../views/UsuariosForm.vue'
import PrestamosList from '../views/PrestamosList.vue'
import PrestamosForm from '../views/PrestamosForm.vue'
import IncidenciasList from '../views/IncidenciasList.vue'
import IncidenciasForm from '../views/IncidenciasForm.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  // Materiales
  {
    path: '/materiales',
    name: 'MaterialesList',
    component: MaterialesList
  },
  {
    path: '/materiales/crear',
    name: 'MaterialesCreate',
    component: MaterialesForm
  },
  {
    path: '/materiales/:id/editar',
    name: 'MaterialesEdit',
    component: MaterialesForm
  },
  // Usuarios
  {
    path: '/usuarios',
    name: 'UsuariosList',
    component: UsuariosList
  },
  {
    path: '/usuarios/crear',
    name: 'UsuariosCreate',
    component: UsuariosForm
  },
  {
    path: '/usuarios/:id/editar',
    name: 'UsuariosEdit',
    component: UsuariosForm
  },
  // Préstamos
  {
    path: '/prestamos',
    name: 'PrestamosList',
    component: PrestamosList
  },
  {
    path: '/prestamos/crear',
    name: 'PrestamosCreate',
    component: PrestamosForm
  },
  {
    path: '/prestamos/:id/editar',
    name: 'PrestamosEdit',
    component: PrestamosForm
  },
  // Incidencias
  {
    path: '/incidencias',
    name: 'IncidenciasList',
    component: IncidenciasList
  },
  {
    path: '/incidencias/crear',
    name: 'IncidenciasCreate',
    component: IncidenciasForm
  },
  {
    path: '/incidencias/:id/editar',
    name: 'IncidenciasEdit',
    component: IncidenciasForm
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

