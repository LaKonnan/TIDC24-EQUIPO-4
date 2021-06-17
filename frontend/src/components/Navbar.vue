<template>
  <div>
    <b-navbar style="background-color: #F39A27; color: #ffff">
      <!-- boton menu lateral -->
      <b-navbar-nav>
        <b-nav-item>
          <b-button class="menu-button" v-b-toggle.sidebar-variant>
            <b-icon icon="justify"></b-icon>
          </b-button>
        </b-nav-item>
      </b-navbar-nav>

      <!-- nombre de empresa -->
      <b-nav-text class="ml-auto">
        <b-navbar-item class="navbar-title">CONSTRUCTORA CAMPODÓNICO</b-navbar-item>
      </b-nav-text>

      <!-- nombre de usuario -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item>
          <!-- Check that the SDK client is not currently loading before accessing is methods -->
          <div v-if="!$auth.loading">
          <!-- show login when not authenticated -->
            <button v-if="!$auth.isAuthenticated" @click="login" class=dark-button>Iniciar sesión</button>
            <!-- show logout when authenticated -->
            <button v-if="$auth.isAuthenticated" @click="logout" class=dark-button>Cerrar sesión</button>
          </div>
        </b-nav-item>
      </b-navbar-nav>
    </b-navbar>

    <!-- menu lateral -->
    <b-sidebar class="side-bar" id="sidebar-variant" title="MENÚ" shadow>
      <b-list-group>
        <b-list-group-item button>
           <b-link :to="'/perfil'">
             <b-icon icon="person-circle"></b-icon>
             Mi perfil
           </b-link>
        </b-list-group-item>
        
        <b-list-group-item button>
           <b-link :to="'/usuarios'">
             <b-icon icon="people"></b-icon>
             Usuarios
           </b-link>
        </b-list-group-item>
        
        <b-list-group-item button>
           <b-link :to="'/obras'">
             <b-icon icon="cone-striped"></b-icon>
             Obras
           </b-link>
        </b-list-group-item>

        <b-list-group-item button>
           <b-link :to="'/cajas-chicas'">
             <b-icon icon="archive-fill"></b-icon>
             Cajas chicas
           </b-link>
        </b-list-group-item>

      </b-list-group>
    </b-sidebar>
  </div>
</template>

<script>
  export default {
    name: 'Navbar',
    data: () => ({ drawer: null,
    items: [
      { title: 'Obras', icon: 'cone-striped', to: '/'},
      { title: 'Cajas chicas', icon: 'archive-fill', to: '/cajas-chicas'}
    ]
    }),
    methods: {
      // Log the user in
      login() {
        this.$auth.loginWithRedirect();
      },
      // Log the user out
      logout() {
        this.$auth.logout({
          returnTo: window.location.origin
        });
      }
    }
  }
</script>

<style lang="scss">
  @import 'estilos.scss';
  
  .menu-button {
    background-color: none !important;
    color: #ffff !important;
  }

  .side-bar{
    background-color: #717D6E !important;
  }
</style>