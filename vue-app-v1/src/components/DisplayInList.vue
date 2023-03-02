<template>
    <v-card
        class="mx-auto card-personalized mb-3">
        <v-card-actions>
            <v-card-title class="titleList">
                {{ content }}
            </v-card-title>
            <v-spacer></v-spacer>
            <slot name="actions"></slot>
        </v-card-actions>
            
        
    </v-card>
</template>

<script>
    export default {
        name: "DisplayInList",
        props: ["content"],
    }
</script>

<style scoped>
    .card-personalized {
        width: 90%;
        background-color: #eeeeeeff;
    }

    .titleList {
        text-transform: uppercase;
    }
</style>