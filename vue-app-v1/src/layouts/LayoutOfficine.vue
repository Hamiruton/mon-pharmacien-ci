<template>
    <v-app>
        <AppBarOfficine />
        <v-main class="bg-grey-lighten-3">
            <v-container class="px-6 py-9" fluid>
                <v-row>
                    <v-col>
                        <v-sheet></v-sheet>
                    </v-col>
                    <v-col cols="10">
                        <LeadSearchBar />
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="2">
                        <SideBtnOfficine />
                    </v-col>
                    <v-col>
                        <slot></slot>
                    </v-col>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
    import AppBarOfficine from '@/components/AppBarOfficine.vue';
    import SideBtnOfficine from '@/components/SideBtnOfficine.vue';
    import LeadSearchBar from '@/components/LeadSearchBar.vue';
    export default {
        name: "LayoutOfficine",
        components: { AppBarOfficine, SideBtnOfficine, LeadSearchBar }
    }
</script>

