<template>
    <div>
        <b-modal id="modal-xl" size="xl" title="NUEVA CAJA CHICA" hide-footer>
            <b-tabs pills card vertical v-model="tabIndex">
                <!-- paso 1 -->
                <b-tab title="PASO 1" active id="Step1">
                    <b-card-text>
                        Tipo de caja
                        <b-form-select  v-model="selected1" :options="options1"></b-form-select>

                        Obra a la que pertenece
                        <b-form-select v-model="selected2" :options="options2"></b-form-select>

                        Estado de caja
                        <b-form-select v-model="selected3" :options="options3"></b-form-select>
                        
                        <b-button :disabled="btnStep1" id="btnStep1" class="button-next dark-button" @click="next1()">Siguiente</b-button>
                    </b-card-text>
                </b-tab>

                <!-- paso 2 -->
                <b-tab title="PASO 2" id="Step2" :disabled="step2">
                    <b-card-text>
                        Fecha de inicio
                        <b-form-datepicker placeholder="" v-model="initial_date" class="mb-2"></b-form-datepicker>

                        Fecha de término
                        <b-form-datepicker placeholder="" v-model="final_date" class="mb-2"></b-form-datepicker>

                        Monto máximo de caja
                        <b-form-input></b-form-input>

                        <b-button :disabled="btnStep1" id="btnStep2" class="button-next dark-button" @click="next1()">Siguiente</b-button>
                    </b-card-text>
                </b-tab>

                <!-- paso 3 -->
                <b-tab title="PASO 3" id="Step3" :disabled="step3">
                    <b-card-text>
                    </b-card-text>
                </b-tab>
            </b-tabs>
        </b-modal>



      
    </div>
</template>

<script>

export default {
    data () {
        return  {
            initial_date: '',
            final_date: '',
            tabIndex: 2,
            step: 1,
            step2: true,
            step3: true,
            btnStep1: true,
            selected1: null,
            selected2: null,
            selected3: null,
            options1: [
                { value: 'Gerencia', text: 'Gerencia'},
                { value: 'Oficina', text: 'Oficina'},
                { value: 'Obra', text: 'Obra' }
            ],
            options2: [
                { value: '53', text: '53 - Oficina central' },
                { value : '54', text: '54 - Gerencia' },
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
                case 1 :
                    if(this.selected1 != null && this.selected2 != null) {
                        this.step2 = false
                    }

                    if( this.selected1 != null && this.selected2 != null && this.selected3 != null){
                        this.btnStep1 = false
                        this.step = 2
                    }
                    break
                case 2:
                    
                    break
                case 3:
                    break
                default:
                    break
            }
            
        },

        next1() {
            this.step2 = false
            const next = document.getElementById('Step1')
            next.classList.remove('active')
            const step = document.getElementById('Step2')
            step.classList.add('active')
            this.tabIndex++
            console.log(this.tabIndex)
        }
    },
    
    updated() {
        this.nextStep()
        console.log(this.tabIndex)
    }    

}
</script>

<style>

</style>