<template>
  <v-app class="black">
    <router-view name="toolbar"/>
    <v-content class="black">
      <v-container fluid>
        <v-fade-transition leave-absolute hide-on-leave>
          <router-view/>
        </v-fade-transition>
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
</style>
