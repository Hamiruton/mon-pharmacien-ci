<template>
    <LayoutOfficine>
        <v-sheet height="70vh" rounded="lg" class="pa-16" elevation="5" style="overflow: scroll;">
            <h1 class="leadTitle pb-5">ordonnances reçues</h1>
            <v-container fluid>
                <DisplayInList v-for="file, index in files" :key="index" :content="file.filename">
                    <template #actions>
                        <v-btn :ref="`status_${index}`" variant="tonal" size="large" :color="traiter ? 'success' : 'warning'" @click="changeStatus(index)">{{ statusOrder }}</v-btn>
                        <DownloadOrdBtn />
                    </template>
                </DisplayInList>
            </v-container>
        </v-sheet>
    </LayoutOfficine>
</template>

<script>
    import DisplayInList from '@/components/DisplayInList.vue';
    import DownloadOrdBtn from '@/components/DownloadOrdBtn.vue';
    export default {
        name: "ReceivePrescrip",
        components: {
            DisplayInList,
            DownloadOrdBtn,
        },
        computed: {
            statusOrder() {
                return "En attente";
            }
        },
        data() {
            return {
                files: [],
                traiter: false,
            }
        },
        async created() {
            this.files = (await this.$axios.get('/officine/prescription/get-all')).data.data
            console.log(this.files)
        },
        methods: {
            changeStatus(index) {
                //const button = event.target
                //this.traiter = !this.traiter
                //this.$refs.status.color = 'primary'
                this.$refs[`status_${index}`].classList.add('btnColor')
                console.log(this.$refs[`status_${index}`])
            }
        },
        /*
        watch: {
            files: {
                async handler() {
                    return (await this.$axios.get('/officine/prescription/get-all')).data.data
                },
            }
        }
        */
    }
</script>

<style>
    .leadTitle {
        text-transform: uppercase;
        text-align: center;
    }

    .btnColor {
        background-color: #4db6ac !important;
        color: #fff !important;
    }
</style>