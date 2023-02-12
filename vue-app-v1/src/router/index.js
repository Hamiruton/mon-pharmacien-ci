import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue')
  },
  {
    path: '/settings',
    name: 'settings',
    component: () => import('../views/SettingsView.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
