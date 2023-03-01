<template>
    <LayoutOfficine>
        <v-sheet min-height="70vh" rounded="lg" class="pa-16 grid" elevation="5">
            <h1 class="leadTitle">gestion du stock de l'officine</h1>

        </v-sheet>
    </LayoutOfficine>
</template>

<script>
    export default {
        name: "HandleStock",
    }
</script>

<style scoped>
    .leadTitle {
        text-transform: uppercase;
        text-align: center;
    }

    .grid {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        grid-template-rows: repeat();
    }
</style>