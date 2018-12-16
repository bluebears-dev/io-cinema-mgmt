<template>
  <v-slide-x-transition
      class="layout row wrap align-start justify-center"
      group
      hide-on-leave
  >
    <v-flex
        :key="movie.id"
        class="card--style text-xs-center"
        v-for="movie in movies()"
    >
      <v-card
          class="mx-auto"
          color="black"
          flat
          width="240px"
      >
        <router-link :to="{name: 'MovieDetails', params: {id: movie.id}}" class="router--link">
          <v-img
              :src="movie.cover"
              class="image--style"
              height="340px"
          ></v-img>
          <div class="alegreya-sc--light movie--title">
            {{movie.title}}
          </div>
        </router-link>
      </v-card>
    </v-flex>
    <v-flex
        class="alegreya-sc--light no--showings text-xs-center"
        key="none"
        v-if="!movies().length"
    >
      Brak seansów na wybrany dzień.
    </v-flex>
  </v-slide-x-transition>
</template>

<script>
  export default {
    name: 'MovieList',
    computed: {
      selectedDate () {
        return this.$store.getters['getSelectedDate']
      }
    },
    watch: {
      selectedDate (newDate, oldDate) {
        if (newDate !== oldDate) {
          this.$store.dispatch('requestMovies')
        }
      }
    },
    methods: {
      movies () {
        return this.$store.getters['getMovies']
      }
    },
    created () {
      this.$store.dispatch('requestMovies')
    }
  }
</script>

<style scoped lang="stylus">
  .image--style
    width: 240px
    border: 1.6px solid var(--v-gold-base)

  .card--style
    padding-bottom: 20px
    flex: 0 0 280px

  .movie--title
    padding-top 7px
    padding-bottom 10px
    color: var(--v-gold-base)
    letter-spacing: 2px
    font-size: 1.5rem
    hyphens: auto

  .router--link
    text-decoration none

  .no--showings
    color: var(--v-white-base)
    font-size: 2rem
    padding-top: 100px
</style>
