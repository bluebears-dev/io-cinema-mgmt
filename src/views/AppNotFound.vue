<template>
  <v-layout
      align-center column
      justify-center
      mt-5
      pt-5
      wrap
  >
    <h1 class="display-3 gold--text alegreya--thin">Nie znaleziono strony</h1>
    <router-link class="router--link" to="/">
      <p class="headline white--text alegreya--thin text-xs-center">Bardzo nam przykro ale wskazana strona nie
        istnieje.
        <br>Kilknij tutaj aby powrócić do strony głównej</p>
    </router-link>
  </v-layout>
</template>

<script>
  export default {
    name: 'AppNotFound'
  }
</script>

<style scoped lang="stylus">
  .router--link
    text-decoration: none

    p
      transition: color .1s ease-in-out

    &:hover p
      color: var(--v-sand-base) !important

</style>
