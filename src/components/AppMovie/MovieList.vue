<template>
  <v-layout
    row wrap
    align-start
    justify-center
  >
    <v-flex v-for="movie in movies()" :key="movie.title" class="card--style text-xs-center">
      <v-card
        color="black"
        flat
        class="mx-auto"
        width="240px"
      >
        <router-link :to="{name: 'MovieDetails'}" class="router--link">
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
  </v-layout>
</template>

<script>
  export default {
    name: 'MovieList',
    methods: {
      movies () {
        return this.$store.getters['getMovies']
      }
    },
    mounted: function () {
      if (!this.movies().length) {
        this.$store.dispatch('requestMovies')
      }
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
</style>
