<template>
    <LayoutOfficine>
        <v-sheet min-height="70vh" rounded="lg" class="pa-16" elevation="5">
            <h1 class="leadTitle">enregistrement de médicament</h1>
            <v-container class="px-16">
                <v-row class="px-16">
                    <v-col class="px-16" cols="12">
                        <v-text-field label="Nom du médicament" variant="solo"></v-text-field>
                    </v-col>
                    <v-col class="px-16" cols="12">
                        <v-text-field label="Molécule" variant="solo"></v-text-field>
                    </v-col>
                    <v-col class="px-16" cols="12">
                        <v-text-field label="Famille" variant="solo"></v-text-field>
                    </v-col>
                    <v-col class="px-16" cols="12">
                        <v-text-field label="Quantité" variant="solo"></v-text-field>
                    </v-col>
                </v-row>
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
import LayoutOfficine from '@/layouts/LayoutOfficine.vue';

    export default {
    name: "RegisterDrugs",
    components: { LayoutOfficine },
    data() {
        return {
            contreIndic: false,
            listContraIndic: [
                {'nom':''},
            ]
        }
    },
    methods: {
        addcontreIndic() {
            this.listContraIndic.push({'nom':''});
        },

        delcontreIndic() {
            this.listContraIndic.splice(-1, 1);
        },

        saveDrugs() {
            // Write function to save drugs in the database
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