<template>
  <div>
      <b-modal id="modal-edit" size="xl" title="EDITAR CAJA CHICA" hide-footer @before-open="getData()">
        <b-card-text>
            <b-tabs pills card vertical>
              <!-- caja chica -->
              <b-tab title="CAJA CHICA" active>
                <!-- ID caja chica -->
                <b-row>
                  <b-col>
                    ID caja
                  </b-col>

                  <b-col cols="9" class="mb-2">
                    {{ this.id_caja }}
                  </b-col>
                </b-row>

                <!-- ID obra -->
                <b-row>
                  <b-col>
                    Obra
                  </b-col>

                  <b-col cols="9" class="mb-2">
                    {{ this.id_obra }}
                  </b-col>
                </b-row>

                <!--  Tipo -->
                <b-row>
                  <b-col>
                    Tipo
                  </b-col>

                  <b-col cols="9" class="mb-2">
                    {{ this.tipo }}
                  </b-col>
                </b-row>

                <!-- Estado -->
                <b-row>
                  <b-col>
                    Estado
                  </b-col>

                  <b-col cols="9">
                    <b-form-select 
                      v-model="estado" 
                      :options="options1"
                      class="mb-2">
                    </b-form-select>
                  </b-col>
                </b-row>

                <!-- Fecha de inicio -->
                <b-row>
                  <b-col>
                    Fecha de inicio
                  </b-col>

                  <b-col cols="9">
                    <b-form-datepicker 
                      :min="min_date1" 
                      placeholder="" 
                      v-model="fecha_inicio"
                      class="mb-2"
                      :disabled="disableInitialDate"
                      @input="setMinFinalDate(); activateButton()">
                    </b-form-datepicker>
                  </b-col>
                </b-row>

                <!-- Fecha de término -->
                <b-row>
                  <b-col>
                    Fecha de termino
                  </b-col>

                  <b-col cols="9">
                    <b-form-datepicker 
                      :min="min_final_date" 
                      :max="max_final_date" 
                      placeholder=""
                      @input="activateButton()" 
                      v-model="fecha_termino" 
                      class="mb-2">
                    </b-form-datepicker>
                  </b-col>
                </b-row>

                <!-- Monto máximo -->
                <b-row>
                  <b-col>
                    Monto máximo
                  </b-col>

                  <b-col cols="9">
                    <b-form-group description="El monto debe ser entre $50.000 y $300.000">
                        <vue-numeric 
                            class="form-control" 
                            id="money"
                            currency="$" 
                            v-bind:min="50000"
                            v-bind:max="300000"
                            v-bind:minus="false"
                            separator="." 
                            v-model="monto_total"
                            v-on:keypress.native="activateButton();">
                        </vue-numeric>
                    </b-form-group>
                  </b-col>
                </b-row>

                <!-- Monto gastos -->
                <b-row>
                  <b-col>
                    Monto gastos
                  </b-col>

                  <b-col cols="9">
                    {{ this.monto_gastos }}
                  </b-col>
                </b-row>

                <br>

                <b-button class="normal-button" :disabled="button"  @click="updateCaja()">GUARDAR</b-button>
              </b-tab>
              
              <!-- caja combustible -->
              <b-tab title="CAJA COMBUSTIBLE">
                <!--- ID -->
                <b-row>
                  <b-col>ID de caja</b-col>
                  <b-col>{{ this.id_caja_combustible }}</b-col>
                </b-row>

                <!-- monto maximo -->
                <b-row>
                  <b-col>Monto máximo</b-col>

                  <b-col>
                    <b-form-group description="El monto debe ser entre $100.000 y $300.000">
                      <vue-numeric 
                          class="form-control" 
                          id="number"
                          currency="$" 
                          v-bind:min="100000"
                          v-bind:max="300000"
                          v-bind:minus="false"
                          separator="." 
                          v-model="monto_combustible"
                          v-on:keypress.native="activateButton()">
                      </vue-numeric>
                    </b-form-group>
                  </b-col>
                </b-row>

                <!-- monto gastos -->
                <b-row>
                  <b-col>Monto gastos</b-col>
                  <b-col>{{ this.comb_monto_gastos }}</b-col>
                </b-row>
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
      const now = new Date()
      const today = new Date(now.getFullYear(), now.getMonth(), now.getDate())
      const minDate = new Date(today) 
      return {
        caja: [],
        button: false,

        // inputs
        options1: [
          { value: 'Inactiva', text: 'Inactiva' },
          { value: 'Activa', text: 'Activa' },
          { value: 'Bloqueada', text: 'Bloqueada' },
          { value: 'Cerrada', text: 'Cerrada' }
        ],
        disableInitialDate: false,

        // datos de caja
        today: minDate,
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
    activateButton() {
      if(![this.monto_total, this.estado, this.fecha_termino, this.fecha_inicio].includes(null)){
        this.button = false
      } else {
        this.button = true
      }
    },

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
    },

    async updateCaja() {
      const accessToken = await this.$auth.getTokenSilently()

      const options = {
        headers: {
            'Content-Type': 'application/json;charset=UTF-8',
            'Access-Control-Allow-Origin': '*',
            'Authorization': `Bearer ${accessToken}`
        }
      }

      const data = JSON.stringify({
        id_caja: this.id_caja,
        estado: this.selected3,
        fecha_inicio: this.initial_date,
        fecha_termino: this.final_date,
        monto_total: this.money,
        maximo_caja_combustible: this.gas_money
      })

      getAPI.put('cajaChica/' + this.id_caja, data, options)
      .then(res => {
          console.log(res)        
          // mensaje de éxito
          this.success_text = 'Caja chica' + this.items[0].id_caja.S + 'actualizada con éxito'
          
          // mostrar modal de éxito
          this.$bvModal.hide('modal-edit')
          this.$bvModal.show('success_modal')

      }).catch(err => {
        this.error_text = 'ERROR: '+ err

        // mostrar modal de error
        this.$bvModal.hide('modal-edit')
        this.$bvModal.show('error_modal')
      })



    },

    // establecer fecha  minima
    setMinFinalDate() {
      // duracion minima de quince dias
      this.min_final_date = new Date(this.initial_date)
      this.min_final_date.setMonth(this.min_final_date.getMonth())
      this.min_final_date.setDate(this.min_final_date.getDate() + 17)
      
      // duracion  maxima de  un mes
      this.max_final_date = new Date(this.initial_date)
      this.max_final_date.setMonth(this.max_final_date.getMonth() + 1)
      this.max_final_date.setDate(this.max_final_date.getDate() + 1)
    },
  },

  mounted() {
    this.$root.$on('bv::modal::shown', (bvEvent, modalId) => {
        if( modalId == 'modal-edit') {
            this.getData()
            console.log('SE MOSTRARA EL MODAL DE EDIT', bvEvent, modalId)
        }
    })
  }

}
</script>

<style>

</style>