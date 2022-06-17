  <template>
  <div class="!h-full">
    <div class="w-3/6 h-[350px] flex m-auto mt-36 shadow-lg border rounded-md">
      <div class="w-1/2 border-r">
        <el-image
          style="width: 336.75px; height: 348px"
          src="https://thumbs.dreamstime.com/b/paisagem-floresta-longa-bonita-das-%C3%A1rvores-da-borracha-da-perspectiva-86293510.jpg"
          fit="cover"
        ></el-image>
      </div>

      <div class="w-1/2">
        <h1 class="p-5 text-gray-600">Faça login!</h1>
        <div class="p-5">
          <el-form
            label-position="top"
            :model="props"
            :rules="rules"
            ref="loginForm"
          >
            <el-form-item prop="username">
              <el-input
                type="text"
                placeholder="Usuário"
                autocomplete="off"
                prefix-icon="el-icon-user"
                v-model="props.username"
              ></el-input>
            </el-form-item>

            <el-form-item prop="password">
              <!-- <div class="flex py-2 justify-end">
          <NuxtLink
            to="/auth/resetPassword"
            class="font-light text-xs cursor-pointer"
            >Esqueceu a senha?</NuxtLink
          >
        </div> -->
              <el-input
                type="password"
                placeholder="Senha"
                autocomplete="off"
                prefix-icon="el-icon-lock"
                v-model="props.password"
              ></el-input>
            </el-form-item>

            <!-- <el-form-item prop="session" class="font-light">
          <el-switch v-model="props.session" active-text="Lembrar de mim.">
          </el-switch>
        </el-form-item> -->

            <el-form-item class="flex justify-end !mb-0">
              <el-button
                type="primary"
                :loading="isLoading"
                @click="fetchLogin"
              >
                Entrar
              </el-button>
            </el-form-item>
          </el-form>
          <span class="text-gray-500 text-xs">Ou</span>
          <span class="text-blue-500 text-xs cursor-pointer"
            >crie uma conta.</span
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  components: {
    Error,
  },
  data: () => {
    return {
      props: {
        username: "",
        password: "",
        session: false,
      },
      rules: {
        password: [
          {
            required: true,
            message: "Informe sua senha.",
            trigger: "blur",
          },
        ],
        username: [
          {
            required: true,
            message: "Informe um nome de usuário.",
            trigger: "blur",
          },
        ],
      },
    };
  },

  methods: {
    fetchLogin() {
      if (this.props.username === "admin" && this.props.password === "admin") {
        this.$router.push("/dashboard");
      } else {
        this.$message.error("Usuário ou senha inválidos.");
      }
    },
  },
};
</script>

</template>