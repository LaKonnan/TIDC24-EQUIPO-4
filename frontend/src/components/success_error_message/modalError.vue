<template>
    <b-modal id="error_modal" :header-bg-variant="danger" :header-text-variant="light" title="ERROR" centered hide-footer>
        <center>
            <p class="error"><b-icon icon="exclamation-circle" animation="fade"></b-icon></p>
            <p>{{ message }}</p>
            <b-button class="normal-button" @click="back()">VOLVER</b-button>
            <b-button class="dark-button" @click="closeModal()">CERRAR</b-button>
        </center>
    </b-modal>
</template>

<script>
export default {
    props: ['message'],

    methods: {
        // cerrar modal y borrar datos del formulario correspondiente
        closeModal() {
            this.$bvModal.hide('error_modal')
            this.$emit('passData', {methodCall: 'resetForm'})
        },

        // llamar metodo para volver al modal correspondiente
        back() {
            this.$emit('passData', {methodCall: 'modalBack'})
        }
    }
}
</script>

<style>

</style>