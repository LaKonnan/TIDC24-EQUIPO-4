<template>
    <div>
        <b-modal id="modal-xld" size="xl" title="ELIMINAR GASTO COMBUSTIBLE" hide-footer>    
                <b-card-text>
                        Los siguientes datos de Gasto combustible seleccionada serán eliminados
                        <hr>
                        <b>Gasto Combustible:</b>
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
                    <p><b>IMPORTANTE: </b>Una vez eliminado el gasto combustible, no podrá ser recuperado.</p>
                    <b-form-input v-model="password" type="password" style="text-align: center;" @keyup="activateButton()"></b-form-input>
                    
                <b-button  class="button-next dark-button" disabled:button @click="deleteGasto()">Eliminar Gasto</b-button>
                        
          </b-card-text>
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
      password:''
     
    };
  },
 
  methods: {
    setFolio(folio){
      this.folio = folio;
    },
    activateButton() {
            this.button = false
        },

    deleteGasto(){
      console.log(this.folio)
      const options = {
        headers: {
         'Content-Type': 'application/json;charset=UTF-8',
         'Access-Control-Allow-Origin': '*'
        }
      }

     if(this.password == '123'){
       getAPI.delete('/gastosc/'+this.items[0].folio.S,'',options)
        .then((res) =>{
          console.log('Datos Eliminados: ', res)
        })
      }
    }
  }
}  
  

</script>