<template>
    <div>
        <b-modal id="modal-xlu" size="xl" title="Subir Nuevo Reglamento" hide-footer @hidden="onHidden">
            <b-col>
                <b-row>{{file.name}}</b-row>
            </b-col>
            <br><br>
            <center>
            <p><b>IMPORTANTE: </b>Una vez actualizado el documento no podrá recuperar el antiguo</p>
            <p><b>¿Desea subir un nuevo reglamento?</b></p></center>
            <b-button class="dark-button" @click="onClickConfirmar">Confirmar</b-button>
            <b-button class="dark-button" @click="onClickCancelar">Cancelar</b-button>
        </b-modal>
    </div>
</template>

<script>
import { getAPIarchivos } from '../axios-api';

export default {
  props: ['file'],
  methods: {
    onHidden() {
      console.log('modal cerrado')
    },
    async onClickConfirmar() {
        const accessToken = await this.$auth.getTokenSilently()
        var formData = new FormData()
        formData.append('user_file', this.file)
        getAPIarchivos.post('/upload', formData,
        {
          headers: {
                Authorization: `Bearer ${accessToken}`
            }
        })
        .then(response => {
          console.log(response.data)
          this.$root.$emit('bv::hide::modal','modal-xlu')

        })
        .catch(err => {
          console.log(err)
        })
    },
    onClickCancelar() {
        this.$root.$emit('bv::hide::modal','modal-xlu')
    }
  }
};
</script>