import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
// import { MapsPlugin } from '@syncfuion/ej2-vue-maps';
// // import { MapsComponent, MapsPlugin } from '@syncfusion/ej2-vue-maps';

// // Vue.component(MapsPlugin.name, MapsComponent);

// Vue.use(MapsPlugin);

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import 'core-js/stable'
import 'regenerator-runtime/runtime'
import 'intersection-observer' // Optional

import Default from '../layout/Default.vue'
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)

Vue.component('define-layout',Default)
// Install BootstrapVue
// Optionally install the BootstrapVue icon components plugin


Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
