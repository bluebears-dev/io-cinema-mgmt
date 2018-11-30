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
            :items="['fajne', 'fajniejsze', 'jeszcze fajniejsze']"
            :menu-props="{'content-class': 'select__menu--black elevation-0'}"
            v-model="cinema"
          ></v-select>
        </v-flex>
        <v-flex xs12 sm12 md7 lg8 class="text-xs-center text-md-right">
          <v-btn
            v-for="day in days" :key="day.title"
            icon
            flat
            depressed
            @click="selectedDay = day.title"
            class="alegreya-sc--light text-capitalize days"
            :color="buttonDayColor(day.title)"
          >{{day.title}}
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
        <v-flex v-for="movie in movies" :key="movie" class="card--style text-xs-center">
          <v-card
            color="black"
            flat
            class="mx-auto"
            width="240px"
          >
            <v-img
              :src="movie.cover"
              class="image--style"
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
  let weekDays = ['Nd', 'Pn', 'Wt', 'Śr', 'Cz', 'Pt', 'So']

  export default {
    name: 'AppMovieList',
    props: {
      cinema: {
        type: String
      }
    },
    methods: {
      buttonDayColor (day) {
        if (day === this.selectedDay) {
          return 'gold'
        } else {
          return 'white'
        }
      }
    },
    computed: {
      days () {
        let cinemaDays = []
        let currentDay = (new Date()).getDay()
        for (let i = 0; i < weekDays.length; i++) {
          cinemaDays[i] = { title: weekDays[(i + currentDay) % 7], action: '' }
        }
        return cinemaDays
      }
    },
    data () {
      return {
        selectedDay: weekDays[(new Date()).getDay()],
        movies: [
          { title: 'Jak Zdać IO', cover: '/static/bohemian.jpg' },
          { title: 'Bohemian Rhapsody', cover: '/static/bohemian.jpg' },
          { title: 'Bohemian Rhapsody', cover: '/static/bohemian.jpg' },
          { title: 'Bohemian Rhapsody', cover: '/static/bohemian.jpg' },
          { title: 'Bohemian Rhapsody', cover: '/static/bohemian.jpg' },
          { title: 'Bohemian Rhapsody', cover: '/static/bohemian.jpg' }
        ]
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
