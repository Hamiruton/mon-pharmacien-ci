<template>
    <v-btn
        icon="mdi-cart"
        variant="elevated"
        color="teal-lighten-2"
        size="small"
        class="mr-5"
        title="Panier de médicaments"
        @click="toggleDialog"
    ></v-btn>
    <v-dialog
        v-model="dialog"
        fullscreen
        :scrim="true"
        transition="dialog-bottom-transition">
        <v-sheet>
            <v-toolbar color="teal-darken-4">
                <v-btn
                    icon
                    dark
                    @click="toggleDialog">
                    <v-icon>mdi-close</v-icon>
                </v-btn>
                <v-toolbar-title>Panier de médicaments</v-toolbar-title>
                <v-spacer></v-spacer>
            </v-toolbar>
            <v-sheet class="w-100 h-80">
                <TableData
                    :listPharmacy="listMedocs"
                    tableHeight="70vh"
                    :hasActions="true"
                >
                    <template #actions>
                        <!--Creer des composants pour chacun de ses boutons pour gérer les différentes actions-->
                        <v-btn color="success" icon="mdi-cash" variant="elevated" class="mr-5" size="small" title="Passer la commande de ce médicament"></v-btn>
                        <v-btn color="error" icon="mdi-delete-forever" variant="elevated" size="small" title="Retirer ce médicament du panier"></v-btn>
                    </template>
                </TableData>
            </v-sheet>
            <v-container fluid>
                <v-row justify="end" class="pa-2">
                    <v-btn
                        active
                        size="large"
                        color="success"
                        rounded="lg"
                        variant="elevated"
                        @click=""
                    >commande groupée</v-btn>
                </v-row>
            </v-container>
        </v-sheet>
    </v-dialog>
</template>

<script>
    import TableData from './TableData.vue';
    export default {
        name: "Order",
        components: {TableData},
        data() {
            return {
                dialog: false,
                listMedocs: [
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                    {nomC: "Medicament 1", nomS: "Benzebol", molecule: "De Methyle aryzoboique"},
                ]
            }
        },
        methods: {
            toggleDialog() {
                this.dialog = !this.dialog;
            }
        }
    }
</script>

<style>
    .dialog-bottom-transition-enter-active,
    .dialog-bottom-transition-leave-active {
        transition: transform .2s ease-in-out;
    }
</style>