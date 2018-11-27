<template>
  <v-layout
    justify-center
    align-center
  >
    <v-flex sm9 md7 lg5>
      <v-form form
        class="cinema--form"
        v-model="validCinemaForm"
      >
        <div class="alegreya-sc--regular form--text text-xs-center">Wybierz Kino</div>
        <v-layout
          justify-center
          align-center
          row
          wrap
        >
          <v-flex sm10 md8 lg7>
            <v-select
              outline
              light
              label="Kino"
              color="gold"
              background-color="gold"
              class="gold--text pb-5"
              :items="['fajne', 'fajniejsze', 'jeszcze fajniejsze']"
              :rules="[v => !!v]"
              hide-details
              v-model="cinema"
            ></v-select>
          </v-flex>
          <v-flex xs12 class="text-xs-center button--padding">
            <v-btn
              class="alegreya-sc--light text-capitalize button--font"
              depressed
              large
              color="gold"
              :disabled="!validCinemaForm"
              @click="chooseCinema()"
            >
              Dalej
            </v-btn>
          </v-flex>
        </v-layout>
      </v-form>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    name: 'AppCinemaSelection',
    data () {
      return {
        validCinemaForm: false,
        cinema: null
      }
    },
    methods: {
      chooseCinema () {
        this.$cookie.set('cinema', this.cinema)
        this.$router.push({ name: 'Movies', params: { cinema: this.cinema } })
      }
    }
  }
</script>

<style scoped lang="stylus">
  .cinema--form
    background-color: var(--v-white-base)
    padding: 60px 20px

  .form--text
    color: var(--v-charcoal-base)
    font-size: 1.8rem
    letter-spacing: 2px !important
    padding-bottom: 30px

  .button--padding
    padding-top: 10px

  .button--font
    font-size 1.6rem
</style>
