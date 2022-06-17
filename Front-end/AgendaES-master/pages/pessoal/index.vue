<template>
  <div class="bg-gray-100">
    <Navbar />
    <h1 class="text-lg pt-5 px-10">Calendário pessoal</h1>
    <Calendario />
  </div>
</template>
<script>
import Navbar from "../components/navbar/index.vue";
import Calendario from "../calendarioSemanal/index.vue";
export default {
  components: { Navbar, Calendario },
};
</script>
