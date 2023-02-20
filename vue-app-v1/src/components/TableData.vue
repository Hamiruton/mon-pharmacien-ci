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
                @click="showDialog"
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
    <InfoMedocs v-if="displayInfosMedocs" :throw-dialog="dialog" />

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
            }
        },
        methods: {
            showDialog() {
                if (this.displayInfosMedocs) {
                    this.dialog = !this.dialog;
                }
            }
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
</style>