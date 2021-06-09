import Vue from 'vue'
import App from './App.vue'
import router from './routes.js'
import Amplify from 'aws-amplify';
import Vuelidate from 'vuelidate'
import aws_exports from './aws-exports';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import {
  applyPolyfills,
  defineCustomElements,
} from '@aws-amplify/ui-components/loader';
import { domain, clientId } from "../auth_config.json";
import { Auth0Plugin } from "./auth";

Amplify.configure(aws_exports);
applyPolyfills().then(() => {
  defineCustomElements(window);
});

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.use(Vuelidate)

Vue.use(Auth0Plugin, {
  domain,
  clientId,
  onRedirectCallback: appState => {
    router.push(
      appState && appState.targetUrl
        ? appState.targetUrl
        : window.location.pathname
    );
  }
});

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')

