<template>
  <v-layout
    align-center
    class="ticket--layout"
    justify-center
  >
    <v-flex :class="hide" class="background" lg5 md7 sm10 xs12>
      <div class="alegreya-sc--regular ticket--text text-xs-center" v-if="finalized">Pobierz swój bilet</div>
      <div class="alegreya-sc--regular ticket--text text-xs-center" v-else>Transakcja została anulowana</div>
      <v-flex class="text-xs-center" v-if="finalized" xs12>
        <v-btn
          class="alegreya--light download--button"
          color="gold"
          large
          :href="ticketLink"
          target="_blank"
        >
          Pobierz bilet
        </v-btn>
      </v-flex>
      <v-flex class="text-xs-center" xs12>
        <v-btn
          class="alegreya--light home--button"
          flat
          large
          :to="{name: 'Movies'}"
        >
          Strona Główna
        </v-btn>
      </v-flex>
    </v-flex>
    <v-progress-circular
      :size="80"
      class="loading"
      color="gold"
      indeterminate
      v-if="!loaded"
    ></v-progress-circular>
  </v-layout>
</template>

<script>
  export default {
    name: 'AppTicket',
    props: {
      bookingId: {
        required: true
      },
      token: {
        required: true
      }
    },
    computed: {
      hide () {
        return this.loaded ? '' : 'hide'
      }
    },
    data () {
      return {
        finalized: true,
        oauth: null,
        ticketLink: null,
        loaded: false
      }
    },
    methods: {
      init (bid, token) {
        this.$store.dispatch('requestOAuthToken')
          .then(oauth => {
            this.oauth = oauth
            this.$store.dispatch('getTransaction', {
              bookingId: bid,
              token: token,
              oauth: oauth
            }).then(response => {
              this.loaded = true
              if (response.data.pdf_file) {
                this.ticketLink = response.data.pdf_file
              } else {
                this.finalized = false
              }
            }).catch(() => {
              this.$router.push({ name: 'NotFound' })
            })
          })
      }
    },
    created () {
      this.init(this.bookingId, this.token)
    },
    beforeRouteUpdate (to, from, next) {
      this.init(to.params.bookingId, to.params.token)
    }
  }
</script>

<style scoped lang="stylus">
  .background {
    background-color: var(--v-white-base)
    transition: opacity .2s ease-in-out
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

  .hide {
    opacity: 0
  }

  .loading {
    position: fixed
  }
</style>
