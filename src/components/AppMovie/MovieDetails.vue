<template>
  <v-layout
      align-start justify-center
      row
      wrap
  >
    <v-flex xs12 class="md-constant movie--cover text-xs-center">
      <div class="d-inline-block">
        <v-img
            :src="selectedMovie.cover"
            :lazy-src="selectedMovie.cover.replace('covers', 'thumbs')"
            :width="imageWidth"
            class="image--style"
        ></v-img>
      </div>
    </v-flex>
    <v-flex xs12 class="md-flex movie--information">
      <div class="movie--title alegreya-sc--regular">{{selectedMovie.title}}</div>
      <div class="movie--details alegreya-sc--regular">
        Data Premiery: {{selectedMovie.releaseDate}} &nbsp;&nbsp;|&nbsp;&nbsp; Reżyseria: {{selectedMovie.producer}}
        &nbsp;&nbsp;|&nbsp;&nbsp;
        {{selectedMovie.length}} min
      </div>
      <div class="movie--details alegreya-sc--regular">
        {{selectedMovie.genre.join(' &nbsp;&nbsp;| &nbsp;&nbsp;')}}
      </div>
      <div class="movie--description roboto--light">
        {{selectedMovie.description}}
      </div>
    </v-flex>
    <v-flex xs12>
      <div class="movie--date alegreya-sc--regular">
        {{createDate}}
      </div>
      <v-layout
          row wrap
      >
        <v-btn
            :key="showing.toString()" :ripple="false"
            block
            class="showing--button roboto--regular text-capitalize"
            color="white"
            flat
            large
            v-for="showing in movieShowings"
        >
          <div>
            <div class="showing--time">{{showing.hour}} <br></div>
            <div class="showing--type">{{showing.picture_type}} {{showing.audio_type}}</div>
          </div>
        </v-btn>
      </v-layout>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    name: 'MovieDetails',
    props: {
      id: {
        type: Number
      }
    },
    computed: {
      imageWidth () {
        let breakpoint = this.$vuetify.breakpoint.name
        let width = 340
        if (breakpoint === 'xs') {
          let calculated = window.innerWidth * 0.7
          return Math.min(width, calculated)
        } else {
          return width
        }
      },
      selectedMovie () {
        return this.$store.getters['getMovieDetails'][0] || {}
      },
      movieShowings () {
        return this.$store.getters['getShowings']
      },
      createDate () {
        let date = new Date(this.$store.state.selectedDate.date)
        let day = date.getDate()
        let month = this.months[date.getMonth()]
        let weekDay = this.days[date.getDay()]
        return weekDay + ', ' + day + ' ' + month
      }
    },
    data () {
      return {
        months: [
          'Stycznia',
          'Lutego',
          'Marca',
          'Kwietnia',
          'Maja',
          'Czerwca',
          'Lipca',
          'Sierpnia',
          'Września',
          'Października',
          'Listopada',
          'Grudnia'
        ],
        days: [
          'Niedziela',
          'Poniedziałek',
          'Wtorek',
          'Środa',
          'Czwartek',
          'Piątek',
          'Sobota'
        ],
        movie: {
          genres: ['Muzyczny', 'Biograficzny']
        }
      }
    },
    watch: {
      createDate () {
        this.$store.dispatch('requestShowings', this.id)
      }
    },
    created () {
      this.$store.dispatch('requestMovieDetails', this.id)
      this.$store.dispatch('requestShowings', this.id)
    }
  }
</script>

<style scoped lang="stylus">
  @import "~vuetify/src/stylus/settings/_variables.styl"
  @media screen and (min-width: $grid-breakpoints.md)
    .md-constant
      flex: 0 0 260px

    .movie--cover
      padding-right: 60px

    .md-flex
      flex: 1

  @media screen and (max-width: $grid-breakpoints.md)
    .movie--information
      padding-top: 40px

  .image--style
    border: 1.6px solid var(--v-gold-base)

  .movie--title
    font-size: 2.5rem
    color: var(--v-white-base)
    padding-bottom: 6px

  .movie--details
    font-size: 1.5rem
    letter-spacing 1px
    color: var(--v-sand-base)

  .movie--description
    padding-top: 15px
    line-height: 34px
    color: var(--v-white-base)
    font-size: 1.5rem
    letter-spacing: 0px

  .movie--date
    padding-top: 40px
    color: var(--v-white-base)
    font-size: 2rem
    letter-spacing: 1px
    padding-bottom: 12px

  .showing--button
    flex: 0 0 100px
    height: 64px
    border: 1.5px solid var(--v-sand-base)
    line-height: 22px
    border-radius: 5px
    margin-right: 20px

    &::before
      background-color: transparent

    &:hover
      color: var(--v-gold-base) !important
      border-color: var(--v-gold-base)

  .showing--time
    padding-top: 5px
    font-size: 1.6rem

  .showing--type
    font-size: 0.9rem
</style>
