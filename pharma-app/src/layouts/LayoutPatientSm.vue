<template>
  <div class="w-screen h-screen bg-bgColor flex flex-col">
    <!--Begin Header-->
    <header class="h-[230px] bg-secondary-normal flex flex-col justify-between">
      <div class="flex py-6 px-6 justify-between">
        <button><i class="mdi mdi-menu text-white text-3xl"></i></button>
        <button><i class="mdi mdi-magnify text-white text-2xl"></i></button>
      </div>
      <div class="mb-10 flex px-2 justify-center items-center space-x-6">
        <!--Remplacer par les données du patient-->
        <div class="w-16 h-16 avatar">
          <!--<img src="../assets/25.jpg" alt="avatar">-->
          <i class="mdi mdi-account text-6xl text-gray-400"></i>
        </div>
        <div class="flex flex-col justify-center items-center">
          <div class="text-white font-semibold">
            <span class="uppercase text-xl">ahoumouan </span>
            <span class="capitalize">axel</span>
          </div>
          <div class="text-white italic">
            <span>21 ans </span>
            <span>Homme <i class="mdi mdi-gender-male"></i> </span>
          </div>
        </div>
      </div>
    </header>
    <!--End Header-->

    <!--Begin Body-->
    <div class="flex-auto bg-bgColor p-5 flex flex-col space-y-5 justify-center cursor-pointer">
      <div v-for="list in lists" :key="list.id" class="bg-gray-300 transition duration-500 active:scale-75 rounded-full h-16 flex items-center space-x-2">
        <div class="avatar h-16 w-16 justify-start">
          <i :class="`mdi ${list.icon} text-2xl text-primary-shades-500 `"></i>
        </div>
        <span class="text-xl capitalize select-none">{{ list.text }}</span>
      </div>
    </div>
    <!--End Body-->

    <!--Begin Footer-->
    <div class="bg-secondary-tints-400 h-16 flex justify-around items-center">
      <button class="btn btn-ghost btn-circle text-white hover:text-primary-normal hover:bg-transparent"><i class="mdi mdi-home text-3xl"></i></button>
      <button class="btn btn-ghost btn-circle text-white hover:text-primary-normal hover:bg-transparent"><i class="mdi mdi-history text-3xl"></i></button>
      <button class="btn btn-ghost btn-circle text-white hover:text-primary-normal hover:bg-transparent"><i class="mdi mdi-cart text-3xl"></i></button>
    </div>
    <!--End Footer-->
  </div>
</template>

<script setup>
import { ref } from 'vue';

const lists = ref([
  {
    id: 1,
    icon: 'mdi-send',
    text: 'Ordonnance'
  },
  {
    id: 2,
    icon: 'mdi-hospital-marker',
    text: 'Pharmacie'
  },
  {
    id: 3,
    icon: 'mdi-pill',
    text: 'Médicaments'
  },
  {
    id: 4,
    icon: 'mdi-cog',
    text: 'Paramètres'
  },
])
</script>

<style scoped>
header {
  border-radius: 0% 0% 55px 55px;
}
</style>