<template>
    <div class="content">
        <br>
        <!-- titulo -->
        <p class="dark-title">GESTIÓN DE GASTOS COMBUSTIBLE</p>
        <hr class="hr">
        
        <table-gastos @row-selected="onRowSelected" @items="rowItems"/>

        <!-- botones para crud -->
        <buttons :selectedRow="selectedRow" :items="items" />
  </div>     
    
    
</template>

<script>
    export default {
        name: 'gastos',
        data(){
            return{
                selectedRow: true,
                items: []
            }
        },
        components: {
         'table-gastos': require('../components/gastos/table').default,
         'buttons': require('../components/gastos/buttons').default
        },
        methods: {
            onRowSelected(params) {
                this.selectedRow = params
            },
            rowItems(params){
                this.items = params;
            }
        }
    }
    
</script>

<style>
</style>