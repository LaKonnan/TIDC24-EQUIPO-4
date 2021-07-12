<template>
    <div>
      <b-modal ref="create" id="modal-xlc" size="xl" title="NUEVO GASTO COMBUSTIBLE" hide-footer>
          <b-tabs pills card vertical v-model="tabIndex">
            <!-- paso 1 -->
            <b-tab title="PASO 1" active id="step1">
                    <b-card-text>
                        N° de Folio
                        <b-form-input  v-model="folio" @keyup="activateButton()" type="number"  aria-describedby="input-live-feedback1" ></b-form-input>
                        <b-form-invalid-feedback id="input-live-feedback1">
                        Requiere ingresar el N° de Folio
                        </b-form-invalid-feedback>

                        Fecha de Emisión
                        <b-form-datepicker  v-model="fechaEmision" @keyup="activateButton()"  aria-describedby="input-live-feedback1" ></b-form-datepicker>
                        <b-form-invalid-feedback id="input-live-feedback1">
                        Requiere ingresar la fecha de emisión
                    </b-form-invalid-feedback>

                        Hora de Emisión
                        <b-form-input v-model="horaEmision" @keyup="activateButton()" type=time  aria-describedby="input-live-feedback2" ></b-form-input>
                        <b-form-invalid-feedback id="input-live-feedback2">
                        Requiere ingresar la hora de emisión
                    </b-form-invalid-feedback>

                     Cantidad de combustible (Lts)
                        <b-form-input v-model="qtyBencina" @keyup="activateButton()" type="number"  aria-describedby="input-live-feedback2" ></b-form-input>
                        <b-form-invalid-feedback id="input-live-feedback2">
                        Requiere ingresar la cantidad de combustible
                    </b-form-invalid-feedback>

                     Estación de bencina
                        <b-form-input v-model="nombreEstacion" @keyup="activateButton()"  aria-describedby="input-live-feedback2" ></b-form-input>
                        <b-form-invalid-feedback id="input-live-feedback2">
                        Requiere ingresar nombre de la estación de bencina
                    </b-form-invalid-feedback>

                      Máquina correspondiente
                        <b-form-input v-model="maquina" @keyup="activateButton()"  aria-describedby="input-live-feedback2" ></b-form-input>
                        <b-form-invalid-feedback id="input-live-feedback2">
                        Requiere ingresar la máquina correspondiente
                    </b-form-invalid-feedback>

                     Monto Total
                        <b-form-input v-model="montoTotal" @keyup="activateButton()"  aria-describedby="input-live-feedback2" ></b-form-input>
                        <b-form-invalid-feedback id="input-live-feedback2">
                        Requiere ingresar el monto total
                    </b-form-invalid-feedback>
                     Tipo de comprobante
                        <b-form-select v-model="tipoComprobante" :options="optionComprobante" @keyup="activateButton()" ></b-form-select>
                        <b-form-invalid-feedback id="input-live-feedback2">
                        Requiere ingresar el tipo de comprobante
                    </b-form-invalid-feedback>



                       

                        <b-button :disabled="btnStep1" id="btnStep1" class="button-next dark-button" @click="next1()">Siguiente</b-button>
                    </b-card-text>
            </b-tab>

            <!-- paso  2 -->
            <b-tab title="PASO 2" id="step2" :disabled="step2">
               <b-card-text>
                        <!-- resumen de nueva obra -->
                <b-card  title="RESUMEN DE NUEVO GASTO COMBUSTIBLE">
                   <b-card-text>
                      <b-row>
                        <b-col>N° Folio</b-col>
                        <b-col>{{ this.folio }}</b-col>
                   </b-row>
                   <b-row>
                        <b-col>Fecha de Emisión</b-col>
                        <b-col>{{ this.fechaEmision }}</b-col>
                   </b-row>

                   <b-row>
                        <b-col>Hora de Emisión</b-col>
                        <b-col>{{ this.horaEmision }}</b-col>
                   </b-row>

                   <b-row>
                        <b-col>Cantidad de combustible (Lts)</b-col>
                        <b-col>{{ this.qtyBencina }}</b-col>
                   </b-row>

                   <b-row>
                        <b-col>Estación de bencina</b-col>
                        <b-col>{{ this.nombreEstacion }}</b-col>
                   </b-row>

                   <b-row>
                        <b-col>Máquina correspondiente</b-col>
                        <b-col>{{ this.maquina }}</b-col>
                   </b-row>
                   <b-row>
                        <b-col>Monto total</b-col>
                        <b-col>{{ this.montoTotal }}</b-col>
                   </b-row>
                    <b-row>
                        <b-col>Tipo de comprobante</b-col>
                        <b-col>{{ this.tipoComprobante }}</b-col>
                   </b-row>
                   </b-card-text>
               </b-card>
               <br>
                        <p>Una vez presionado el botón, se registrará el gasto en el sistema.</p>
                    <b-button id="btnStep3" class="button-next dark-button" @click="create()">GUARDAR</b-button>
             </b-card-text>
            </b-tab>
        </b-tabs>
      </b-modal>
      <b-modal ref="success-modal" id="modal-no-backdrop" hide-backdrop hide-footer hide-header>
            <center>
                <p class="success"><b-icon icon="check-circle" animation="fade"></b-icon></p>
                <p>Gasto creado con éxito</p>
            </center>
    </b-modal>
  </div>
</template>

<script>
import { getAPI } from '../axios-api';



export default {
   
  data() {
    return {
      folio:'',
      fechaEmision: '',
      horaEmision: '',
      qtyBencina: '',
      nombreEstacion: '',
      maquina: '',
      montoTotal: '',
      tipoComprobante: null,

      success: false,
      tabIndex: 2,
      btnStep1: true,
      step2: true,
      
      
      optionComprobante: [
                { value: 'Boleta', text: 'Boleta'},
                { value: 'Vale', text: 'Vale'},
                { value: 'Factura', text: 'Factura' }
            ],
     
      
    };
  },
  
  methods: {
   
   activateButton(){
     switch(this.tabIndex){
     case 0:
      if(![this.folio,
           this.fechaEmision,
           this.horaEmision,
           this.qtyBencina,
           this.nombreEstacion,
           this.maquina,
           this.montoTotal,
           this.tipoComprobante].includes(null)) {
        this.btnStep1 = false
        this.step2 = false
     }
     break;

     case 1:
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


     create(){
     console.log(this.folio)
     const options = {
       headers: {
         'Content-Type': 'application/json;charset=UTF-8',
         'Access-Control-Allow-Origin': '*'
       }
     }

     const data = JSON.stringify(
       {
         folio: this.folio,
         fechaEmision: this.fechaEmision,
         horaEmision: this.horaEmision,
         qtyBencina: this.qtyBencina,
         nombreEstacion: this.nombreEstacion,
         maquina: this.maquina,
         montoTotal: this.montoTotal,
         tipoComprobante: this.tipoComprobante
       }
     )

     getAPI.post('/gastosc', data, options)
        .then((res) =>{
          if(res.statusText == 'OK'){
            this.success = true
            this.$refs['create'].hide()
            setTimeout(() => {
               this.$refs['success-modal'].show()
            },500)
            this.$refs['success-modal'].hide()
          }

        })
        .catch((err)=>{
          console.log('Error: ', err)
        })

     }
  },

  }

</script>