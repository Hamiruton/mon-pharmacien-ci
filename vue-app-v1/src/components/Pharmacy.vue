<template>
    <v-btn
        color="teal-lighten-3"
        size="x-large"
        rounded="lg"
        title="Cliquer pour voir les pharmacies (de garde)"
        class="w-100"
        @click="toggleDialog"
    >PHARMACIE</v-btn>
    <v-dialog
        v-model="dialog"
        persistent
        max-width="800px"
    >
        <v-sheet>
            <v-container fluid>
                <v-row>
                    <v-col cols="12" class="text-center">
                        <h1>INFORMATIONS PHARMACIES</h1>
                    </v-col>
                    <v-col class="mx-5">
                        <v-row>
                            <v-col>
                                <v-btn
                                    variant="elevated"
                                    rounded="lg"
                                    size="x-large"
                                    ref="btnCommune"
                                    :color="changeColor.IfCommune ? 'success' : 'white'"
                                    @click="showPharmacySameCommune"
                                >Dans ma commune</v-btn>
                            </v-col>
                            <v-col class="text-right">
                                <v-btn
                                    variant="elevated"
                                    rounded="lg"
                                    size="x-large"
                                    ref="btnGarde"
                                    :color="changeColor.IfGarde ? 'success' : 'white'"
                                    @click="showPharmacyDeGarde"
                                >De garde</v-btn>
                            </v-col>
                        </v-row>
                    </v-col>
                </v-row>
            </v-container>

            <TableData :listPharmacy="listPharmacy" />

            <v-divider class="my-2"></v-divider>

            <v-container fluid>
                <v-row justify="end" class="pa-2">
                    <v-btn
                        size="large"
                        color="success"
                        class="mr-5"
                        rounded="lg"
                        @click="toggleDialog"
                    >Envoyer</v-btn>
                    <v-btn
                        size="large"
                        color="error"
                        rounded="lg"
                        @click="toggleDialog"
                    >Fermer</v-btn>
                </v-row>
            </v-container>
        </v-sheet>
    </v-dialog>
</template>

<script>
import TableData from './TableData.vue';
export default {
    name: "Pharmacy",
    components: { TableData },
    data() {
        return {
            dialog: false,
            listPharmacy : [
                {nom: "Pharmacie 1", titulaire: "Persona 1", Adresse: "Rue 1", tel: "0173"},
                {nom: "Pharmacie 2", titulaire: "Persona 2", Adresse: "Rue 2", tel: "0173"},
                {nom: "Pharmacie 3", titulaire: "Persona 3", Adresse: "Rue 3", tel: "0173"},
                {nom: "Pharmacie 4", titulaire: "Persona 4", Adresse: "Rue 4", tel: "0173"},
                {nom: "Pharmacie 5", titulaire: "Persona 5", Adresse: "Rue 5", tel: "0173"},
                {nom: "Pharmacie 6", titulaire: "Persona 6", Adresse: "Rue 6", tel: "0173"},
                {nom: "Pharmacie 7", titulaire: "Persona 7", Adresse: "Rue 7", tel: "0173"},
                {nom: "Pharmacie 8", titulaire: "Persona 8", Adresse: "Rue 8", tel: "0173"},
                {nom: "Pharmacie 9", titulaire: "Persona 9", Adresse: "Rue 9", tel: "0173"},
                {nom: "Pharmacie 10", titulaire: "Persona 10", Adresse: "Rue 10", tel: "0173"},
                {nom: "Pharmacie 11", titulaire: "Persona 11", Adresse: "Rue 11", tel: "0173"},
            ],
            changeColor: {
                IfCommune: false,
                IfGarde: false
            }
        }
    },
    methods: {
        toggleDialog() {
            this.dialog = !this.dialog;
        },
        // Fonction qui doit filtrer et afficher les pharmacies de garde (Pas au point !!!)
        showPharmacyDeGarde() {
            let originalList = JSON.parse(JSON.stringify(this.listPharmacy));
            if (this.changeColor.IfGarde === false) {
                this.changeColor.IfGarde = true;
                this.listPharmacy = this.listPharmacy.filter(pharmacy => pharmacy.commune === "Cocody");
                console.log(originalList)
            } else {
                this.changeColor.IfGarde = false;
                console.log(originalList)
                this.listPharmacy = JSON.parse(JSON.stringify(originalList));
            }
        },
        // Fonction qui doit filtrer et afficher les pharmacies qui sont dans la même commune que le client (Pas au point !!!)
        showPharmacySameCommune() {
            this.changeColor.IfCommune = !this.changeColor.IfCommune
        },
    }
}
</script>
