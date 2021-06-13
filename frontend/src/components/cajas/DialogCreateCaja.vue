<template>
  <div>
      <b-modal id="modal-create" size="xl" title="NUEVA CAJA CHICA" hide-footer>
          <b-tabs pills card vertical v-model="tabIndex">
            <!-- paso 1 -->
            <b-tab title="PASO 1" active id="step1">
                    <b-card-text>
                        Tipo de caja
                        <b-form-select  v-model="selected1" :options="options1" @change="getObras(); activateButton()" ></b-form-select>
                        
                        Obra a la que pertenece
                        <b-form-select v-model="selected2" :options="options2" :disabled="booleanSelect2" @change="activateButton()"></b-form-select>

                        Estado de caja
                        <b-form-select v-model="selected3" :options="options3" @change="activateButton()"></b-form-select>

                        <b-button :disabled="btnStep1" id="btnStep1" class="button-next dark-button" @click="next1()">Siguiente</b-button>
                    </b-card-text>
            </b-tab>

            <!-- paso  2 -->
            <b-tab title="PASO 2" id="step2" :disabled="step2">
                <b-card-text>
                    Fecha de inicio
                    <b-form-datepicker :min="min_date1" placeholder="" v-model="initial_date" class="mb-2" @input="setMinFinalDate(); activateButton()"></b-form-datepicker>

                    Fecha de término
                    <b-form-datepicker :min="min_final_date" :max="max_final_date" @input="activateButton()" placeholder="Esta fecha debe ser mínimo quince días después de la fecha inicial y máximo treinda días después" v-model="final_date" class="mb-2"></b-form-datepicker>

                    Monto máximo de caja
                    <b-form-input v-model="money" value="" type="number" @keyup="validateMoney(); activateButton()" id="money" :state="validateRangeMoney" aria-describedby="input-live-feedback1"></b-form-input>
                    <b-form-invalid-feedback id="input-live-feedback1">
                        El mínimo es $50.000 y el máximo $300.000
                    </b-form-invalid-feedback>

                    Monto máximo de caja combustible
                    <b-form-input v-model="gas_money" value="" type="number" @keyup="validateGasMoney(); activateButton()" id="number" :state="validateRangeGasMoney" aria-describedby="input-live-feedback2"></b-form-input>
                    <b-form-invalid-feedback id="input-live-feedback2">
                        El mínimo es $100.000 y el máximo $300.000
                    </b-form-invalid-feedback>

                    <b-button :disabled="btnStep2" id="btnStep2" class="button-next dark-button" @click="next2">Siguiente</b-button>
                </b-card-text>
            </b-tab>

            <b-tab title="PASO 3" id="step3" :disabled="step3">
                <b-card-text>
                        <!-- resumen de nueva caja -->
                        <b-card  title="RESUMEN DE NUEVA CAJA CHICA">
                            <b-card-text>
                                <b-row>
                                    <b-col>TIPO DE CAJA</b-col>
                                    <b-col>{{ this.selected1 }}</b-col>
                                </b-row>

                                <b-row>
                                    <b-col>OBRA</b-col>
                                    <b-col>{{ this.selected2 }}</b-col>
                                </b-row>

                                <b-row>
                                    <b-col>ESTADO</b-col>
                                    <b-col>{{ this.selected3 }}</b-col>
                                </b-row>

                                <b-row>
                                    <b-col>FECHA DE INICIO</b-col>
                                    <b-col>{{ this.initial_date }}</b-col>
                                </b-row>

                                <b-row>
                                    <b-col>FECHA DE TÉRMINO</b-col>
                                    <b-col>{{ this.final_date }}</b-col>
                                </b-row>

                                <b-row>
                                    <b-col>MONTO MÁXIMO</b-col>
                                    <b-col>{{ this.money }}</b-col>
                                </b-row>

                                <b-row>
                                    <b-col>MONTO MÁXIMO CAJA COMBUSTIBLE</b-col>
                                    <b-col>{{ this.gas_money }}</b-col>
                                </b-row>   
                            </b-card-text>
                        </b-card>
                        <br>
                        <p>Una vez presionado el botón, se registrará la caja en el sistema, puede regresar a cualquiera de los pasos anteriores para editar los datos.</p>
                    <b-button id="btnStep3" class="button-next dark-button" @click="create()">GUARDAR</b-button>
                    </b-card-text>
                    
            </b-tab>
        </b-tabs>
      </b-modal>
  </div>
</template>

