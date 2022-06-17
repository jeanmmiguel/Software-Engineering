<template>
  <div id="app" class="p-10">
    <v-app id="inspire">
      <v-row>
        <v-col>
          <v-sheet>
            <v-toolbar flat>
              <v-menu bottom right>
                <template v-slot:activator="{ on }">
                  <v-spacer></v-spacer>
                  <v-btn
                    class="float-right"
                    @click="handleEvent"
                    elevation="6"
                    color="primary"
                    v-on="on"
                  >
                    <v-icon> mdi-plus </v-icon>
                    <span>Novo</span>
                  </v-btn>
                </template>
              </v-menu>
            </v-toolbar>
            <v-calendar
              ref="calendar"
              :now="today"
              :value="today"
              :events="events"
              color="primary"
              type="week"
              @click:event="showEvent"
              :event-color="getEventColor"
              locale="pt"
            ></v-calendar>
            <v-menu
              v-model="selectedOpen"
              :close-on-content-click="false"
              :activator="selectedElement"
              min-width="350px"
              max-width="500px"
              offset-x
            >
              <!-- {{ selectedEvent }} -->
              <v-card :color="selectedEvent.color" flat>
                <v-toolbar :color="selectedEvent.color" dark>
                  <v-btn icon @click="handleEditEvent(selectedEvent)">
                    <v-icon>mdi-pencil</v-icon>
                  </v-btn>
                  <v-toolbar-title
                    class="text-white"
                    v-html="selectedEvent.name"
                  ></v-toolbar-title>
                  <v-spacer></v-spacer>
                  <v-btn icon @click="adicionaFavs()">
                    <v-icon>mdi-heart</v-icon>
                  </v-btn>
                  <v-btn icon @click="deleteEvent(selectedEvent)">
                    <v-icon>mdi-delete</v-icon>
                  </v-btn>
                </v-toolbar>
                <v-card-text>
                  <v-icon aria-hidden="false" small color="white">
                    mdi-clock
                  </v-icon>
                  <span class="text-white"
                    >{{ selectedEvent.startTime }} -
                    {{ selectedEvent.endTime }}</span
                  >
                  <br />
                  <br />
                  <span class="text-white" v-html="selectedEvent.obs"></span>
                </v-card-text>
                <!-- <v-card-actions>
                  <v-btn text color="secondary" @click="selectedOpen = false">
                    <p class="float-right">Fechar</p>
                  </v-btn>
                </v-card-actions> -->
              </v-card>
            </v-menu>
          </v-sheet>
        </v-col>
      </v-row>
      <v-row>
        <v-dialog v-model="dialog" persistent max-width="600px">
          <!-- {{ evento }} -->
          <v-card>
            <v-card-title>
              <span class="text-h5">Novo evento</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col>
                    <v-text-field
                      solo
                      v-model="evento.name"
                      label="Nome do evento"
                      required
                    ></v-text-field>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col cols="12" lg="6">
                    <v-menu
                      ref="menu1date"
                      v-model="menu1date"
                      :close-on-content-click="false"
                      transition="scale-transition"
                      offset-y
                      max-width="290px"
                      min-width="auto"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                          solo
                          v-model="evento.start"
                          label="Data de início"
                          hint="MM/DD/YYYY format"
                          persistent-hint
                          append-icon="mdi-calendar"
                          v-bind="attrs"
                          v-on="on"
                        ></v-text-field>
                        <!-- @blur="date = parseDate(evento.start)" -->
                      </template>
                      <v-date-picker
                        v-model="evento.start"
                        @input="menu1date = false"
                      ></v-date-picker>
                    </v-menu>
                  </v-col>
                  <v-col cols="12" lg="6">
                    <v-menu
                      ref="menu1"
                      v-model="menu1"
                      :close-on-content-click="false"
                      :nudge-right="40"
                      :return-value.sync="time"
                      transition="scale-transition"
                      offset-y
                      max-width="290px"
                      min-width="290px"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                          solo
                          v-model="evento.startTime"
                          label="Hora de início"
                          append-icon="mdi-clock-time-four-outline"
                          readonly
                          v-bind="attrs"
                          v-on="on"
                        ></v-text-field>
                      </template>
                      <v-time-picker
                        v-if="menu1"
                        v-model="evento.startTime"
                        full-width
                        @click:minute="$refs.menu1.save(evento.startTime)"
                      ></v-time-picker>
                    </v-menu>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" lg="6">
                    <v-menu
                      ref="menu2date"
                      v-model="menu2date"
                      :close-on-content-click="false"
                      transition="scale-transition"
                      offset-y
                      max-width="290px"
                      min-width="auto"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                          solo
                          v-model="evento.end"
                          label="Data de fim"
                          hint="MM/DD/YYYY format"
                          persistent-hint
                          append-icon="mdi-calendar"
                          v-bind="attrs"
                          v-on="on"
                        ></v-text-field>
                        <!-- @blur="date = parseDate(evento.end)" -->
                      </template>
                      <v-date-picker
                        v-model="evento.end"
                        @input="menu2date = false"
                      ></v-date-picker>
                    </v-menu>
                  </v-col>
                  <v-col cols="12" lg="6">
                    <v-menu
                      ref="menu2"
                      v-model="menu2"
                      :close-on-content-click="false"
                      :nudge-right="40"
                      :return-value.sync="time"
                      transition="scale-transition"
                      offset-y
                      max-width="290px"
                      min-width="290px"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                          solo
                          v-model="evento.endTime"
                          label="Hora de fim"
                          append-icon="mdi-clock-time-four-outline"
                          readonly
                          v-bind="attrs"
                          v-on="on"
                        ></v-text-field>
                      </template>
                      <v-time-picker
                        v-if="menu2"
                        v-model="evento.endTime"
                        full-width
                        @click:minute="$refs.menu2.save(evento.endTime)"
                      ></v-time-picker>
                    </v-menu>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" lg="6">
                    <!-- <v-color-picker class="ma-2" hide-canvas></v-color-picker> -->
                    <v-select
                      v-model="evento.color"
                      :items="colors"
                      label="Cor"
                      return-object
                      solo
                    ></v-select>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <v-textarea
                      v-model="evento.obs"
                      solo
                      label="Descrição"
                    ></v-textarea>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="error" text @click="dialog = false">
                Cancelar
              </v-btn>
              <v-btn color="success" text @click="submitEvent()">
                Salvar
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-row>
    </v-app>
  </div>
