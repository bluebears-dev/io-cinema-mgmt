<template>
  <v-layout
      align-center
      class="ticket--layout"
      justify-center
  >
    <v-flex class="background" lg5 md7 sm10 xs12>
      <div class="alegreya-sc--regular ticket--text text-xs-center" v-if="finalized">Pobierz swój bilet</div>
      <div class="alegreya-sc--regular ticket--text text-xs-center" v-else>Transakcja została anulowana</div>
      <v-flex class="text-xs-center" v-if="finalized" xs12>
        <v-btn
            class="alegreya--light download--button"
            color="gold"
            large
        >
          Pobierz
        </v-btn>
      </v-flex>
      <v-flex class="text-xs-center" xs12>
        <v-btn
            class="alegreya--light home--button"
            flat
            large
        >
          Strona Główna
        </v-btn>
      </v-flex>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    name: 'AppTicket',
    props: {
      transactionId: {
        required: true
      }
    },
    data () {
      return {
        finalized: true
      }
    }
  }
</script>

<style scoped lang="stylus">
  .background {
    background-color: var(--v-white-base)
  }

  .ticket--layout {
    padding-top: 100px
  }

  .ticket--text {
    font-size: 1.8rem
    letter-spacing: 3px
    margin-top: 40px
    margin-bottom: 100px

  }

  .download--button {
    letter-spacing: 2px
    font-size: 1.2rem
    margin-top: 20px
    margin-bottom: 20px
  }

  .home--button {
    letter-spacing: 2px
    font-size: 1.2rem
    margin-bottom: 30px
  }
</style>
