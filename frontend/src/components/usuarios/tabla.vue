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
            fields: [{key: 'created_at', label: 'Fecha de creación'}, {key: 'name', label: 'Nombre'}, {key: 'email', label: 'email'}],
            usuarios: [],
            perPage: 10,
            selectMode: 'single',
            currentPage: 1
        }
    },

    mounted() {
        this.get_users()
    },

    computed: {
        // obtener cantidad de elementos de cajas para paginado
        rows() {
            return this.usuarios.length
        }
    },

    methods: {
        onRowSelected(items) {
            this.$emit('row-selected', false);
            this.$emit('items', items);
        },
        async get_users(){
            const accessToken = await this.$auth.getTokenSilently()
            getAPI.get('/usuarios', {
                headers: {
                    Authorization: `Bearer ${accessToken}`
                }
            })
                    .then(response => {
                        console.log('Datos de usuario recibidos')
                        this.usuarios = response.data
                    })
                    .catch(err => {
                        console.log(err)
                    })
        }
    }
}
</script>
