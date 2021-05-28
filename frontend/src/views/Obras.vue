<template>
    <div class="obras">
        <Navbar></Navbar>
        <div>
            <h1>Obras de la empresa.</h1>
            <div>
                <!--Tabla que recibe datos de obras y las muestra -->
            <div class="container">
           <b-table 
           selectable
           :headers="header"
           :items="APIData"
           :select-mode="selectMode">
            </b-table>
                <div>
       <!--Estructura de botones CRUD con diseño predeterminado sin funcionalidad (aún) -->             
  <b-button-toolbar key-nav aria-label="Toolbar de CRUD">
     <b-button-group class="mx-1">
        <b-button> &laquo; </b-button>
        <b-button> &lsaquo; </b-button>
     </b-button-group>

     <b-button-group class="mx-1">
        <b-button>Crear Nueva Obra</b-button>
        <b-button>Editar Obra</b-button>
        <b-button>Eliminar Obra</b-button>
     </b-button-group>

     <b-button-group class="mx-1">
        <b-button> &rsaquo; </b-button>
        <b-button> &raquo; </b-button>
     </b-button-group>
   </b-button-toolbar>
               </div>
            </div>
         </div>
      </div>
  </div>     
    
    
</template>

<script>
    import { getAPI } from '../axios-api'
    export default {
        name: 'Obras',
        data () {
            return {
                APIData:[],
                   selectMode: 'single',
                 header: ['id', 'encargado', 'nombre', 'estado'],                                        
            }
        },
        components: {
            'navbar': require('../components/Navbar.vue').default
        },
        created () {
            getAPI.get('/obras',)
                .then(response => {
                    console.log('Obra API has receieved data')
                    this.APIData = response.data
                })
                .catch(err => {
                    console.log(err)
                })
        },
        methods: {
        }
    }
    
</script>

<style lang="scss">
    @import '../components/estilos.scss';

</style>