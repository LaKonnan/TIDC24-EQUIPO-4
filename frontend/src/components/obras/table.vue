<template>
  <div>
      <!-- tabla -->
      <b-table
        class = "table table-responsive-sm"
        :fields="fields"
        :items="obras" 
        :select-mode="selectMode"
        :per-page="perPage"
        @row-selected="onRowSelected"
        :current-page="currentPage"
        hover
        selectable 
        >
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
                obras: [],
                perPage: 10,
                selectMode: 'single',
                currentPage: 1,
                selected: [],
                fields: [
                    {key: 'obraId.S', label: 'ID', sortable: true},
                    {key: 'encargado.S', label: 'Encargado', sortable: true}, 
                    {key: 'nombre.S', label: 'Nombre', sortable: true}, 
                    {key: 'estado.S', label: 'Estado', sortable: true}, 
                    {key: 'tipo.S', label: 'Tipo', sortable: true}
                ],
            }
        },
        
        //  obtener datos de obras
        mounted() {
            this.get_obras();
        },
        
        computed: {
            // obtener cantidad de elementos de cajas para paginado
            rows() {
                return this.obras.length
            }
        },

        methods: {
            // obtener id de caja elegida
            onRowSelected(items) {
                this.selected = items
                this.$emit('row-selected', false);
                this.$emit('items', items);
            },
            async get_obras() {
                const accessToken = await this.$auth.getTokenSilently()
                getAPI.get('/obras', {
                    headers: {
                        Authorization: `Bearer ${accessToken}`
                    }
                })
                .then(response => {
                    this.obras = response.data
                })
                .catch(err => {
                    console.log(err)
                })
            }
    }
}

</script>

<style>

</style>