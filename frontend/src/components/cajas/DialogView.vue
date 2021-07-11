<template>
  <div>
    <b-modal id="modal-view" size="lg" title="CAJA CHICA" hide-footer @hidden="resetData()">
        <b-card-text>
            <b-tabs pills card vertical>

              <!-- caja chica -->
              <b-tab title="CAJA CHICA" active>
                <b-table stacked :items="resume1"></b-table>
                <br>
                <b-button class="normal-button">VER GASTOS</b-button>
              </b-tab>
              

              <!-- caja combustible -->
              <b-tab title="CAJA COMBUSTIBLE">
                <b-table stacked :items="resume2"></b-table>
                <br>
                <b-button class="normal-button">VER GASTOS</b-button>
              </b-tab>
        </b-tabs>
            
        </b-card-text>
    </b-modal>
  </div>
</template>

<script>
import { getAPI } from '../axios-api'

export default {
  props: ['items'],
  data() {
    return {
      caja: [],
      resume1: [],
      resume2: [],

      // datos caja combustible
      id_caja_combustible: '',
      comb_monto_gastos: '',
      comb_monto_total: ''
    }
  },

  methods: {
    getData() {
      // obtener datos de caja chica
      getAPI.get('/cajasChicas/'+ this.items[0].id_caja.S ,)
        .then(response => {
          this.caja = response.data
          
          this.resume1.push({
            ID: this.caja[0].id_caja.S,
            Obra: this.caja[0].id_obra.S,
            Tipo: this.caja[0].tipo.S,
            Estado: this.caja[0].estado.S,
            Fecha_de_inicio: this.caja[0].fecha_inicio.S,
            Fecha_de_termino: this.caja[0].fecha_termino.S,
            Monto_gastos: this.caja[0].monto_gastos.S,
            Monto_total: this.caja[0].monto_total.S
          })
          
      })

      // obtener datos de caja combustible
      getAPI.get('/cajasChicas/combustible' ,)
        .then(response => {
          this.caja = response.data

          this.resume2.push({
            ID: this.caja[0].id_caja_combustible.S,
            Monto_gastos: this.caja[0].monto_gastos.S,
            Monto_total: this.caja[0].monto_maximo.S
          })
          
        })
    },

    resetData() {
      this.resume1.splice(0)
      this.resume2.splice(0)
    }
  },

  mounted() {
    this.$root.$on('bv::modal::shown', (bvEvent, modalId) => {
        if( modalId == 'modal-view') {
          this.getData()
          console.log('SE MOSTRARA EL MODAL DE VIEW', bvEvent, modalId)
        }
    })
  }

}
</script>

<style>

</style>