import Vue from 'vue'
import VueRouter from 'vue-router'
import Obras from './views/Obras'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'obras',
            component: Obras,
        }
    ]
})