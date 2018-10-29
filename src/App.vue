<template>
  <v-app>
    <v-navigation-drawer app></v-navigation-drawer>
    <v-toolbar app>Cinema</v-toolbar>
    <v-content>
      <v-container fluid>
        <img src="./assets/logo.png">
        <router-view></router-view>
        <v-text-field
          label="Prepend"
          prepend-icon="mdi-map-marker"
        ></v-text-field>
      </v-container>
    </v-content>
    <v-footer app></v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style lang="stylus">
@import '@mdi/font/css/materialdesignicons.min.css'
@import 'vuetify/dist/vuetify.min.css'
</style>
