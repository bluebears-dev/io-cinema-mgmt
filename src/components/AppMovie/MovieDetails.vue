<template>
  <v-layout
    row wrap
    align-start
    justify-center
  >
    <v-flex xs12 class="md-constant movie--cover text-xs-center">
      <div class="d-inline-block">
        <v-img
          :src="movie.cover"
          class="image--style"
          :width="imageWidth"
        ></v-img>
      </div>
    </v-flex>
    <v-flex xs12 class="md-flex movie--information">
      <div class="movie--title alegreya-sc--regular">{{movie.title}}</div>
      <div class="movie--details alegreya-sc--regular">
        Rok Produkcji: {{movie.year}} &nbsp;&nbsp;|&nbsp;&nbsp; Reżyseria: {{movie.production}} &nbsp;&nbsp;|&nbsp;&nbsp;
        {{movie.length}} min
      </div>
      <div class="movie--details alegreya-sc--regular">
        {{movie.genres.join(' &nbsp;&nbsp;| &nbsp;&nbsp;')}}
      </div>
      <div class="movie--description roboto--light">
        {{movie.description}}
      </div>
    </v-flex>
    <v-flex xs12>
      <div class="movie--date alegreya-sc--regular">
        {{date}}
      </div>
      <v-layout
        row wrap
      >
        <v-btn
          v-for="showing in showings" :key="showing.toString()"
          block
          flat
          large
          :ripple="false"
          class="showing--button roboto--regular text-capitalize"
          color="white"
        >
          <div>
            <div class="showing--time">{{showing.time}} <br></div>
            <div class="showing--type">{{showing.picture}} {{showing.sound}}</div>
          </div>
        </v-btn>
      </v-layout>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    name: 'MovieDetails',
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
      }
    },
    data () {
      return {
        date: 'Piątek, 19 Listopada',
        movie: {
          title: 'Bohemian Rhapsody',
          cover: 'static/bohemian.jpg',
          description: 'Porywająca opowieść o zespole Queen, jego muzyce i niezwykłym wokaliście Freddie’em Mercurym ' +
            '(Rami Malek – serial TV ”Mr. Robot”), który przełamując stereotypy i konwencje, zdobył uwielbienie niezliczonych fanów. ',
          year: 2018,
          production: 'Brian Singer',
          length: 135,
          genres: ['Muzyczny', 'Biograficzny']
        },
        showings: [
          {time: '11:00', picture: '2D', sound: 'Napisy'},
          {time: '14:00', picture: '3D', sound: 'Lektor'},
          {time: '15:30', picture: '3D', sound: 'Dubbing'},
          {time: '16:45', picture: '2D', sound: 'Napisy'},
          {time: '21:00', picture: '2D', sound: 'Dubbing'},
          {time: '11:00', picture: '2D', sound: 'Napisy'},
          {time: '14:00', picture: '3D', sound: 'Lektor'},
          {time: '15:30', picture: '3D', sound: 'Dubbing'},
          {time: '16:45', picture: '2D', sound: 'Napisy'},
          {time: '21:00', picture: '2D', sound: 'Dubbing'},
          {time: '11:00', picture: '2D', sound: 'Napisy'},
          {time: '14:00', picture: '3D', sound: 'Lektor'},
          {time: '15:30', picture: '3D', sound: 'Dubbing'},
          {time: '16:45', picture: '2D', sound: 'Napisy'},
          {time: '21:00', picture: '2D', sound: 'Dubbing'}
        ]
      }
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
