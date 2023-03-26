<template>
  <LayoutSm v-if="isSmallScreen" />
  <LayoutLg v-else />
</template>

<script setup>
import {useMediaQuery} from '@vueuse/core'
import { defineAsyncComponent } from 'vue';

const isSmallScreen = useMediaQuery('(max-width: 576px)')
const LayoutLg = defineAsyncComponent(() => import('./LayoutPatientLg.vue'))
const LayoutSm = defineAsyncComponent(() => import('./LayoutPatientSm.vue'))

</script>