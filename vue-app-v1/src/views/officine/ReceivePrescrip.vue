<template>
    <LayoutOfficine>
        <v-sheet min-height="70vh" rounded="lg" class="pa-16" elevation="5">
            <h1 class="leadTitle pb-5">ordonnances reçues</h1>
            <v-container fluid>
                <DisplayInList content="Fichier 1">
                    <template #actions>
                        <DownloadOrdBtn />
                    </template>
                </DisplayInList>
                <DisplayInList content="Fichier 2">
                    <template #actions>
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
    }
</script>

<style>
    .leadTitle {
        text-transform: uppercase;
        text-align: center;
    }
</style>