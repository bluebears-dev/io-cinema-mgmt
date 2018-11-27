<template>
  <v-app class="black">
    <AppToolbar/>
    <v-content class="black">
      <v-container
        fluid
        fill-height
      >
        <AppMovieList/>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  import AppToolbar from './components/AppToolbar'
  import AppMovieList from './views/AppMovieList'

  export default {
    name: 'App',
    components: { AppMovieList, AppToolbar }
  }
</script>

<style lang="stylus">
  @import '@mdi/font/css/materialdesignicons.min.css'
  @import 'vuetify/dist/vuetify.min.css'
  @import "assets/stylus/main.styl"
</style>
