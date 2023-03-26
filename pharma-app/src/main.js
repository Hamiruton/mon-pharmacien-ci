import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axiosPlugin from './plugins/axios'

import App from './App.vue'
import router from './router'

import './assets/style.css'
import '@mdi/font/css/materialdesignicons.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(axiosPlugin)

app.mount('#app')
