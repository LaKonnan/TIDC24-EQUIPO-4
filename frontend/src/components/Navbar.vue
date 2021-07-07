<template>
  <div class="div-sidebar">
    <b-sidebar class="sidebar" bg-variant="dark" no-header id="sidebar" v-model="sidebar" :no-slide="slide">
      <!-- logo parte superior -->
      <div class="sidebar-header">
        <img src="@/assets/header-sidebar.png">
      </div>
      
      <!-- menu -->
      <div class="sidebar-body">
        <b-list-group-item :active="isActive(item.to)" v-for="item in items" :key="item.id" :id="item.id">
          <b-link :href="item.to">
            <b-icon :icon="item.icon"></b-icon>
            {{ item.title }}
          </b-link>
        </b-list-group-item>
      </div>
    </b-sidebar>

    <b-navbar>
      <div class="page-title">
          {{ this.title }}
      </div>

      <b-button @click="toggleSidebar()">Toggle Sidebar</b-button>

      <div class="username">
        Nombre Apellido
      </div>
    </b-navbar>

  </div>
</template>

<script>
  export default {
    name: 'Navbar',
    data: () => ({ 
      drawer: null,
      active_page: null,
      sidebar: true,
      slide: false,
      title: '',
      items: [
        { title: 'Usuarios', icon: 'people', to: '/usuarios', id: 'usuarios'},
        { title: 'Obras', icon: 'cone-striped', to: '/obras', id: 'obras'} ,
        { title: 'Máquinas', icon: 'cone-striped', to: '/maquinas', id: 'maquinas'},
        { title: 'Cajas chicas', icon: 'archive-fill', to: '/cajas-chicas', id: 'cajas'},
        { title: 'Reglamento', icon: 'file-text-fill', to: '/reglamento', id: 'reglamento'}
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
      isActive(item_path) {
        this.active_page = this.$router.currentRoute.fullPath
        this.title = this.$route.name

        if(item_path == this.active_page){
          return true
        } else{
          return false
        }
      },

      responsiveChanges() {
        if(window.innerWidth <= 1000) {
          // ajustes de menu lateral
          var var_sidebar = document.getElementById('sidebar')
          var_sidebar.style.setProperty("display", "flex", "important")

          this.sidebar = false
          this.slide = false
        }
      }
    },

    created() {
      // ejecutar método cada vez que las dimensiones cambian
      window.addEventListener('resize', this.responsiveChanges)
    },

    beforeDestroy() {
      // desactivar ejecución del método
      window.removeEventListener('resize', this.responsiveChanges)
    }
  }
</script>

<style lang="scss">
  @import '@/components/styles/navbar.scss';
</style>