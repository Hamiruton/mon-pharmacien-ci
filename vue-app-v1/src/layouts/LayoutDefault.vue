<template>
    <v-app>
        <AppBar />
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
                        <SideButton />
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
import AppBar from '@/components/AppBar.vue';
import SideButton from '@/components/SideButton.vue';
import LeadSearchBar from '@/components/LeadSearchBar.vue';
export default {
    components: {
        AppBar,
        SideButton,
        LeadSearchBar
    },
    data() {
        return {
            myStyle: { backgroundColor: '#F9FAF0' }
        }
    }
}
</script>