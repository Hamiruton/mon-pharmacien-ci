import { createRouter, createWebHistory } from 'vue-router';

// Patient
import HomeView from '../views/HomeView.vue';
import LoginView from '../views/LoginView.vue';
import RegisterView from '../views/RegisterView.vue';

// Officine
import HomeViewOfficine from '../views/officine/HomeViewOfficine';
import RegisterDrugs from "../views/officine/RegisterDrugs";
import HandleStock from "../views/officine/HandleStock";
import HandlePrescrip from "../views/officine/HandlePrescrip";
import Historic from "../views/officine/Historic";
import SalesStats from "../views/officine/SalesStats";
import ReceivePrescrip from '../views/officine/ReceivePrescrip';
import RegisterOrd from '../views/officine/RegisterOrd';


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView
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
  // Routes for officine
  {
    path: '/officine/homeOfficine',
    name: 'homeOfficine',
    component: HomeViewOfficine
  },
  {
    path: '/officine/register-drugs',
    name: 'register_drugs',
    component: RegisterDrugs
  },
  {
    path: '/officine/gestion-stock',
    name: 'HandleStock',
    component: HandleStock
  },
  {
    path: '/officine/gestion-ordonnance',
    name: 'HandlePrescrip',
    component: HandlePrescrip
  },
  {
    path: '/officine/historic',
    name: 'historic',
    component: Historic
  },
  {
    path: '/officine/stats',
    name: 'stats',
    component: SalesStats
  },
  {
    path: '/officine/gestion-ordonnance/ord-recus',
    name: 'receivePrescrip',
    component: ReceivePrescrip
  },
  {
    path: '/officine/gestion-ordonnance/register-ord',
    name: 'registerOrd',
    component: RegisterOrd
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

/*
router.beforeEach((to, from, next) => {
  
  if (!localStorage.getItem('token') && to.name !== 'login') {
    next({name: 'login'})
  } else {
    next()
  }
  if (to.matched.length < 1) {
    return {name: 'home'};
  }
});
*/

export default router;
