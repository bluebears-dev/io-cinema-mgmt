<template>
  <v-layout
      class="layout--align-fix"
      fill-height
      justify-center row
      wrap
  >
    <v-flex class="top__bar--padding" xs11>
      <v-layout
          class="top__bar" row
          wrap
      >
        <v-flex lg4 md5 sm12 xs12>
          <v-select
              class="select--cinema"
              :items="cinemas()"
              :menu-props="{'content-class': 'select__menu--black elevation-0'}"
              flat
              hide-details
              @change="setCinemaCookie()"
              background-color="black"
              color="gold"
              dense
              label="Kino"
              item-text="name"
              item-value="id"
              light
              v-model="currentCinema"
              solo
          ></v-select>
        </v-flex>
        <v-flex class="text-xs-center text-md-right" lg8 md7 sm12 xs12>
          <v-btn
              :color="buttonDayColor(day.title)" :key="day.title"
              @click="setDate(day)"
              depressed
              flat
              :ripple="false"
              icon
              class="alegreya-sc--light text-capitalize day-button"
              v-for="day in days"
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

  const weekDays = ['Nd', 'Pn', 'Wt', 'Śr', 'Cz', 'Pt', 'So']

  export default {
    name: 'AppMovieList',
    mixins: [ChangesCinema],
    methods: {
      buttonDayColor (day) {
        if (day === this.currentDate.title) {
          return 'gold'
        } else {
          return 'white'
        }
      }
    },
    computed: {
      currentDate: {
        get () {
          return this.$store.getters['getSelectedDate']
        },
        set (newValue) {
          this.$store.commit('SET_SELECTED_DATE', newValue)
        }
      },
      days () {
        let cinemaDays = []
        let date = new Date()
        let currentDay = date.getDay()
        for (let i = 0; i < weekDays.length; i++) {
          // We use ISO format to split date into two pieces because time zone is not relevant
          cinemaDays[i] = { title: weekDays[(i + currentDay) % 7], date: date.toISOString().split('T')[0] }
          date.setDate(date.getDate() + 1)
        }
        return cinemaDays
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
