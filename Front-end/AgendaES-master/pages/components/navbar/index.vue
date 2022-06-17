<template>
  <el-menu class="el-menu-demo" mode="horizontal">
    <el-menu-item>
      <nuxt-link to="/dashboard"> Página inicial </nuxt-link>
    </el-menu-item>
    <el-menu-item>
      <nuxt-link to="/pessoal"> Página pessoal </nuxt-link>
    </el-menu-item>
    <div class="ml-10 mt-2 float-right">
      <el-dropdown trigger="click" class="h-full" @command="handleCommand">
        <!-- <div class="flex h-full items-center"> -->
        <el-avatar
          class="cursor-pointer"
          :size="50"
          src="https://yt3.ggpht.com/ytc/AAUvwngnttqe97MjxQ8OEsZojJnMWpKIBTJhFm2z4k-G=s900-c-k-c0x00ffffff-no-rj"
        >
          <img
            src="https://cube.elemecdn.com/e/fd/0fc7d20532fdaf769a25683617711png.png"
          />
        </el-avatar>
        <!-- </div> -->

        <el-dropdown-menu slot="dropdown" class="w-48">
          <nuxt-link to="/login"
            ><el-dropdown-item> Sair </el-dropdown-item></nuxt-link
          >
        </el-dropdown-menu>
      </el-dropdown>
    </div>
  </el-menu>
</template>

<script>
export default {
  created() {
    // console.log(this.$auth.user.data)
  },
  methods: {
    async handleCommand(command) {
      switch (command) {
        case "logout":
          this.$confirm(
            "Confirma o encerramento da sua sessão?",
            "Encerrar sessão",
            {
              confirmButtonText: "Confirmar",
              cancelButtonText: "Cancelar",
              type: "warning",
            }
          ).then(async () => {
            await this.$auth.logout();
          });
          break;
      }
    },
  },
};
</script>


<style>
.el-menu-item:active {
  background: blue;
}
</style>

