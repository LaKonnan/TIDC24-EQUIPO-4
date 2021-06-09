<template>
    <div>
      <!-- tabla -->
      <b-table
        class = "table"
        selectable 
        :fields="fields" 
        :items="cajas"
        :select-mode="selectMode"
        :per-page="perPage"
        @row-selected="onRowSelected"
        hover
        fixed
        responsive
        :current-page="currentPage">
      </b-table>

      <!-- paginado -->
      <b-pagination 
        v-model="currentPage" 
        :total-rows="rows" 
        :per-page="perPage" 
        aria-controls="my-table">
      </b-pagination>
        
        <b-button class="normal-button" @click="getCajas">cajas</b-button>
        {{ test }}
  </div>
</template>

<script>
import { getAPI } from '../axios-api'
export default {
    props: ['caja'],
    data () {
        return {
            cajas: [],
            test: [],
            perPage: 10,
            selectMode: 'single',
            currentPage: 1,
            selected: [],
            fields: [{key: 'obraId.S', label: 'ID'}, {key: 'encargado.S', label: 'Encargado'}, {key: 'nombre.S', label: 'Nombre'}, {key: 'estado.S', label: 'Estado'}],
        }
    },

    created() {
        // obtener lista de obras
        getAPI.get('/obras',)
            .then(response => {
                console.log('Datos de caja recibidos')
                this.cajas = response.data
                console.log(this.cajas)
            })
            .catch(err => {
                console.log(err)
            })
    },

    computed: {
        // obtener cantidad de elementos de cajas para paginado
        rows() {
            return this.cajas.length
        }
    },

    methods: {
        onRowSelected(items) {
            this.selected = items
            console.table(this.selected)
            
        },

        getCajas() {
            getAPI.get('/cajas_chicas',)
            .then(response => {
                console.log('Datos de caja recibidos')
                this.test = response.data
            })
            .cath(err => {
                console.log(err)
            })
        }
        
    },
}
</script>

<style>

</style>