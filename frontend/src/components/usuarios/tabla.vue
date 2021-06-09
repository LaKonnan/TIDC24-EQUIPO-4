<template>
    <div>
      <!-- tabla -->
      <b-table
        class = "table"
        selectable 
        :fields="fields"
        :items="usuarios" 
        :usuario="usuario"
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

  </div>
</template>

<script>
import { getAPI } from '../axios-api'

export default {
    props: ['usuario'],
    data () {
        return {
            fields: [{key: 'obraId.S', label: 'ID'}, {key: 'nombre.S', label: 'Nombre'}, {key: 'encargado.S', label: 'email'}],
            usuarios: [],
            perPage: 10,
            selectMode: 'single',
            currentPage: 1,
            selected: []
        }
    },

    created() {
        // obtener lista de obras
        getAPI.get('/obras',)
                .then(response => {
                    console.log('Datos de usuario recibidos')
                    this.usuarios = response.data
                })
                .catch(err => {
                    console.log(err)
                })
    },

    computed: {
        // obtener cantidad de elementos de cajas para paginado
        rows() {
            return this.usuarios.length
        }
    },

    methods: {
        onRowSelected(items) {
            this.selected = items
            this.$emit('row-selected', false);
            this.$emit('items', items);
        }
    }
}
</script>
