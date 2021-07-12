<template>
    <div>
        <b-modal ref="create" id="modal-xle" size="xl" title="EDITAR GASTO COMBUSTIBLE" hide-footer>    
                <b-card-text>
                        Los siguientes datos de gasto combustible seleccionado serán editados
                        <hr>
                        <b>Gasto combustible:</b>
                          <b-card-text>
                      <b-row>
                        <b-col>N° Folio</b-col>
                        <b-col>{{items[0].folio.S}}
                          {{setFolio(items[0].folio.S)}}</b-col>
                   </b-row>
                   <b-row>
                        <b-col>Fecha de emisión</b-col>
                        <b-col>{{items[0].fechaEmision.S}}</b-col>
                   </b-row>

                   <b-row>
                        <b-col>Hora de emisión</b-col>
                        <b-col>{{items[0].horaEmision.S}}</b-col>
                   </b-row>

                   <b-row>
                        <b-col>Cantidad de combustible (Lts)</b-col>
                        <b-col>{{items[0].qtyBencina.S}}</b-col>
                   </b-row>

                   <b-row>
                        <b-col>Estación de bencina</b-col>
                        <b-col>{{items[0].nombreEstacion.S}}</b-col>
                   </b-row>

                    <b-row>
                        <b-col>Máquina correspondiente</b-col>
                        <b-col>{{items[0].maquina.S}}</b-col>
                   </b-row>

                   <b-row>
                        <b-col>Monto total</b-col>
                        <b-col>{{items[0].montoTotal.S}}</b-col>
                   </b-row>

                   <b-row>
                        <b-col>Tipo de comprobante</b-col>
                        <b-col>{{items[0].tipoComprobante.S}}</b-col>
                   </b-row>
                   </b-card-text>
                  
                  <hr>
                    

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
                <b-button :disabled="btnEdit" id="btnEdit" class="button-next dark-button" @click="createEdit()">Editar</b-button>
                        
          </b-card-text>
        </b-modal>
        <b-modal ref="success-modal" id="modal-no-backdrop" hide-backdrop hide-footer hide-header>
          <center>
          <p class="success"><b-icon icon="check-circle" animation="fade"></b-icon></p>
          <p>Gasto combustible editado con éxito</p>
          </center>
    </b-modal>
    </div>
</template>

<script>
import { getAPI } from '../axios-api';


export default {
  
  props: ['items'],
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
      btnEdit: true,
      estado: null,
      
       optionComprobante: [
                { value: 'Boleta', text: 'Boleta'},
                { value: 'Vale', text: 'Vale'},
                { value: 'Factura', text: 'Factura' }
            ],
    };
  },
  methods: {
    setFolio(folio){
      this.folio = folio;
    },
   activateButton(){
       if(![this.folio,
           this.fechaEmision,
           this.horaEmision,
           this.qtyBencina,
           this.nombreEstacion,
           this.maquina,
           this.montoTotal,
           this.tipoComprobante].includes(null)) {
        this.btnEdit = false
     }
     },
    
   createEdit(){
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
    getAPI.put('/gastosc', data, options)
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

computed: {
      validLength2() {
        return this.encargado.length > 0 ? true : false
      },
       validLength3() {
        return this.nombre.length > 0 ? true : false
      }
    },
  
}
    
    

    
  

</script>