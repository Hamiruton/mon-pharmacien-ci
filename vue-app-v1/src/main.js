import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import LayoutDefault from './layouts/LayoutDefault.vue'

loadFonts()

createApp(App)
  .use(router)
  .use(store)
  .use(vuetify)
  .component('LayoutDefault', LayoutDefault)
  .mount('#app')
