<template>
  <div>
      <!-- tabla -->
      <b-table
        class = "table"
        selectable 
        :items="APIData" 
        :fields="fields"
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
        props: ['obra'],
        data () {
            return {
                fields: [
                 {key: 'obraId.S', label: 'ID'},
                 {key: 'encargado.S', label: 'Encargado'}, 
                 {key: 'nombre.S', label: 'Nombre'}, 
                 {key: 'estado.S', label: 'Estado'}, 
                 {key: 'tipo.S', label: 'Tipo'}],
                APIData: [],
                perPage: 10,
                currentPage: 1,
                selectMode: 'single',
                selected: []
            }
        },
        
        created() {
            getAPI.get('/obras',)
                .then(response => {
                    console.log('Obra API has recieved data')
                    this.APIData = response.data
                })
                .catch(err => {
                    console.log(err)
                })
        },
        
        computed: {
            rows() {
                return this.APIData.length
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

<style>

</style>