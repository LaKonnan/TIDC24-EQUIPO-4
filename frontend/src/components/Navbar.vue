<template>
  <div>
    <!-- barra superior -->
    <b-navbar>
      <div v-if="show_sb_button" v-b-toggle.sidebar class="sidebar-button" @click="hide_menubar = !hide_menubar; hide_closemenu = !hide_closemenu" id="sb_button">
        <b-icon id="menubar" icon="list" variant="light" font-scale="2.5" :hidden="hide_menubar" @click="hideTitle('hide')"></b-icon>
        <b-icon id="closemenu" icon="x" variant="light" font-scale="2.5" :hidden="hide_closemenu" @click="hideTitle('show')"></b-icon>
      </div>          

      <div class="page-title" id="page-title">
        {{ this.title }}
      </div>

      <div class="username">
        Bienvenido, {{ $auth.user.name }}
      </div>     
    </b-navbar>

    <!-- sidebar -->
    <b-sidebar id="sidebar" bg-variant="dark" no-header :no-close-on-route-change="show_sidebar" :no-slide="show_sidebar" :visible="show_sidebar">
      <!-- logo en parte superior -->
      <div class="logo">
        <img src="@/assets/header-sidebar.png" alt="">
      </div>

      <!-- menu -->
      <div v-for="item in items" :key="item.id" :id="item.id" :to="item.to">
        <b-link class="menu-item" v-if="item.access" @click="isActive(); hideTitle('show'); !show_sb_button ? '#' : hide_menubar = !hide_menubar; !show_sb_button ? '#' : hide_closemenu = !hide_closemenu" :key="item.id" :id="item.id" :to="item.to" >
          <b-icon :icon="item.icon"></b-icon>
          {{ item.title }}
        </b-link>
      </div>

      <b-link class="sidebar-footer" @click="logout()">
        <b-icon class="logout" icon="power" title="Cerrar sesión"></b-icon>
        Cerrar sesión
      </b-link>
    </b-sidebar>

  </div>

</template>

<script>
import { getAPI } from './axios-api'

  export default {
    props:['user_hasAccess'],
    name: 'Navbar',
    data: () => ({ 
      // titulo de pagina
      title: '',

      // variables de barra superior y menu  lateral
      active_page: null,
      hide_menubar: false,
      hide_closemenu: true,
      show_sidebar: true,
      show_sb_button: false,
      
      // elementos del menu
      items: [
        { title: 'Usuarios', icon: 'people', to: '/usuarios', id: 'usuarios', access: true},
        { title: 'Obras', icon: 'cone-striped', to: '/obras', id: 'obras', access: true} ,
        { title: 'Máquinas', icon: 'cone-striped', to: '/maquinas', id: 'maquinas', access: true},
        { title: 'Cajas chicas', icon: 'archive-fill', to: '/cajas-chicas', id: 'cajas', access: true},
        { title: 'Reglamento', icon: 'file-text-fill', to: '/reglamento', id: 'reglamento', access: true},
      ]
    }),

    methods: {
      // autenticación de usuario para ingreso
      login() {
        this.$auth.loginWithRedirect();
      },

      // cierre de sesion
      logout() {
        this.$auth.logout({
          returnTo: window.location.origin
        });
      },

      get_rol() {
        const id = this.$auth.user.sub
        console.log(id)
        getAPI.get('/rol/'+id)
        .then(response => {
            console.log(response.data.roles[0].name)
            if(response.data.roles[0].name == 'gerente') {
              this.items[0].access = false
            }
            if(response.data.roles[0].name == 'encargado') {
              this.items[0].access = false
            }
            if(response.data.roles[0].name == 'residente') {
              this.items[0].access = false
              this.items[1].access = false
            }
        })
        .catch(err => {
            console.log(err)
        })
      },
      
      // determinar el item del menu que esta activo
      isActive() {
        this.active_page = this.$router.currentRoute.fullPath
        this.title = this.$route.name

        var menu_item = ''
        switch(this.active_page) {
          case '/usuarios':
            menu_item  = document.getElementById('usuarios')
            break;

          case '/obras':
            menu_item  = document.getElementById('obras')
            break;

          case '/maquinas':
            menu_item  = document.getElementById('maquinas')
            break;

          case '/cajas-chicas':
            menu_item  = document.getElementById('cajas')
            break;

          case '/perfil':
            menu_item  = document.getElementById('perfil')
            console.log('ENCONTRADO PERFIL')
            break;

          case '/reglamento':
            menu_item  = document.getElementById('reglamento')
            break;
        }

        // quitar clase active de existir un antecesor
        var elements = document.querySelector(".active")
        if(elements != null) {
          elements.classList.remove("active")
        }
        
        console.log(menu_item) 
        menu_item.classList.add('active')
      },

      // acciones reponsivas a realizar
      responsiveActions() {
        // elementos a utilizar
        var e_sidebar = document.getElementById('sidebar')
        var width  =  window.innerWidth

        switch(true) {
          case width <= 900:
            // Mostrar boton para abrir y cerrar menu lateral
            this.show_sb_button = true
            
            if(this.show_sidebar != false) {
              // Habilitar deslizamiento de menu lateral
              e_sidebar.style = "display: flex !important"
              this.show_sidebar = false
            }

            break

          case width >= 901:
            this.show_sb_button = false
            e_sidebar.style = "display: block !important"

            // regresar variables a estado inicial
            this.hide_menubar = false
            this.hide_closemenu = true
            this.show_sidebar = true

            // mostrar titulo nuevamente, esto para asegurar que suceda al cambiar el tamaño
            // de la ventana
            var title  = document.getElementById('page-title')
            title.style.display = "block"

            var  button = document.getElementById('sb_button')
            button.style.marginLeft = "20px"

            break
        }
      },

      // ocultar o mostrar titulo
      hideTitle(action) {
        var title  = document.getElementById('page-title')
        var  button = document.getElementById('sb_button')

        switch(action) {
          case 'hide':
            title.style.display = "none"
            button.style.marginLeft = "310px"

            break
          case 'show':
            title.style.display = "block"
            button.style.marginLeft = "20px"
            break
        }
      }
    },

    mounted() {
      this.isActive();
    },

    created() {
      window.addEventListener("resize", this.responsiveActions)
      this.get_rol()
    },

    destroyed() {
      window.removeEventListener("resize", this.responsiveActions)
    }
  }
</script>

<style lang="scss">
  @import '@/components/styles/navbar.scss';
</style>