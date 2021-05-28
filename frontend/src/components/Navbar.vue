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
        <b-navbar-item class="light-title">CONSTRUCTORA CAMPODÓNICO</b-navbar-item>
      </b-nav-text>

      <!-- nombre de usuario -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item>
          Nombre Apellido
          <b-icon icon="power"></b-icon>
        </b-nav-item>
      </b-navbar-nav>
    </b-navbar>

    <!-- menu lateral -->
    <b-sidebar class="side-bar" id="sidebar-variant" title="MENÚ" shadow>
      <b-list-group>
        <b-list-group-item button>
           <b-link :to="'/'">
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
    })
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