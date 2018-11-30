<template>
  <v-layout
    justify-center
    align-center
    fill-height
    row wrap
  >
    <v-flex xs11 class="top__bar--padding">
      <v-layout
        justify-space-between
        row wrap
        class="top__bar"
      >
        <v-flex xs12 sm12 md5 lg4>
          <v-select
            class="select--cinema"
            solo
            light
            flat
            hide-details
            dense
            color="gold"
            label="Kino"
            background-color="black"
            :items="cinemas()"
            :menu-props="{'content-class': 'select__menu--black elevation-0'}"
            v-model="currentCinema"
            @change="setCinemaCookie()"
          ></v-select>
        </v-flex>
        <v-flex xs12 sm12 md7 lg8 class="text-xs-center text-md-right">
          <v-btn
            v-for="day in days" :key="day"
            icon
            flat
            depressed
            @click="selectedDay = day"
            class="alegreya-sc--light text-capitalize days"
            :color="buttonDayColor(day)"
          >{{day}}
          </v-btn>
        </v-flex>
      </v-layout>
    </v-flex>
    <v-flex xs9>
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
            <v-img
              :src="movie.cover"
              class="image--style"
              height="340px"
            ></v-img>
            <div class="alegreya-sc--light movie--title">
              {{movie.title}}
            </div>
          </v-card>
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
</template>

<script>
  import ChangesCinema from '../mixins/ChangesCinema'

  export default {
    name: 'AppMovieList',
    mixins: [ChangesCinema],
    methods: {
      buttonDayColor (day) {
        if (day === this.selectedDay) {
          return 'gold'
        } else {
          return 'white'
        }
      },
      movies () {
        return this.$store.getters['getMovies']
      }
    },
    data () {
      return {
        days: ['Pn', 'Wt', 'Śr', 'Cz', 'Pt', 'So', 'Nd'],
        selectedDay: 'Pn'
      }
    },
    mounted: function () {
      if (!this.movies().length) {
        this.$store.dispatch('requestMovies', this.currentCinema)
      }
    }
  }
</script>

<style scoped lang="stylus">
  .top__bar
    border-bottom: 1.5px solid var(--v-gold-base)
    &--padding
      padding-bottom: 40px
      padding-top: 100px

  .days
    font-size: 1.4rem
    letter-spacing: 3px

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

</style>