<script>
import { getAPI } from '../axios-api'

export default {
    data() {
        // establecer fecha minima la actual
        const now = new Date()
        const today = new Date(now.getFullYear(), now.getMonth(), now.getDate())
        const minDate = new Date(today) 

        return {
            //  pasos
            tabIndex: 2,
            btnStep1: true,
            btnStep2: true,
            step2: true,
            step3: true,

            //select paso 1
            aux: [],
            selected1: null,
            options1: [
                { value: 'Gerencia', text: 'Gerencia' },
                { value: 'Oficina', text: 'Oficina  central' },
                { value: 'Obra', text: 'Obra' }
            ],
            selected2: null,
            options2: [],
            booleanSelect2: true,
            selected3: null,
            options3: [
                { value: 'Activa', text: 'Activa'},
                { value: 'Inactiva', text: 'Inactiva'},
                { value: 'Cerrada', text: 'Cerrada'}
            ],

            // inputs paso  2
            min_date1: minDate,
            initial_date: '',
            final_date: '',
            min_final_date: '',
            max_final_date: '',
            money: '',
            gas_money: ''
        }
    },

    methods: {
        // obtener obras segun tipo de caja
        getObras() {
            if(this.aux.length >= 1){
                this.aux = []
                this.options2 = []
            }

            getAPI.get('/obra/tipos/'+this.selected1,)
                .then(response => {
                    this.aux= response.data
                    // paasar datos a opciones de select obra
                    for(var i = 0; i < this.aux.length; i++){
                        this.options2.push({ value: this.aux[i].obraId.S, text: (this.aux[i].obraId.S +' - '+this.aux[i].nombre.S) })
                    }
                })
            
            this.booleanSelect2 = false
        },

        // habilitar boton
        activateButton() {
            // identificar boton segun el paso 
            switch(this.tabIndex){
                // paso 1
                case 0:
                    if(![this.selected1, this.selected2, this.selected3].includes(null)) {
                        this.btnStep1 = false
                        this.step2 = false
                    }
                    break;

                // paso 2
                case 1:
                    if(this.initial_date != '' && this.final_date != '' && this.money != '' && this.gas_money != ''){7
                        this.btnStep2 = false
                        this.step3 = false
                    }
                    break;

                // paso 3
                case 2:
                    break;
            }
        },

        // pasar a paso 2 a traves del boton de paso 1
        next1() {
            const next = document.getElementById('step1')
            next.classList.remove('active')
            const step = document.getElementById('step2')
            step.classList.add('active')
            this.tabIndex++
        },

        // pasar a paso 3 a traves del boton de paso 2
        next2() {
            const next = document.getElementById('step2')
            next.classList.remove('active')
            const step = document.getElementById('step3')
            step.classList.add('active')
            this.tabIndex++
        },

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

        // validar largo de monto 
        validateMoney() {
            var out = ''
            // validar largo 
            if(this.money.length > 6){
                for(var i = 0; i <= 6; i++){
                    out += this.money.charAt(i)
                }

                this.money = out 
            }
        },

        validateGasMoney() {
            var out = ''
            // validar largo 
            if(this.gas_money.length > 6){
                for(var i = 0; i <= 6; i++){
                    out += this.gas_money.charAt(i)
                }

                this.gas_money = out
            }
        },
        
        // registrar nueva caja
        create() {

            console.log(this.selected2)
            // cofiguracion
            const options = {
                headers: {
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Access-Control-Allow-Origin': '*'
                }
            }

            // datos
            const data = JSON.stringify(
                { tipo: this.selected1 ,
                id_obra: this.selected2,
                estado: this.selected3,
                fecha_inicio: this.initial_date,
                fecha_termino: this.final_date,
                monto_total: this.money,
                monto_combustible: this.gas_money }
            )

            // crear caja chica
            getAPI.post('/cajasChicas', data, options)
                .then((res) => {
                    console.log('DATOS ENVIADOS: ', res)
                })
                .catch((err) => {
                    console.log('ERROR: ', err)
                })
        }
    },
    computed: {
        validateRangeMoney() {
            if(this.money != '') {
                const aux = parseInt(this.money)
                return aux >= 50000 && aux <= 300000 ? true : false
            }else {
                return null
            }
        },

        validateRangeGasMoney() {
            if(this.money != '') {
                const aux = parseInt(this.gas_money)
                return aux >= 100000 && aux <= 300000 ? true : false
            }else {
                return null
            }
        }
    }
}
</script>

<style>

</style>