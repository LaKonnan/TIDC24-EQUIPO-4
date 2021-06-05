<template>
    <div>
        <b-modal id="modal-create" size="xl" title="NUEVA CAJA CHICA" hide-footer>
            <b-tabs pills card vertical v-model="tabIndex">
                <!-- paso 1 -->
                <b-tab title="PASO 1" active id="Step1">
                    <b-card-text>
                        Tipo de caja
                        <b-form-select  v-model="selected1" :options="options1"></b-form-select>

                        Obra a la que pertenece
                        <b-form-select v-model="selected2" :options="options2" :disabled="booleanSelect2">
                        </b-form-select>

                        Estado de caja
                        <b-form-select v-model="selected3" :options="options3"></b-form-select>
                        
                        <b-button :disabled="btnStep1" id="btnStep1" class="button-next dark-button" @click="next1()">Siguiente</b-button>
                    </b-card-text>
                </b-tab>

                <!-- paso 2 -->
                <b-tab title="PASO 2" id="Step2" :disabled="step2">
                    <b-card-text>
                        Fecha de inicio
                        <b-form-datepicker :min="min_date1" placeholder="" v-model="initial_date" class="mb-2"></b-form-datepicker>

                        Fecha de término
                        <b-form-datepicker placeholder="" v-model="final_date" class="mb-2" :state="errorDate"></b-form-datepicker>

                        Monto máximo de caja
                        <b-form-input v-model="money" value="" type="number" @keyup="validateMoney" id="number"></b-form-input>

                        <b-button :disabled="btnStep2" id="btnStep2" class="button-next dark-button" @click="next2">Siguiente</b-button>
                    </b-card-text>
                </b-tab>

                <!-- paso 3 -->
                <b-tab title="PASO 3" id="Step3" :disabled="step3">
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
                            </b-card-text>
                        </b-card>
                    </b-card-text>
                    <p>Una vez presionado el botón, se registrará la caja en el sistema</p>
                    <b-button id="btnStep3" class="button-next dark-button">GUARDAR</b-button>
                </b-tab>
            </b-tabs>
        </b-modal>



      
    </div>
</template>

<script>

export default {
    data () {
        // establecer minimo de fecha inicial
        const now = new Date()
        const today = new Date(now.getFullYear(), now.getMonth(), now.getDate())
        const minDate = new Date(today)
        return  {
            money: '',
            initial_date: '',
            final_date: '',
            tabIndex: 2,
            step: 1,
            step2: true,
            step3: true,
            btnStep1: true,
            btnStep2: true,
            selected1: null,
            selected2: null,
            booleanSelect2: true,
            selected3: null,
            errorDate: null,
            min_date1: minDate,
            options1: [
                { value: 'Gerencia', text: 'Gerencia'},
                { value: 'Oficina', text: 'Oficina'},
                { value: 'Obra', text: 'Obra' }
            ],
            options2: [
                { value : '54', text: '54 - Gerencia' },
                { value : '53', text: '53 - Oficina central' },
                { value: '459', text: '459 - Obra en ejemplo' },
                { value: '460', text: '460 - Obra en ejemplo' }

            ],
            options3: [
                { value: 'Activa', text: 'Activa'},
                { value: 'Inactiva', text: 'Inactiva'},
                { value: 'Cerrada', text: 'Cerrada'}
            ]
        }
    },

    methods: {
        nextStep() {
            switch(this.step){
                // habilitar paso 2
                case 1 :
                    if(this.selected1 != null && this.selected2 != null) {
                        this.step2 = false
                    }

                    if( this.selected1 != null && this.selected2 != null && this.selected3 != null){
                        this.btnStep1 = false
                        this.step = 2
                    }
                    break

                // habilitar paso 3
                case 2:
                    if(this.intial_date != '' && this.final_date != '' && this.money !='') {
                        this.btnStep2 = false
                        this.step3 = false
                        this.step = 3
                    }

                    break

                default:
                    break
            }
            
        },

        next1() {
            const next = document.getElementById('Step1')
            next.classList.remove('active')
            const step = document.getElementById('Step2')
            step.classList.add('active')
            this.tabIndex++
        },

        next2() {
            const next = document.getElementById('Step2')
            next.classList.remove('active')
            const step = document.getElementById('Step3')
            step.classList.add('active')
            this.tabIndex++
        },


        // validaciones input monto maximo  ------ hay que corregir esto para que funcione aunque se mantenga presionada la tecla
        validateMoney() {
            var out = ''
            // validar largo 
            if(this.money.length > 6){
                for(var i = 0; i <= 6; i++){
                    console.log('a')
                    out += this.money.charAt(i)
                }

                this.money = out
            }      
        },

        // actualizar select de obra segun tipo de obra
        activateSelect2() {
            if(this.selected1 != null){
                // habilitar select 
                this.booleanSelect2 = false

                // remover opciones no necesarias
                
               
            }
        },

        // validar fecha final
        validateFinalDate() {
            if(this.initial_date == this.final_date && this.initial_date != '' && this.final_date != ''){
                this.errorDate = false
                this.pop1 = true
            } else {
                this.errorDate = null
            }
        }
    },
    
    updated() {
        this.nextStep()
        this.activateSelect2()
        this.validateFinalDate()
    }    

}
</script>

<style>

</style>