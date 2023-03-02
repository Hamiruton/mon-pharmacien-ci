<template>
    <LayoutOfficine>
        <v-sheet height="70vh" rounded="lg" class="pa-16" style="overflow: scroll;" elevation="5">
            <h1 class="leadTitle">enregistrer ordonnance</h1>
            <v-container class="px-16">
                <v-row class="px-16">
                    <v-col class="px-16" cols="12">
                        <v-text-field label="Assurance" variant="solo"></v-text-field>
                    </v-col>
                    <v-col class="px-16" cols="12" v-for="liste, index in listMedoc" :key="index">
                        <v-text-field v-model="liste.nom" label="Nom médicament" variant="solo"></v-text-field>
                    </v-col>
                </v-row>
                <v-row class="align-center justify-center">
                    <v-col class="text-center">
                        <v-btn class="w-25" size="x-large" rounded="lg" color="teal-lighten-3" @click="addMedoc">ajouter une section</v-btn>
                    </v-col>
                </v-row>
                <v-row class="align-center justify-center">
                    <v-col class="text-center">
                        <v-btn class="w-25" size="x-large" rounded="lg" color="teal-lighten-3" @click="saveOrd">enregistrer</v-btn>
                    </v-col>
                </v-row>
            </v-container>
        </v-sheet>
    </LayoutOfficine>
</template>

<script>
    export default {
        name: "RegisterOrd",
        data() {
            return {
                listMedoc:[
                    {nom: ""}
                ]
            }
        },
        methods: {
            addMedoc() {
                this.listMedoc.push({nom:''});
            },
            saveOrd() {
                // Save ordonnance
            }
        }
    }
</script>

<style>
    .leadTitle {
        text-transform: uppercase;
        text-align: center;
    }
</style>