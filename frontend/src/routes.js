import Vue from 'vue'
import VueRouter from 'vue-router'
import Obras from './views/Obras'
import cajas from './views/cajas_chicas'
import Perfil from './views/Perfil'
import Usuarios from './views/Usuarios'
import { authGuard } from "./auth/authGuard";


Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/obras',
            name: 'obras',
            component: Obras,
            beforeEnter: authGuard
        },
        {
            path: '/cajas-chicas',
            name: 'cajas',
            component: cajas,
            beforeEnter: authGuard
        },
        {
            path: '/perfil',
            name: 'perfil',
            component: Perfil,
            beforeEnter: authGuard
        },
        {
            path: '/usuarios',
            name: 'usuarios',
            component: Usuarios,
            beforeEnter: authGuard
        }
    ]
})