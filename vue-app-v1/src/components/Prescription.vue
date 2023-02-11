<template>
    <v-btn
        color="teal-lighten-3"
        size="x-large"
        rounded="lg"
        title="Cliquer pour envoyer ton ordonnane/bon d'assurance"
        class="w-100"
        @click="toggleDialog"
    >ORDONNANCE</v-btn>
    <v-dialog
        v-model="dialog"
        persistent
        max-width="800px"
    >
        <v-sheet>
            <v-container fluid>
                <v-row>
                    <v-col cols="12" class="text-center">
                        <h1>BON D'ASSURANCE OU ORDONNANCE</h1>
                    </v-col>
                    <v-col cols="12">
                        <v-file-input
                            prepend-icon="mdi-image"
                            label="Insérer une photo de l'ordonnance ou du bon d'assurance"
                            title="Sélectionner un fichier"
                            variant="solo"
                        ></v-file-input>
                    </v-col>
                    <v-col>
                        <v-row>
                            <v-col>
                                <v-checkbox label="Bon d'assurance"></v-checkbox>
                            </v-col>
                            <v-col>
                                <v-checkbox label="Ordonnance"></v-checkbox>
                            </v-col>
                        </v-row>
                    </v-col>
                </v-row>
            </v-container>
            
            <v-divider></v-divider>

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
export default {
    name: "Prescription",
    data() {
        return {
            dialog: false,
        }
    },
    methods: {
        toggleDialog() {
            this.dialog = !this.dialog
        }
    }
}
</script>