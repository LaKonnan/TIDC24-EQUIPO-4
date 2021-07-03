<template>
<div class="resume-cajas">
    <div class="cards-group">
        <b-card>
            <div class="title-register">
                10 CAJAS REGISTRADAS
            </div>

            <div class="icon-register">
                <b-icon icon="pencil-square"></b-icon>
            </div>
        </b-card>

        <b-card>
            <div class="title-active">
                3 CAJAS ACTIVAS
            </div>

            <div class="icon-active">
                <b-icon icon="check-circle"></b-icon>
            </div>
        </b-card>

        <b-card>
            <div class="title-alert">
                2 CAJAS HAN OCUPADO UN 75% DE SU FONDO
            </div>

            <div class="icon-alert">
                <b-icon icon="exclamation-circle"></b-icon>
            </div>
        </b-card>

        <b-card>
            <div class="title-slash">
                1 CAJAS HAN OCUPADO TODO SU FONDO
            </div>

            <div class="icon-slash">
                <b-iconstack>
                    <b-icon stacked icon="cash-stack" scale="0.75"></b-icon>
                    <b-icon stacked icon="slash-circle" ></b-icon>
                </b-iconstack>
            </div>
        </b-card>
    </div>
    <br>
  </div>

</template>

<script>
export default {

}
</script>

<style lang="scss">
    @import '@/components/styles/cards.scss';


</style>