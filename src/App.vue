<template>
  <v-app dark class="black">
    <AppToolbar/>
    <v-content class="black">
      <v-container fluid>

      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  import AppToolbar from './components/AppToolbar'
  export default {
    name: 'App',
    components: {AppToolbar}
  }
</script>

<style lang="stylus">
  @import '@mdi/font/css/materialdesignicons.min.css'
  @import 'vuetify/dist/vuetify.min.css'
  @import "assets/stylus/main.styl"

  $gold = #f00
</style>


