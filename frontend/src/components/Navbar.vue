<template>
  <div>
    <!-- barra superior -->
    <b-navbar>
        <div v-b-toggle.sidebar class="sidebar-button" @click="hide_menubar = !hide_menubar; hide_closemenu = !hide_closemenu">
          <b-icon id="menubar" icon="list" variant="light" font-scale="2.5" :hidden="hide_menubar"></b-icon>
          <b-icon id="closemenu" icon="x" variant="light" font-scale="2.5" :hidden="hide_closemenu"></b-icon>
        </div>          

      <div class="page-title">
          {{ this.title }}
      </div>

      <div class="username">
        <b-icon class="logout" icon="power" @click="logout()" title="Cerrar sesión"></b-icon>
        <!-- {{ $auth.username }} -->
        Nombre Apellido
      </div>

      <!-- menu lateral -->
      
    </b-navbar>

    <!-- sidebar -->
    <b-sidebar id="sidebar" bg-variant="dark" no-header>
      <!-- logo en parte superior -->
      <div class="logo">
        <img src="@/assets/header-sidebar.png" alt="">
      </div>

      <!-- menu -->
      <b-link class="menu-item" @click="isActive(); hide_menubar = !hide_menubar; hide_closemenu = !hide_closemenu" v-for="item in items" :key="item.id" :id="item.id" :to="item.to" >
        <b-icon :icon="item.icon"></b-icon>
        {{ item.title }}
      </b-link>

      <div class="sidebar-footer">
        <b-icon class="logout" icon="power" @click="logout()" title="Cerrar sesión"></b-icon>
        <!-- {{ $auth.username }} -->
        Nombre Apellido
      </div>
    </b-sidebar>

  </div>

</template>

<script>
  export default {
    name: 'Navbar',
    data: () => ({ 
      drawer: null,
      active_page: null,
      hide_menubar: false,
      hide_closemenu: true,
      title: '',
      items: [
        { title: 'Usuarios', icon: 'people', to: '/usuarios', id: 'usuarios'},
        { title: 'Obras', icon: 'cone-striped', to: '/obras', id: 'obras'} ,
        { title: 'Máquinas', icon: 'cone-striped', to: '/maquinas', id: 'maquinas'},
        { title: 'Reglamento', icon: 'file-text-fill', to: '/reglamento', id: 'reglamento'},
        { title: 'Cajas chicas', icon: 'archive-fill', to: '/cajas-chicas', id: 'cajas'},

      ]
    }),

    methods: {
      // Autenticación de usuario para ingreso
      login() {
        this.$auth.loginWithRedirect();
      },

      // Cierre de sesion
      logout() {
        this.$auth.logout({
          returnTo: window.location.origin
        });
      },
      
      // determinar el item del menu que esta activo
      isActive() {
        this.active_page = this.$router.currentRoute.fullPath
        this.title = this.$route.name
        console.log(this.active_page)
        var menu_item = ''
        switch(this.active_page) {
          case '/usuarios':
            menu_item  = document.getElementById('usuarios')
            console.log('ENCONTRADO USUARIOS')
            break;

          case '/obras':
            menu_item  = document.getElementById('obras')
            console.log('ENCONTRADO OBRAS')
            break;

          case '/maquinas':
            menu_item  = document.getElementById('maquinas')
            console.log('ENCONTRADO MAQUINAS')
            break;

          case '/cajas-chicas':
            menu_item  = document.getElementById('cajas')
            console.log('ENCONTRADO CAJAS')
            break;

          case '/perfil':
            menu_item  = document.getElementById('perfil')
            console.log('ENCONTRADO PERFIL')
            break;

          case '/reglamento':
            menu_item  = document.getElementById('reglamento')
            console.log('ENCONTRADO REGLAMENTO')
            break;
        }

        // quitar clase active de existir un antecesor
        var elements = document.querySelector(".active")
        if(elements != null) {
          elements.classList.remove("active")
        }
        
        console.log(menu_item) 
        menu_item.classList.add('active')
      }
    },

    mounted() {
      this.isActive()
    }
  }
</script>

<style lang="scss">
  @import '@/components/styles/navbar.scss';
</style>