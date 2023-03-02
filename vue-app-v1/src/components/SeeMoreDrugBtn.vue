<template>
    <v-btn icon="mdi-eye" color="teal-lighten-3" variant="tonal" @click="toggleDialog"></v-btn>
    <v-dialog
        v-model="dialog"
        max-width="800px">
        <v-card>
            <v-card-title>Détails de {{ drug }}</v-card-title>
            <v-card-text>
                <v-text-field label="Nom" variant="underlined" readonly append-icon="mdi-pencil"></v-text-field>
                <v-text-field label="Quantité" variant="underlined" readonly append-icon="mdi-pencil"></v-text-field>
                <v-text-field label="Molécule" variant="underlined" readonly append-icon="mdi-pencil"></v-text-field>
                <v-checkbox label="Sur prescription ?"></v-checkbox>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="error" variant="tonal" size="large" @click="toggleDialog">Annuler</v-btn>
                <v-btn color="success" variant="tonal" size="large" @click="">Modifier</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
    export default {
        name: "SeeMoreDrugBtn",
        props: ['drug'],
        data() {
            return {
                dialog: false
            }
        },
        methods: {
            toggleDialog() {
                this.dialog = !this.dialog;
            },
        }
    }
</script>