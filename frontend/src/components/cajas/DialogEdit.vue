<template>
  <div>
      <b-modal id="modal-edit" size="xl" title="EDITAR CAJA CHICA" hide-footer>
        <b-card-text>
            <b-tabs pills card vertical>
              <!-- caja chica -->
              <b-tab title="CAJA CHICA" active>
              <b-row>
                <b-col>ID de caja</b-col>
                <b-col cols="10">{{ this.id_caja }}</b-col>
              </b-row>

              <b-row>
                <b-col>Obra perteneciente</b-col>
                <b-col cols="10">{{ this.id_obra }}</b-col>
              </b-row>

              <b-row>
                <b-col>Tipo de caja</b-col>
                <b-col cols="10">{{ this.tipo }}</b-col>
              </b-row>

              <b-row>
                <b-col>Estado</b-col>
                <b-col cols="10">
                  <b-form-select v-model="selected3" :options="options3" @change="activateButton()"></b-form-select>
                </b-col>
              </b-row>

              <b-row>
                <b-col>Fecha de inicio</b-col>
                <b-col cols="10">
                  <b-form-datepicker :min="min_date1" placeholder="" v-model="initial_date" class="mb-2" @input="setMinFinalDate(); activateButton()"></b-form-datepicker>
                </b-col>
              </b-row>

              <b-row>
                <b-col>Fecha de término</b-col>
                <b-col cols="10">
                  <b-form-datepicker :min="min_final_date" :max="max_final_date" @input="activateButton()" placeholder="Esta fecha debe ser mínimo quince días después de la fecha inicial y máximo treinda días después" v-model="final_date" class="mb-2"></b-form-datepicker>
                </b-col>
              </b-row>

              <b-row>
                <b-col>Monto máximo</b-col>
                <b-col cols="10">
                  <b-form-input v-model="money" value="" type="number" @keyup="validateMoney(); activateButton()" id="money" :state="validateRangeMoney" aria-describedby="input-live-feedback1"></b-form-input>
                </b-col>
              </b-row>
              <b-form-invalid-feedback id="input-live-feedback1">
                El mínimo es $50.000 y el máximo $300.000
              </b-form-invalid-feedback>

              <b-row>
                <b-col>Monto gastos</b-col>
                <b-col cols="10">{{ this.monto_gastos }}</b-col>
              </b-row>
                
              </b-tab>
              
              <!-- caja combustible -->
              <b-tab title="CAJA COMBUSTIBLE">

                <b-row>
                  <b-col>ID de caja</b-col>
                  <b-col>{{ this.id_caja_combustible }}</b-col>
                </b-row>

                <b-row>
                  <b-col>Monto gastos</b-col>
                  <b-col>{{ this.comb_monto_gastos }}</b-col>
                </b-row>
                
                <b-row>
                  <b-col>Monto máximo</b-col>
                  <b-col>
                    <b-form-input v-model="gas_money" value="" type="number" @keyup="validateGasMoney(); activateButton()" id="number" :state="validateRangeGasMoney" aria-describedby="input-live-feedback2"></b-form-input>
                  </b-col>
                </b-row>
      
                <b-form-invalid-feedback id="input-live-feedback2">
                El mínimo es $100.000 y el máximo $300.000
                </b-form-invalid-feedback>
              </b-tab>
        </b-tabs>
            
        </b-card-text>
      </b-modal>
  </div>
</template>

<script>
import { getAPI } from '../axios-api'

export default {
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

}
</script>

<style>

</style>