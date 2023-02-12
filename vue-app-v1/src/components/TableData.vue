<template>
    <v-table fixed-header height="300px" class="table">
        <thead>
            <tr>
                <th class="text-center" v-for="obj, index in Object.keys(listPharmacy[0])" :key="index">{{ obj }}</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="item,n in listPharmacy" :key="n">
                <td v-for="nb, key in Object.keys(item)" :key="key">{{ item[nb] }}</td>
            </tr>
        </tbody>
    </v-table>
</template>

<script>
    export default {
        name: "TableData",
        props: {
            listPharmacy: {
                type: Array,
                required: true
            }
        }
    }
</script>

<style>
    .table {
        background: #fafafa;
        text-align: center;
        border-collapse: collapse;
        border-spacing: 0;
    }

    th {
        background-color: #ba68c8;
        color: #fafafa;
        text-transform: uppercase;
    }

    tr:nth-child(odd) {
        background-color: #eeeeee;
    }
</style>