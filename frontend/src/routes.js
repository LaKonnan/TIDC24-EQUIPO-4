import Vue from 'vue'
import VueRouter from 'vue-router'
import Obras from './views/Obras'
import cajas from './views/cajas_chicas'


Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'obras',
            component: Obras,
        },
        {
            path: '/cajas-chicas',
            name: 'cajas',
            component: cajas,
        }
    ]
})