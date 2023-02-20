<template>
    <v-dialog v-model="showDialog" max-width="800px">
        <v-sheet>
            <v-container fluid>
                <v-row>
                    <v-col cols="12" class="text-center">
                        <h1>INFORMATIONS MEDICAMENTS</h1>
                    </v-col>
                    <v-col class="mx-5">
                        <v-row justify="space-around">
                            <v-col>
                                <v-btn
                                    variant="elevated"
                                    rounded="lg"
                                    size="x-large"
                                >Ajouter au panier</v-btn>
                            </v-col>
                            <v-col class="text-center">
                                <v-btn
                                    variant="elevated"
                                    rounded="lg"
                                    size="x-large"
                                >De garde</v-btn>
                            </v-col>
                            <v-col>
                                <v-btn
                                    variant="elevated"
                                    rounded="lg"
                                    size="x-large"
                                >Dans ma commune</v-btn>
                            </v-col>
                        </v-row>
                    </v-col>
                </v-row>
            </v-container>

            <v-col cols="12">
                <v-text-field
                    class="field"
                    model-value="Nom médicament"
                    variant="underlined"
                    density="compact"
                    readonly
                ></v-text-field>
            </v-col>
            <v-col cols="12">
                <v-text-field
                    class="field"
                    model-value="Prix médicament"
                    variant="underlined"
                    density="compact"
                    readonly
                    hint="Les prix peuvent varier d'environ 10% selon les officines"
                    persistent-hint
                ></v-text-field>
            </v-col>

            <v-sheet
                height="200px"
                color="#eeeeee"
                rounded="lg"
                class="ma-5"
                style="overflow: scroll;"
            >
                <!--A remplacer par les pharmacies qui ont le médicament en stock-->
                <v-chip
                    v-for="n in 15"
                    :key="n"
                    class="ma-2"
                    size="large"
                    color="teal-darken-4"
                    variant="elevated">
                    Pharmacie du Boulevard {{ n }}
                </v-chip>
                
            </v-sheet>

            <v-divider class="my-2"></v-divider>

            <v-container fluid>
                <v-row justify="end" class="pa-2">
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
        name: "InfoMedocs",
        props: {
            throwDialog: {
                type: Boolean,
            }
        },
        data() {
            return {
                dialog: true,
            }
        },
        computed: {
            showDialog() {
                return this.throwDialog
            }
        },
        methods: {
            toggleDialog() {
                console.log(this.throwDialog, this.dialog)
                this.dialog = !this.dialog;
            }
        }
    }
</script>

<style>
    /** Cette classe est la classe de l'attribut `hint` de v-text-field */
    .v-messages__message {
        color: red;
    }
</style>