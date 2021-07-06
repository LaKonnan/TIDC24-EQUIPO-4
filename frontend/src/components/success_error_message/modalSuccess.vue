<template>
    <b-modal id="success_modal" hide-backdrop hide-footer hide-header show="show">
        <center>
            <p class="success"><b-icon icon="check-circle" animation="fade"></b-icon></p>
            <p>{{ success_text }}</p>
            <b-button class="dark-button" @click="closeModal()">CERRAR</b-button>
        </center>
    </b-modal>
</template>

<script>
export default {
    props: ['message'],
    data() {
        return {
            succes_text: ''
        }
    },

    methods: {
        getText() {
            console.log('text')
        },

        closeModal() {
            this.$bvModal.hide('success_modal')
            this.$emit('passData', {methodCall: 'resetForm'})
        }
    },
}
</script>

<style>

</style>