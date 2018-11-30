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
            v-for="day in days" :key="day.title"
            icon
            flat
            depressed
            :ripple="false"
            @click="selectedDay = day.title"
            class="alegreya-sc--light text-capitalize day-button"
            :color="buttonDayColor(day.title)"
          >{{day.title}}
          </v-btn>
        </v-flex>
      </v-layout>
    </v-flex>
    <v-flex xs9>
      <router-view/>
    </v-flex>
  </v-layout>
</template>

<script>
  import ChangesCinema from '../mixins/ChangesCinema'

  let weekDays = ['Nd', 'Pn', 'Wt', 'Śr', 'Cz', 'Pt', 'So']

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
        selectedDay: weekDays[(new Date()).getDay()]
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

  .day-button
    font-size: 1.4rem
    letter-spacing: 3px

    &::before
      background-color: transparent !important
</style>
