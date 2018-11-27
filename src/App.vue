<template>
  <v-app class="black">
    <AppToolbar/>
    <v-content class="black">
      <v-container
        fluid
        fill-height
      >
        <AppCinemaSelection/>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  import AppToolbar from './components/AppToolbar'
  import AppCinemaSelection from './views/AppCinemaSelection'

  export default {
    name: 'App',
    components: { AppCinemaSelection, AppToolbar }
  }
</script>

<style lang="stylus">
  @import '@mdi/font/css/materialdesignicons.min.css'
  @import 'vuetify/dist/vuetify.min.css'
  @import "assets/stylus/main.styl"
</style>
