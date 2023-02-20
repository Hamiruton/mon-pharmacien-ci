import { createApp } from 'vue'
import App from './App.vue'
import axiosPlugin from './plugins/axios'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import LayoutDefault from './layouts/LayoutDefault.vue'
import LayoutOfficine from './layouts/LayoutOfficine'

loadFonts()

createApp(App)
  .use(axiosPlugin)
  .use(router)
  .use(store)
  .use(vuetify)
  .component('LayoutDefault', LayoutDefault)
  .component('LayoutOfficine', LayoutOfficine)
  .mount('#app')
