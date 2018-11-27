<template>
  <v-layout
    justify-center
    align-center
  >
    <v-flex sm9 md7 lg5>
      <form class="cinema--form">
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
              class="gold--text"
              :items="['fajne', 'fajniejsze', 'jeszcze fajniejsze']"
            ></v-select>
          </v-flex>
          <v-flex xs12 class="text-xs-center button--padding">
            <v-btn
              class="alegreya-sc--light text-capitalize button--font"
              depressed
              large
              color="gold"
            >Dalej
            </v-btn>
          </v-flex>
        </v-layout>
      </form>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    name: 'AppCinemaSelection'
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
