import Vue from 'vue'
import VueRouter from 'vue-router'
import Obras from './views/Obras'
import cajas from './views/cajas_chicas'
import Perfil from './views/Perfil'
import Usuarios from './views/Usuarios'
import Reglamento from './views/Reglamento'
import { authGuard } from "./auth/authGuard";


Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'login',
            beforeEnter: authGuard
        },
        {
            path: '/obras',
            name: 'GESTIÓN DE OBRAS',
            component: Obras,
            beforeEnter: authGuard
        },
        {
            path: '/cajas-chicas',
            name: 'GESTIÓN DE CAJAS CHICAS',
            component: cajas,
            beforeEnter: authGuard
        },
        {
            path: '/perfil',
            name: 'PERFIL',
            component: Perfil,
            beforeEnter: authGuard
        },
        {
            path: '/usuarios',
            name: 'GESTIÓN DE USUARIOS',
            component: Usuarios,
            beforeEnter: authGuard
        },
        {
            path: '/reglamento',
            name: 'REGLAMENTO INTERNO',
            component: Reglamento,
            beforeEnter: authGuard
        }
    ]
})