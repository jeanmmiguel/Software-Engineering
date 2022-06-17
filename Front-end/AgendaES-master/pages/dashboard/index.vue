<template>
  <div class="bg-neutral-100">
      <Navbar/>
      <h1 class="text-lg pt-5 px-10">Calendário da prefeitura</h1>
      <Calendario/>
  </div>
</template>
<script>
import Navbar from "../components/navbar/index.vue";
import Calendario from "../calendario/index.vue";
export default {
  components: { Calendario, Navbar },
};
</script>
