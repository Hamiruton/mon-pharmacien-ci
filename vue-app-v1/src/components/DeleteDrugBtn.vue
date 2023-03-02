<template>
    <v-btn icon="mdi-delete" color="error" variant="tonal" @click="toggleDialog"></v-btn>
    <v-dialog
        v-model="dialog"
        max-width="800px">
        <v-card>
            <v-card-title>Suppression de {{ drug }}</v-card-title>
            <v-card-text>
                Êtes-vous sûr(e) de vouloir supprimer faire sortir {{ drug }} et sa quantité de votre stock ?
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="success" variant="tonal" size="large" @click="toggleDialog">Annuler</v-btn>
                <v-btn color="error" variant="tonal" size="large" @click="">Supprimer</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
    export default {
        name: "DeleteDrugBtn",
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