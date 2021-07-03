<template>
  <div class="div-sidebar">
    <b-sidebar class="style-sidebar" v-model="sidebar" bg-variant="dark" no-header no-slide>
      <!-- logo parte superior -->
      <div class="sidebar-header">
        <img src="@/assets/header-sidebar.png">
      </div>
      
      <!-- menu -->
      <div class="sidebar-body">
        <b-list-group-item :active="isActive(item.to, item.id)" v-for="item in items" v-bind:key="item" :id="item.id" @click="changeActive()">
          <a class="menu-item" :href="item.to">
            <b-icon :icon="item.icon"></b-icon>
            {{ item.title }}
          </a>
        </b-list-group-item>
      </div>
    </b-sidebar>
    <b-navbar>
      <div class="page-title">
          {{ this.title }}
      </div>

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
      title: '',
      items: [
        { title: 'Usuarios', icon: 'people', to: '/usuarios', id: 'usuarios'},
        { title: 'Obras', icon: 'cone-striped', to: '/obras', id: 'obras'} ,
        { title: 'Máquinas', icon: 'cone-striped', to: '/maquinas', id: 'maquinas'},
        { title: 'Cajas chicas', icon: 'archive-fill', to: '/cajas-chicas', id: 'cajas'}
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
      
      isActive(item_path, item_id) {
        this.active_page = this.$router.currentRoute.fullPath
        
        if(item_path == this.active_page){
          var element = document.getElementById(item_id)
          element.classList.add('active')
        }
      },

      setTitle() {
        this.title = this.$router.currentRoute.path
        console.log(this.$router.currentRoute)
        console.log(this.title)
        switch(this.title) {
          case '/obras':
            this.title = 'GESTIÓN DE OBRAS'
            break
          case '/cajas-chicas':
            this.title = 'GESTIÓN DE CAJAS CHICAS'
            break
          case '/usuarios':
            this.title = 'GESTIÓN DE USUARIOS'
            break
          case '/maquinas':
            this.title = 'GESTIÓN DE MAQUINAS'
            break
          case '/gastos':
            this.title = 'GESTIÓN DE GASTOS'
            break
        }
      }
    },

    beforeMount() {
      this.setTitle()
    }
  }
</script>

<style lang="scss">
  @import '@/components/styles/navbar.scss';
</style>