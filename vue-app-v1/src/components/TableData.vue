<template>
    <v-table v-if="listPharmacy" fixed-header :height="tableHeight" class="table ma-5">
        <thead>
            <tr>
                <th class="text-center" v-for="obj, index in Object.keys(listPharmacy[0])" :key="index">{{ obj }}</th>
                <th class="text-center" v-if="hasActions">Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr
                v-for="item,n in listPharmacy"
                :key="n"
                :class="clickCell"
                @click="openInfo(item)"
            >
                <td
                    v-for="nb, key in Object.keys(item)"
                    :key="key"
                >
                    {{ item[nb] }}
                </td>
                <td v-if="hasActions">
                    <slot name="actions"></slot>
                </td>
            </tr>
        </tbody>
    </v-table>
    <v-sheet v-else :height="tableHeight">

    </v-sheet>
    <!--<InfoMedocs v-if="displayInfosMedocs" :throw-dialog="dialog" />-->
    <!--NE JAMAIS FAIRE ÇA-->
    <v-dialog v-model="dialog" max-width="800px">
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
                                    @click="addCart"
                                    :class="isClicked.addCart ? 'changeBtn' : 'table'"
                                >Ajouter au panier</v-btn>
                            </v-col>
                            <v-col class="text-center">
                                <v-btn
                                    variant="elevated"
                                    rounded="lg"
                                    size="x-large"
                                    @click="deGarde"
                                    :class="isClicked.deGarde ? 'changeBtn' : 'table'"
                                >De garde</v-btn>
                            </v-col>
                            <v-col>
                                <v-btn
                                    variant="elevated"
                                    rounded="lg"
                                    size="x-large"
                                    @click="closeToMe"
                                    :class="isClicked.closeToMe ? 'changeBtn' : 'table'"
                                >Dans ma commune</v-btn>
                            </v-col>
                        </v-row>
                    </v-col>
                </v-row>
            </v-container>

            <v-col cols="12">
                <v-text-field
                    class="field"
                    v-model="nomMedoc"
                    variant="underlined"
                    density="compact"
                    readonly
                ></v-text-field>
            </v-col>
            <v-col cols="12">
                <v-text-field
                    class="field"
                    v-model="prixMedoc"
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
                <v-chip
                    v-for="phar, index in pharmacy"
                    :key="index"
                    class="ma-2"
                    size="large"
                    color="teal-darken-4"
                    variant="elevated">
                    {{ phar.name }}
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
    import InfoMedocs from './InfoMedocs.vue';
    export default {
        name: "TableData",
        components: {InfoMedocs},
        props: {
            listPharmacy: {
                required: true
            },
            tableHeight: {
                type: String,
                default: '300px'
            },
            displayInfosMedocs: {
                type: Boolean,
                default: false
            },
            clickCell: {
                type: String,
            },
            hasActions: {
                type: Boolean,
                default: false
            }
        },
        data() {
            return {
                dialog: false,
                nomMedoc: null,
                prixMedoc: null,
                pharmacy: [],
                isClicked: {
                    deGarde: false,
                    closeToMe: false,
                    addCart: false,
                },
            }
        },
        methods: {
            toggleDialog() {
                if (this.displayInfosMedocs) {
                    this.dialog = !this.dialog;
                }
            },
            async openInfo(item) {
                this.dialog = true;
                this.nomMedoc = item.nameMedoc;
                this.prixMedoc = 1500;
                this.pharmacy = await this.$store.dispatch('getAffiliatedOfficineByNameMedoc', {axios: this.$axios, nameMedoc: item.nameMedoc});
            },
            addCart() {

            },
            deGarde() {

            },
            async closeToMe() {
                this.isClicked.closeToMe = !this.isClicked.closeToMe;

                if (this.isClicked.closeToMe) {
                    // Sauvegarde les pharmacies originales avant le filtrage
                    this.$data.originalPharmacy = this.pharmacy;

                    // Filtrage
                    let pharmacies = this.pharmacy;
                    let clientTown = this.$store.getters.user.town;

                    this.pharmacy = [];
                    for (let obj of pharmacies) {
                        if (obj.town.toLowerCase() === clientTown.toLowerCase()) {
                            this.pharmacy.push(obj);
                        }
                    }
                } else {
                    this.pharmacy = this.$data.originalPharmacy;
                    this.$data.originalPharmacy = null;
                }
                
            },
        }
    }
</script>

<style lang="scss" scoped>
    .table {
        background: #fafafa;
        text-align: center;
        border-collapse: collapse;
        border-spacing: 0;
    }

    th {
        color: #fafafa;
        text-transform: uppercase;
    }

    tr:nth-child(odd) {
        background-color: #eeeeee;
    }

    .clickCellHome {
        cursor: pointer;
        &:hover {
            background-color: #ba68c8;
            color: #eeeeee;
        }
    }

    .changeBtn {
        background-color: #004d40ff;
        color: white !important;
    }
</style>