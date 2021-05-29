<template>
  <div>
      <!-- tabla -->
      <b-table
        class = "table"
        selectable 
        :headers="header" 
        :items="APIData" 
        :select-mode="selectMode"
        :per-page="perPage"
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
        data () {
            return {
                APIData: [],
                perPage: 10,
                currentPage: 1,
                selectMode: 'single',
                header: ['ESTADO', 'ENCARGADO', 'NOMBRE', 'ID']
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
        }
    }

</script>

<style>

</style>