<template>
    <LayoutOfficine>
        <v-sheet max-height="65vh" rounded="lg" class="pa-16 container_historiq" elevation="5">
            <h1 class="leadTitle">historique des actions effectuées</h1>
            <v-container>
                <v-timeline align="start">
                    <v-timeline-item
                        v-for="item, i in items"
                        :key="i"
                        :dot-color="item.color"
                        :icon="item.icon"
                        fill-dot
                    >
                        <v-card>
                            <v-card-title :class="['text-h6', `bg-${item.color}`]">
                                {{ item.date }}
                            </v-card-title>
                            <v-card-text class="bg-white text--primary">
                                <p class="pa-5">{{ item.text }}</p>
                            </v-card-text>
                        </v-card>
                    </v-timeline-item>
                </v-timeline>
            </v-container>
        </v-sheet>
        <v-container fluid>
            <v-row>
                <v-col>
                    <v-btn class="w-100 text--white" size="x-large" color="teal-lighten-3">Imprimer l'historique</v-btn>
                </v-col>
            </v-row>
        </v-container>
    </LayoutOfficine>
</template>

<script>
    export default {
        name: "Historic",
        data() {
            return {
                items: [
                    {
                        color: 'red-lighten-2',
                        icon: 'mdi-star',
                        date: '02 Janvier 2023 à 07:48',
                        text: "Traitement de l'ordonnance x du patient y",
                    },
                    {
                        color: 'purple-lighten-2',
                        icon: 'mdi-book-variant',
                        date: '19 Décembre 2022 à 07:48',
                        text: "Entrée de 40 médicaments de polycarbone",
                    },
                    {
                        color: 'green-lighten-1',
                        icon: 'mdi-airballoon',
                        date: '17 Décembre 2022 à 07:48',
                        text: "Destockage de toutes les tonnes de paracetamol",
                    },
                    {
                        color: 'indigo-lighten-2',
                        icon: 'mdi-buffer',
                        date: '02 Décembre 2022 à 07:48',
                        text: "Ajout de chlorure du calcium au médicament z",
                    },
                ],
            }
        }
    }
</script>

<style scoped>
    .leadTitle {
        text-transform: uppercase;
        text-align: center;
    }

    .container_historiq {
        overflow: scroll;
    }
</style>