<template>
    <b-modal ref="success_modal" id="modal-no-backdrop" hide-backdrop hide-footer hide-header>
        <center>
            <p class="success"><b-icon icon="check-circle" animation="fade"></b-icon></p>
            <p>{{ success_text }}</p>
            <b-button class="dark-button" @click="closeModal('success')">CERRAR</b-button>
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
        }
    },
}
</script>

<style>

</style>