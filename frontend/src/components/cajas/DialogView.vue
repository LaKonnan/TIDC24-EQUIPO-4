<template>
  <div>
    <b-modal id="modal-view" size="lg" title="CAJA CHICA" hide-footer>
        <b-card-text>
            <b-tabs pills card vertical>
              <!-- caja chica -->
              <b-tab title="CAJA CHICA" active>
                <b-card>
                  <b-row>
                      <b-col>ID CAJA CHICA</b-col>
                      <b-col> {{ this.id_caja }} </b-col>
                  </b-row>
                  <b-row>
                      <b-col>OBRA</b-col>
                      <b-col> {{ this.id_obra }} </b-col>
                  </b-row>
                  <b-row>
                      <b-col>TIPO DE CAJA</b-col>
                      <b-col> {{ this.tipo }} </b-col>
                  </b-row>
                  <b-row>
                      <b-col>ESTADO</b-col>
                      <b-col> {{ this.estado }} </b-col>
                  </b-row>
                  <b-row>
                      <b-col>FECHA DE INICIO</b-col>
                      <b-col> {{ this.fecha_inicio }} </b-col>
                  </b-row>
                  <b-row>
                      <b-col>FECHA DE TÉRMINO</b-col>
                      <b-col> {{ this.fecha_termino }} </b-col>
                  </b-row>
                  <b-row>
                      <b-col>MONTO GASTOS</b-col>
                      <b-col> {{ this.monto_gastos }} </b-col>
                  </b-row>
                  <b-row>
                      <b-col>MONTO ASIGNADO</b-col>
                      <b-col> {{ this.monto_total }} </b-col>
                  </b-row>
                </b-card>
                <br>
                <b-button class="normal-button">VER GASTOS</b-button>
              </b-tab>
              

              <!-- caja combustible -->
              <b-tab title="CAJA COMBUSTIBLE">
                <b-card>
                  <b-row>
                    <b-col>ID CAJA COMBUSTIBLE</b-col>
                    <b-col> {{ this.id_caja_combustible }} </b-col>
                  </b-row>
                  <b-row>
                    <b-col>ID CAJA ASOCIADA</b-col>
                    <b-col> {{ this.id_caja }} </b-col>
                  </b-row>
                  <b-row>
                    <b-col>MONTO GASTOS</b-col>
                    <b-col>{{ this.comb_monto_gastos }}</b-col>
                  </b-row>
                  <b-row>
                    <b-col>MONTO TOTAL</b-col>
                    <b-col>{{ this.comb_monto_total }}</b-col>
                  </b-row>
                </b-card>
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

        // datos de caja
        id_caja: '',
        id_obra: 0,
        tipo: '',
        estado: '',
        fecha_inicio: '',
        fecha_termino: '',
        monto_gastos: '',
        monto_total: '',

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
                
                // determinar datos
                this.id_caja = this.caja[0].id_caja.S
                this.id_obra = this.caja[0].id_obra.N
                this.tipo = this.caja[0].tipo.S
                this.estado = this.caja[0].estado.S
                this.fecha_inicio = this.caja[0].fecha_inicio.S
                this.fecha_termino = this.caja[0].fecha_termino.S
                this.monto_gastos = this.caja[0].monto_gastos.S
                this.monto_total = this.caja[0].monto_total.S
        })

        // obtener datos de caja combustible
        

      },
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