</template>

<script>
import moment from "moment";
function clearEvent() {
  return {
    name: null,
    start: null,
    startTime: "00:00",
    end: null,
    endTime: "23:59",
    color: "blue",
    obs: null,
    // dateRange: null,
  };
}
export default {
  components: { moment },
  mounted() {
    this.$refs.calendar.checkChange();
  },
  data() {
    return {
      time: null,
      dialog: false,
      menu1: false,
      menu2: false,
      menu1date: false,
      menu2date: false,
      method: null,
      selectedEvent: {},
      selectedElement: null,
      selectedOpen: false,
      focus: "",
      // locale: pt,
      type: "month",
      typeToLabel: {
        month: "Month",
      },
      selectedEvent: {},
      selectedElement: null,
      selectedOpen: false,
      evento: clearEvent(),
      colors: [
        // { title: "Azul", value: "blue" },
        // { title: "Indigo", value: "indigo" },
        // { title: "Roxo", value: "deep-purple" },
        // { title: "Ciano", value: "cyan" },
        // { title: "Verde", value: "green" },
        // { title: "Laranja", value: "orange" },
        // { title: "Cinza", value: "grey darken-1" },
      ],
      events: [
        {
          name: "Encontro",
          start: "2022-06-05 09:00",
          end: "2022-06-05 10:00",
          color: "blue",
          obs: "Observação",
          startTime: "09:00",
          endTime: "10:00",
        },
      ],
      colors: [
        "blue",
        "indigo",
        "deep-purple",
        "cyan",
        "green",
        "orange",
        "grey darken-1",
      ],
    };
  },
  methods: {
    // parseDate(date) {
    //   if (!date) return null;

    //   const [month, day, year] = date.split("/");
    //   return `${year}-${month.padStart(2, "0")}-${day.padStart(2, "0")}`;
    // },
    getEventColor(event) {
      // console.log("cor: ", event.color);
      return event.color;
    },
    prev() {
      this.$refs.calendar.prev();
    },
    next() {
      this.$refs.calendar.next();
    },
    showEvent({ nativeEvent, event }) {
      const open = () => {
        this.selectedEvent = event;
        console.log("selected event-->", event);
        this.selectedElement = nativeEvent.target;
        requestAnimationFrame(() =>
          requestAnimationFrame(() => (this.selectedOpen = true))
        );
      };

      if (this.selectedOpen) {
        this.selectedOpen = false;
        requestAnimationFrame(() => requestAnimationFrame(() => open()));
      } else {
        open();
      }

      nativeEvent.stopPropagation();
    },
    handleEvent() {
      this.evento = clearEvent();
      this.dialog = true;
      this.method = "POST";
    },
    handleEditEvent(selectedEvent) {
      var indexEvent = this.events.indexOf(selectedEvent);
      var splitarray = new Array();
      selectedEvent.start = moment(selectedEvent.start).format(
        "YYYY-MM-DD hh:mm"
      );
      splitarray = selectedEvent.start.split(" ");
      selectedEvent.start = splitarray[0];
      selectedEvent.startTime = splitarray[1];
      selectedEvent.end = moment(selectedEvent.end).format("YYYY-MM-DD hh:mm");
      splitarray = selectedEvent.end.split(" ");
      selectedEvent.end = splitarray[0];
      selectedEvent.endTime = splitarray[1];
      this.dialog = true;
      this.method = "PUT";
      console.log("selectedEvent", selectedEvent);
      this.evento = selectedEvent;
    },
    submitEvent() {
      this.evento.start = this.evento.start + " " + this.evento.startTime;

      this.evento.end = this.evento.end + " " + this.evento.endTime;

      if (this.method === "POST") {
        this.events.push(this.evento);
      } else {
        this.events[this.indexEvent] = this.evento;
      }
      this.dialog = false;
      // console.log("eventos --> ", this.events);
    },
    adicionaFavs() {
      alert("adicionado aos favoritos");
    },
   async deleteEvent(selectedEvent) {
      var index = this.events.findIndex((func) => {
        return func.id === selectedEvent.id;
      });

      this.$confirm(
        "Você deseja realmente deletar esse evento?",
        "Atenção",
        {
          confirmButtonText: "OK",
          cancelButtonText: "Cancelar",
          type: "warning",
        }
      )
        .then(() => {
          this.events.splice(index);
          this.$message({
            type: "success",
            message: "Item deletado.",
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "Operação cancelada.",
          });
        });
      this.selectedOpen = false;
    },
  },
};
</script>