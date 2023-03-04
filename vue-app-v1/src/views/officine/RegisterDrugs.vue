<template>
    <LayoutOfficine>
        <v-sheet height="70vh" rounded="lg" class="pa-16" style="overflow: scroll;" elevation="5">
            <h1 class="leadTitle">enregistrement de médicament</h1>
            <v-container class="px-16">
                <v-row class="px-16">
                    <v-col class="px-16" cols="12">
                        <v-text-field v-model="box.nameMedoc" label="Nom du médicament" variant="solo"></v-text-field>
                    </v-col>
                    <v-col class="px-16" cols="12">
                        <v-select v-model="box.nameMol" :items="itemsM" label="Molécule" variant="solo" clearable></v-select>
                    </v-col>
                    <v-col class="px-16" cols="12">
                        <v-select v-model="box.catMedoc" :items="itemsF" label="Famille" variant="solo" clearable></v-select>
                    </v-col>
                    <v-col class="px-16" cols="12">
                        <v-text-field v-model="box.qtyMedoc" label="Quantité" variant="solo"></v-text-field>
                    </v-col>
                    <v-col class="px-16" cols="12">
                        <v-checkbox label="Sur prescription ?" color="teal-lighten-3" v-model="box.onPrescip"></v-checkbox>
                    </v-col>
                </v-row>
                <v-snackbar v-model="snackbar" :color="typeAlert" :timeout="timeout">
                <v-alert :type="typeAlert" :text="textSnackbar"></v-alert>
            </v-snackbar>
                <v-checkbox label="Contre-indications ?" color="teal-lighten-3" v-model="contreIndic"></v-checkbox>
                <v-row v-if="contreIndic" class="px-16" no-gutters>
                    <v-col class="px-16" cols="10" v-for="liste, index in listContraIndic" :key="index">
                        <v-text-field
                            label="Contre-indications"
                            variant="solo"
                            v-model="liste.nom"
                        ></v-text-field>
                    </v-col>
                    <v-col class="text-right">
                        <v-btn
                            icon="mdi-plus"
                            variant="elevated"
                            color="teal-lighten-3"
                            @click="addcontreIndic"
                        ></v-btn>
                    </v-col>
                    <v-col class="ps-3">
                        <v-btn
                            v-if="listContraIndic.length > 1"
                            icon="mdi-minus"
                            variant="elevated"
                            color="error"
                            @click="delcontreIndic"
                        ></v-btn>
                    </v-col>
                </v-row>
                <v-row class="align-center justify-center">
                    <v-col class="text-center">
                        <v-btn class="w-25" size="x-large" rounded="lg" color="teal-lighten-3" @click="saveDrugs">VALIDER</v-btn>
                    </v-col>
                </v-row>
            </v-container>
        </v-sheet>
    </LayoutOfficine>
</template>

<script>
    export default {
    name: "RegisterDrugs",
    data() {
        return {
            box: {
                nameMedoc: null,
                catMedoc: null,
                nameMol: null,
                onPrescip: null,
                qtyMedoc: null,
            },
            contreIndic: false,
            itemsM: [],
            itemsF: [],
            listContraIndic: [
                {nom:''},
            ],
            snackbar: false,
            timeout: 3000,
            textSnackbar: '',
            typeAlert: '',
        }
    },
    async mounted() {
        this.itemsM = await this.$store.dispatch('getAllMolecules', { axios: this.$axios });
        this.itemsF = await this.$store.dispatch('getAllDrugCat', { axios: this.$axios });
    },
    methods: {
        addcontreIndic() {
            this.listContraIndic.push({nom:''});
        },

        delcontreIndic() {
            this.listContraIndic.splice(-1, 1);
        },

        toLower(obj) {
            for (let o in obj) {
                o = o.toLowerCase();
            }
        },

        async saveDrugs() {
            try {
                const idOfficine = this.$store.getters.idUser;
                const response = (await this.$axios.post(`/officine/${idOfficine}/register-medoc`, this.box)).data;
                console.log(response)
                
                if (response.data === true) {
                    this.textSnackbar = "L'enregistrement a bien été effectué";
                    this.typeAlert = "success";
                    this.timeout = 6000;
                    this.snackbar = true;
                } else {
                    this.textSnackbar = response.message;
                    this.typeAlert = "error";
                    this.timeout = 6000;
                    this.snackbar = true;
                }
            } catch (error) {
                if (error.response) {
                    this.textSnackbar = error.response.data.error;
                    this.typeAlert = "error";
                    this.snackbar = true;
                } else {
                    this.textSnackbar = error;
                    this.typeAlert = "error";
                    this.snackbar = true;
                }
            }
        }
    }
}
</script>

<style scoped>
    .leadTitle {
        text-transform: uppercase;
        text-align: center;
    }

    .bg-teal-lighten-3 {
        color: #fff !important;
    }
</style>